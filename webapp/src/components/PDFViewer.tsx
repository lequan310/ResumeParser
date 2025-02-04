import { useState } from "react";
import { pdfjs, Document, Page } from "react-pdf";
import type { PDFDocumentProxy } from "pdfjs-dist";
import usePDFContext from "@/hooks/usePDFContext";
import "react-pdf/dist/esm/Page/AnnotationLayer.css";
import "react-pdf/dist/esm/Page/TextLayer.css";

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
  "pdfjs-dist/build/pdf.worker.min.mjs",
  import.meta.url
).toString();

const options = {
  cMapUrl: "/cmaps/",
  standardFontDataUrl: "/standard_fonts/",
};

const PDFViewer = () => {
  const pdfContext = usePDFContext();
  const [numPages, setNumPages] = useState<number>();

  function onDocumentLoadSuccess({
    numPages: nextNumPages,
  }: PDFDocumentProxy): void {
    setNumPages(nextNumPages);
  }

  return (
    <Document
      file={pdfContext.currentPdf}
      onLoadSuccess={onDocumentLoadSuccess}
      options={options}
      className="flex flex-col items-center text-xl"
    >
      {Array.from(new Array(numPages), (_el, index) => (
        <Page
          key={`page_${index + 1}`}
          pageNumber={index + 1}
          className="mb-4"
        />
      ))}
    </Document>
  );
};

export default PDFViewer;
