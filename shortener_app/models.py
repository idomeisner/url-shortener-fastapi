from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)   # db primary key
    key = Column(String, unique=True, index=True)     # the shortened url
    secret_key = Column(String, unique=True, index=True)   # admin url (manage url and see statistics)
    target_url = Column(String, index=True)    # target url
    is_active = Column(Boolean, default=True)  # enable / disable url
    clicks = Column(Integer, default=0)    # clicks on shortened url
