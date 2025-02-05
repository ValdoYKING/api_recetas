from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud, database, utils

router = APIRouter()

#Endpoint para crear una receta
@router.post("/recipes/", response_model=schemas.Recipe)
# def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(database.get_db), admin_user: schemas.User = Depends(utils.get_admin_user)):
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(database.get_db)):
    return crud.create_recipe(db=db, recipe=recipe)

#Endpoint para obtener una receta por ID
@router.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(database.get_db)):
    db_recipe = crud.get_recipe(db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

#Endpoint para obtener todas las recetas
@router.get("/recipes/", response_model=list[schemas.Recipe])
def read_recipes(skip: int = 0, limit: int= 10, db: Session = Depends(database.get_db)):
    recipes = crud.get_recipes(db, skip=skip, limit=limit)
    return recipes

#Endpoint para actualizar una receta
@router.put("/recipes/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(recipe_id: int, recipe:schemas.RecipeCreate, db: Session = Depends(database.get_db)):
    db_recipe = crud.update_recipe(db, recipe_id=recipe_id, updated_recipe=recipe)
    if db_recipe is  None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

#Endpoint para eliminar una receta
@router.delete("/recipes/{recipe_id}", response_model=schemas.Recipe)
def delete_recipe(recipe_id: int, db: Session = Depends(database.get_db), admin_user: schemas.User = Depends(utils.get_admin_user)):
    db_recipe = crud.delete_recipe(db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe