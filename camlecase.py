def word(s):
    count=0
    for i in range(len(s)):
        if i==0 or s[i].isupper():
            count+=1
    return(count)
s=str(input())
print(word(s))
