# comment all lines and only uncomment demo code that you are interested with

# Input() 	vs    sys.stdin.readline()
# Input()  -- The input takes input from the user but does not read escape character. 	
# sys.stdin.readline()  --  The readline() also takes input from the user but also reads the escape character.

# IO_in1.txt
"""
3
1 2
5 7
6 3
"""

import sys
inputs = iter(sys.stdin.readlines())
TC = int(next(inputs))
for _ in range(TC):
    print(sum(map(int, next(inputs).split())))

# # IO_in2.txt
"""
1 2
5 7
6 3
0 0
1 1
"""

# import sys
# for line in sys.stdin.readlines():
#     if line == '0 0\n': break
#     print(sum(map(int, line.split())))

# # IO_in3.txt
"""
1 2
5 7
6 3
"""

# import sys
# for line in sys.stdin.readlines():
#     print(sum(map(int, line.split())))

# # IO_in3.txt, same input file as before
# import sys
# for c, line in enumerate(sys.stdin.readlines(), 1):
#     print("Case %s: %s\n" % (c, sum(map(int, line.split()))))

# # IO_in3.txt, same input file as before
# import sys
# for c, line in enumerate(sys.stdin.readlines(), 1):
#     if c > 1: print()
#     print("Case %s: %s" % (c, sum(map(int, line.split()))))

# # IO_in4.txt
"""
1 1
2 3 4
3 8 1 1
4 7 2 9 3
5 1 1 1 1 1
"""
# import sys
# for line in sys.stdin.readlines():
#     print(sum(map(int, line.split()[1:]))) # skip the first integer

# # IO_in5.txt
"""
1
3 4
8 1 1
7 2 9 3
1 1 1 1 1
"""

# import sys
# for line in sys.stdin.readlines():
#     print(sum(map(int, line.split())))
