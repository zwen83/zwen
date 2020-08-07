#key-value

dict1 = {'tom':60,"lilei":70}
print (dict1["tom"],dict1.get("sunck"))
dict1["hanmeimei"] = 99


print (dict1)

for k in dict1:
    print(k)
print (dict1.items())
for k,v in dict1.items():
    print(k,v)

for k,v in enumerate(dict1):
    print (k,v)


import re
timeStr = input()

time1 = re.split(r'[&*:\s]\s*',timeStr)

h = int(time1[0])
m = int(time1[1])
s = int(time1[2])

s += 1
if s == 60:
    m += 1
    s = 0
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0
print("%.2d:%.2d:%.2d"%(h,m,s))