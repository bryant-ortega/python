import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user='cf-python', passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id                  INT PRIMARY KEY AUTO_INCREMENT,
    name                VARCHAR(50),
    ingredients         VARCHAR(255),
    cooking_time        INT,
    difficulty          VARCHAR(20)
    )''')


def main_menu(conn, cursor):
   choice = ""
   while (choice != "quit"):
    print("Main Menu") + "\n"
    print("=============================") + "\n"
    print("Choose a function by number: ") + "\n"
    print("   1. Create a new recipe")
    print("   2. Search for a recipe by ingredient")
    print("   3. Update an existing recipe")
    print("   4. Delete a recipe")
    print("   5. View all recipes")
    print("\n   Type 'quit' to exit the program.")
    choice = input("Your choice: ")

    if choice == "1":
       create_recipe(conn, cursor)
    elif choice == "2":
       search_recipe(conn, cursor)
    elif choice == "3":
       update_recipe(conn, cursor)
    elif choice == "4":
       delete_recipe(conn, cursor)




def create_recipe(conn, cursor):
  recipe_ingredients = []

  name = str(input("\nEnter the name of the recipe: "))

  cooking_time = int(input("\nEnter the cooking time in minutes: "))

  ingredients_input = str(input("n\Enter the ingredients separated by comma: "))
  ingredients = ingredients_input.split(",")

  difficulty = calculate_difficulty(cooking_time, ingredients)


  # adds the recipe to the Recipes table
  sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
  val = (name, ingredients_input, cooking_time , difficulty)

  cursor.execute(sql, val)

  # Commits changes made to the Recipes table
  conn.commit()
  print("Recipe saved into the database.")



# def search_recipe(conn, cursor):
#   all_ingredients = []
#   cursor.execute("SELECT ingredients FROM Recipes")
#   results = cursor.fetchall()
#   for each ingredient in results:
     

def update_recipe(conn, cursor):
  # Display every recipe in full
  view_all_recipes(conn, cursor)

  # Asks the user to input the ID of the recipe he wants to update
  recipe_id_for_update = int((input("Choose a recipe ID to update: ")))

  # Asks the user which column they would like to update
  column_for_update = str(input("Which attribute (only one) would you like to change: name, cooking_time, or ingredients: "))

  # Asks the user to input the new value for the selected attribute
  updated_value = (input(f"Enter your new value of your {column_for_update}:"))
  print(f"{updated_value} will replace current {column_for_update} in recipe with ID: {recipe_id_for_update}")

  if column_for_update == "name":
    cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (updated_value, recipe_id_for_update))
    print("Recipe name successfully updated.")
  
  elif column_for_update == "cooking_time":
    cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (updated_value, recipe_id_for_update))
    print("Recipe cooking_time successfully updated.")
    # As cooking_time was changed, it is needed to recalculate the difficulty
    # At first we need to fetch the recipe parameters
    cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id_for_update, ))
    result_recipe_for_update = cursor.fetchall()

    name = result_recipe_for_update[0][1]
    ingredients = tuple(result_recipe_for_update[0][2].split(','))
    cooking_time = result_recipe_for_update[0][3]

    updated_difficulty = calculate_difficulty(cooking_time, ingredients)
    cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, recipe_id_for_update))
    print(f"Difficulty for {result_recipe_for_update} updated to: ", updated_difficulty)
  
  elif column_for_update == "ingredients":
    cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (updated_value, recipe_id_for_update))
    print("Recipe ingredients successfully updated.")

    # As ingredients were changed, it is needed to recalculate the difficulty
    # At first we need to fetch the recipe parameters
    cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id_for_update, ))
    result_recipe_for_update = cursor.fetchall()

    name = result_recipe_for_update[0][1]
    ingredients = tuple(result_recipe_for_update[0][2].split(','))
    cooking_time = result_recipe_for_update[0][3]
    difficulty = result_recipe_for_update[0][4]

    updated_difficulty = calculate_difficulty(cooking_time, ingredients)
    cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, recipe_id_for_update))
    print(f"Difficulty for {result_recipe_for_update} updated to: ", updated_difficulty)

  # Commits changes made to the Recipes table
  conn.commit()


def delete_recipe(conn, cursor):
  return


# function to define recipe difficulty
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = 'Intermediate'
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = 'Hard'
    else:
        print("Something went wrong")

    return difficulty

# get list of all saved recipes
def view_all_recipes(conn, cursor):
  print("\nAll saved recipes: ")
  print("==================")

  # Stores the entire list of recipes into results
  cursor.execute("SELECT * FROM Recipes")
  results = cursor.fetchall()

  # Displays the data from each recipe found
  for row in results:
    print("\nID: ", row[0])
    print("name: ", row[1])
    print("ingredients: ", row[2])
    print("cooking_time: ", row[3])
    print("difficulty: ", row[4])

main_menu(conn, cursor)