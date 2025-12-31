from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import DB_URL

engine=create_engine(DB_URL,echo=True)

sessionLocal=sessionmaker(bind=engine, autoflush=False)


def get_db():
    db=sessionLocal()

    try:
        yield db
    finally:
        db.close()