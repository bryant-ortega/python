import pickle

def take_recipe():
  name = input("Enter your recipe name: ")
  cooking_time = int(input("Enter your recipe's cooking time in minutes: "))
  ingredients = input("Enter your recipe's ingredients (separated by comma): ").split(", ")

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


my_file = input("Enter the name of your recipes file: ")

try:
  file = open(my_file, 'rb')
  data = pickle.load(file)
  print("File loaded successfully!")
except FileNotFoundError:
  print("File doesn't exist - exiting.")
except: 
  print("An unexpected error has occurred.")
else:
  file.close()
finally:
  recipes_list = data['recipes_list']
  all_ingredients = data['all_ingredients']