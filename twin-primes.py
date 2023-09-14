# List twin primes < a given number
# p1 and p2 are twin primes iff both are prime and p1 + 2 = p2
#
# Need a function that determines if a candidate number is prime
# Iterate (loop) over numbers between 2 and the candidate
# If any iterated number evenly divides the candidate then the candidate
# is not prime; FUNCTION RETURNS FALSE
# If the loop executes to completion (without returning False) RETURN TRUE
def is_prime(candidate): 
    for num in range(2, candidate):
        if candidate % num == 0:
            return False
        
    return True

# Write a function that accepts a single integer parm to serve
# as the upper bound for the twin prime table (find twin primes < upper bound)
# The function should SAVE AND RETURN the twin primes in an appropriate structure
# Initialize a structure to hold the twin primes
# Iterate (loop) over numbers 2 to upper bound
# Inside the loop, add 2 to the loop iterate variable, assign to another variable 
# Check if both numbers are prime. If so, we have a pair of twins; 
# Add them to the structure
# When the loop terminates, return the structure containing the twin primes 
def find_twin_primes_loop(upper_bound):
    twin_primes = []
    for num in range(2, upper_bound):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append( (num, num + 2) )
            
    return twin_primes  

def find_twin_primes(bound):
    '''
    def is_prime(candidate): 
        for num in range(2, candidate):
            if candidate % num == 0:
                return False   
        return True
    '''
    return [ (num, num + 2) for num in range(2, bound) if is_prime(num) and is_prime(num+2)]
      
            
# Set a bound and call the function
bound = 1_000
twin_primes = find_twin_primes(bound)
# Let's print them here
# 269 and 271 are twin primes
for pair in twin_primes:    # pair (333, 555)
    print(f'{ pair[0] } and { pair[1] } are twin primes')
    
for pair0, pair1 in twin_primes:
    print(f'{ pair0 } and { pair1 } are twin primes')
    

# We can use a comprehension instead of the loop in function find_twin_primes
twin_primes = [ (num, num + 2) for num in range(2, bound) if is_prime(num) and is_prime(num+2)]