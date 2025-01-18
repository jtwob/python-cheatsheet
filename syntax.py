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
for i in range(4,8):
    print(i)

for idx, i in enumerate(z):
    i += 1
    z[idx] = i
    print(idx, i)

while(x < 10):
    x += 1
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

# continue below