from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Integer, Float, DateTime, func
from api.db.base import Base

class Anomalies(Base):
    """
    Journal des anomalies détectées par le système.
    """
    __tablename__ = "anomalies"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ts: Mapped = mapped_column(DateTime(timezone=False), server_default=func.current_timestamp())
    source: Mapped[str | None] = mapped_column(String(50), nullable=True)
    type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    score: Mapped[float | None] = mapped_column(Float, nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    entity_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    entity_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
