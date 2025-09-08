import os
files = os.listdir()   
txt_count = 0
py_count = 0
for f in files:
    if f.endswith(".txt"):
        txt_count += 1
    elif f.endswith(".py"):
        py_count += 1
print("Text files:", txt_count)
print("Python files:", py_count)
