from sqlmodel import Session, create_engine

engine = create_engine("sqlite:///database.db")


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
