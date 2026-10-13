# Day6 C：用五个点训练一条直线（90分钟）

目标：用nn.Linear(1,1)学出接近y=2x+1的关系。B已保存正确计算/累积/no_grad对照；先用本准备阶段修正B笔记两点，再开始训练，不重刷B。CPU、已有torch311环境，不下载数据或新装库。

这是教学步骤和示例；由你整合运行并记录实际结果，教练不替你创建训练Notebook、执行训练或填写输出。

## 先用2分钟补清B笔记

autograd_notes.md写x=2/3时y=x²+3x的梯度4/6，漏了3x的导数3；正确是2x+3，对应7/9。你当前Notebook x=4、y=28、grad=11的保存输出正确，向量平方梯度2*v同样正确，两个函数不能混用导数。

loss.shape=torch.Size([])表示0维标量：这里只有一个数，如保存的loss=14。它有1个元素，没有行/列维度；空张量torch.tensor([])则shape=(0,)、0个元素。自己补一句说明，可打印loss.numel()验证。这里无需另开长实验。

最后未执行格含inference_result.backward()，与已保存no_grad结果不匹配：当前计算结果不跟踪梯度，不能对它反传。可以注释该行，不要求故意运行报错；旧输出不能当该行真实运行证据。

## 第1格：准备五个样本（准备阶段20分钟内）

新建day6/tiny_train.ipynb（或自己用.py组织），选已有环境，从上到下运行：

~~~python
import torch
from torch import nn

torch.manual_seed(42)

x = torch.tensor([[-2.0], [-1.0], [0.0], [1.0], [2.0]],
                 dtype=torch.float32)
target = 2 * x + 1

print("输入 =", x)
print("目标 =", target)
print("shape =", x.shape, target.shape)
~~~

两个shape都应是(5,1)：5个样本，每个样本1个输入/输出。x和target在本例是固定数据，不需要设置requires_grad=True；下一步模型的w/b需要梯度。

自己解释target每个值怎么来的。实际输入使用二维形状，避免(5,)和(5,1)混用导致广播成错误的误差表。

## 第2格：创建模型、误差和更新工具

~~~python
model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)

print("初始w =", model.weight.item())
print("初始b =", model.bias.item())
~~~

每个输入只有一个特征，所以Linear(1,1)给每个样本一个输出；计算就是prediction=w*x+b。w/b随机初始化，训练负责更新它们，不手动赋值为2和1。

MSELoss默认把每个预测与目标的差平方后取平均，得到一个标量loss。SGD接收model.parameters()，所以后续更新的对象是该model的参数；lr是更新幅度系数。

创建模型/optimizer只做一次，放在训练循环外。

## 第3格：记录训练前基线

~~~python
with torch.no_grad():
    pred_before = model(x).clone()
    initial_loss = criterion(pred_before, target).item()

print("训练前预测 =", pred_before)
print("训练前loss =", initial_loss)
~~~

记录初始loss、w、b。clone保存一份前预测，之后可与训练后直接比较。no_grad用于观察结果，不包住下面训练循环。

## 第4格：训练50轮（训练阶段40分钟）

逐行理解并运行：

~~~python
for step in range(1, 51):
    optimizer.zero_grad(set_to_none=True)
    prediction = model(x)
    loss = criterion(prediction, target)
    loss.backward()
    optimizer.step()

    if step % 10 == 0:
        with torch.no_grad():
            current_loss = criterion(model(x), target).item()
        print(
            f"step={step}, loss={current_loss:.6f}, "
            f"w={model.weight.item():.6f}, "
            f"b={model.bias.item():.6f}"
        )
~~~

五步分别是：
1. zero_grad：清掉这个模型上一轮保存的梯度。
2. model(x)：用当前w/b得到预测。
3. criterion：将预测误差汇成一个数。
4. backward：计算loss对w/b的梯度。
5. step：根据梯度更新w/b。

本例无动量SGD可直观理解成“新参数=旧参数-学习率×梯度”。B只算梯度，C加上了实际参数更新。

记录第0/10/20/30/40/50轮的loss、w、b。第0轮来自初始记录，后续打印重新计算更新后的loss，与同一更新状态的w/b配套，避免把更新前loss和更新后参数误认为同一状态。

想从头重做时，从创建模型/优化器和初始记录开始。只重跑训练格会在当前模型上继续训练50轮，要如实注明。

## 第5格：比较训练前后（观察阶段30分钟）

~~~python
with torch.no_grad():
    pred_after = model(x)
    final_loss = criterion(pred_after, target).item()

print("各列：x、目标、训练前预测、训练后预测")
print(torch.cat([x, target, pred_before, pred_after], dim=1))
print("loss：", initial_loss, "->", final_loss)
print("最终w =", model.weight.item())
print("最终b =", model.bias.item())
~~~

看三件事：参数是否实际变化，loss是否降低，预测是否更接近target。目标关系是w接近2、b接近1，不要求50轮后浮点数恰好等于它们；结果有什么就记什么。不能把这个小例成功记为完整大模型训练或GPU性能能力。

## 保存与验收

tiny_train.ipynb保存干净顺序输出，training_notes.md保存：
- x/target/prediction都是(5,1)，loss是标量。
- 第0/10/20/30/40/50轮真实loss/w/b。
- 五个输入的训练前后预测与目标。
- 自己解释zero_grad/backward/step，以及哪些变量是数据、哪些是可学习参数。

如果loss不下降，先保存当前结果并查：预测/目标shape、梯度是否存在、optimizer是否对应当前模型、是否执行step、训练是否被no_grad包住、是否每轮重建model。先解决原因，不加几千轮掩盖。90分钟内遇卡点保留报错；不叠加新任务。

官方资料：[Linear](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Linear.html)、[MSELoss](https://docs.pytorch.org/docs/2.11/generated/torch.nn.MSELoss.html)、[SGD](https://docs.pytorch.org/docs/2.11/generated/torch.optim.SGD.html)。只需查上述三个用途，不要求通读。

