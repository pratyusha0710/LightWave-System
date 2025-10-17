n= int(input("Enter the number of vehicle numbers to input: "))
cnt = 0
t = 0
Y = ""
for k in range(1,n+1):
        x=input("Enter information of vehicle"+str(k)+": ")
        if x.startswith("UP")==True:
                Y = x[-4::]
                t=int(Y, base=10)
                if t>5555:
                        cnt+=1
print(cnt)