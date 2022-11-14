def is_dot_com(mystring):
   
   # doctest verify 
    '''
    >>> x = "vermos.ac.uk"
    >>> print(x)
    vermos.ac.uk
    '''
    if mystring[-6:] == 'ac.uk': 
     print(mystring) 
     return; True
     
    



import doctest
doctest.testmod(verbose=True)

# Test passed on console 
PS C:\Users\lucas\OneDrive\Desktop\Website> & C:/Python310/python.exe c:/Users/lucas/OneDrive/Desktop/Website/exam/designrecipe4.py
Trying:
    x = "vermos.ac.uk"
Expecting nothing     
ok
Trying:
    print(x)
Expecting:
    vermos.ac.uk
ok
1 items had no tests:
    __main__
1 items passed all tests:        
   2 tests in __main__.is_dot_com
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
PS C:\Users\lucas\OneDrive\Desktop\Website>
