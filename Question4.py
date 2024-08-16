# **Substring Search**

s:str = "the quick brown fox jump over the lasy dog"

find = s.find("fox")

if find == -1:
    print("index of fox is -1")
else:
    print(f"index of fox is {find}")    


count_of_the = s.count("the")
print(f"'the' appears {count_of_the} times")
