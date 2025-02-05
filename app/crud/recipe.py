from sqlalchemy.orm import Session
from .. import models, schemas

def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def update_recipe(db: Session, recipe_id: int, updated_recipe: schemas.RecipeCreate):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe:
        db_recipe.title = updated_recipe.title
        db_recipe.description = updated_recipe.description
        db_recipe.ingredients = updated_recipe.ingredients
        db_recipe.instructions = updated_recipe.instructions
        db_recipe.category = updated_recipe.category
        db.commit()
        db.refresh(db_recipe)
    return db_recipe

def delete_recipe(db: Session, recipe_id: int):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe:
        db.delete(db_recipe)
        db.commit()
    return db_recipe