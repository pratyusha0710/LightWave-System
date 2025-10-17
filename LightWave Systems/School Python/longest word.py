str = input("Enter sentence: ")
s1 = ""
l = str.split(" ")
for i in l:
        if len(i) > len(s1):
                s1 = i
print(s1)