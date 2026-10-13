# Day7 B：把五个样本分成小批次（90分钟）

B的目标：亲自观察Dataset中的一条样本，以及DataLoader一次返回的一批样本。今天用已有五条数据，不下载数据，不再训练50轮。新建自己的day7/batch_practice.ipynb，选已有torch311环境，按下面格子运行并保存实际输出。

示例是教学材料，需要你自行复制、改参数、预测、运行和解释；教练没有创建你的练习Notebook或执行实验。

## 第1格：五条数据装成Dataset（20分钟）

~~~python
import torch
from torch.utils.data import TensorDataset, DataLoader

x = torch.tensor([[-2.0], [-1.0], [0.0], [1.0], [2.0]])
target = 2 * x + 1

dataset = TensorDataset(x, target)

print("所有输入的shape:", x.shape)
print("样本总数:", len(dataset))
print("第0条样本:", dataset[0])
print("第0条输入shape:", dataset[0][0].shape)
print("第0条目标shape:", dataset[0][1].shape)
~~~

一条样本是一对“输入、目标”。TensorDataset把x的第i行与target的第i行配成一条；不是把输入与目标分别算作两条样本。

整个x的shape=(5,1)：5条样本，每条1个输入特征。dataset[0]取一条，输入shape=(1,)，目标也为(1,)。这里的1是特征/输出维度，不是样本总数。

运行后用自己的话指认第一条的输入与目标，说明len(dataset)数的是什么。

## 第2格：DataLoader每次取两条（25分钟）

先创建读取器：

~~~python
loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=False,
    drop_last=False,
    num_workers=0
)
print("一轮有几批:", len(loader))
~~~

参数逐个看：
- batch_size=2：每批最多2条样本。
- shuffle=False：这一轮按原顺序取，方便核对。
- drop_last=False：最后不满2条也保留。
- num_workers=0：本次直接在当前进程取数据，不开额外加载进程。

再遍历一轮：

~~~python
for batch_index, (batch_x, batch_target) in enumerate(loader, start=1):
    print("第", batch_index, "批")
    print("输入:", batch_x)
    print("目标:", batch_target)
    print("shape:", batch_x.shape, batch_target.shape)
    print("本批样本数:", batch_x.shape[0])
    print("-----")
~~~

for每次得到的是两样东西：这一批的输入batch_x和对应目标batch_target；不会每次都得到全部五条数据。enumerate额外给这批一个编号。

**预期供你先预测，不是已运行记录：**
- 第1批输入是前两条，shape=(2,1)。
- 第2批输入是接下来的两条，shape=(2,1)。
- 第3批只有剩下一条，shape=(1,1)。

观察每批目标是否仍与输入配对。每批shape的第0维是本批样本数，第1维仍是每条样本的特征数。

## 第3格：自己改两个参数做对照（25分钟）

先不改原loader，另建一个读取器：

~~~python
loader_3 = DataLoader(
    dataset, batch_size=3, shuffle=False, drop_last=False, num_workers=0
)

for i, (batch_x, batch_target) in enumerate(loader_3, start=1):
    print("batch_size=3，第", i, "批:", batch_x.shape, batch_target.shape)
    print(batch_x)
~~~

运行前预测有几批、各有几条，再看实际。数据还是原来五条，改变batch_size只改变怎样分组。

接着新建：

~~~python
loader_drop = DataLoader(
    dataset, batch_size=2, shuffle=False, drop_last=True, num_workers=0
)

seen = 0
for i, (batch_x, batch_target) in enumerate(loader_drop, start=1):
    seen += batch_x.shape[0]
    print("drop_last=True，第", i, "批:", batch_x.shape)
    print(batch_x)

print("本轮实际取到样本数:", seen)
print("Dataset仍有样本数:", len(dataset))
~~~

对比drop_last=False与True：不足一批的样本有没有被取到？dataset本身是否变短？用真实输出区分“这一轮没取到”和“数据被删除”。

本次不增加shuffle随机实验或多进程实验，先把分组理解清楚。

## 最后20分钟：记录和连接昨天训练

创建batch_notes.md，自己填写：

| 设置 | 运行前预测批数 | 实际批数 | 各批shape | 这一轮实际取到几条 |
| --- | --- | --- | --- | --- |
| batch_size=2，drop_last=False | 自己填写 | 自己填写 | 自己填写 | 自己填写 |
| batch_size=3，drop_last=False | 自己填写 | 自己填写 | 自己填写 | 自己填写 |
| batch_size=2，drop_last=True | 自己填写 | 自己填写 | 自己填写 | 自己填写 |

再写三句：
1. Dataset取一条与DataLoader取一批的区别。
2. 最后一批的shape为什么可以不同。
3. 昨天model(x)一次使用全部5条；改成model(batch_x)会处理当前这一批。如果每批都做一次完整训练更新，遍历一次batch_size=2/drop_last=False的loader，会有几次step？这只是理解题，不要求今天加一整段训练。

这次只是取数据，所以没有optimizer.step；遍历打印不算训练。训练时才会把每一批接到“预测→loss→backward→step”。epoch指遍历一轮训练数据，在按每批更新的训练设置下，一个epoch可能包含多个更新步骤；drop_last设置会影响这一轮实际用到的样本。

验收：保存Notebook真实输出与上表；能解释样本/特征/批次、最后一批以及drop_last。不要只复制预期当作实际结果，90分钟内有卡点就保留相应格。完成后继续今日C，不把这次讲解记作已完成。

官方资料：[PyTorch 2.11 TensorDataset/DataLoader](https://docs.pytorch.org/docs/2.11/data.html)、[Dataset与DataLoader入门](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html)。仅查用到的参数即可。

