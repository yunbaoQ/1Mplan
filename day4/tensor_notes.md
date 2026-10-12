使用torch.ones(3,2)创建出的tensor是：
torch.Size([3, 2])
torch.float32
cpu

将tensor转到cuda：
cuda:0
torch.Size([3, 2])
torch.float32
除了位置全都不变


逐个加法和逐个乘法，我都在1.ipynb中尝试了，确实了解到一些新东西。下面是关于尺寸不对的报错：
RuntimeError                              Traceback (most recent call last)
Cell In[29], line 2
      1 t4 = torch.ones(5,5)
----> 2 t = t + t4

RuntimeError: The size of tensor a (4) must match the size of tensor b (5) at non-singleton dimension 1

reshape让相同数量元素进入相同数量的矩阵中，如果数量不正确，则会报错：
RuntimeError                              Traceback (most recent call last)
Cell In[32], line 2
      1 x = torch.tensor([1., 2., 3., 4., 5.])
----> 2 A = x.reshape(2, 3)
      3 B = x.reshape(3, 2)
      4 
      5 print('x:', x, x.shape)

RuntimeError: shape '[2, 3]' is invalid for input of size 5

矩阵乘法@，学习过矩阵了解其乘法机制。


关于x@w+b,我没想到居然当b为（1，2）矩阵居然能跟（2，2）的矩阵相加，结果是z[0]和z[1]都与b相加。
学习过矩阵，相关计算会

GPU结果: tensor([[ 4.5000,  4.5000],
        [10.5000, 10.5000]], device='cuda:0') cuda:0
CPU/GPU数值接近: True
