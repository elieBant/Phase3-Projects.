

from database import engine
from models import Base

print("Création des tables...")
Base.metadata.create_all(bind=engine)
print("Base de données initialisée !")
