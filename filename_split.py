import os

answer = os.listdir("./")

for i in answer:
    print(i.split('.')[1])

