from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional
from api.models.devices import Devices
from api.schemas.device import DeviceCreate, DeviceUpdate

class DeviceRepository:
    """Couche d'accès aux données pour la table 'devices'."""

    @staticmethod
    def list(db: Session, q: Optional[str] = None, limit: int = 100) -> List[Devices]:
        stmt = select(Devices).order_by(Devices.created_at.desc()).limit(limit)
        if q:
            stmt = stmt.where((Devices.name.ilike(f"%{q}%")) | (Devices.ip_address == q))
        return db.execute(stmt).scalars().all()

    @staticmethod
    def get(db: Session, device_id: int) -> Optional[Devices]:
        return db.get(Devices, device_id)

    @staticmethod
    def create(db: Session, data: DeviceCreate) -> Devices:
        # unicité “logique” IP (à toi d’ajouter une contrainte unique si tu veux)
        existing = db.execute(select(Devices).where(Devices.ip_address == str(data.ip_address))).scalar_one_or_none()
        if existing:
            raise ValueError("Device with this IP already exists")
        obj = Devices(
            name=data.name,
            ip_address=str(data.ip_address),
            snmp_profile_id=data.snmp_profile_id,
            location=data.location,
            tags=data.tags,
            enabled=data.enabled,
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def update(db: Session, device: Devices, data: DeviceUpdate) -> Devices:
        for field, value in data.model_dump(exclude_unset=True).items():
            if field == "ip_address" and value is not None:
                value = str(value)
            setattr(device, field, value)
        db.commit()
        db.refresh(device)
        return device

    @staticmethod
    def delete(db: Session, device: Devices) -> None:
        db.delete(device)
        db.commit()
