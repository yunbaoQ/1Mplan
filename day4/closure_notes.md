很明显，这些东西我在day3的Python_device_train.ipynb已经验证过了，就是tensor可以直接选择在cpu或者在cuda上，而numpy的数组，则只能桥接在cpu上的tensor，如果想要桥接cuda上的tensor则会报错：
TypeError                                 Traceback (most recent call last)
Cell In[11], line 3
      1 first_gpu = torch.ones(3, device='cuda')
      2 print('显式指定:', first_gpu.device)
----> 3 arrnp = first_gpu.numpy()

TypeError: can't convert cuda:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.

