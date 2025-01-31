import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from dotenv import load_dotenv

#Cargar las variables de entorno
load_dotenv()

# Añadir la ruta de tu aplicación
sys.path.append('.')

# Importar la configuración de la base de datos y los modelos
from app.database import Base  # Asegúrate de que esto apunte a la configuración correcta
from app.models import user, recipe  # Importa todos tus modelos aquí

# Configurar el archivo de configuración de logging
config = context.config
fileConfig(config.config_file_name)

# Asignar el modelo Base
target_metadata = Base.metadata
#Leer la url de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
# Establecer la URL de conexión
config.set_main_option('sqlalchemy.url', DATABASE_URL)  # Cambia esto a tu URL de conexión

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
