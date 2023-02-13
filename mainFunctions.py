dic={" ":"00000","a":"00001"}

def ret(string):
    l=[dic[s.lower()] for s in string]
    l.append("00000")
    return l
print(ret(" A aa aaa "))