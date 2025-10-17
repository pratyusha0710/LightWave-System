s = input('Enter string: ')
sh = input("Enter the shift of the cipher: ")
t = input("Type e for encryption or d for decryption: ")
s1 = ""
if sh == "":
    shift = 13
else:
    shift = int(sh, base=10)
if t.lower() == "d":
    shift = -shift
for i in s:
    if 'A' <= i <= 'Z':
        s1 += chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
    elif 'a' <= i <= 'z':
        s1 += chr((ord(i) - ord('a') + shift) % 26 + ord('a'))
        
print(s1)