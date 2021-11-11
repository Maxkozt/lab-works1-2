print("""This program have two function. 
First calculates the number of each letter.
Second makes a dictionary of the provided words.
If you need first function write 1, otherwise write 2 if you need second function. """)   
decision = input("Write number: ")


if decision == 1:
    text = str.lower(input("Please write you text: "))
    print("Your list")
    print(' a =',text.count('a'),'\n b =', text.count('b'),'\n c =', text.count('c'), '\n d =', text.count('d'),'\n e =', text.count('e'),
'\n f =', text.count('f'), '\n g =', text.count('g'), '\n h =', text.count('h'), '\n i =', text.count('i'), '\n k =', text.count('k'),
'\n l =', text.count('l'), '\n m =', text.count('m'), '\n n =', text.count('n'), '\n o =', text.count('o'),
'\n p =', text.count('p'), '\n q =', text.count('q'), '\n r =', text.count('r'), '\n s =', text.count('s'), '\n t =', text.count('t'),
'\n u =', text.count('u'), '\n v =', text.count('v'), '\n w =', text.count('w'), '\n x =', text.count('x'), '\n y =', text.count('y'), '\n z =', text.count('z'))

elif decision == 2:
    word = str.lower(input("Please write you text: "))
    print("Your dictionary")
    dictionary = sorted(word.split())
    print('\n'.join(dictionary))

