# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio

class T:
    def __hash__(self):
        return hash(0)
    def hash(self):
        return -1
    
obj = T()

print(f'{obj.hash() = }')  
print(f'{hash(obj) = }')   

