#portfolio
#handle: _MUMINUL__ISLAM___

#code
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine=create_engine("sqlite:///app.db")
Session=sessionmaker(bind=engine)


def get_db():
    new_session=Session()
    try:
        yield new_session
    finally:
        new_session.close()


