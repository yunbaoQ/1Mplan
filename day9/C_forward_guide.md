# C操作指南｜从token编号到下一token分数｜90分钟

进入条件：能解释B中行查询、列参考，以及QK负责算比例、V负责被汇总。没通过就把本块时间用来继续B。

用途：把今天的Attention放到语言模型流程中。完整模型的大致链条是：输入文字→token编号→向量表示→多层上下文处理→词表分数→选择下一个token。你不需要现在独立实现整个Transformer。

## 1．先区分“位置”与“词表”｜15分钟

教学词表有5个编号，暂写成0=我、1=喜欢、2=学习、3=今天、4=结束。真实tokenizer的切分不必是一个汉字或词，这里只为看清流程。

输入ids=[0,1,2]，有3个输入位置，但候选词表有5种。每个位置用2维向量表示。自己先预测向量表和候选分数表的shape。

## 2．先观察编号如何查向量｜25分钟

自己新建forward_demo.ipynb。只用已有PyTorch，CPU即可。以下是教学起点，请自己运行、打印，并加上你预测的shape：

```python
import torch
from torch import nn
torch.manual_seed(42)
ids = torch.tensor([0, 1, 2], dtype=torch.long)
embedding = nn.Embedding(num_embeddings=5, embedding_dim=2)
x = embedding(ids)
```

打印ids、embedding.weight.shape、x.shape；比较x[0]与embedding.weight[0]。再将ids改成[0,1,0]，观察相同编号在此查表步骤是否取出相同向量。

这里没有加入位置编码、Attention或其他上下文处理，所以不能把“相同token查表向量相同”推广成“完整模型中相同token的最终表示永远相同”。资料：[Embedding，只读描述、num_embeddings/embedding_dim和Shape](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Embedding.html)。

## 3．观察向量如何变成词表分数｜25分钟

在这个查表演示上创建nn.Linear(2,5)，将x送进去得到logits。打印shape：3个输入位置，各有5个候选分数。对最后一行logits沿最后一维softmax得到概率，并用argmax选出编号；自行用上方词表显示它对应的标签。

先记录预测，再运行。检查概率和约1；比较直接对logits取argmax与对softmax概率取argmax的编号是否一致。解释Attention权重是在“参考位置之间分比例”，这里概率是在“词表候选之间分比例”，二者不是同一张表。

这只是查表加线性层的玩具演示，参数随机、没有训练，也没有上下文模块，输出的词不应被当作合理续写或语言模型质量。今天不要求把完整Transformer补进去。

## 4．理解prefill和decode｜15分钟

先看[知识问答](knowledge_interview.md)第7题。把输入“我/喜欢/学习”画成3个已知位置。prefill处理已有提示并为后续生成准备状态；之后每生成一个新token，再用新信息继续预测。

用两句话说明：什么是已知输入，什么是本轮新生成的编号；为什么下一轮不能提前知道更后面的token。KV cache只作概念认识，不运行缓存API、不测性能。资料：[Hugging Face How caching works：开头、Attention matrices的缓存说明](https://huggingface.co/docs/transformers/cache_explanation)。其中示例仅供看流程；mask具体写法沿用本地PyTorch指南。

## 5．交付与限制｜10分钟

交forward_demo.ipynb和forward_notes.md：实际shape、选出的编号、两种softmax对象的区别、prefill/decode两句解释，以及“没有训练/没有完整Transformer”的实验边界。真实完整前向和缓存实践留到后续验收，不因这个玩具演示而提前勾选完成。
