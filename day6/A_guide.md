# Day6 A-1 / A-3 / A-4：用途与完成流程

这是教学说明，示例代码和预期结果不算你的完成记录。预算仍为A共60分钟，不增加练习量。A-1与A-4的缺文件检查合并为一次；已有本人测试记录可直接引用，不重做。

## A-1：try/except入门与缺文件处理（15分钟）

你在Day4已经观察过FileNotFoundError，并正确说明：读取失败，后续没有产生新JSON。这项观察已有证据，不要求重新证明“Python会报错”。

当前day4/word_count_try.py的main直接open读取，尚未捕获这个异常。今天只补：找不到输入时，告诉使用者哪个路径找不到，并结束当前处理；成功读取才统计、写结果。比如将来模型配置/权重路径写错，程序应让你迅速知道问题在哪里，不把失败输入当成功继续处理。

流程由你加入自己的main：
1. 读文件这一步放进try。
2. 用except FileNotFoundError捕获对应异常。
3. 异常分支打印明确路径，再return结束main；不要只是打印完继续写结果，也不要假造空内容继续。
4. 成功读取后沿用现有统计/JSON逻辑。

只验证一次新增行为：将练习版本的input_path临时指向一个不存在的新文件名，output_path使用专门的新测试文件名，正常原文件不删除、不重命名。预期是你的提示出现且不产生该测试输出。记录提示与输出是否存在，随后恢复正常路径。这条记录同时计入A-4第4行。

无须为了作业收集多种报错。完成这次后，这个问题不再当每日固定练习；以后相关代码有改动或真实故障时再检查。

参考：[Python异常处理](https://docs.python.org/3.11/tutorial/errors.html)。交付自己的修订代码与一次真实记录。

### 对照你现有脚本的具体修改

1. 自己把day4/word_count_try.py复制到day6，保留原文件；把正常输入input1.txt也放到day6（可复制自己的原输入）。已有word_count、import和最后的main入口都保留。
2. 将练习版本的output_path改为base_dir / 'try_except_result.json'，避免覆盖旧结果。
3. 只将main换成下面的教学示例，由你自己整合并运行：

~~~python
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
~~~

try里面尝试读取；except只在发生FileNotFoundError时进入；return结束main。因此读取失败时，下面的统计和写JSON不会执行。except与try对齐，return在except内；不要把所有后续逻辑缩进异常分支。

4. 正常输入路径保持input1.txt，运行一次。预期：统计成功，输出结果文件，并打印结果保存路径。
5. 再将input_path改为base_dir / 'missing_input_for_test.txt'（确认该文件不存在），output_path改为一个尚不存在的新测试输出名，例如base_dir / 'missing_case_result.json'。运行一次，预期看到自己写的缺文件提示，不产生该新输出。
6. 恢复正常路径，保存两种真实记录。异常这一次同时用于A-4，不另做一遍。记录“复制了教学代码”之外，还要能解释return为什么放这里。

本段是语法教学示例，不是教练替你修改或执行了练习；需由你整合、观察并解释。


## A-3：按维度求和、转换类型、理解偏置广播（20分钟）

新建day6/A3_tensor.ipynb（或.py），选已有torch311环境，全部在CPU做。无需重新安装，也无需故意制造shape错误。

### 第1步：创建小矩阵（约3分钟）

先运行：

~~~python
import torch
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]], dtype=torch.int64)
print(x)
print(x.shape, x.dtype)
~~~

shape=(2,3)表示两行三列，dtype表示元素的数据类型。

### 第2步：先算，再运行求和（约6分钟）

在文本格里先写自己的预测：
- dim=0：沿第0维合并上下两行，逐列相加，每列得到一个数。
- dim=1：沿第1维合并一行里的三个位置，逐行相加，每行得到一个数。

写好预测值和shape后，自己添加并运行这几行：

~~~python
s0 = x.sum(dim=0)
s1 = x.sum(dim=1)
print(s0, s0.shape)
print(s1, s1.shape)
~~~

这里使用默认keepdim=False，求和的那个维度不保留。检查预测与实际是否一致；不一致就解释自己之前把哪一维弄反了。不要直接复制示例当“本人手算”。

### 第3步：把整数转换为浮点（约4分钟）

~~~python
x_float = x.to(torch.float32)
print(x.dtype, x_float.dtype)
print(x_float)
~~~

注意接住to返回的结果。记录转换前/后类型，说明“类型变化，当前整数值转换后数值仍对应”。下一步求导训练要用浮点张量，这项是准备知识。

### 第4步：看一个长度2的偏置如何加到每行（约4分钟）

~~~python
scores = torch.zeros((2, 2))
b = torch.tensor([0.5, -0.5])
print(scores.shape, b.shape)
print(scores + b)
~~~

先预测每行会变成什么，再运行。scores是两行、每行两个输出；b的两个数分别对应两个输出位置，同一组偏置应用到每行。b实际shape是(2,)，不需要真的复制成两行才能相加。广播按末尾维度对齐，这个例子相当于将(1,2)应用到(2,2)。

### 第5步：保存解释（约3分钟）

在closure_notes.md里写：
1. dim=0和dim=1在这个二维例子分别合并什么，结果shape是什么。
2. 转换前后dtype，to的返回值保存在了哪个变量。
3. b实际shape，以及为什么每一行都能加它。

验收是你的预测、实际输出与解释。代码可参考这份教学片段，但不能只有复制的代码而没有输出/理解记录。

API参考：[sum](https://docs.pytorch.org/docs/2.11/generated/torch.sum.html)、[Tensor.to](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.to.html)、[广播规则](https://docs.pytorch.org/docs/2.11/notes/broadcasting.html)。不需要通读网页。

## A-4：检查你自己的词频程序（15分钟）

测试对象是已有word_count函数，以及A-1改过的文件读取流程。正常输入、边界输入都测；不是要求搜集报错。

| 检查 | 输入/动作 | 预期 | 你填写的实际 |
| --- | --- | --- | --- |
| 空输入 | word_count("") | {} | 待本人运行 |
| 重复与大小写 | word_count("AI ai AI") | {"ai":3} | 待本人运行 |
| 非字母作分隔 | word_count("Hello,AI! abc123def") | {"hello":1,"ai":1,"abc":1,"def":1} | 待本人运行 |
| 文件缺失 | A-1用不存在路径运行main | 明确提示路径；不产生本次测试输出 | 直接引用A-1一次记录 |

前3行可在Notebook导入自己的函数后分别调用，不用每次改输入文件；这三行验证计数/清洗，最后一行验证文件处理。字典键顺序不影响结果比较。abc123def按你当前“非a-z是分隔符”的规则应分为abc/def。

有本人之前保存的同等测试，写文件入口即可；教练先前的检查不能写成你自己运行了。表格放closure_notes.md，不要求写测试框架或重写词频函数。

最后用一句话解释复杂度：当前循环内反复replace会多次扫描字符串，最坏可能达到O(n²)，不能仅因外层看起来一个循环就写整体O(n)。今天只说明，不要求优化重写。

A-1/A-3/A-4做完就进入B自动求导，不为了凑预算反复练同一输入。

