from sqlalchemy import column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NoteModel(Base):
    __tablename__ = 'notes'

    id = column(Integer, primary_key=True), index=True
    title = column(String(255), nullable=False)
    content = column(Text, nullable=False)