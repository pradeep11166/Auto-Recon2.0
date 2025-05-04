import shutil
import os

a = open("gold.txt", "r")
b = a.readlines()

js = []


for x in b:
    c = x.strip()
    if ".js" in x:
        js.append(c)
fc = ".js"
for x in js:
    print(x[:x.index(fc)+len(fc)])

# for x in b:
#     c = x.strip()
#     if c.endswith(".js"):
#         js.append(c)


# for x in js:
#     print(x)
