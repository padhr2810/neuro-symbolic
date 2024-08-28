
# strings are immutable 
# so cannot simply do this: s1[0] = "x" 
# throws an exception

# APPROACH 1 TO RESOLVE THIS:
s1 = "the"
for c in "abc":
    s1 += c
print(f"s1 = {s1}")
  
# APPROACH 2 TO RESOLVE THIS:
str1 = "the"
list1 = list(str1)
list1[2] = 'u'
str1 = ''.join(list1)
print(f"str1 = {str1}")
