[Running] python -u "c:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4\word_count_try.py"
Traceback (most recent call last):
  File "c:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4\word_count_try.py", line 22, in <module>
    with open("day4\\input1.txt", "r", encoding="utf-8") as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'day4\\input1.txt'

报错之后并没有产生后续的新的.json文件，因为在当前阶段整个py脚本运行中断了。而且当前文本不存在它也不会像后面的代码那样能够生成一个新的文件，因为这个是"r"只读不写入，所以无法生成文件。