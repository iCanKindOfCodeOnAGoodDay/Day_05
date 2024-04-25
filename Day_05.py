"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 5
    April 25 2024

    ------
    Description:    Password Generator 
    ------
    
    ------
    Inputs:         Length, symbols, numbers
    ------
    
    ------
    Outputs:        Strong Password
    ------
    
    ------
    Dependencies:   Random
    ------

    ------
    Assumptions:    Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

import random


def main():
    """
    
    Description -   Creates random password, converts to string

    ----------                    
    Parameters -    Constants, user input
    ----------
    Output -        String - Strong password
    -------

    """
    print('Let\'s make you a password')
    possibles_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    possibles_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    possibles_symbols = ['!', '@', '#', '$', '%', '&', '*', '=', '+', '?']


    c_count = request_int('How many characters? ')
    
    s_count = request_int('How many symbols? ')
    
    n_count = request_int('How many numbers? ')
    
    S = create(s_count, possibles_symbols)
    
    N = create(n_count, possibles_numbers)
    
    L = create((c_count - s_count - n_count), possibles_letters)
    
    password = scramble_password_2( L + S + N )
    
    #eprint(convert_to_string(password))
    
    p = ''.join(password)
    
    print(f'Your password: {p}')
    
    
    
    

def create( count, possibles ):
    """
    
    Description -   Reusable func that takes that creates a random list of characters

    ----------                    
    Parameters -    Count, List of character choices
    ----------
    Output -        List
    -------

    """
    creation = [possibles[random.randint(0, len(possibles) - 1)] for i in range(count)]
    
    return creation
    

def scramble_password( unscrambled_password ):  
    """
    
    Description 
    ----------
    
    Scrambles password by creating a new list with elements ordered randomly based
    on random index
                    
    ----------
    Parameters -    List
    ----------
    Output -        String
    -------

    """
    s = []
    
    for i in unscrambled_password:
        
        s.append(unscrambled_password[random.randint(0, ((len(unscrambled_password) - len(s) - 1)))])

    return s


def scramble_password_2(unscrambled_password):
    """
    Description - Scrambles password by shuffling the elements in the list.
    ----------
    Parameters -    List
    ----------
    Output -        List
    -------
    """
    random.shuffle(unscrambled_password)
    
    return unscrambled_password


    
def request_int( prompt ):
    """
    
    Description - Input func modified to only accept integers
    ----------
    Parameters - Prompt
    ----------
    Output - Int
    -------

    """
    while True:
        
        try:
            
            num = int( input( prompt ) ) # parse string into int
            
        except ValueError:
            
            print( "Try again." )
            
            continue
        
        return num
    
    

# run code
if __name__ == '__main__':
    main()
    
    