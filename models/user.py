import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from config.db_setup import Base

from .mixins import Timestamp #Permite combinar clases para crear tablas

class Role(enum.Enum):
    admin = 1
    normal = 2
    consulta = 3
    externo = 4


class User(Timestamp, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)

    profile = relationship("Profile", back_populates="owner", uselist = False) #uselist = false para que la relación se entienda como 1 a 1

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    firs_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")