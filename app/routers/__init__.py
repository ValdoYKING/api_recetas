# routers/__init__.py

from .recipes import router as recipes_router
from .users import router as users_router

__all__ = ["recipes_router", "users_router"]
