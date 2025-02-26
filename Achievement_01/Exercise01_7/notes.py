# 1 connect
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://cf-python:password@localhost/my_database")  ## Notice!!

from sqlalchemy.orm import declarative_base  ## Notice!!
Base = declarative_base()  ## Notice!!

# 2 Create Tables
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

class Recipe(Base):
    __tablename__ = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
		
		
Base.metadata.create_all(engine)

# Insert
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

tea = Recipe(
        name = "Tea",
        cooking_time = 5,
        ingredients = "Tea Leaves, Water, Sugar"
)
session.add(tea)
session.commit()

# Reading
recipes_list = session.query(Recipe).all()
for recipe in recipes_list:
    print("Recipe ID: ", recipe.id)
    print("Recipe Name: ", recipe.name)
    print("Ingredients: ", recipe.ingredients)
    print("Cooking Time: ", recipe.cooking_time)
    
recipe = session.get(Recipe, 1)  ## Notice!!
session.query(Recipe).filter(Recipe.name == 'Tea').one()

# Reading - different ways
session.query(Recipe.name).all()
session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()


# Reading by Like
session.query(Recipe).filter(Recipe.ingredients.like("%Water%")).all()
session.query(Recipe).filter(Recipe.ingredients.like("%Milk%"), Recipe.ingredients.like("%Baking Powder%")).all()

recipes_list[0].ingredients
recipes_list[0].ingredients += ', Cardamom'
recipes_list[0].ingredients
session.commit()

# Update
session.query(Recipe).filter(Recipe.name == 'Tea').update({Recipe.name: 'Early Gray'})
session.commit()

# Delete
buttered_toast = Recipe(
    name = "Buttered Toast",
    ingredients = "Bread, Butter",
    cooking_time = 4
)
session.add(buttered_toast)
session.commit()

recipe_to_be_deleted = session.query(Recipe).filter(Recipe.name == 'Buttered Toast').one()
session.delete(recipe_to_be_deleted)
session.commit()

