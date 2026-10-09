##我先将text全部小写，随后将所有小写字母列出来放入set中，让每一个字符全部判定一遍是否是小写字母，如果不是，将其改为空格。
##这样就能够保证不管是什么情况的字符都会被消除。
import json


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
with open("day3\\input.txt", "r", encoding="utf-8") as f:
    text = f.read()
#counts_sort = {}
#counts_sort = sorted(word_count(text).values(), reverse=True)
#print(word_count(text))
demo = word_count(text)
with open("day3\\result.json", "w", encoding="utf-8") as f:
    json.dump(demo, f, ensure_ascii=False, indent=2)