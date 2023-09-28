import pickle

# function to display each recipe
def display_recipe(recipe):
  print('Name: ', recipe['name'])
  print('Cooking Time: ', recipe['cooking_time'])
  print('Ingredients: ', recipe['ingredients'])
  print('Difficulty: ', recipe['difficulty'])

def search_ingredient(data):
# add numbers to each ingredient
  index_all_ingredients = enumerate(data['all_ingredients'])
# display a list of all the ingredients
  list_all_ingredients = list(index_all_ingredients)
  print(list_all_ingredients)

  try:
    