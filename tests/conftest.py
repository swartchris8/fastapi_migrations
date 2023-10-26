import pytest
import sqlalchemy
from pytest_alembic.config import Config
from alembic.config import Config as AlembicConfig

from pathlib import Path

repo_root_dir = Path(__file__).parent.parent

ALEMBIC_INI_PATH = str(
    repo_root_dir / "server" / "alembic.ini"
)  # Specify the path to your alembic.ini

ALEMBIC_SCRIPTS_PATH = str(repo_root_dir / "server" / "alembic")

SQLITE_DB_PATH = str(repo_root_dir / "sql_app.db")

from pytest_alembic.config import Config


@pytest.fixture
def alembic_config():
    """Override this fixture to configure the exact alembic context setup required."""
    return Config(
        config_options={
            "config_file_name": ALEMBIC_INI_PATH,
            "script_location": ALEMBIC_SCRIPTS_PATH,
        }
    )


@pytest.fixture
def alembic_engine():
    """Override this fixture to provide pytest-alembic powered tests with a database handle."""
    # Adjust the URL to your actual database setup if not using SQLite in memory.
    return sqlalchemy.create_engine(f"sqlite:///{SQLITE_DB_PATH}")
