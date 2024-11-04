
"""
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 
0 means empty and 1 means not empty, and an integer n, 
return TRUE if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and false otherwise.
"""



class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
    
        ### TRICK: PAD THE FLOWER BED WITH 2 ZEROES. 
        ###     THEN NAIVELY ITERATE THROUGH.
        ###     SUBTRACT ONE FROM 'n' (I.E. TARGET EVERY TIME GET A HIT)
        ###     OK TO UPDATE THE ORIGINAL ARRAY IN-PLACE, DON'T CARE ABOUT IT.
        ###     LIMITATION: ITERATE THROUGH ENTIRE ARRAY EVEN IF 'n' <= 0
         
        ##### METHOD 1:
        f = [0] + flowerbed + [0]       ### BECAUSE IT'S OK TO PLANT AT THE EDGES.
        for i in range(1, len(f)-1):    ### BECAUSE 'f' IS 2 PLOTS LONGER NOW.
            if f[i-1] == 0 and f[i] == 0 and f[i + 1] == 0:     ### OBVIOUSLY NEED 3 IN A ROW.
                f[i] = 1                ### PLANT A FLOWER IN THIS PLOT.
                n-=1                    ### KNOCK ONE OFF THE TARGET.
        return n <= 0                   ### CHECK IF TARGET HAS BEEN REACHED.


        ##### METHOD 2:
        empty = 0 if flowerbed[0] else 1 
        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)
                empty = 0
            else:
                empty += 1

        n -= (empty) // 2
        return n <= 0 
        
soln = Solution()
assert soln.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1) == True 
assert soln.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2) == False  



