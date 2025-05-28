from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base  # ✅ Import corrigé

class MealPlan(Base):
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    week = Column(Integer, nullable=False)
    meals = Column(String)

    def __repr__(self):
        return f"<MealPlan(id={self.id}, user_id={self.user_id}, week={self.week}, meals={self.meals})>"

