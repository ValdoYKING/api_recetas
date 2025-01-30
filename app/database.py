from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

#Cargar las variables de entorno 
load_dotenv()

#Leer la url de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
#Crear el motor de la base de datos 
engine = create_engine(DATABASE_URL)
#Crear la fabrica de sesiones 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Definir base para los modelos SQLAlchemy
Base = declarative_base()
#Dependencia para obtener una sesion de base de datos en las rutas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()