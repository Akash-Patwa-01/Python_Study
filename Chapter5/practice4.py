s = set()
s.add(20) # 20 = 20.0 is same
s.add(20.0) # 20.0 = 20 is same
s.add("20")

print(s) # {'20', 20} 

print(len(s))