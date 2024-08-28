
s1 = "the"
for c in "abc":
    s1 += c
print(f"s1 = {s1}")
  

str1 = "the"
list1 = list(str1)
list1[2] = 'u'
str1 = ''.join(list1)
print(f"str1 = {str1}")
