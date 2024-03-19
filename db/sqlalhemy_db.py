from sqlalchemy import create_engine

class DatabaseConnection:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)