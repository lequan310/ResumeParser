import pytest
from unittest.mock import patch, MagicMock
from utils.pdf_utils import get_links_from_pdf, get_context

# Mock data for pymupdf responses
MOCK_LINK_PAGE_1 = [{"uri": "http://example.com"}, {"uri": "http://test.org"}]
MOCK_LINK_PAGE_2 = [{"uri": "https://github.com"}]


@pytest.fixture
def dummy_file_bytes():
    """Provides dummy bytes data for tests."""
    return b"dummy pdf content"


class TestPdfUtils:
    @patch("utils.pdf_utils.open")
    def test_get_links_from_pdf_with_links(
        self, mock_pymupdf_open, dummy_file_bytes
    ):  # Add fixture name as arg
        """Test get_links_from_pdf when the PDF has links."""
        # Arrange
        mock_doc = MagicMock()
        mock_page1 = MagicMock()
        mock_page2 = MagicMock()

        mock_page1.get_links.return_value = MOCK_LINK_PAGE_1
        mock_page2.get_links.return_value = MOCK_LINK_PAGE_2

        mock_doc.__enter__.return_value = mock_doc
        mock_doc.__iter__.return_value = iter([mock_page1, mock_page2])
        mock_doc.has_links.return_value = True
        mock_pymupdf_open.return_value = mock_doc

        # Act
        links = get_links_from_pdf(dummy_file_bytes)  # Use the fixture

        # Assert
        mock_pymupdf_open.assert_called_once_with(
            stream=dummy_file_bytes, filetype="pdf"
        )  # Use the fixture
        assert mock_doc.has_links.called
        assert mock_page1.get_links.called
        assert mock_page2.get_links.called
        assert links == ["http://example.com", "http://test.org", "https://github.com"]

    @patch("utils.pdf_utils.open")
    def test_get_links_from_pdf_no_links(
        self, mock_pymupdf_open, dummy_file_bytes
    ):  # Add fixture name as arg
        """Test get_links_from_pdf when the PDF has no links."""
        # Arrange
        mock_doc = MagicMock()
        mock_doc.__enter__.return_value = mock_doc
        mock_doc.has_links.return_value = False
        mock_pymupdf_open.return_value = mock_doc

        # Act
        links = get_links_from_pdf(dummy_file_bytes)  # Use the fixture

        # Assert
        mock_pymupdf_open.assert_called_once_with(
            stream=dummy_file_bytes, filetype="pdf"
        )  # Use the fixture
        assert mock_doc.has_links.called
        assert links == []

    @patch("utils.pdf_utils.open")
    @patch("utils.pdf_utils.logger")
    def test_get_links_from_pdf_exception(
        self, mock_logger, mock_pymupdf_open, dummy_file_bytes
    ):  # Add fixture name as arg
        """Test get_links_from_pdf when an exception occurs."""
        # Arrange
        mock_pymupdf_open.side_effect = Exception("PDF processing error")

        # Act
        links = get_links_from_pdf(dummy_file_bytes)  # Use the fixture

        # Assert
        mock_pymupdf_open.assert_called_once_with(
            stream=dummy_file_bytes, filetype="pdf"
        )  # Use the fixture
        mock_logger.exception.assert_called_once()
        assert links == []

    @patch("utils.pdf_utils.get_links_from_pdf")
    def test_get_context_with_links(self, mock_get_links, dummy_file_bytes):
        """Test get_context when links are found."""
        # Arrange
        mock_links = ["http://example.com", "https://github.com"]
        mock_get_links.return_value = mock_links
        expected_context = (
            "Additional Context: This file contains the following hyperlinks:\n"
            "http://example.com\nhttps://github.com\n\n"
            "Include this information in the resume markdown conversion."
        )

        # Act
        context = get_context(dummy_file_bytes)  # Use the fixture

        # Assert
        mock_get_links.assert_called_once_with(dummy_file_bytes)  # Use the fixture
        assert context == expected_context

    @patch("utils.pdf_utils.get_links_from_pdf")
    def test_get_context_no_links(self, mock_get_links, dummy_file_bytes):
        """Test get_context when no links are found."""
        # Arrange
        mock_get_links.return_value = []
        expected_context = ""

        # Act
        context = get_context(dummy_file_bytes)  # Use the fixture

        # Assert
        mock_get_links.assert_called_once_with(dummy_file_bytes)  # Use the fixture
        assert context == expected_context
