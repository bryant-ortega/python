class Recipe:
  
  all_ingredients = []

  def __init__(self, name, cooking_time):
    self.name = name
    self.ingredients = []
    self.cooking_time = cooking_time
    self.difficulty = None

  # function to define recipe difficulty
  def calculate_difficulty(self):
    if self.cooking_time < 10 and len(self.ingredients) < 4:
      self.difficulty = 'Easy'
    elif self.cooking_time < 10 and len(self.ingredients) >= 4:
      self.difficulty = 'Medium'
    elif self.cooking_time >= 10 and len(self.ingredients) < 4:
      self.difficulty = 'Intermediate'
    elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
      self.difficulty = 'Hard'
    else:
      print("something went wrong")

  
  # initialize getter & setter methods for name
  def get_name(self):
    return self.name
  
  def set_name(self, name):
    self.name = name

  # initialize getter & setter methods for cooking time
  def get_cooking_time(self):
    return self.cooking_time
  
  def set_cooking_time(self, cooking_time):
    self.cooking_time = cooking_time

  # a method that takes in variable number of arguments and adds them 
  # to the recipe's ingredients  
  def add_ingredients(self, *ingredients):
    self.ingredients = ingredients
    self.update_all_ingredients()

  def get_ingredients(self):
    return self.ingredients
  
  # A getter method for difficulty
  def get_difficulty(self):
    if self.difficulty is None:
      self.calculate_difficulty()
    return self.difficulty
  
  def search_ingredient(self, ingredient):
    if ingredient in self.ingredients:
      return True
    else:
      return False


  # A method that goes through the current object’s ingredients and 
  # adds them to all_ingredients, if they’re not already present. 
  def update_all_ingredients(self):
    for ingredient in self.ingredients:
      if ingredient not in self.all_ingredients:
        self.all_ingredients.append(ingredient)

  def __str__(self):
    output = "\n----------------------------------" + \
    "\nRecipe Name: " + str(self.name) + \
    "\nCooking Time: " + str(self.cooking_time) + " minutes" + \
    "\nDifficulty: " + str(self.difficulty) + \
    "\nIngredients:\n"
    for ingredient in self.ingredients:
       output += "-" + ingredient + "\n"
    return output

  # To find recipes that contain a specific ingredient
  def recipe_search(self, data, search_term):
    print(f"Recipes that contain '{search_term}':\n")
    for recipe in data:
      if recipe.search_ingredient(search_term):
        print(recipe)

recipes_list = []

tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.get_difficulty()

recipes_list.append(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee", "Powder", "Sugar", "Water")
coffee.get_difficulty()

recipes_list.append(coffee)

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.get_difficulty()

recipes_list.append(cake)

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.get_difficulty()

recipes_list.append(banana_smoothie)

# Display string representation of each recipe
for recipe in recipes_list:
  print(recipe)

# Create a list of ingredients to search for
ingredients_to_search = ["Water", "Sugar", "Bananas"]

# Iterate over each ingredient and search for recipes
for ingredient in ingredients_to_search:
    print(f"\nResults for recipe_search with {ingredient}:" + \
      "\n----------------------------------")
    for recipe in recipes_list:
      if recipe.search_ingredient(ingredient):
        print(f"- {recipe.name}")
    print("\n")