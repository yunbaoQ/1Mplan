# Day 4 B：把现有词频程序整理好｜90分钟

你已经写出了“文字→词频字典”的函数。B围绕这份程序做三件事：固定找文件的方式、分开函数与运行入口、用小例子验证。不需要先看懂整页官方文档，也不需要另写一套词频算法。按下面步骤操作，每一步跑通再继续。

当前代码：word_count_try.py；已有py_error.md说明缺文件时脚本停止。这个观察正确，但自动报错停止不等于已经写了自己的异常处理。以下只是教学操作与结构提示，代码改动、测试和结果由你完成。

## 第一步：让程序总能找到同目录的输入（35分钟）

先在VS Code的day4目录自己创建input1.txt，写一行小英文并保存。当前目录没有这个文件；先有正常输入，才能验证成功路径。输出result.json会由程序写入，不需要手工创建。使用学习用的小文件。

你现在读取的是 day4\\input1.txt，这是相对“程序当前工作目录”找文件。如果工作目录已经是day4，会多找一层day4。它和文件是.py或.ipynb没有必然关系。

今天采用一个简单规则：在.py脚本旁边找input1.txt，结果也保存在脚本旁边。

在文件顶部的import区加入from pathlib import Path。接着在读取之前使用：

```python
base_dir = Path(__file__).resolve().parent
input_path = base_dir / 'input1.txt'
output_path = base_dir / 'result.json'
```

逐项理解：__file__指当前脚本的文件路径；resolve得到完整路径；parent取所在文件夹；/在Path对象这里拼接下一级路径，不是除法。最终input_path指day4里面的input1.txt。

只改两处：原open('day4\\input1.txt',...)改用open(input_path,...); 原open('day4\\result.json',...)改用open(output_path,...)。保留自己的计数函数。

先打印当前目录和目标输入，确认你读的是哪个文件：

```python
print('当前工作目录:', Path.cwd())
print('实际输入路径:', input_path)
```

用VS Code终端里已激活的torch311运行；没有激活先conda activate torch311。依次做两次启动（每行单独执行）：

```powershell
Set-Location -LiteralPath 'C:\Users\IPIC-ZQY\Desktop\codex\AI-infra'
python day4/word_count_try.py
Set-Location -LiteralPath 'C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4'
python word_count_try.py
```

两次工作目录不同，但实际输入路径应指向同一份input1.txt。打开result.json检查结果。以上__file__写法先只在.py脚本使用，普通Notebook不直接照搬。

## 第二步：分清“定义工具”和“运行流程”（35分钟）

word_count(text)像一个工具：给它文字，它返回字典。main()负责整套流程：找到路径→读取→调用词频函数→保存。这类似你熟悉的C++中主函数组织其他函数，但Python中仅仅命名main不会自动执行。

结构示意（不是完整替换答案；注释处放你自己已有的代码）：

```python
import json
from pathlib import Path

def word_count(text):
    # 保留你已有的计数逻辑，包括最后的 return counts
    pass

def main():
    # 路径设置、读取、计数、保存放在这里
    pass

if __name__ == '__main__':
    main()
```

不要把你已有word_count里的内容替换为pass；pass只是说明这里还有内容要填。将当前函数下面的文件操作搬到main里，每层多缩进4个空格；原with下面的代码还要继续多一层。word_count与main是两个并列函数，不相互嵌套。调试用的路径打印也放main里。

最后两行的意思：直接运行本文件时执行main；别人import本文件时，只定义这些函数，不自动开始读写文件。[官方入口说明](https://docs.python.org/3.11/library/__main__.html)。

在day4目录的同一终端验证：

```powershell
python word_count_try.py
python -c "import word_count_try; print('导入完成')"
```

第一行应按你的main处理输入。第二行应能导入，不自动执行main；检查结果文件不会因为单纯导入而重写。不要删文件来做此检查，可对照修改时间。还可以用下面的一次性调用验证函数能单独使用：

```powershell
python -c "import word_count_try; print(word_count_try.word_count('AI ai'))"
```

## 第三步：确认真的会用（20分钟）

用自己的函数测空串、重复词、大小写/标点、含数字的文字，写输入→预期→实际。按现有规则，非ASCII字母作为分隔符；规则暂不重写。

缺文件测试用一个明确不存在的新文件名，不删除正常输入。已有A-2输出可引用。目标是自己捕获FileNotFoundError，打印找不到哪条路径，然后结束main，不继续保存结果。可以查try/except/return语法，先理解这条错误路径，不追加复杂框架。

在python_notes.md写三句：脚本所在目录与当前工作目录有何区别；word_count和main分别做什么；为什么import不会自动读写文件。再简单说明清洗与字典计数的循环：反复replace会反复扫描字符串，不能把整程序简单记成线性，不要求今天先优化。

交付：你的修订word_count_try.py（文件名可保持）、input1.txt、生成的result.json、python_notes.md。不强制多个测试文件。

网页只作为需要时的参考：[pathlib](https://docs.python.org/3.11/library/pathlib.html)、[main入口](https://docs.python.org/3.11/library/__main__.html)、[异常](https://docs.python.org/3.11/tutorial/errors.html)。本次是学习帮助，收到指南不计完成；保留原90分钟预算。
