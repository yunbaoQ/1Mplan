# B-2 分步提示｜2026-10-09

现有 word_count(text) 已接收字符串并返回字典。新内容只有文件读取、JSON 保存与失败处理，暂不要求命令行参数、类或复杂工程。下面是教学片段，不是完整作业脚本；用户将它们与自己的函数衔接后保存、运行。

## 1. 先验证读取（15分钟）

在 day3 自己创建 UTF-8 文本 input.txt，写一小段英文。从 day3 目录运行程序，观察：

```python
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)
print(type(text))
```

open 打开文件，r 表示只读，read 返回字符串，with 在离开代码块时关闭文件。相对路径以运行时当前工作目录为起点，不自动以脚本位置为起点。看到文件原文后，再把 text 交给已有词频函数。

## 2. 单独理解 JSON 保存（15分钟）

先用与作业无关的小字典演示：
```python
import json
demo = {"apple": 2, "pear": 1}
with open("demo_result.json", "w", encoding="utf-8") as f:
    json.dump(demo, f, ensure_ascii=False, indent=2)
```

w 写入并覆盖同名文件；选用自己的新练习输出文件。dump 把对象写为 JSON；indent=2 便于阅读，ensure_ascii=False 避免非ASCII字符被转成转义序列。打印字典不会自动生成文件。

## 3. 自己衔接（20分钟）

用读到的字符串调用自己的 word_count，把返回字典交给 JSON 保存操作，结果存为自己新建的 result.json。第二份输入由自己准备。检查文件词频和之前直接传字符串时的行为一致。

不要只照抄 demo 中的水果字典作为作业输出；核心是把自己函数的结果交给保存动作。

## 4. 文件不存在（10分钟）

在“读取 input.txt”外层写 try/except FileNotFoundError，捕获时打印你自己的清楚提示；只有读取成功时才计数和保存，可以把后续操作放 try 的 else 内。换成不存在的文件名实际验证一次。暂不要求捕获全部异常。

验收：两份输入对应正确结果文件；失败时能给出提示；本人能解释每步数据类型。当前只是收到教学提示，不计 B-2 完成。

资料：[文件读写](https://docs.python.org/3.11/tutorial/inputoutput.html#reading-and-writing-files)、[JSON](https://docs.python.org/3.11/library/json.html)。
