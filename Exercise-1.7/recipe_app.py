# import sqlalchemy to manage SQL
from sqlalchemy import create_engine


# Add security to login credentials
# import os
# mysql_user = os.environ.get("MYSQL_USER")
# mysql_password = os.environ.get("MYSQL_PASSWORD")

# Use the credentials to create an engine object called engine that connects to your database
engine = create_engine("mysql://cf-python:password@localhost/task_database")


# Import types for the table you will create
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

# Make the session object that you’ll use to make changes to your database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Store your declarative base class into a variable called Base
from sqlalchemy.orm import declarative_base
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
      "=" * 28 
      + f"\nRecipe: {self.name} ID: {self.id}"
      + f"\nCooking Time: {self.cooking_time} minutes"
      + f"\nDifficulty: {self.difficulty}"
      + f"\nIngredients:\n"
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

def main_menu():
  choice = ""
  while (choice != "quit"):
    print("\nMain Menu")
    print("=" * 28)
    print("Choose a function by number: ")
    print("\t1. Create a new recipe")
    print("\t2. Search by ingredient")
    print("\t3. Edit an existing recipe")
    print("\t4. Delete a recipe")
    print("\t5. View all recipes")
    print("\n\tType 'quit' to exit the program.")

    choice = input("\nEnter your choice: ")

    if choice == "1":
      create_recipe()
    elif choice == "2":
      search_by_ingredients()
    elif choice == "3":
      edit_recipe()
    elif choice == "4":
      delete_recipe()
    elif choice == "5":
      view_all_recipes()
    elif choice.lower() == "quit":
      session.close()
      engine.dispose()
      print("Goodbye! Application closed.")
      break
    else:
      print("Invalid input. Please choose a valid option.")


def create_recipe():
  # Collect recipe details from the user
  name = input("Enter the name of the recipe: ")
  cooking_time = input("Enter the cooking time in minutes: ")

  # Validate the cooking time
  if not cooking_time.isdigit() or int(cooking_time) <= 0:
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
    print("You must enter at least one ingredient.")
    return

  # Convert the list of ingredients to a string
  ingredients_str = ", ".join(ingredients)

  # Create a new Recipe object
  recipe_entry = Recipe(
    name = name, 
    ingredients = ingredients_str,
    cooking_time = int(cooking_time)
  )

  # Calculate and set the difficulty
  recipe_entry.difficulty = recipe_entry.calculate_difficulty(recipe_entry.cooking_time, ingredients)

  # Add the recipe to the database
  session.add(recipe_entry)
  session.commit()
  print("\nRecipe successfully saved to the database.")


def view_all_recipes():
  # Retrieve all recipes from the database
  recipes = session.query(Recipe).all()

  # Check if there are no entries
  if not recipes:
    print("There are no recipes in your database")
    # Exit the function to return to the main menu
    return
   
  # Loop through the list of recipes and display each recipe using their __str__ methods
  for recipe in recipes:
    print(recipe.__str__())

def search_by_ingredients():
  # Check if there are any entries in the table
  if session.query(Recipe).count() == 0:
    print("\nThere are no recipes in your database")
    # Exit the function to return to the main menu
    return

  # Retrieve the values from the ingredients column
  results = session.query(Recipe.ingredients).all()

  # Initialize a list to store all unique ingredients
  all_ingredients = []

  # Iterate through the results and add unique ingredients to all_ingredients
  for ingredients in results:
     ingredient_list = ingredients[0].split(", ")
     for ingredient in ingredient_list:
        if ingredient not in all_ingredients:
          all_ingredients.append(ingredient)

  # Display available ingredients with corresponding numbers to the user
  print("\nIngredients list:")
  print("=" * 28)
  for index, ingredient in enumerate(all_ingredients):
    print(f"{index + 1}. {ingredient}")

  try:
    # Ask the user to select ingredients by entering corresponding numbers
    user_input = input("Enter the numbers of the ingredients you'd like to search for (separated by spaces): ")
    selected_numbers = [int(number) for number in user_input.split()]
        
    # Check if user's inputs match the available options
    if any(number <= 0 or number > len(all_ingredients) for number in selected_numbers):
      print("Invalid ingredient selection. Please select valid ingredient numbers.")
      return

    # Create a list of ingredients to be searched for
    search_ingredients = [all_ingredients[number - 1] for number in selected_numbers]

    # Initialize a list to store search conditions
    conditions = []

    # Generate search conditions for each selected ingredient
    for ingredient in search_ingredients:
      like_term = f"%{ingredient}%"
      conditions.append(Recipe.ingredients.like(like_term))  

    # Retrieve recipes from the database based on the search conditions
    recipes = session.query(Recipe).filter(*conditions).all()

    # Display the matching recipes using their __str__ methods
    if recipes:
      print("\nRecipes containing the selected ingredients:")
      print("="* 28) 
      for recipe in recipes:
        print(recipe.__str__())
    # No recipes found with the selected ingredients.
    else:
      print("\nNo recipes found with the selected ingredients.")
  except ValueError:
    print("\nInvalid input. Please enter valid ingredient numbers.")

