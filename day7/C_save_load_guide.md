# Day7 C：保存模型参数，再加载回来（90分钟）

C主要练三件事：保存当前参数、创建一个新模型加载参数、核对同一输入的预测是否恢复。复用你现有的day7/tiny_train.ipynb与Linear(1,1)，CPU完成。

打开该Notebook，在你自己的训练代码之后追加下面几格。如果当前内核里已有训练后的model与x，可以直接继续；如果刚重启内核，就先从头顺序执行现有准备与训练。不要为了读取变量只创建一个新的随机model，然后把它当作之前训练好的模型。无需新增数据或另一套训练作业。

这些是供你整合执行的教学示例，教练不创建你的参数文件、不运行模型、不填写结果。

## 第1格：保存前的基准（15分钟）

~~~python
from pathlib import Path
import torch
from torch import nn

# 当前例子沿用CPU上的Linear(1,1)与五条x
model.eval()
with torch.no_grad():
    prediction_saved = model(x).clone()

print("保存前w/b:", model.weight.item(), model.bias.item())
print("保存前预测:", prediction_saved)
print("要保存的内容:", model.state_dict())
~~~

本例state_dict里主要是weight和bias，也就是训练后的w/b。它不是五条输入数据，也不是预测输出。

model.eval()选择评估模式；torch.no_grad()让这段观察计算不记录梯度。对于这个没有Dropout/BatchNorm的Linear小模型，eval不会改变前向公式。这里没有调用step，因此不做训练更新。

## 第2格：把参数写到文件（15分钟）

~~~python
output_dir = Path(r"C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day7")
save_path = output_dir / "linear_day7_state.pth"

torch.save(model.state_dict(), save_path)

print("保存到:", save_path)
print("文件存在:", save_path.exists())
~~~

本例明确指定已存在的day7目录，避免Notebook工作目录不同而找不到文件。自己查看打印的路径和文件；本次新文件用于本实验，保留旧练习。

torch.save做写入；state_dict提供要写入的参数。文件保存好后，不需要重新训练才能使用这些参数。

## 第3格：创建一个尚未加载的新模型（20分钟）

~~~python
restored_model = nn.Linear(1, 1)
restored_model.eval()

with torch.no_grad():
    prediction_before_load = restored_model(x).clone()

print("新模型加载前w/b:",
      restored_model.weight.item(), restored_model.bias.item())
print("新模型加载前预测:", prediction_before_load)
~~~

它是新的model对象，刚创建时参数来自新初始化。结构仍需是Linear(1,1)，这样参数名称与shape才匹配。不要把restored_model直接写成model：那只是让两个变量指同一个对象，无法验证文件恢复。

先保存这格输出，再进行加载。

## 第4格：读取文件、装进新模型并核对（25分钟）

~~~python
state = torch.load(save_path, map_location="cpu", weights_only=True)
restored_model.load_state_dict(state)
restored_model.eval()

with torch.no_grad():
    prediction_after_load = restored_model(x)

print("加载后w/b:",
      restored_model.weight.item(), restored_model.bias.item())
print("加载后预测:", prediction_after_load)

print("保存前与恢复后预测相近:",
      torch.allclose(prediction_saved, prediction_after_load))
print("最大绝对差:",
      (prediction_saved - prediction_after_load).abs().max().item())
~~~

注意两步用途：
- torch.load：从文件取出参数字典state；仅执行这一行不会自动改restored_model。
- load_state_dict：把字典中的参数装进restored_model。

map_location="cpu"指定读取到CPU；weights_only=True适合本次只保存参数字典的文件。只读取本实验刚保存的文件即可。

同一结构、参数、输入和本例执行条件下，恢复预测应与保存前一致；用实际allclose及差值记录，不手填True。如果不一致，先查保存的model是哪一个、文件路径、是否比较同一个x，以及保存基准后是否又更新了参数。

## 最后15分钟：保留产出与短解释

在原Notebook保存顺序输出，另写save_load_notes.md，记录：
1. 参数文件路径、state_dict键名。
2. 保存前w/b、新模型加载前w/b、新模型加载后w/b。
3. 三份预测及真实allclose/最大差值。
4. 自己用一句话区分torch.load与load_state_dict。
5. 保存这份模型参数是否也保存了训练轮数、数据和优化器设置。

本任务保存的是model.state_dict，不含完整训练过程。用于恢复这个模型做预测已有必要参数；若想按原设置继续训练，还通常需要优化器状态、训练进度等。今天只需知道这个区别，不额外实现完整训练checkpoint。

验收：本人生成参数文件，新模型从文件加载，真实预测核对通过，并能指出两条加载语句各做什么。若A对参数更新仍有卡点，可用这90分钟补A，总预算不增加。

官方依据：[保存加载教程](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html)、[PyTorch 2.11 torch.load](https://docs.pytorch.org/docs/2.11/generated/torch.load.html)。网页仅查对应语句，不必通读。

