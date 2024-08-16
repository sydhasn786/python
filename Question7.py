# **String Stripping and Justifying**

s:str = "   Python is fun!   "
s = s.strip()
print(s)
s= s.rjust(20,'*')
print(s)
s:str = "   Python is fun!   "
s = s.strip()
s= s.ljust(20,'*')
print(s)