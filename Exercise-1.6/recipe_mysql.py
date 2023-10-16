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
    choice = input("Your Choice: ")

    if choice == "1":
       create_recipe(conn, cursor)



def create_recipe(conn, cursor):
  recipe_ingredients = []

  name = str(input("\nEnter the name of the recipe: "))

  cooking_time = int(input("\nEnter the cooking time in minutes: "))

  ingredients = str(input("n\Enter the ingredients separated by comma: "))
  return

  


def search_recipe(conn, cursor):
  return 

def update_recipe(conn, cursor):
  return ""

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



main_menu(conn, cursor)