# class Date(object):
#   def __init__(self, day, month, year):
#     self.day = day
#     self.month = month
#     self.year = year

#   def get_date(self):
#     output = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
#     return output

  # def set_date(self):
  #   self.day = int(input("Enter the day of the month: "))
  #   self.month = int(input("Enter the month: "))
  #   self.year = int(input("Enter the year: "))

  # def is_leap_year(self):
  #   return self.year % 4 == 0

  # def is_valid_date(self):
  #   if not (type(self.day) == int and type(self.month) == int and type(self.year) == int):
  #     return False

  #   if self.year < 0:
  #     return False

  #   if self.month < 1 or self.month > 12:
  #     return False
    
  #   last_dates = {
  #     1: 31,
  #     2: 29 if self.is_leap_year() else 28,
  #     3: 31,
  #     4: 30,
  #     5: 31,
  #     6: 30,
  #     7: 31,
  #     8: 31,
  #     9: 30,
  #     10: 31,
  #     11: 30,
  #     12: 31
  #   }

  #   if self.day < 1 or self.day > last_dates.get(self.month):
  #     return False
    
  #   return True

# date = Date(1, 1, 2001)

# print(Date.get_date(date))


# class Height(object):
#   def __init__(self, feet, inches):
#     self.feet = feet
#     self.inches = inches
  
#   def __str__(self):
#     output = str(self.feet) + " feet, " + str(self.inches) + " inches, "
#     return output
  
#   def __sub__(self, other):
#     # Converting both objects' heights into inches
#     height_A_inches = self.feet * 12 + self.inches
#     height_B_inches = other.feet * 12 + other.inches

#     # Adding them up
#     total_height_inches = height_A_inches - height_B_inches

#     # Getting the output in feet
#     output_feet = total_height_inches // 12

#     # Getting the output in inches
#     output_inches = total_height_inches - (output_feet * 12)

#     # Returning the final output as a new Height object
#     return Height(output_feet, output_inches)
  
#   def __lt__(self, other):
#     height_inches_A = self.feet * 12 + self.inches
#     height_inches_B = other.feet * 12 + other.inches
#     return height_inches_A < height_inches_B
  
#   def __le__(self, other):
#     height_inches_A = self.feet * 12 + self.inches
#     height_inches_B = other.feet * 12 + other.inches
#     return height_inches_A <= height_inches_B
  
#   def __eq__(self, other):
#     height_inches_A = self.feet * 12 + self.inches
#     height_inches_B = other.feet * 12 + other.inches
#     return height_inches_A == height_inches_B
  
#   def __gt__(self, other):
#     height_inches_A = self.feet * 12 + self.inches
#     height_inches_B = other.feet * 12 + other.inches
#     return height_inches_A > height_inches_B
  
#   def __ge__(self, other):
#     height_inches_A = self.feet * 12 + self.inches
#     height_inches_B = other.feet * 12 + other.inches
#     return height_inches_A >= height_inches_B
  
#   def __ne__(self, other):
#     height_inches_A = self.feet * 12 + self.inches
#     height_inches_B = other.feet * 12 + other.inches
#     return height_inches_A != height_inches_B


  
# height_1 = Height(4, 10)
# height_2 = Height(5, 6)
# height_3 = Height(7, 1)
# height_4 = Height(5, 5)
# height_5 = Height(6, 7)
# height_6 = Height(5, 6)

# heights = [height_1, height_2, height_3, height_4, height_5, height_6]

# heights = sorted(heights, reverse=True)
# for height in heights:
#   print(height)

# class Person:
#   def walk():
#     print("Hello, I can walk!")

# class Athlete(Person):
#   def run():
#     print("Hey, I can run too")

# class Animal(object):
#     # Every animal has an age, but a name may not be necessary
#     def __init__(self, age):
#         self.age = age
#         self.name = None

#     # We'll throw in getter methods for age and name       
#     def get_age(self):
#         return self.age

#     def get_name(self):
#         return self.name

#     # And setter methods as well
#     def set_age(self, age):
#         self.age = age

#     def set_name(self, name):
#         self.name = name

#     # We'll also have a well-formatted string representation, too!
#     def __str__(self):
#         output = "\nClass: Animal\nName: " + str(self.name) + \
#             "\nAge: " + str(self.age)
#         return output
  
# class Cat(Animal):
#     # Introducing a new method where it speaks. init already inherited from Animal.
#     def speak(self):
#         print("Meow")

#     # Another neat string representation for cats
#     def __str__(self):
#         output = "\nClass: Cat\nName: " + str(self.name) + \
#           "\nAge: " + str(self.age)
#         return output
    
# class Dog(Animal):
#     # Implementing another speak() method for dogs
#     def speak(self):
#         print("Woof")
      
#     # String representation for dogs
#     def __str__(self):
#         output = "\nClass: Dog\nName: " + str(self.name) + \
#           "\nAge: " + str(self.age)
#         return output
    
# class Human(Animal):
#     def __init__(self, name, age):
#       # Calling the parent class' init method to initialize
#       # other attributes like 'name' and 'age'
#       Animal.__init__(self, age)

#       # Setting a name, since humans must have names
#       self.set_name(name)

#       # Our new attribute for humans, 'friends'!
#       self.friends = []

#     def add_friend(self, friend_name):
#         self.friends.append(friend_name)

#     def show_friends(self):
#         for friend in self.friends:
#             print(friend)

#     def speak(self):
#         print("Hello, my name's " + self.name + "!")

#     def __str__(self):
#         output = "\nClass: Human\nName: " + str(self.name) + \
#         "\nAge: " + str(self.age) + "\nFriends list: \n"
#         for friend in self.friends:
#             output += friend + "\n"
#         return output

# human = Human("Tobias", 35)

# human.add_friend("Robert")
# human.add_friend("Elise")
# human.add_friend("Abdoullah")
# human.add_friend("Asha")
# human.add_friend("Lupita")
# human.add_friend("Saito")

class Car(object):
  id = 0
  def __init__(self, name, model, year):
    self.name = name
    self.model = model
    self.year = year
    self.id = Car.id
    Car.id += 1

  def __str__(self):
    output = "\nID: " + str(self.id) + \
    "\nName: " + str(self.name) + \
    "\nModel: " + str(self.model) + \
    "\nYear: " + str(self.year)
    return output 


