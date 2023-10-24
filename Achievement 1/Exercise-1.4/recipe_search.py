import pickle

# function to display each recipe
def display_recipe(recipe):
  print('Name: ', recipe['Name'])
  print('Cooking Time: ', recipe['Cooking_time'])
  print('Ingredients: ')
  for ingredient in recipe['Ingredients']:
    print(ingredient)
  print('Difficulty: ', recipe['Difficulty'])

def search_ingredient(data):
# add numbers to each ingredient
  index_all_ingredients = enumerate(data['all_ingredients'])
# display a list of all the ingredients
  list_all_ingredients = list(index_all_ingredients)
  print(list_all_ingredients)

  try:
    n = int(input("Enter the number of the corresponding ingredient you want to search for: "))
    ingredient_searched = list_all_ingredients[n][1]
  except:
    ingredient_searched not in list_all_ingredients
    print("Oops incorrect input. Please choose a number that corresponds to an ingredient listed.")
  else:
    for recipe in data['recipes_list']:
      if ingredient_searched in recipe["Ingredients"]:
        print('\nThe following recipe includes your searched ingredient: ')
        print('------------------------------------------------------')
        display_recipe(recipe)


# user enters their file name
filename = input("Enter file name that contains your recipes: ")

# opens the file, and then extract its contents into data
try:
  file = open(filename, 'rb')
  data = pickle.load(file)
  print("File loaded successfully!")
except FileNotFoundError:
  print("File doesn't exist - exiting.")
else:
  search_ingredient(data)

finally:
  file.close()
