l=[]
l1=[10,20,30,40,"uday"]

s = "kiran"
s1 = "kiran"

print(id(s))
print(id(s1))


print("bbb")
print(id(l1[4]))
print(l1)
print(type(l1))
print(id(l1[0]))
print(id(l1[1]))
l2=[10,20,10,20,"uday"]
print("bbb")
print(id(l2[4]))
print(id(l2[0]))
print(id(l2[1]))
print(id(l2[2]))
print("Create list with ten valus")
li=[10,20,30,40,50,60,70,80,90,99]
print(li[0:])
print(li[2:8:1])
print(li[7:3:1])
print(li[7:3:-1])
print(li[1:9:2])
print(li[5:])
print(li[-1])
print(li[-1::])
print(li[-1::-1])
print("Add data at run time")
n_list=[]
print((n_list))
for i in range(1,8):
    # l=int(input("enter ",i, "th number"))
    n_list.append(l)
print(n_list)
if l1[4]==l2[4]:
    print("hi")