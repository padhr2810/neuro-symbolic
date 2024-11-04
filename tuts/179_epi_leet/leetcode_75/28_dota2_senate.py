

"""
In the world of Dota2, there are two political parties: the RADIANT and the DIRE.

All senators are from these two parties. 
Now the Senate wants to decide on a change in the Dota2 game. 
The voting for this change is a round-based procedure. 
In each round, EACH SENATOR can exercise one of the TWO RIGHTS:

1- Ban one senator's right: A senator can make another senator lose all his rights in this and ALL the following ROUNDS.
2- Announce the victory: If this senator found the senators who still have rights to vote are ALL from the same PARTY, 
    he can announce the victory and decide on the change in the game.

INPUT: Given a string senate representing each senator's party belonging. 
    The character 'R' and 'D' represent the 2 parties.
    if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. 
This procedure will last until the end of voting. 
All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. 
Predict which party will finally announce the victory and change the Dota2 game. 

OUTPUT:
      The output should be "Radiant" or "Dire".
"""

from collections import deque 

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # TRICK: DEQUE - I.E. THIS HAS .popleft()
        #        ONLY NEED 2 METHODS - ".append()" AND ".popleft()"
        #        FIRST:
        #           INITIALISE 2 DEQUES - QR & QD FOR THE 2 PARTIES.
        #           PUT THE ENUMERATED COUNTER INTO THEIR RESPECTIVE QUEUES (DON'T PUT IN THE LETTERS)
        #        THEN RUN A WHILE LOOP UNTIL ONE OF THE QUEUES IS EMPTY:
        #           
        
        qr = deque()
        qd = deque()
        for i, c in enumerate(senate):
            if c == "R":
                qr.append(i)
            else:
                qd.append(i)
                
        n = len(senate)
        
        while_counter = 1 
        while qr and qd:
            print("\n\n################################################################################################")
            print(f"WHILE LOOP #{while_counter}:")
            print("################################################################################################")
            print(f"\nqd = {qd}")
            print(f"qr = {qr}")
            print(f"n = {n}")
            print(f"qr[0] < qd[0] = {qr[0] < qd[0]}")
            print(f"qr[0] + n = {qr[0] + n}")
            print(f"qd[0] + n = {qd[0] + n}")
            
            if qr[0] < qd[0]:
                qr.append(qr[0] + n)
            else:
                qd.append(qd[0] + n)
                
            qr.popleft()                ### POP BOTH QUEUES ON THE LEFT.
            qd.popleft()
            
            while_counter += 1
        return "Radiant" if qr else "Dire"

soln = Solution()
assert soln.predictPartyVictory(senate = "RD") == "Radiant"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

assert soln.predictPartyVictory(senate = "RDD") == "Dire"
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And the third senator comes from Dire and he can ban the first senator's right in round 1. 
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
