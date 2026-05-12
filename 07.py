file = open('example.txt', 'r')
print(file.read())
print(file.closed)

with open ('example.txt', 'r')as file_in_open:
    print(file_in_open.read())
    print("Againn")
    print(file_in_open.read())
print(file_in_open.closed)

with open('newfile.txt', 'w') as file_in_write:
    file_in_write.write("Hello World!!!")

with open('example.txt', 'r') as file:
    print(file.read())
 
# with open('newfile_exclusive.txt', 'x') as file_in_write:
#     file_in_write.write("Hello World!!!")

import os
print(os.path.exists("example.txt"))
print(os.path.exists("random.txt"))

from pathlib import Path
file_path = Path('example.txt')

 