from pydantic import BaseSettings, Field
from typing import List, Optional
from pathlib import Path

from dotenv import load_dotenv

class Settings(BaseSettings):
    # Load environment variables from .env file
    load_dotenv()

    # Application settings
    