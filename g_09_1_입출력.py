import pandas as pd
from pandas import DataFrame, Series 

f = open("test.csv", "w")
f.write("1,2,3,4,5 \n")
f.close()

with open("test.csv", "a") as f:
    f.write("6,7,8,9,10 \n")
    f.write("4,5,6,7,8 \n")

with open("test.csv",'r') as f:
    for line in f:
        print(line)

# 'r'	Open a file for reading. (default)  
# 'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.  
# 'x'	Open a file for exclusive creation. If the file already exists, the operation fails.  
# 'a'	Open for appending at the end of the file without truncating it.   Creates a new file if it does not exist.
# 't'	Open in text mode. (default)  
# 'b'	Open in binary mode.  
# '+'	Open a file for updating (reading and writing)  

with open("test.csv", "w") as f:
    f.write("a,b,c,d,message \n")
    f.write("1,2,3,4,hello \n")
    f.write("5,6,7,8,world \n")
    f.write("9,10,11,12,foo \n")
    
df = pd.read_csv('test.csv', names=['A','B','C','D','E'])
df.to_csv('output.csv')

with open("output.csv",'r') as f:
    for line in f:
        print(line)
        
import os
lst = os.listdir()

# for x in lst:
#     print(x) 

# os.rename('test','new_one')
# os.remove('output.csv')
# os.rmdir('new_one')
# os.listdir()

import json
obj = """
{
    "name": "Kim",
    "places_lived": ["Seoul", "Korea"],
    "pet": null, "siblings": [{"name": "Scott", "age":25, "pet":"Zuko"}]
}
"""
result = json.loads(obj)
print(result)
print(type(result))

# json 타입
asjson = json.dumps(result)
print(asjson)
