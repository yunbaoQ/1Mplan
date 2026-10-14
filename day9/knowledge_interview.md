# 常用知识与校招面试基础问答｜Day9

这组是围绕当前阶段整理的基础练习题，不冒充某公司真题，也不声称有面试频率统计。先能用自己的实验解释，再练30–60秒简答。前5题用于今天20分钟自测；后两题随C学习，不额外加课时。

## 1．Q、K、V分别做什么？

简答：Q表示当前查询，K用于计算与查询的匹配分，V是根据匹配比例被汇总的内容。拿你的实验说，Q两行、K/V三行，就是两个查询各参考三份内容。

易错点：Q/K/V不必相等，也不能把向量维度当作位置数。实际自注意力通常由输入表示经过不同投影得到Q/K/V。查[Attention论文3.2与3.2.2](https://arxiv.org/html/1706.03762v7#S3.SS2)，这里只需理解角色。

## 2．为什么要按行softmax？

简答：每一行对应一个查询，要在这个查询的全部参考位置之间分配比例。归一化后该行和为1，接着按比例混合V。

易错点：输出向量不要求各特征和为1；只有权重沿所归一化维度满足这个条件。softmax减去同一行最大值不改变结果，实践中有利于避免直接指数溢出。查[PyTorch softmax定义和dim](https://docs.pytorch.org/docs/2.11/generated/torch.nn.functional.softmax.html)。

## 3．为什么缩放点积？

简答：维度增大时，点积分数的波动可能增大，使softmax过于集中。在常见独立、零均值、单位方差假设下，点积方差随维度d增长，除以sqrt(d)可控制尺度。

易错点：这是尺度控制，不保证模型一定收敛，也不是为了让每个分数都落在0到1。今天知道目的即可，不额外做完整概率推导。查[原论文3.2.1的缩放解释](https://arxiv.org/html/1706.03762v7#S3.SS2.SSS1)。

## 4．因果mask解决什么问题？

简答：自回归预测下一token时，未来答案尚未知。训练也要禁止当前位置读取未来输入，避免信息泄漏。保留当前位置与过去位置，屏蔽未来分数，再softmax。

易错点：0分数不等于0概率；布尔True代表允许还是禁止取决于API。查[SDPA参考代码及布尔mask说明](https://docs.pytorch.org/docs/2.11/generated/torch.nn.functional.scaled_dot_product_attention.html)。

## 5．为什么固定Q/K改V，不会改Attention权重？

简答：当前实验权重只由QK分数、缩放和固定mask决定；V参与最后的加权汇总。只改V改变内容，不改变这次比例。

易错点：结论依赖“只改V”的条件；改输入通常会同时影响Q/K/V。证据直接引用你的Day8对照，不需要另背一段定义。

## 6．模型参数weight、Attention weights和logits有什么区别？

| 名称 | 指什么 | 是否本次输入的结果 |
| --- | --- | --- |
| Linear.weight | 线性层可学习参数，模型状态的一部分 | 固定参数推理时不因每个输入而更新 |
| Attention weights | 当前查询对参考位置的混合比例 | 是，通常随Q/K变化 |
| logits | 对候选类别/token的未归一化分数 | 是，可经softmax转成分布 |

常见误区是看到weight这个英文就当成同一种东西。查[Module.state_dict](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Module.html#torch.nn.Module.state_dict)了解保存对象；用C演示理解词表分数。

## 7．prefill、decode与KV cache是什么关系？

简答：prefill处理已有提示；随后decode逐个生成。KV cache保存各层已处理位置的K/V，让后续步骤复用，减少重复计算；它不保存未来答案，也不是模型训练参数文件。

为什么AI Infra关心：缓存占用内存，服务并发、上下文长度和延迟都需要考虑它。此处只建立概念，不据玩具实验声称测过吞吐、显存或缓存性能。

查[Hugging Face How caching works：Attention matrices与Cache class](https://huggingface.co/docs/transformers/cache_explanation)，只读复用与追加K/V的描述；完整代码等后续任务安排。

## 如何用这些材料

闭卷先回答，再打开答案标出“我漏了什么/说错了什么”。不直接复制参考答案算通过。网页打不开或读不懂时，保留链接与具体句子，写入当天notes；下一天的questions_answers会据此解答。
