# variable definition and assignment
x = 1
y = 0
z = [ 12, 8, 4 ]

# print
print(z[0] % z[2])

# branching 
if not x:
    print(x)
elif not y:
    print(y)
else:
    print(-1)

# loops
for i in range(4,8,2):
    print(i)

for idx, i in enumerate(z):
    i += 1
    z[idx] = i
    print(idx, i)

while(x < 10):
    x += 1
print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)


# special stuff
data = [
    {'id': 1, 'name': 'Jeff'},
    {'id': 2, 'name': 'James'},
    {'id': 3, 'name': 'Jeff'},
    {'id': 4, 'name': 'Alice'}
]

unique_name = set(item['name'] for item in data)

for name in unique_name:
    print(name)

# data structures

#set
cards = {"apple", "banana", "apple", "cherry"}
for item in cards:
    print(item)

#dictionary
state = {
    'name':'Colorado',
    'population': 5878000,
    'avg_home_price': 553534
}

print(state['avg_home_price'])

#array
list = [1, 2, 3, 4, 5]

print(list[:3])
print(list[3:])

# exception handling

x = 2
try:
    assert(x==1)
except:
    print("Nums not equal")

# reverse a string
a="python"
print("Reverse is", a[::-1])

# split a string

a="Python is the language of the future"
b=a.split()
print(b)

