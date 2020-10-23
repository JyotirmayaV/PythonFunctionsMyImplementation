from termcolor import colored
def lstrip_(s,removal):
    f = 0
    s1=""
    for i in s:
        if f == 0 and i in removal:
            pass
        else:
            f = 1
            s1 = s1 + i
    
    return s1


def rstrip_(s,removal):
    f = 0
    s1=""
    s = s[::-1]
    for i in s:
        if f == 0 and i in removal:
            pass
        else:
            f = 1
            s1 = i + s1
    
    return s1

def strip_(s,removal):
    s = lstrip_(s,removal)
    s = rstrip_(s,removal)
    return s

def execute(s,removal):
    print("--------------------Built by me : Built by Python : Difference----------------")
    print(colored("Effect of lstrip : ","blue"))
    s1 = lstrip_(s,removal)
    s2 = s.lstrip(removal)
    print(s1," : ",s2," : ",s1 == s2)
    print(colored("Effect of rstrip : ","blue"))
    s1 = rstrip_(s,removal)
    s2 = s.rstrip(removal)
    print(s1," : ",s2," : ",s1 == s2)
    print(colored("Effect of strip : ",'blue'))
    s1 = strip_(s,removal)
    s2 = s.strip(removal)
    print(s1," : ",s2," : ",s1 == s2)

execute("incomprehensibilities","is")





