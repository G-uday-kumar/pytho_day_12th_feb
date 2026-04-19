if __name__=="__main__":
    row=5
    k=1
    for i in range(1,row+1):
        for j in range(1,i+1):
            if k%2==0:
                print(1,end="")
            else:
                print(0,end="")
            k+=1
        print()