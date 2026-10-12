# Day 4 A-3：设备与硬件确认｜20分钟

在 day4/tensor_practice.ipynb 新建几个单元格，选 torch311。先保存现有内容，再重启内核，从本实验第一格顺序执行；后续重跑也从第一格开始，避免 add_ 累积修改。可以将输出保存在同一Notebook，不必重复创建文件。

本教程给操作示例，数值和设备先由自己预测再运行；教练不代执行、不生成验收结果。

## 1. CPU tensor 与 NumPy（5分钟）

```python
import torch

cpu_tensor = torch.tensor([1., 2., 3.], device='cpu')
arr = cpu_tensor.numpy()
print('CPU:', cpu_tensor, cpu_tensor.device)
print('NumPy:', arr)

cpu_tensor.add_(1)
print('修改CPU后:', cpu_tensor)
print('NumPy现在:', arr)
print('CUDA可用:', torch.cuda.is_available())
```

先预测修改后 arr 是否变化，再解释。add_ 的下划线表示在原tensor上修改；这个无梯度、普通CPU浮点tensor的 numpy() 与它共享存储。不是所有tensor都可直接numpy转换。[官方numpy说明](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.numpy.html)。

## 2. 迁移与重新赋值（10分钟）

上一格 CUDA 可用为 True 时继续；为 False 或报错时保存输出，GPU部分标待验证，后续张量课用CPU，不重装已可用环境。

```python
gpu_tensor = cpu_tensor.to('cuda')
print('原CPU设备:', cpu_tensor.device)
print('迁移返回设备:', gpu_tensor.device)

gpu_tensor.add_(10)
print('GPU修改后:', gpu_tensor)
print('原CPU:', cpu_tensor)
print('原NumPy:', arr)

back_cpu = gpu_tensor.cpu()
back_cpu.add_(100)
print('新CPU:', back_cpu)
print('原CPU:', cpu_tensor)
print('原NumPy:', arr)
```

预测并回答：修改GPU会不会修改原CPU/NumPy？返回CPU是否自动和旧arr共享？保留变量方便看对象关系。此次设备改变时 to 返回另一个设备上的tensor；相同设备/类型的to不一定复制，不要把to泛化成总是复制或总是原地修改。[官方to说明](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.to.html)。

继续观察新建与变量覆盖：

```python
x = gpu_tensor
print('赋值前:', x.device)
x = torch.ones(3)
print('新建覆盖后:', x.device)

explicit_gpu = torch.ones(3, device='cuda')
print('显式指定:', explicit_gpu.device)
```

本实验没有更改默认设备，默认新建通常在CPU；应以打印为准。变量x改指向新张量，不是GPU对象被自动搬回CPU。gpu_tensor仍可保留原对象。

## 3. 查询显存并写结论（5分钟）

CUDA正常时运行只读查询：

```python
props = torch.cuda.get_device_properties(0)
print('GPU:', props.name)
print('总显存字节:', props.total_memory)
print('总显存GiB:', props.total_memory / (1024 ** 3))
```

记录的是总显存容量，不是当前空闲容量，不从GPU型号猜数值。[设备属性查询](https://docs.pytorch.org/docs/2.11/generated/torch.cuda.get_device_properties.html)。

在 closure_notes.md 写自己的解释并保留实际输出：
- CPU/NumPy修改为何一起变化；
- GPU修改与转回CPU为何不自动改变原arr；
- 默认新建与显式CUDA创建的设备；
- 显存总字节数和GiB。

若此前已有同样完整、可复现的记录，直接引用并补缺即可。收到教程或仅看到CUDA True不等于A-3全部验收通过。
