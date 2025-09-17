from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# --------- Entrées ---------
class SnmpProfileCreate(BaseModel):
    """
    Payloads pour créer/modifier un profil SNMP
    """
    version: str = Field(pattern="^(v2c|v3)$")
    community: Optional[str] = Field(default=None, max_length=100)
    v3_user: Optional[str] = Field(default=None, max_length=50)
    v3_auth_proto: Optional[str] = Field(default=None, max_length=20)
    v3_auth_key: Optional[str] = None
    v3_priv_proto: Optional[str] = Field(default=None, max_length=20)
    v3_priv_key: Optional[str] = None
    security_level: Optional[str] = Field(default=None, max_length=20)
    engine_id: Optional[str] = Field(default=None, max_length=100)
    notes: Optional[str] = None

class SnmpProfileUpdate(BaseModel):
    """
    Payloads pour créer/modifier un profil SNMP
    """
    version: Optional[str] = Field(default=None, pattern="^(v2c|v3)$")
    community: Optional[str] = Field(default=None, max_length=100)
    v3_user: Optional[str] = Field(default=None, max_length=50)
    v3_auth_proto: Optional[str] = Field(default=None, max_length=20)
    v3_auth_key: Optional[str] = None
    v3_priv_proto: Optional[str] = Field(default=None, max_length=20)
    v3_priv_key: Optional[str] = None
    security_level: Optional[str] = Field(default=None, max_length=20)
    engine_id: Optional[str] = Field(default=None, max_length=100)
    notes: Optional[str] = None

# --------- Sorties ---------
class SnmpProfileOut(BaseModel):
    """
    Représentation complète renvoyée au client
    """
    id: int
    version: str
    community: Optional[str]
    v3_user: Optional[str]
    v3_auth_proto: Optional[str]
    v3_auth_key: Optional[str]
    v3_priv_proto: Optional[str]
    v3_priv_key: Optional[str]
    security_level: Optional[str]
    engine_id: Optional[str]
    notes: Optional[str]
