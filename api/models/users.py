from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, DateTime, func
from api.db.base import Base

class Users(Base):
    """
    Gère authentification et rôles
    """
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(Text)
    role: Mapped[str] = mapped_column(String(20))
    api_key_hash: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped = mapped_column(DateTime(timezone=False), server_default=func.current_timestamp())
    last_login: Mapped | None = mapped_column(DateTime(timezone=False), nullable=True)
