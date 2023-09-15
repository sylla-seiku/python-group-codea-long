#Write function that accepta and return an integar as input from user

def enter_an_integer (prompt) :
 
 while True:
    try:
     user_input = int(input(prompt))
     return user_input
    
    except ValueError:   # except Exception
      print("Value entered is not an int. Try again")


def enter_a_float (prompt) :
 
 while True:
    try:
     user_input = float(input(prompt))
     return user_input
    
    except ValueError:   # except Exception
      print("Value entered is not an float. Try again")

def enter_correct_data_type (prompt, data_type) :
 
 while True:
    try:
     user_input = data_type(input(prompt))
     return user_input
    
    except ValueError:   # except Exception
      print("Value entered is not the proper type. Try again")
"""
def enter_an_integer(propmt):
  return enter_correct_data_type(prompt, int)

def enter_a_float( propmt) :
  return enter_correct_data_type(prompt, float)
  
 """ 

int_1= enter_an_integer("Please enter your age as an integer ==>")
int_1 = enter_a_float("Please enter a float ==>")
      
def returns_nothing():
  pass


value_from_rn = returns_nothing()
print(f'{value_from_rn =}')




an_int = enter_correct_data_type(" Please enter an integar value ==> ",int)
print(an_int)

an_float = enter_correct_data_type(" Please enter an integar value ==> ",float)
print(an_float)


an_int = enter_an_integer (" Please enter an integar value ==> ")
print(an_int)

a_float= enter_a_float("Please enter a number with decimal digits ==>")
print(a_float)