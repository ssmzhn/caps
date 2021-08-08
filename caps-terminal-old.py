import sys
argv=sys.argv
def main():
    issmall=True
    ans=[]
    for x in argv[1:]:
        for y in x:
            if 65<=ord(y)<=90:
                if issmall==True:
                    tmp=chr(ord(y)+32)
                    ans.append(tmp)
                    issmall=False
                else:
                    ans.append(y)
                    issmall=True
            elif 97<=ord(y)<=122:
                if issmall==True:
                    ans.append(y)
                    issmall=False
                else:
                    tmp=chr(ord(y)-32)
                    ans.append(tmp)
                    issmall=True
            else:
                ans.append(y)
        ans.append(' ')
        issmall=True
    str2=''.join(ans)
    print(str2)

if len(argv)<=1:
    print('Usage: python '+argv[0]+' string')
    print('For example: python '+argv[0]+' hello world')
else:
    main()