def edit_recipe():
  # Check if there are any recipes in the database
  if session.query(Recipe).count() == 0:
    print("\nThere are no recipes in your database")
    # Exit the function
    return

  # Retrieve id and name for each recipe
  recipes = session.query(Recipe.id, Recipe.name).all()
  
  # Display available recipes to the user
  print("\nRecipes available for editing:")
  print("=" * 28)
  for recipe_id, recipe_name in recipes:
    print(f"{recipe_id}. {recipe_name}")

  # Ask the user to select a recipe by entering its ID
  selected_recipe = int(input("Enter the ID of the recipe you'd like to edit: "))

  # Check if the selected ID exists
  if not session.query(Recipe).filter(Recipe.id == selected_recipe).count():
    print("Invalid recipe ID. Please try again and select a valid ID.")
    return
  

  # Retrieve the selected recipe from the database
  recipe_to_edit = session.query(Recipe).filter(Recipe.id == selected_recipe).first()

  # Display the recipe attributes for editing
  print("\nEdit Recipe Attributes:")
  print("=" * 28)
  print(f"1. Name: {recipe_to_edit.name}")
  print(f"2. Cooking Time: {recipe_to_edit.cooking_time} minutes")
  print(f"3. Ingredients: {recipe_to_edit.ingredients}")

  # Ask the user which attribute to edit
  selected_attribute = int(input("Enter the number of the attribute you'd like to edit: "))

  # Check if the user's input is valid
  if selected_attribute < 1 or selected_attribute > 3:
    print("Invalid attribute number. Please enter a 1, 2, or 3.")
    return

  # Editing the chosen attribute
  if selected_attribute == 1:
    new_name = input("Enter the new name: ")
    recipe_to_edit.name = new_name
  
  elif selected_attribute == 2:
    new_cooking_time = int(input("Enter the new cooking time (in minutes): "))
    recipe_to_edit.cooking_time = new_cooking_time

  elif selected_attribute == 3:
    new_ingredients = input("Enter the new ingredients: ")
    recipe_to_edit.ingredients = new_ingredients

  # Recalculate the difficulty for the edited recipe
  recipe_to_edit.calculate_difficulty(recipe_to_edit.cooking_time, recipe_to_edit.return_ingredients_as_list())

  # Commit the changes to the database
  session.commit()
  print("\nRecipe successfully edited and saved to the database.")

def delete_recipe():
  # Check if there are any recipes in the database
  if not session.query(Recipe).count():
    print("There are no recipes in your database.")
    return

  # Retrieve id and name for each recipe
  recipes = session.query(Recipe).all()

  # Display available recipes to the user
  print("Recipes available for deletion:")
  for recipe in recipes:
    print(recipe.__repr__())


  try:
    # Ask the user to select a recipe to delete by entering its ID
    user_input_id = int(input("Enter the ID of the recipe you want to delete:"))

    # Retrieve the selected recipe from the database
    recipe_to_delete = session.query(Recipe).filter(Recipe.id == user_input_id).first()

    # Check if the selected ID exists
    if not recipe_to_delete:
      print("Invalid recipe ID. Please select a valid recipe.")
      return

    # Ask for confirmation
    confirm = input(f"Are you sure you want to delete '{recipe_to_delete.name}' (ID: {recipe_to_delete.id})? (yes/no): ")

    if confirm.lower() == "yes":
      session.delete(recipe_to_delete)
      session.commit()
      print("Recipe successfully deleted.")
    elif confirm == "no":
      print("Deletion canceled. Recipe was not deleted.")
    else:
      print("Invalid input. Please enter 'yes' to confirm deletion or 'no' to cancel.")

  except ValueError:
    print("Invalid input. Please enter a valid recipe ID.")

main_menu()