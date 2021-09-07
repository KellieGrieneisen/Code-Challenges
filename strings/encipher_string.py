"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""

 

def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""
    # list of the alphabet accounting for both upper and lower case. 
    # ignore symbols.

    alpha = list('abcdefghijklmnopqrstuvwxyz')
    Alpha=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
   
    # create list to save encoded characters
    new_txt=[]

    for ch in txt:

        # check character against alphabets
        if ch in alpha:
            new_txt.append(alpha[(alpha.index(ch) + shift) % 26])
        elif ch in Alpha:
            new_txt.append(Alpha[(Alpha.index(ch) + shift) % 26])
            
        else:
            # if not a character just append the symbol
            new_txt.append(ch)

    # return as string
    return ''.join(new_txt)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
