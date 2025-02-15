from sqlalchemy.orm import Mapped, mapped_column
from database import db
from .entry import Entry



class Article(Entry):
    __tablename__ = "article"
    author: Mapped[str] = mapped_column(db.String, nullable=False)
    title: Mapped[str] = mapped_column(db.String, nullable=False)
    year: Mapped[str] = mapped_column(db.String, nullable=False)
    journal: Mapped[str] = mapped_column(db.String, nullable=False)

