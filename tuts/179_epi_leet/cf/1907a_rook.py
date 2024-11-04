# 1907a rook problem from CF

"""
verbatim:
for x,y,_ in[*open(0)][1:]:
    print(*{u+y for u in'abcdefgh'}^{x+u for u in'12345678'})
"""

print(open("data_1907a_rook.txt")) 
exit() 
    
if __name__ == "__main__":
    for x,y,_ in[*open("data_1907a_rook.txt")][1:]:
        # DOESN'T WORK IF OMIT THE ASTERISK AT *open() 
        # IF OMIT * YOU JUST GET AN  "IO.TEXTIOWRAPPER" OBJECT
        # IF INCLUDE * YOU GET THE VARIABLES I.E. DATA YOU WANT
        
        print(f"x = {x}")
        print(f"y = {y}")
        
        print("\n\nPRINTS ALL 8 COLUMNS i.e. A3 - H3:")
        for u in'abcdefgh':
            print(u+y)
            
        print("\n\nPRINTS ALL 8 ROWS i.e. D1 - D8:")
        for u in'12345678':
            print(x+u) 
        
        # CLEVER TRICK!
        # USE ^ ... COZ THIS REMOVES ONE SQUARE THAT SHOULDN'T BE THERE.
        # I.E. IN THIS CASE, 8 ^ 8 = 14 ... I.E. TURNS IT INTO 7+7
        print(*{u+y for u in'abcdefgh'}^{x+u for u in'12345678'})

