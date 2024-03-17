def totalCommonLetters(str1,str2):  #functino return the total number of common letters in two names
    list1=list(str1)
    list2=list(str2)
    arr=[]
    for i in list1:
        for j in list2:
            if(i==j):
                list2.remove(j)
                arr.append(i)
                break
    return len(arr)

def remainingLetter(name1,name2):  #functions return the remaining letters
    return len(name1)+len(name2)-(2*totalCommonLetters(name1,name2))

def checkArr(arr): # function check whether all the elements in the are equal or not
    result=False
    for i in arr:
        if(i==arr[0]):
            result=True
        else:
            result=False
            break
    return result

def findRelationLetter(n):  # the function return the relation letter between two names
    flames=["F","L","A","M","E","S"]
    arr=["F","L","A","M","E","S"]
    k=6
    while(True):
        arr+=(flames*n)
        ele=arr[n-1]
        arr=arr[n:]
        flames.remove(ele)
        for i in arr:
            if(i==ele):
                arr.remove(i)
        if(checkArr(arr)):
            arr=arr[0]
            break
    return arr



def finalRelation(ch):
    if (ch=='F'):
        return "Your are seems to be friends"
    elif (ch=='L'):
        return "So, You both are lovers!!"
    elif (ch=='A'):
        return "You're affectionate to each other"
    elif (ch=='M'):
        return "You're gonna marry each other in future"
    elif (ch=='E'):
        return "OOPS!! You don't like each other, Enemies:("
    else:
        return "Your both are soulmates, Stayforever"