from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from api.db.base import Base

class JobOids(Base):
    """
    Association table between jobs and OIDs to poll.
    """
    __tablename__ = "job_oids"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id", ondelete="CASCADE"))
    oid: Mapped[str] = mapped_column(String(200))
