from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, DateTime, ForeignKey, func
from api.db.base import Base

class Traps(Base):
    """
    Réceptions des traps SNMP
    """
    __tablename__ = "traps"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_id: Mapped[int | None] = mapped_column(ForeignKey("devices.id", ondelete="SET NULL"), nullable=True)
    ts: Mapped = mapped_column(DateTime(timezone=False), server_default=func.current_timestamp())
    source_ip: Mapped[str | None] = mapped_column(String(50), nullable=True)
    version: Mapped[str | None] = mapped_column(String(10), nullable=True)
    community_or_user: Mapped[str | None] = mapped_column(String(50), nullable=True)
    enterprise_oid: Mapped[str | None] = mapped_column(String(200), nullable=True)
    severity: Mapped[str | None] = mapped_column(String(20), nullable=True)
    validated: Mapped[bool] = mapped_column(Boolean, server_default="false")
