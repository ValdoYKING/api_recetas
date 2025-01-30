from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud, database

router = APIRouter()

#Endpoint para crear un usuario
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db=db, user=user)

#Endpoint para obtener un usuario por ID
@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#Endpoint para obtener todos los usuarios
@router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

#Endpoint para actualizar un usuario
@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.update_user(db, user_id=user_id, updated_user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#Endpoint para eliminar un usuario
@router.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user= crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user