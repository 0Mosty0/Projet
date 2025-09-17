from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, DateTime, func
from api.db.base import Base

class Mibs(Base):
    """
    Référentiel des MIBs importées
    """
    __tablename__ = "mibs"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    version: Mapped[str | None] = mapped_column(String(50), nullable=True)
    vendor: Mapped[str | None] = mapped_column(String(100), nullable=True)
    path: Mapped[str | None] = mapped_column(Text, nullable=True)
    imported_at: Mapped = mapped_column(DateTime(timezone=False), server_default=func.current_timestamp())
