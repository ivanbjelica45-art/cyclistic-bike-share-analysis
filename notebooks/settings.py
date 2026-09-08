import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

RAW_DIR = Path(os.environ["CYCLISTIC_RAW_DIR"])
