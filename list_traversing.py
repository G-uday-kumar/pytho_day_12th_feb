my_list=[]
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list[3]="Uday"
print(my_list)
for i in range(0,len(my_list)):
    print("list elements with indx",i,my_list[i])

k=1
for element in my_list:

    print(k,". element without the index by using the other traversing methos:",element)
    k+=1

my_list.remove("Uday")
print(my_list)
my_list.insert(0,40)
print(my_list)
my_list.pop()#removes last values
print(my_list)
my_list.sort()
print(my_list)
l=my_list.count(10)
print(l)
y=my_list.copy()
print(y)
list_in_list=[1,2,3,4,5,[6,7,8,9]]
print(list_in_list)
my_list.sort(reverse=True)
print(my_list)
# list_in_list.sort()



# rev the given list
lis1t=[10,20,30,40,50,60,70,80,90]
res=[]
for i in range(len(lis1t)-1,-1,-1):
    res.append(lis1t[i])
print(res)

list1=[10,20,30,40,50,60,70,80,90]
sum=0
for i in range(len(list1)-1,-1,-1):
    sum+=list1[i]
print(sum[])
