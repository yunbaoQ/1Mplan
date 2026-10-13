# Day7 A：亲眼看optimizer怎样更新参数（120分钟）

你已经大致看懂训练顺序，今天观察“更新发生在哪一行、改了哪些数”。下面是教学示例，由你复制到自己新建的day7/optimizer_practice.ipynb，选择已有torch311环境，逐格运行、预测并保存实际输出。最后留下几句解释即可。

“B/C预算”就是今天B小批次的90分钟、C保存恢复的90分钟。A仍卡住时，可以把后面的时间挪给A，总共仍不超过360分钟；不是额外增加180分钟。提前通过可以直接做B，无需凑满时间。

## opt到底是什么

opt通常是optimizer的变量名简写。SGD接收model.parameters()，管理的是这个model里的w/b；lr是学习率。这里不使用动量或权重衰减，更新规则为：

    新w = 旧w - lr × w的梯度
    新b = 旧b - lr × b的梯度

loss.backward()把梯度放进参数的.grad；optimizer.step()读取这些梯度，修改model的w/b。普通step不会自动改变此处设置的lr，也不会清除.grad。今天不用看优化器源码。

## 实验1：拆开一次参数更新（50分钟）

第一格创建数据、模型和优化器。为方便比较，仅在本实验初始化时把w/b设为0；不是每轮清零，也不是填入目标参数2/1。

~~~python
import torch
from torch import nn

x = torch.tensor([[-2.0], [-1.0], [0.0], [1.0], [2.0]])
target = 2 * x + 1

model = nn.Linear(1, 1)
with torch.no_grad():
    model.weight.fill_(0.0)
    model.bias.fill_(0.0)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(
    model.parameters(), lr=0.05, momentum=0.0, weight_decay=0.0
)
print("初始w/b:", model.weight.item(), model.bias.item())
print("学习率:", optimizer.param_groups[0]["lr"])
~~~

第二格只算梯度，先不step。item()取普通数字，便于保存更新前快照。

~~~python
optimizer.zero_grad(set_to_none=True)
w_before = model.weight.item()
b_before = model.bias.item()

prediction = model(x)
loss = criterion(prediction, target)
print("预测:", prediction.detach())
print("loss:", loss.item())
print("backward前梯度:", model.weight.grad, model.bias.grad)

loss.backward()

grad_w = model.weight.grad.item()
grad_b = model.bias.grad.item()
print("backward后梯度:", grad_w, grad_b)
print("backward后w/b:", model.weight.item(), model.bias.item())
print("原来的w/b:", w_before, b_before)
~~~

先观察：梯度有没有出现？w/b有没有改变？不要求先推导MSE的全部公式。

第三格之前，自己用刚才保存的旧w/b、梯度和lr，在笔记算出预测的新w/b。然后执行step核对。

~~~python
lr = optimizer.param_groups[0]["lr"]

# 仅计算普通数字，还没有修改模型
expected_w = w_before - lr * grad_w
expected_b = b_before - lr * grad_b

optimizer.step()

actual_w = model.weight.item()
actual_b = model.bias.item()
print("公式预测w/b:", expected_w, expected_b)
print("step实际w/b:", actual_w, actual_b)
print("核对w:", abs(expected_w - actual_w) < 1e-6)
print("核对b:", abs(expected_b - actual_b) < 1e-6)
print("step后学习率:", optimizer.param_groups[0]["lr"])

with torch.no_grad():
    loss_after = criterion(model(x), target).item()
print("更新前/后loss:", loss.item(), loss_after)
~~~

step调用一次就更新一次。不要只重复运行第三格来查看输出：它会继续使用已保存的梯度改参数。要从同一起点重做，就从第一格重新创建model和optimizer，再顺序运行。

验收：自己的公式预测与step实际结果相符；用输出指出哪一步改变参数。这组实验从初始状态只做一次更新，不再额外要求原来的10步重跑。

## 实验2：清梯度会把模型练回原点吗（20分钟）

接着实验1做，不重新初始化。先预测哪些值会变化，再运行：

~~~python
print("清除前w/b:", model.weight.item(), model.bias.item())
print("清除前grad:", model.weight.grad, model.bias.grad)

optimizer.zero_grad(set_to_none=True)

print("清除后w/b:", model.weight.item(), model.bias.item())
print("清除后grad:", model.weight.grad, model.bias.grad)
~~~

记录w/b与grad的前后差别。set_to_none=True会把已有梯度设为None，w/b保留已学到的值；下一轮重新前向/backward产生新梯度。这里无需重做昨天整套累积实验。

验收：能根据实际输出区分“清梯度”与“重新初始化参数”。

## 实验3：改变学习率（35分钟）

留下两行对照表，实际值由你运行后填写：

| lr | 初始w/b | grad_w/grad_b | 更新后w/b | 更新后loss |
| --- | --- | --- | --- | --- |
| 0.05 | 本人填写 | 本人填写 | 本人填写 | 本人填写 |
| 0.10 | 本人填写 | 本人填写 | 本人填写 | 本人填写 |

第一行用实验1的结果。第二行只把第一格lr改成0.10，然后从第一格重新创建相同初始w/b、数据和优化器，顺序执行第二、第三格。每组都只更新一次。

新建model时也要重新创建optimizer，使其管理新模型的参数，不能沿用管理旧model的优化器。

比较两组梯度、参数改变量和更新后loss。思考同初值时，学习率翻倍怎样影响这一小步的参数改变量；不从单个例子推出“学习率越大永远越好”。今天不展开Adam或调度器。

## 最后15分钟：保存与验收

保存Notebook输出，optimizer_notes.md只写：
1. backward之后与step之后，w/b和grad分别怎样。
2. 用一组真实数字写一次“旧参数-lr×梯度=新参数”。
3. zero_grad清的是什么；两个lr的一步对照有什么差别。
4. 还不清楚的具体代码行或观察。

解释围绕实操，不写长篇理论。标量shape、旧笔记漏3x导数等可以顺手短修，不另开整套复习。若结果对不上，先查是否重复运行step，或新建model却没重新创建optimizer。

官方依据：[SGD更新规则](https://docs.pytorch.org/docs/2.11/generated/torch.optim.SGD.html)、[zero_grad行为](https://docs.pytorch.org/docs/2.11/generated/torch.optim.Optimizer.zero_grad.html)。这是待本人执行的指南，不代表已完成。

