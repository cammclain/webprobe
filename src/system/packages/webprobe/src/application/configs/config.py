from pydantic import BaseSettings, Field
from typing import List, Optional
from pathlib import Path

from dotenv import load_dotenv

class DatabaseSettings(BaseSettings):

    dbms: str = Field(env="DATABASE_DBMS")
    if dbms == "sqlite":
        db_path: Path = Field(env="DATABASE_PATH")
    elif dbms == "postgresql":
        db_url: str = Field(env="DATABASE_URL")
        db_name: str = Field(env="DATABASE_NAME")
        db_user: str = Field(env="DATABASE_USER")
        db_password: str = Field(env="DATABASE_PASSWORD")
        db_host: str = Field(env="DATABASE_HOST")
        db_port: int = Field(env="DATABASE_PORT")



class Settings(BaseSettings):
    # Load environment variables from .env file
    load_dotenv()

    database_settings: DatabaseSettings = DatabaseSettings()
    # Application settings
    