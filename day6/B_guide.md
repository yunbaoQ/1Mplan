# Day6 B：自动求导逐格操作（150分钟）

继续使用自己已经创建的grad_try.ipynb，选已有torch311环境，全部CPU。此文给教学片段；自己整合、预测、运行并保存，不把本文示例视为本人完成输出。不修改你现有Notebook。

## 先处理当前文件里的三处问题

当前保存的NameError: torch is not defined，说明运行计算时环境里没有torch变量。先运行import torch那一格；重启内核后也要从上到下重新运行。

你写的torch.tensor([2], requires_grad=True)会按整数推断dtype，整数张量不能开启这项求导。本例改成torch.tensor(2.0, requires_grad=True)，是浮点标量；不用方括号，便于观察标量loss。

先移除loss = F.binary_cross_entropy_with_logits(y)。这个函数用于二分类损失，调用还需要目标target；当前练习直接用y作为要对x求导的标量，无需另加损失函数。nn/F导入可以保留，但本实验只用torch。

## B-1：一个浮点标量的梯度（60分钟）

### 格1：导入

~~~python
import torch
~~~

### 格2：创建输入与前向计算

~~~python
x = torch.tensor(2.0, requires_grad=True)
y = x * x + 3 * x

print("x =", x.item())
print("y =", y.item())
print("y的shape =", y.shape)
print("求导前x.grad =", x.grad)
~~~

解释：requires_grad=True让自动求导系统跟踪相关运算；y是前向算出的数；求导前x.grad还未计算，所以None正常。

先写自己的预测：y=x²+3x，导数dy/dx=2x+3。把本次x代入，算出预测梯度，然后再运行下一格。可以看成x变化一点时，y变化速度由这个导数描述。

### 格3：求导并查看

~~~python
y.backward()
print("求导后x.grad =", x.grad)
print("求导后x =", x.item())
~~~

核对梯度和手算。观察x本身仍是原来的值：backward负责计算/累积梯度，参数更新是后续训练任务。

注意：不要反复只运行格3。要重新测试就先运行格2，创建新输入和新前向，再运行格3。重复对同一个已反传的旧图操作不是本段目标。

### 格4：自己换一个数验证

把格2中的2.0换成自己选的浮点数，先计算新y与新导数，再按格2→格3运行。留两组实际结果与解释，不要求GPU或证明导数公式。

验收：一个手算梯度和实际一致，能解释x/y/x.grad各表示什么。

## B-2：把张量输出合成标量（45分钟）

新建一格，与B1用不同变量，避免混淆：

~~~python
v = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
squared = v * v
loss = squared.sum()

print("逐元素平方 =", squared)
print("平方结果shape =", squared.shape)
print("loss =", loss.item())
print("loss的shape =", loss.shape)
~~~

先手算逐元素平方、它们的总和、至少一个元素的梯度。这个loss是v[0]²+v[1]²+v[2]²，对每个元素的导数都是对应的2*v[i]。随后在下一格：

~~~python
loss.backward()
print("v.grad =", v.grad)
~~~

记录每个元素的梯度，核对手算。loss.shape通常显示torch.Size([])：它是一个标量，不是“没有数据”。标量loss方便把多个输出合成一个优化目标。

本例先sum再不带参数backward。多元素输出若直接backward，需提供对应gradient；今天不学习该用法，也不要求故意触发这个错误。

验收：能区分长度3的平方结果和标量loss，至少一个元素梯度核对正确。重跑此段时从创建v那格开始。

## B-3：观察梯度累积、清除和no_grad（45分钟）

### 格1：第一次反传

~~~python
u = torch.tensor(2.0, requires_grad=True)
loss1 = u * u
loss1.backward()
print("第一次 =", u.grad)
~~~

### 格2：同一个u，重新前向再反传

~~~python
loss2 = u * u
loss2.backward()
print("第二次，没清梯度 =", u.grad)
~~~

先预测第二次会是多少，再运行。保留同一个u，但loss2来自一次新的前向运算；这样观察的是grad累积，不用retain_graph。

### 格3：清除后再次重新计算

~~~python
u.grad = None
print("清除后 =", u.grad)

loss3 = u * u
loss3.backward()
print("清除后重新求导 =", u.grad)
~~~

None表示目前没有存储的梯度，并不意味着u的值清零。重新反传后grad保存本次梯度。对照三次真实输出，自己解释“为什么训练每轮通常要清梯度”。

这三格按顺序跑；想重新做整组对照，就从重新创建u的格1开始，避免Notebook反复点格2造成额外累积。

### 格4：只计算结果时关闭跟踪

~~~python
normal_result = u * u

with torch.no_grad():
    inference_result = u * u

print("正常计算 =", normal_result.requires_grad)
print("no_grad计算 =", inference_result.requires_grad)
print("u本身 =", u.requires_grad)
print("原来的u.grad =", u.grad)
~~~

观察这里的两份计算结果的requires_grad。no_grad让范围内这项新计算不建立用于反传的跟踪；它不会自动清除已有u.grad，也不会把原输入u的requires_grad改为False。推理时需要结果、无需反向求导，可以使用这类方式。无需对inference_result调用backward故意报错。

验收：同一u在新的前向下，两次反传会累积；清除后保存本次梯度；能解释no_grad对新结果的影响。

## 保存什么与何时进入C

保存Notebook中的顺序真实输出，以及一份短autograd_notes.md，包含：
- B1：自己的x、y、预测梯度、实际梯度；第二组不同输入。
- B2：squared和loss的shape；至少一个手算元素梯度。
- B3：第一次/未清第二次/清后再次的实际梯度，no_grad对照。
- 三句话：backward做什么；为何清grad；no_grad适合什么情况。

未运行或只是复制本文不能算掌握。先能解释这三段再进C训练；卡住时用C的90分钟补求导，不新增必做时间。

资料：[backward](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.backward.html)、[no_grad](https://docs.pytorch.org/docs/2.11/generated/torch.no_grad.html)。官方文档证实反传累积叶子梯度，清除可设None；这里只做最基本用法。

