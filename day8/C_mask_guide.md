# Day8 C：给Attention规定“允许参考到哪里”｜90分钟

先联想补全句子：已看到“我想喝一杯”，你需要猜接下来是什么。猜的时候未来的答案尚不存在，因此只能参考已看到的部分。训练时往往把完整序列一起送入网络，也要阻止前面位置读取后面信息，否则会把后续答案泄漏给预测。

今天做的是**因果mask**：给B的Attention加一张允许/禁止参考的表。对输入位置i的表示，允许参考位置0到i，包括自己；这个表示随后可以用于预测下一个token，因此不是把要预测的下一个token放进允许范围。其他阅读理解场景可能允许看整段文字，这个限制用于从左到右的生成任务。[原论文的Decoder masking说明](https://arxiv.org/html/1706.03762v7#S3.SS1)

B决定“参考各个位置多少”，C决定“哪些位置根本不允许参考”。代码写在原attention_practice.ipynb后面，不重新创建模型，不重训。以下都是教学代码格；本人需要实际运行、记录结果和解释。

## 第1步：把三个位置的规则看懂｜10分钟

三个位置依次叫A、B、C。第0行是在处理A，它只能参考A；第1行处理B，可以参考A/B；第2行处理C，可以参考A/B/C。

| 当前查询 | 参考A | 参考B | 参考C |
| --- | --- | --- | --- |
| A | 允许 | 禁止 | 禁止 |
| B | 允许 | 允许 | 禁止 |
| C | 允许 | 允许 | 允许 |

规则与分数表一样：行是查询位置，列是参考位置。这里和序列的先后有关，不是根据分数高低临时选位置。

## 第2步：保留B的原始数据，创建这张表｜15分钟

B最后的Q_changed只用来对照；C回到原Q，不用零查询的结果。先运行B中定义原Q/K/V的格子，然后运行这一格：

```python
# 需要B已经定义原Q、K、V，并import math和torch
scores_base = (Q @ K.T) / math.sqrt(Q.shape[-1])
weights_base = torch.softmax(scores_base, dim=-1)
output_base = weights_base @ V

allowed = torch.tensor([
    [True,  False, False],
    [True,  True,  False],
    [True,  True,  True ],
])
print("允许参考的位置：\n", allowed)
print("未屏蔽的权重：\n", weights_base)
```

这里True表示允许，False表示禁止。今天使用的是自己定义的allowed表，不把其他Attention接口的布尔mask规则混在一起。

## 第3步：在softmax之前屏蔽分数｜20分钟

```python
scores_masked = scores_base.masked_fill(~allowed, float("-inf"))
weights_masked = torch.softmax(scores_masked, dim=-1)

print("屏蔽后的分数：\n", scores_masked)
print("屏蔽后的权重：\n", weights_masked)
print("每行权重之和：", weights_masked.sum(dim=-1))
```

逐个读懂：`~allowed`把允许/禁止翻转，选中原来False的位置；`masked_fill`给这些位置填负无穷，返回新张量，原scores_base保留。softmax中负无穷对应的指数为0，所以禁止位置不分到参考比例，其余允许位置重新分配比例。

**不要填0来表示禁止。** softmax会计算exp(0)=1，填0仍会分到比例。也不要把一整行都屏蔽：本实验保留对角线，每行至少一个允许位置。

预期第0行权重是[1,0,0]；第1行最后一个权重是0；三行的权重和都约1。将预期和自己打印的实际输出比较。[官方参考实现中的causal mask](https://docs.pytorch.org/docs/2.11/generated/torch.nn.functional.scaled_dot_product_attention.html)

## 第4步：看输出是怎样被限制的｜20分钟

```python
output_masked = weights_masked @ V
print("无mask输出：\n", output_base)
print("有mask输出：\n", output_masked)
print("第一行是否等于V第一行：",
      torch.allclose(output_masked[0], V[0]))
```

第0行只允许参考V[0]，比例是1，所以输出等于V[0]。第1行只由V[0]/V[1]组成，不会混入V[2]；第2行三个都允许。使用打印出的第1行比例，把该行两个输出分量分别展开手算。

## 第5步：故意改变“未来内容”｜15分钟

只改V最后一行，Q、K、两套权重都保持固定。这能隔离“是否读取这行内容”的影响。

```python
V_changed = V.clone()
V_changed[2] = torch.tensor([100.0, 100.0])

base_changed = weights_base @ V_changed
masked_changed = weights_masked @ V_changed

print("无mask：前两行原/改：\n", output_base[:2], "\n", base_changed[:2])
print("有mask：前两行原/改：\n", output_masked[:2], "\n", masked_changed[:2])
print("无mask前两行是否保持不变：",
      torch.allclose(output_base[:2], base_changed[:2]))
print("有mask前两行是否保持不变：",
      torch.allclose(output_masked[:2], masked_changed[:2]))
print("有mask最后一行是否保持不变：",
      torch.allclose(output_masked[2], masked_changed[2]))
```

先预测三个布尔结果，再运行。对今天这组数据，预期分别为False、True、False。你要解释的重点是：前两行有mask时完全不读取第三行，最后一行允许读取它。这只是本次固定Q/K的受控实验，不等同于完整模型任意输入变化都会遵循同样数值结果。

## 第6步：保存本人解释｜10分钟

在attention_notes.md增加C段，回答：

1. 为什么生成后文时，要限制前面位置不能看未来？
2. allowed的行/列分别表示什么？
3. 为什么禁止位置填负无穷而不是0？
4. 改V最后一行后，有mask/无mask前两行分别怎样变化？用你的实际输出解释。

保存Notebook。时间合计90分钟。B的“根据需要汇集内容”若还没理解，可以用C预算继续B的小例子，今天不强行同时完成两份。无需训练、GPU、下载模型或学习其他mask种类。
