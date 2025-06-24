"""
Dependency injection container using dependency-injector library.
"""

from dependency_injector import containers, providers

from core.workflows.analysis.graph import AnalysisGraph
from core.workflows.chat.graph import ChatGraph
from core.workflows.parser.graph import ParserGraph
from services.analysis_service import AnalysisService
from services.chat_service import ChatService
from services.file_service import FileService


class Container(containers.DeclarativeContainer):
    """
    Dependency injection container using dependency-injector library.
    """

    # Wiring configuration
    wiring_config = containers.WiringConfiguration(
        modules=[
            "api.v1.endpoints.files",
            "api.v1.endpoints.chat",
            "api.v1.endpoints.analysis",
        ]
    )

    # Configuration
    config = providers.Configuration()

    # Graph providers (singletons)
    parser_graph = providers.Singleton(ParserGraph)
    chat_graph = providers.Singleton(ChatGraph)
    analysis_graph = providers.Singleton(AnalysisGraph)

    # Service providers (singletons with dependencies)
    file_service = providers.Singleton(FileService, graph=parser_graph)
    chat_service = providers.Singleton(ChatService, graph=chat_graph)
    analysis_service = providers.Singleton(AnalysisService, graph=analysis_graph)
