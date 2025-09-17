from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, ForeignKey
from api.db.base import Base

class Jobs(Base):
    """
    Planification des tâches de collecte SNMP
    """
    __tablename__ = "jobs"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id", ondelete="CASCADE"))
    type: Mapped[str] = mapped_column(String(20))  # poll|getbulk|set|discovery
    period_s: Mapped[int | None] = mapped_column(Integer, nullable=True)
    timeout_ms: Mapped[int | None] = mapped_column(Integer, default=2000)
    retries: Mapped[int | None] = mapped_column(Integer, default=1)
    next_run_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=False), nullable=True)
    status: Mapped[str | None] = mapped_column(String(20), nullable=True)
