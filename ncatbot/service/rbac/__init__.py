"""
RBAC (Role-Based Access Control) 服务

提供基于角色的访问控制功能。
"""

from enum import Enum
from .service import RBACService
from .path import PermissionPath
from .trie import PermissionTrie


class PermissionGroup(Enum):
    # 权限组常量
    ROOT = "root"
    ADMIN = "admin"
    USER = "user"


__all__ = [
    "RBACService",
    "PermissionPath",
    "PermissionTrie",
]
