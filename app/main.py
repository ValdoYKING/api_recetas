from fastapi import FastAPI, HTTPException
from .routers import recipes, users
from .database import engine, Base
from .models import recipe, user

# Crea las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(recipes.router)
app.include_router(users.router)
# app.include_router(auth.router)


""" from typing import Union, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI() """

""" class Recipe(BaseModel):
    title: str
    description: Union[str, None] = None
    ingredients: List[str]
    intruccions: str
    
recipes = [] """

""" @app.get("/")
def read_root():
    return{"Hello": "Welcome to the Recipe API"}

@app.post("/recipes/")
def create_recipe(recipe: Recipe):
    recipes.append(recipe)
    return recipe

@app.get("/recipes/")
def read_recipes():
    return recipes

@app.get("/recipes/{recipe_id}")
def read_recipe(recipe_id: int):
    if recipe_id >= len(recipes) or recipe_id < 0:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes[recipe_id]

@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe: Recipe):
    if recipe_id >= len(recipes) or recipe_id < 0:
        raise HTTPException(status_code=404, detail="Recipe not found")
    recipes[recipe_id] = recipe
    return recipe

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    if recipe_id >= len(recipes) or recipe_id < 0:
        raise HTTPException(status_code=404, detail="Recipe not found")
    recipe = recipes.pop(recipe_id)
    return recipe """