# Day 4 C-4：一次小型计算 Y = XW + b｜45分钟

在你现有的tensor_practice1.ipynb或tensor_practice.ipynb新建单元格，选择torch311。先完成C-3的二维矩阵乘法；这里沿用同样的@，再加一组偏置。教练提供教学例子，实际输出、手算和说明由你完成，不代跑或代填结果。

## 1. 构造两个输入、三项特征、两个输出（10分钟）

把每行想成一条数据：X有2行，每行3个数字。W有两列，每列规定怎样组合这3个数字；因此每条数据产生2个输出。b是每个输出额外加上的固定数。这里只使用自己指定的权重，不要求训练。

```python
import torch

X = torch.tensor([[1., 2., 3.],
                  [4., 5., 6.]], dtype=torch.float32, device='cpu')
W = torch.tensor([[1., 0.],
                  [0., 1.],
                  [1., 1.]], dtype=torch.float32, device='cpu')
b = torch.tensor([0.5, -0.5], dtype=torch.float32, device='cpu')

print('X:', X.shape, X.dtype, X.device)
print('W:', W.shape, W.dtype, W.device)
print('b:', b.shape, b.dtype, b.device)
```

预测：(2×3) @ (3×2) 得到2×2。X第0行产生Y第0行；W第0列用于每条数据的第0个输出，第1列用于第1个输出。b长度为2，每项对应一个输出列。

## 2. 分成矩阵乘法与加偏置（10分钟）

```python
Z = X @ W
Y = Z + b
print('乘法结果:', Z, Z.shape)
print('加偏置后:', Y, Y.shape)
```

比较Z和Y：每一行的第0项都加b[0]，第1项都加b[1]。长度2的b可按最后一维匹配，应用到2×2结果的每一行，称为广播；无需自己复制两行b。[广播文档](https://docs.pytorch.org/docs/2.11/notes/broadcasting.html)。矩阵相乘使用@，不是*。[矩阵乘法文档](https://docs.pytorch.org/docs/2.11/generated/torch.matmul.html)。

## 3. 自己手算一个值（10分钟）

手算Y[0,0]：X第0行与W第0列对应相乘再求和，最后加b[0]。本例算式为1×1 + 2×0 + 3×1 + 0.5；结果自己计算，再核对Notebook的Y[0,0]。也可选择另一个输出元素。

然后只修改b[0]，先预测哪些输出位置会变化，再运行检查；这样确认你理解偏置对应输出列。保留原实验记录和修改记录，不要把旧输出混入新代码。恢复原数据后再比较CPU/GPU。

## 4. GPU对照（10分钟，CUDA可用时）

先检查torch.cuda.is_available()。True时将X/W/b都迁移，不能只搬一个。

```python
if torch.cuda.is_available():
    X_gpu = X.to('cuda')
    W_gpu = W.to('cuda')
    b_gpu = b.to('cuda')
    Y_gpu = X_gpu @ W_gpu + b_gpu
    print('GPU结果:', Y_gpu, Y_gpu.device)
    print('CPU/GPU数值接近:',
          torch.allclose(Y, Y_gpu.cpu(), rtol=1e-5, atol=1e-6))
else:
    print('GPU对照未完成：CUDA不可用')
```

allclose按容差检查数值是否接近，比较时把结果搬回CPU，保持设备一致。GPU失败时保存原错误，GPU部分待验证；不重装环境或编造通过。[allclose文档](https://docs.pytorch.org/docs/2.11/generated/torch.allclose.html)。该实验只验证正确性，不能证明GPU速度更快。

## 5. 写自己的记录（5分钟）

在tensor_notes.md补：X/W/b/Y的shape；每行输入、每列权重与偏置的意义；至少一个元素的手算及实际输出；修改b[0]的预测/观察；GPU对照通过/待验证的真实状态。

保存Notebook完整输出。完成条件是能解释一次计算，而非只粘贴例子；教学指南不作为已完成进度。沿用原45分钟预算。
