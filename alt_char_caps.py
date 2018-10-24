#nnayak
#this program is to capitalize alternate characters in the string
#example: input = 'Abcde' | output = 'aBcDe'

def myfunc(s):
    mylist = list(s)
    newlist = []
    for index in range(len(mylist)):
        if index == 0:
            newlist.append(mylist[index].lower())
            #break
        elif index % 2 != 0:
            newlist.append(mylist[index].upper())
            #break
        else :
            newlist.append(mylist[index].lower())
            #break
    str1 =  ''.join(newlist)
    return str1