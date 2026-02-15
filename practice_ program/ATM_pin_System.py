
attempt=3
key=1234
for i in range(attempt):
    passe = int(input("enter the pass ward:-"))
    if passe==key:
        print("access granted: ")
        break
    else:
        print("invalid access\n remaining attempt is:-", attempt-i-1)
else:
    print("card bloked")