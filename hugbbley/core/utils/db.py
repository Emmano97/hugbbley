from hugbbley.core.utils.config_manager import get_database_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session():
    # Database configuration
    # Create database engine
    engine = create_engine(get_database_url())

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Yield a session
    session = Session()
    try:
        yield session
    finally:
        session.close()
