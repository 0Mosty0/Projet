from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, JSON, func
from api.db.base import Base

class AuditLog(Base):
    """
    Traçabilité des actions utilisateur et système.
    """
    __tablename__ = "audit_log"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ts: Mapped = mapped_column(DateTime(timezone=False), server_default=func.current_timestamp())
    actor: Mapped[str | None] = mapped_column(String(50), nullable=True)
    action: Mapped[str | None] = mapped_column(String(100), nullable=True)
    entity: Mapped[str | None] = mapped_column(String(50), nullable=True)
    entity_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    metadata: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # JSONB côté PG
