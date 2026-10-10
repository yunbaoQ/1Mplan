# Day 4 C-3：reshape 与矩阵乘法｜30分钟

在 day4/tensor_practice.ipynb 的新单元格中操作，选择现有 torch311 内核；也可写入自己的 .py 文件。先用 CPU。以下是教学步骤，结果由你自己预测、运行并记录，教练未运行实验或代填答案。

## 1. reshape：同样6个元素，改变形状（10分钟）

先预测 A、B 每行有哪些数，再运行：

```python
import torch

x = torch.tensor([1., 2., 3., 4., 5., 6.])
A = x.reshape(2, 3)
B = x.reshape(3, 2)

print('x:', x, x.shape)
print('A:', A, A.shape)
print('B:', B, B.shape)
print('元素数:', x.numel(), A.numel(), B.numel())
```

reshape 目标形状的元素总数必须与原张量一致；此处2×3和3×2均为6。它不是矩阵转置。暂时不深究共享存储，但不要断定 reshape 一定复制或一定共享。[reshape 文档](https://docs.pytorch.org/docs/2.11/generated/torch.reshape.html)。

## 2. 矩阵乘法：行与列相乘求和（10分钟）

二维矩阵规则：(m×n) @ (n×p) 得到(m×p)，中间维度必须相等。本例 A 为2×3，B为3×2，因此结果为2×2。[matmul 文档](https://docs.pytorch.org/docs/2.11/generated/torch.matmul.html)。

先自己计算左上角元素：A第0行与B第0列的对应元素相乘，再求和。然后运行并核对：

```python
C = A @ B
print('矩阵乘法:', C)
print('结果形状:', C.shape)
print('左上角:', C[0, 0])

D = A * A
print('逐元素乘法:', D)
print('结果形状:', D.shape)
```

@ 在这里做矩阵乘法；A*A 是同位置元素相乘，每个位置独立，结果形状仍为2×3。不要把 A*B 当作 A@B：本例 A/B 的形状也不能逐元素广播相乘。

## 3. 自己验证并记解释（10分钟）

- 在单独单元格尝试 x.reshape(4,2)，保存报错并解释元素数量为何不匹配；.py 中可用 try/except 捕获 RuntimeError。
- 换一组六个小数，自己再手算一个矩阵乘法元素，核对程序结果。
- 在 tensor_notes.md 写三句话：reshape 的元素约束、矩阵乘法的维度约束、*与@的区别。附一组预测和真实输出。

做到这些即完成C-3的小实验；C-4的偏置/小型计算随后再做，不增加本块30分钟预算。收到教程不代表已经验收通过。
