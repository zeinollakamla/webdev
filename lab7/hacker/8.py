#sWAP cASE

def swap_case(s):
    s2 = ""
    for i in s:
        if i.isupper()==True:
            s2 += i.lower()
        elif i.islower()==True:
            s2 += i.upper()
        else:
            s2 += i
    return s2

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result