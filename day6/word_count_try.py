##我先将text全部小写，随后将所有小写字母列出来放入set中，让每一个字符全部判定一遍是否是小写字母，如果不是，将其改为空格。
##这样就能够保证不管是什么情况的字符都会被消除。
import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent
input_path = base_dir / 'input.txt'
output_path = base_dir / 'try_except_result.json'
#print('当前工作目录:', Path.cwd())
#print('实际输入路径:', input_path)
def word_count(text):
    set1 = set()
    for tik in 'abcdefghijklmnopqrstuvwxyz':
        set1.add(tik)
    text = text.lower()
    for mark in text:
        if mark not in set1:
            text = text.replace(mark, " ")
    words = text.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1    
    return counts

def main():
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"找不到输入文件：{input_path}")
        return

    demo = word_count(text)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(demo, f, ensure_ascii=False, indent=2)

    print(f"结果已保存：{output_path}")

if __name__ == '__main__':
    main()

#在读取文件或者写入文件时，.ipynb文件可以直接用该目录下的文件input.txt，而.py文件需要添加当前根目录day3\\input.txt



#10-12-day6:
#今天尝试使用try/except进行，当进行try时，如果文件不存在则出现：
#PS C:\Users\IPIC-ZQY\Desktop\codex\AI-infra> & C:\Users\IPIC-ZQY\AppData\Local\Programs\Python\Python313\python.exe c:/Users/IPIC-ZQY/Desktop/codex/AI-infra/day6/word_count_try.py
#找不到输入文件：C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day6\input.txt
#并且return直接结束当前main函数。
#如果未报错则继续进行下去，感觉跟if/else有些相似，但是其可以利用报错来进行，并且继续进程，而if，如果报错则会暂停程序。