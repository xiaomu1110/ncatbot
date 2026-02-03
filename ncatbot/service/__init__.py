"""
服务层

提供可动态加载/卸载的外部服务，支持依赖注入到插件和 API 组件。
"""

from .base import BaseService
from .manager import ServiceManager
from .message_router import MessageRouter
from .rbac import RBACService
from .preupload import PreUploadService
from .plugin_config import PluginConfigService
from .file_watcher import FileWatcherService
from .plugin_data import PluginDataService
from .time_task import TimeTaskService
from .unified_registry import UnifiedRegistryService

__all__ = [
    "BaseService",
    "ServiceManager",
    "MessageRouter",
    "PreUploadService",
    "RBACService",
    "PluginConfigService",
    "FileWatcherService",
    "PluginDataService",
    "TimeTaskService",
    "UnifiedRegistryService",
]
