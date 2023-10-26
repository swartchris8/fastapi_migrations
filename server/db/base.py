# Import all the models, so that Base has them before being
# imported by Alembic
from server.db.base_class import Base  # noqa
from server.models import Item, User  # noqa
