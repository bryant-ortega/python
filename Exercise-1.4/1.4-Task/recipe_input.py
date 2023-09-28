import pickle

# Function initially called so the user can enter a recipe
def take_recipe():
  name = input("Enter your recipe name: ")
  cooking_time = int(input("Enter your recipe's cooking time in minutes: "))
  ingredients = input("Enter your recipe's ingredients (separated by comma): ").split(", ")

# variable that stores the result from the function that defines the recipe's difficulty
  difficulty = calc_difficulty(cooking_time, ingredients)

  recipe = {
    'Name': name, 
    'Cooking_time: ': cooking_time, 
    'Ingredients: ': ingredients,
    'Difficulty: ': difficulty
  }
  print('===================================')
  print('Recipe: ', name)
  print('Cooking Time (min): ', cooking_time)
  print('Ingredients: ')
  for ingredient in ingredients:
    print(ingredient)
  print('Difficulty level: ', difficulty)
  return recipe

# function to define recipe difficulty
def calc_difficulty(cooking_time, ingredients):
  if cooking_time < 10 and len(ingredients) < 4:
    difficulty = 'Easy'
  elif cooking_time < 10 and len(ingredients) >= 4:
    difficulty = 'Medium'
  elif cooking_time >= 10 and len(ingredients) < 4:
    difficulty = 'Intermediate'
  elif cooking_time > 10 and len(ingredients) >= 4:
    difficulty = 'Hard'
  return difficulty

take_recipe()

# User enters the name of their file
my_file = input("Enter the name of your recipes file: ")

# Try to open the file.
try:
  file = open(my_file, 'rb')
  data = pickle.load(file)
  print("File loaded successfully!")
# error displayed if file not found
except FileNotFoundError:
  print("File doesn't exist - exiting.")
  data = {"recipes_list": [], "all_ingredients": []}
# error displayed if anything else goes wrong
except: 
  print("An unexpected error has occurred.")
  data = {"recipes_list": [], "all_ingredients": []}
# closes the file
else:
  file.close()
# Extracts from the dictionary into two separate lists
finally:
  recipes_list = data['recipes_list']
  all_ingredients = data['all_ingredients']

# Asks the user how many recipes they want to enter
n = int(input("How many recipes would you like to enter?: "))

# calls take_recipe function n times, adds ingredients to all_ingredients, and recipes to recipes_list
for i in range(n):
  recipe = take_recipe()
  for ingredient in recipe['Ingredients']:
    if ingredient not in all_ingredients:
      all_ingredients.append(ingredient)
  recipes_list.append(recipe)
  print("Recipe successfully added!")

# Creates a new dictionary with the updated data
data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

with open(my_file, 'wb') as file:
  pickle.dump(data,file)
file.close()
print("Your Recipe file has been updated!")