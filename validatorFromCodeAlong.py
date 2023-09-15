# Write function that accepts and return as input from user     
def enter_correct_data_type( prompt, data_type, error_msg ):    
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input          
        except ValueError:              # except Exception
            print(f"Value entered is not {data_type.__name__}. Try again")     
            print(error_msg)       
  
               
def enter_an_integer( prompt ):    
    return enter_correct_data_type(prompt, int)
    
def enter_a_float( prompt ):    
    return enter_correct_data_type(prompt, float)

int_1 = enter_an_integer("Please enter your age as an integer ==> ")
int_1 = enter_a_float("Please enter a float ==> ")

exit()
     
an_int = enter_correct_data_type("Please enter an integer value ==> ", int)
print(an_int)

a_float = enter_correct_data_type("Please enter a number with decimal digits ==> ", float)
print(a_float)