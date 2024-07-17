print("problem 1")

s = 'fullstackslp'
print(s[0])
print(s[-1])
print(s[4:9])
print(s[-3:])
print(s[-5:-2])
print(s[::-1])

print("problem 2")
l = [3,7,[7,[1,4,'hello']]]
l[2][1][2]= "goodbye"

print(l[2][1][2])

print("problem 3")

d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2' : 'hello'}}
d3 = {'k1':[{'nest_key' :['this is deep',['hello']]}]}


print(d1["simple_key"])

print(d2["k1"]["k2"])

print(d3["k1"][0]["nest_key"][1][0])


print('problem 4')


mylist = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]

unique_elements = list(set(mylist))

print(unique_elements)

print('problem 5')

age =45

name = "Kyle"

my_string = "Hello my dog's name is {} and he looks {} years old" .format(name,age)

print(my_string)


