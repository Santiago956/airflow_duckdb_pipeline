import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import NoSuchModuleError
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

duckdb_url = os.getenv("URL_DUCKDB")

if duckdb_url:
	SQLALCHEMY_DATABASE_URL = duckdb_url
else:
	duckdb_path = Path(os.getenv("DUCKDB_PATH", "data/pipeline.duckdb")).expanduser()
	duckdb_path.parent.mkdir(parents=True, exist_ok=True)
	SQLALCHEMY_DATABASE_URL = f"duckdb:///{duckdb_path.as_posix()}"

try:
	engine = create_engine(SQLALCHEMY_DATABASE_URL)
except NoSuchModuleError as exc:
	raise RuntimeError(
		"DuckDB com SQLAlchemy requer o pacote 'duckdb-engine'. "
		"Instale com: uv add duckdb-engine"
	) from exc

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()