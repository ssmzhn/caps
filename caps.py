#!/usr/bin/python3

import random
import argparse
from pypinyin.core import lazy_pinyin

# 随机将文本中的字母转换大小写
class str_of_chitang(str):
    def chitang(self):
        text=self
        upper = False
        text = "".join(lazy_pinyin(text))
        for i in range(len(text)):
            if text[i].isalpha():
                if upper:
                    text = text[:i] + text[i].upper() + text[i+1:]
                    upper = False
                else:
                    text = text[:i] + text[i].lower() + text[i+1:]
                    upper = True
                #感谢 None 大佬的支持！
                """
                if random.randint(0,1) == 1:
                    text = text[:i] + text[i].upper() + text[i+1:]
                else:
                    text = text[:i] + text[i].lower() + text[i+1:]
                """
        return text

def main():
    parser = argparse.ArgumentParser(description="仿池沼的大小写114514写的程序")
    parser.add_argument("text", help="输入的文本，可以是中文，也可以是Homo语")
    args = parser.parse_args()
    #print(random_case(args.text))
    print(str_of_chitang(args.text).chitang())
if __name__=='__main__':
    main()
