recipes_list = []
ingredients_list = []

def take_recipe(name='No name', cooking_time='No cooking time', ingredients='No ingredients', recipe='No recipe'):
  name = input("Enter your recipe name: ")
  cooking_time = int(input("Enter your recipe's cooking time in minutes: "))
  ingredients = input("Enter your recipe's ingredients: ").split(", ")

  recipe = {
    'Name': name, 
    'Cooking_time': cooking_time, 
    'Ingredients': ingredients
    }
  return recipe

n = int(input("How many recipes would you like to enter?: "))

for i in range(n):
  recipe = take_recipe()
  for ingredient in recipe['Ingredients']:
    if ingredient not in ingredients_list:
      ingredients_list.append(ingredient)
  recipes_list.append(recipe)

for recipe in recipes_list:
  if recipe['Cooking_time'] < 10 and len(recipe['Ingredients']) < 4:
    difficulty = 'Medium'
  elif recipe['Cooking_time'] >= 10 and len(recipe['Ingredients']) < 4:
    difficulty = 'Intermediate'
  elif recipe['Cooking_time'] >= 10 and len(recipe['Ingredients']) >= 4:
    difficulty = 'Hard'
  elif recipe['Cooking_time'] < 10 and len(recipe['Ingredients']) >= 4:
    difficulty = 'Intermediate'
  

  print('===================================')
  print('Recipe: ', recipe['Name'])
  print('Cooking Time (min): ', recipe['Cooking_time'])
  print('Ingredients: ')
  for ingredient in recipe['Ingredients']:
    print(ingredient)
  print('Difficulty level: ', difficulty)
  
print("---------------------------------------------\nIngredients used across all recipes\n===================================")
sorted_list = sorted(ingredients_list)

for ingredient in sorted_list:
    print(ingredient)