from sqlalchemy import create_engine


def get_connection():
    return create_engine("mysql+pymysql://root:ZSEfvd55@47.120.37.245:3306/dev")
