from sqlalchemy import Column, Integer, String, Date
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import Base


class FoodEntry(Base):
    __tablename__ = "food_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    food = Column(String, nullable=False)
    calories = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<FoodEntry(id={self.id}, food={self.food}, calories={self.calories}, date={self.date})>"

if __name__ == "__main__":
    fe = FoodEntry()
    print(fe)



