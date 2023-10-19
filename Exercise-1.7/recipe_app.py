# import sqlalchemy to manage SQL
from sqlalchemy import create_engine


# Add security to login credentials
import os
mysql_user = os.environ.get("MYSQL_USER")
mysql_password = os.environ.get("MYSQL_PASSWORD")

# Use the credentials to create an engine object called engine that connects to your database
engine = create_engine("mysql://mysql_user:mysql_password@localhost/task_database")

# Import types for the table you will create
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

# Make the session object that you’ll use to make changes to your database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Store your declarative base class into a variable called Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Define the Recipe model
class Recipe(Base):
  __tablename__ = 'final_recipes'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50))
  ingredients = Column(String(255))
  cooking_time = Column(Integer)
  difficulty = Column(String(20))

  # method that shows a quick representation of the recipe
  def __repr__(self):
    return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

  # method that prints a well-formatted version of the recipe
  def __str__(self): 
    list_ingredients = self.ingredients.split(", ")
    output = (
      "=" * 15 
      + f"\nRecipe: {self.name} ID: {self.id}"
      + f"\nCooking Time: {self.cooking_time} minutes"
      + f"\nDifficulty: {self.difficulty}"
      + f"\nIngredients: "
    )
    for ingredient in list_ingredients:
        output += f"\t- {ingredient}\n"
        return output
    
  # Method to calculate the difficulty of a recipe based on the number of ingredients and cooking time
  def calculate_difficulty(self, cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        self.difficulty = 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        self.difficulty = 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
        self.difficulty = 'Intermediate'
    elif cooking_time >= 10 and len(ingredients) >= 4:
        self.difficulty = 'Hard'
    else:
        print("Something went wrong")

    return self.difficulty
  
  # method that retrieves the ingredients string inside your Recipe object as a list
  def return_ingredients_as_list(self):
      # if no ingredients return empty list
     if not self.ingredients:
        return []
     else:
        return self.ingredients.split(", ")
    
# method in the base class to create tables of the model
Base.metadata.create_all(engine)

def create_recipe():
  # Collect recipe details from the user
  name = input("Enter the name of the recipe: ")
  cooking_time = input("Enter the cooking time in minutes: ")

  # Validate the cooking time
  if not cooking_time.isnumeric():
        print("Cooking time must be a valid number.")
        return

  # Collect the number of ingredients and ingredients list
  num_ingredients = int(input("How many ingredients would you like to enter? "))
  ingredients = []
  for ingredient in range(num_ingredients):
     # Make the ingredient numbering user friendly
     ingredient = input(f"Enter ingredient {ingredient + 1}: ")
     ingredients.append(ingredient)

  # Validate the length of the recipe name
  if len(name) > 50:
     print("Recipe name should not exceed 50 characters.")
     return

  # Validate the number of ingredients
  if len(ingredients) == 0:
     print("You must enter at least one ingredient")
     return

  # Convert the list of ingredients to a string
  ingredients_str = ", ".join(ingredients)

  # Create a new Recipe object

  # Calculate and set the difficulty

  # Add the recipe to the database

  # Call the create_recipe function to create a new recipe