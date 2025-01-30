# crud/__init__.py

from .recipe import create_recipe, get_recipe, get_recipes, update_recipe, delete_recipe
from .user import create_user, get_user, get_user_by_email, get_users, update_user, delete_user

__all__ = [
    "create_recipe", "get_recipe", "get_recipes", "update_recipe", "delete_recipe",
    "create_user", "get_user", "get_user_by_email", "get_users", "update_user", "delete_user"
]
