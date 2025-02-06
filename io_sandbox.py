import os
with open('test.txt', 'w') as f:
    f.write("Hello World!\n")

with open('test.txt', 'r') as f:
    content = f.read()
    print(content)

os.remove("test.txt")