from hugbbley.core.utils.config_manager import get_database_url
from hugbbley.platform.hugbbleyn_models import Base
from sqlalchemy import create_engine


def create_tables(*args, **kwargs):
    engine = create_engine(get_database_url())
    Base.metadata.create_all(engine)

