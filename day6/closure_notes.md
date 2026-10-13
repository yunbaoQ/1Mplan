我光靠二维还是没弄懂dim=0/1是什么意思，我就自己弄了个三维的，然后我发现，dim=0实际就是将shape中的第1的数字消失，将这个维度上的数字累加，将这个维度的shape变为1，就相当于三维变成二维。dim=1对应shape第二个数字，以此类推。
转换dtype保留了其值，可以相当于int + (float32=0.)。
b实际的shape就是2，就是一维数组,而其具有广播机制，只要该数组的shape最后一位是和b相等的，就能够直接相加（我尝试用三维数组相加，因为我的数组为（4，3，2）的，所以相加成功了：
tensor([[[1.5000, 0.5000],
         [1.5000, 0.5000],
         [1.5000, 0.5000]],

        [[1.5000, 0.5000],
         [1.5000, 0.5000],
         [1.5000, 0.5000]],

        [[1.5000, 0.5000],
         [1.5000, 0.5000],
         [1.5000, 0.5000]],

        [[1.5000, 0.5000],
         [1.5000, 0.5000],
         [1.5000, 0.5000]]])
），如果不相等比如是3则会报错：
RuntimeError                              Traceback (most recent call last)
Cell In[14], line 2
      1 t_tryb = torch.ones(2,3)
----> 2 print(t_tryb + b)

RuntimeError: The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 1