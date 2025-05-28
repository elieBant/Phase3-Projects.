from sqlalchemy import Column, Integer, ForeignKey
from database import Base  # ✅ Corriger l'import ici

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    daily = Column(Integer, nullable=False)
    weekly = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Goal(id={self.id}, user_id={self.user_id}, daily={self.daily}, weekly={self.weekly})>"

