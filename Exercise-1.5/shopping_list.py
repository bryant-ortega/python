class ShoppingList(object):
  def __init__(self, list_name):
    self.list_name = list_name
    self.shopping_list = []

  # Method to add new items to self.shopping_list
  def add_item(self, item):
    if not item in self.shopping_list:
      self.shopping_list.append(item)
      print(f"{item} has been added to the {self.list_name} shopping list.")
    else:
      print(f"{item} is already in the {self.list_name} shopping list.")

  # Method to remove an item from self.shopping_list.
  def remove_item(self, item):
    try:
      self.shopping_list.remove(item)
      print(f"{item} has been removed from the {self.list_name} shopping list.")
    except:
      print(f"{item} is not found in the {self.list_name} shopping list.")

  # Method to view the contents of self.shopping_list.
  def view_list(self):
    print("\nItems in " + str(self.list_name) + '\n' + 30*'-')
    for item in self.shopping_list:
      print(' - ' + str(item))

  def merge_lists(self, obj):
    # creating a name for our new, merged shopping list
    merged_lists_name = 'Merged List - ' + str(self.list_name) + " + " + str(obj.list_name)

    # creating an empty ShoppingList object
    merged_lists_obj = ShoppingList(merged_lists_name)

    # Adding the first shopping list's items to our new list
    merged_lists_obj.shopping_list = self.shopping_list.copy()

    # Adding the second shopping list's items to our new list -
    # we're doing this so that there won't be any repeated items
    # in the final list, if both source lists contain common
    # items between each other
    for item in obj.shopping_list:
      if not item in merged_lists_obj.shopping_list:
        merged_lists_obj.shopping_list.append(item)

    # Returning our new, merged object    
    return merged_lists_obj




pet_store_list = ShoppingList("Pet Store Shopping List")
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

grocery_store_list = ShoppingList("Grocery Store List")

for item in ['fruits' ,'vegetables', 'bowl', 'ice cream']:
    grocery_store_list.add_item(item)

merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

merged_list.view_list()