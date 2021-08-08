#!/usr/bin/python3

import random
import argparse
from pypinyin.core import lazy_pinyin

# 随机将文本中的字母转换大小写
def random_case(text):
    text = "".join(lazy_pinyin(text))
    for i in range(len(text)):
        if text[i].isalpha():
            if random.randint(0,1) == 1:
                text = text[:i] + text[i].upper() + text[i+1:]
            else:
                text = text[:i] + text[i].lower() + text[i+1:]
    return text

def main():
    parser = argparse.ArgumentParser(description="仿池塘的大小写崩坏写的程序")
    parser.add_argument("text", help="输入的文本，可以是中文")
    args = parser.parse_args()
    print(random_case(args.text))

main()
