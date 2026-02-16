import sqlalchemy

def get_engine():
    engine = sqlalchemy.create_engine(
        "mysql+pymysql://root:Jeandedieu%402808@localhost/projet_industriel"
    )
    return engine