from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, ForeignKey
from api.db.base import Base

class TrapVarbinds(Base):
    __tablename__ = "trap_varbinds"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    trap_id: Mapped[int] = mapped_column(ForeignKey("traps.id", ondelete="CASCADE"))
    oid: Mapped[str] = mapped_column(String(200))
    value: Mapped[str | None] = mapped_column(Text, nullable=True)
