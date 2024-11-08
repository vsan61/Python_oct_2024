 #Create an empty list
list1=[]
print(type(list1))
#Concatenate with [5,6,7,8]
list2=[5,6,7,8]
print(list1+list2)
#add 8,9,1,5,6,7,8,1 elements to that list
list3=[8,9,1,5,6,7,8,1]
print(list2.extend(list3))
#Find frequency of 8 (count)
print(list2.count(8))
#find the mean of the list
mean=(sum(list2)/len(list2))
print(f"mean of the list2 is {float(mean)}")
#find sum (List) + min + Max
print(f"Minimum value of list2 is {min(list2)} and Maximum value of list2 is {max(list2)}")
#remove duplicates from list and give output in the format of tuple
print(tuple(set(list2)))
#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
t1=(1,4,5,6,7,8)
t2=(5,6,7,8,9)
#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple
s=t1+t2
print(tuple(set(s)))
#Find the index value of 9 (after concatenation)
print(s.index(9))
#multiply above elements 3 times
print(s * 3)
#Create two empty sets
set1=set()
set2=set()
print(type(set1))
print(type(set2))
#update set1 with 7,8,9,1,2,3,4,5,0 and #update set2 with 4,5,6,0
#update set1 with 7,8,9,1,2,3,4,5,0 and #update set2 with 4,5,6,0
set1={7,8,9,1,2,3,4,5,0}
set2={4,5,6,0}
set1.update(set1)
print(set1)
#check whether set2 is subset of set1 or no ?
print(set2.issubset(set1))
#check whether both have common elements are no ?
print(set2.issuperset(set1))
#remove 8 from set 1 and set 2 ==> and #discard 0 from set1 and set2
set1.remove(8)
set2.discard(8)
set1.discard(0)
set1.discard(0)
print(set1)
print(set2)
#find collection of both sets ===> set1 and set2
set1.intersection(set2)
print(set1)
#create a dictionary {1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
dict1={}
print(type(dict1))
dict1={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
print(dict1)
#Extract "bobtn" from above dictionary
print(dict1[3][0][0:9:2])
#Extract "arbeg" from above dictionary
print(dict1[3][2][:-6:-1])
#print all keys in dictionary and convert it into tuple
print(tuple(dict1.keys()))
#Find the average of all numbers available under key "2"
dict2={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
a=dict2[2]
print(sum(a)/len(a))


