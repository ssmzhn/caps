import sys
argv=sys.argv
def main(isc=False):
    if isc:
        try:
            from pypinyin import lazy_pinyin
        except:
            print('You haven\'t installed pypinyin package yet. Use\"pip install pypinyin\" to install it.')
            sys.exit(255)
    issmall=True
    ans=[]
    if isc:
        tmp2=lazy_pinyin(' '.join(argv[2:]))
    else:
        tmp2=argv[1:]
    for x in tmp2:
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

opt=['-c','--chinese','-h','--help']
import re
if len(argv)<=1:
    print('Usage: python '+argv[0]+' [options] <string>')
    print('    For example: python '+argv[0]+' hello world')
    print('-c|--chinese: support Chinese characters')
    print('    Another example: python '+argv[0]+' [-c] 你好')
    print('-h|--help: get help')
elif argv[1][0]=='-' and not(argv[1] in opt):
    print('No such option. Type -h or --help for help.')
elif argv[1]=='-c' or argv[1]=='--chinese':
    if re.match('^哼{3}啊+$',' '.join(argv[2:])):
        print('臭死力')
    else:main(True)
elif argv[1]=='-h' or argv[1]=='--help':
    print('Usage: python '+argv[0]+' [options] <string>')
    print('    For example: python '+argv[0]+' hello world')
    print('-c|--chinese: support Chinese characters')
    print('    Another example: python '+argv[0]+' [-c] 你好')
    print('-h|--help: get help')
else:
    if re.match('^哼{3}啊+$',' '.join(argv[2:])):
        print('臭死力')
    else:main(False)
