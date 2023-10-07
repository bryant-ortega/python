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


class Height(object):
  def __init__(self, feet, inches):
    self.feet = feet
    self.inches = inches
  
  def __str__(self):
    output = str(self.feet) + " feet, " + str(self.inches) + " inches, "
    return output
  
  def __sub__(self, other):
    # Converting both objects' heights into inches
    height_A_inches = self.feet * 12 + self.inches
    height_B_inches = other.feet * 12 + other.inches

    # Adding them up
    total_height_inches = height_A_inches - height_B_inches

    # Getting the output in feet
    output_feet = total_height_inches // 12

    # Getting the output in inches
    output_inches = total_height_inches - (output_feet * 12)

    # Returning the final output as a new Height object
    return Height(output_feet, output_inches)

    

person_A_height = Height(5, 10)
person_B_height = Height(3, 9)
height_difference = person_A_height - person_B_height

print("Total height:", height_difference)