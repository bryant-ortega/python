class ShoppingList(object):
  def __init__(self, list_name):
    self.list_name = list_name
    self.shopping_list = []

  # Method to add new items to self.shopping_list
  def add_item(self, item):
    if item not in self.shopping_list:
      self.shopping_list.append(item)
      print(f"{item} has been added to the {self.list_name} shopping list.")
    else:
      print(f"{item} is already in the {self.list_name} shopping list.")

  # Method to remove an item from self.shopping_list.
  def remove_item(self, item):
    if item in self.shopping_list:
      self.shopping_list.remove(item)
      print(f"{item} has been removed from the {self.list_name} shopping list.")
    else:
      print(f"{item} is not found in the {self.list_name} shopping list.")

# Method to print the contents of self.shopping_list.
  def view_list(self):
    print()
    print(self.list_name)
    print("---------------")
    for item in self.shopping_list:
      print(item)
    print()

pet_store_list = ShoppingList("Pet Store Shopping List")
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

pet_store_list.view_list()

pet_store_list.remove_item("flea collars")

pet_store_list.add_item("frisbee")

pet_store_list.view_list()