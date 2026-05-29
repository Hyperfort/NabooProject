import os
import sys
from pathlib import Path

os.environ.setdefault("DATABASE_PROVIDER", "mongodb")
os.environ.setdefault("MONGODB_URI", "mongodb://127.0.0.1:27017")
os.environ.setdefault("MONGODB_DATABASE", "naboo_test")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
