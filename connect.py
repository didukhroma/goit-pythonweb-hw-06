from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from config_db import url_to_db


engine = create_engine(url_to_db)
Session = sessionmaker(bind=engine)
session = Session()

# Check connection to db
if __name__ == "__main__":
    print(url_to_db)
    try:
        connection = engine.connect()
        print("Successful connection")
        connection.close()
    except:
        print("Error connection to db")
