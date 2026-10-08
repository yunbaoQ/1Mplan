# AI Infra 校招学习综述

AI INFRA / CAMPUS PREPARATION　·　01

AI Infra 校招学习综述

检索与下载：2026-10-07　｜　面向学生与应届求职者　｜　中文原创导读

AI Infra 负责让模型训练与推理在算力、显存、通信和服务约束下高效运行。校招准备的核心是：**计算机基础 + 模型执行原理 + 一个有测量结果的系统项目**。岗位名称相同，实际职责可能差别很大。

先确定你要应聘哪条分支

| 分支 | 主要任务 | 学习重点 |
| --- | --- | --- |
| 推理系统 | 让模型更快、更省显存地服务请求 | PyTorch、vLLM / SGLang、KV Cache、batching、profiling |
| 训练系统 | 让多 GPU 训练正确、稳定、高效 | DDP / FSDP / ZeRO、NCCL、并行与 checkpoint |
| GPU 算子 / 编译器 | 把模型计算映射为高效 GPU 代码 | C++、CUDA / Triton、访存、并行归约、编译与运行时 |
| 算力平台 / 集群 | 管理 GPU 资源、任务、稳定性与成本 | Linux、Go / Python、容器、K8s、调度、网络与监控 |

这份资料怎么读

先看第 3 页的共同基础，再用第 4 页选择主线；第 5 页汇总网上求职讨论；第 6 页是 16 周安排；第 7 页给出简历项目；第 8 页说明已下载的英文综述如何选读。第 9-10 页为可点击来源。

我建议校招先以**推理系统**做主项目入口，再按目标 JD 决定向 CUDA、训练通信还是平台调度深入。这是基于可做出可测项目的学习建议，不代表推理方向岗位最多。

<link href="https://talent.baidu.com/jobs/detail/GRADUATE/b9f68e95-00a5-4dcd-9c32-876865e79916" color="#087F8C">[S01] 百度校园招聘：大模型推理基建相关岗位</link>　<link href="https://arxiv.org/abs/2506.21901" color="#087F8C">[S10] A Survey of LLM Inference Systems</link>

说明：本文件是基于公开招聘、面经、社区讨论和官方教程重新组织的原创综述；不是网上已有文章的完整转载。英文论文为原始 PDF 下载。匿名经验及个别 JD 不构成就业统计，也不能推出薪资或录用概率。

AI INFRA / CAMPUS PREPARATION　·　02

招聘要求怎样拆解

区分官方招聘、个人面经和社招能力上限；避免把所有关键词当成校招必修课。

官方招聘：校招推理研发样本

百度公开校园招聘页面列出了 C++ / Python、CUDA / CUTLASS / CuTe / Triton / TileLang 等 GPU 编程能力，以及注意力、矩阵计算、批调度、分离部署和 Cache 优化。vLLM / SGLang / TensorRT-LLM 经验与开源贡献也被列为加分项。

对你的启示：若目标是推理内核研发，应能讲清模型计算与显存开销，并展示一个算子或推理性能实验；只调用模型 API 的聊天应用很难呈现这些能力。

<link href="https://talent.baidu.com/jobs/detail/GRADUATE/b9f68e95-00a5-4dcd-9c32-876865e79916" color="#087F8C">[S01] 百度校园招聘：大模型推理基建相关岗位</link>

平台调度：另一种 AI Infra

字节 Compute Infrastructure 的搜索索引描述强调 Kubernetes 集群、统一调度、CPU / GPU 等异构资源与训练 / 推理平台。该页面正文未能直接读取，这里仅用索引内容识别分支，不把它当作已确认的校招开放岗位。

对你的启示：这类岗位更接近后端和分布式平台。可以用 Go / Python 的资源队列、任务调度、故障恢复项目证明能力，而不必一开始就做复杂 CUDA 算子。

<link href="https://jobs.bytedance.com/en/position/7491726420784777480/detail" color="#087F8C">[S02] 字节跳动：Compute Infrastructure / Orchestration &amp; Scheduling</link>

社招集群样本：了解工作环境，不照搬门槛

Prime Intellect 的 GPU Infrastructure 招聘搜索索引涉及 GPU 容器运行时、Linux 调优和网络拓扑。超大 GPU 集群经验属于资深岗位环境，不是学生应具备的起点；直开网页需要 JavaScript，未核验当前招聘状态。

<link href="https://jobs.ashbyhq.com/PrimeIntellect/297d925e-5a42-40bd-b02f-5c928d226f18/" color="#087F8C">[S03] Prime Intellect：GPU Infrastructure</link>

把目标 JD 转为准备清单

为你愿意投递的 10-15 个校招 / 实习岗位建表：记录方向、语言、共同基础、核心专项、项目偏好、学历与实习条件。用**同一分支内的重复要求**决定优先级，并在投递时回到官方页面确认状态。

AI INFRA / CAMPUS PREPARATION　·　03

共同基础：先补这些

P0 = 各分支常用基础；专项深度按目标岗位决定。以下优先级是本导读的建议。

| 模块 | 需要学到什么程度 | 可以证明学会的产出 |
| --- | --- | --- |
| 编程与算法 / P0 | Python 熟练；C++ 掌握内存、RAII、容器、线程；平台线可加强 Go。会常见数据结构、复杂度、并发与测试。 | LRU / 队列实现；小型并发服务；能够解释锁与内存开销。 |
| Linux 与 OS / P0 | 进程线程、虚拟内存、页缓存、I/O、文件描述符、同步；用日志与系统指标排障。 | 定位一个 CPU 高、内存涨或 I/O 等待的问题；写复现与修复记录。 |
| 网络与分布式 / P0 | TCP / HTTP / RPC；超时、重试、幂等、背压、队列；理解吞吐、延迟和尾延迟。 | 设计有限并发队列；测试过载下的延迟与失败率。 |
| 数学与模型 / P0 | 线性代数与基础概率；Transformer、attention、token、张量 shape、前反向传播、优化器。 | 小模型训练 / 推理；标注各层 shape；估算参数与中间张量大小。 |
| PyTorch 与 GPU / P0 | 张量布局、dtype、autograd、设备迁移；GPU 内存层次、warp / block、异步执行与同步。 | 做 tensor profiling；解释数据拷贝、算子启动和显存瓶颈。 |
| 实验工程 / P0 | Git、环境版本、正确性检查、基准测试、原始日志；读英文官方文档。 | 一条命令可复现实验；固定硬件、模型、输入与随机种子。 |

学模型是为了理解执行代价

能解释训练与推理的区别、prefill 与 decode 的区别、为什么长上下文占更多 KV Cache；能区分算力受限、带宽受限、CPU 调度 / kernel launch 受限。进入具体优化时以 profile 验证瓶颈。

<link href="https://dlsyscourse.org/" color="#087F8C">[S13] CMU Deep Learning Systems</link>　<link href="https://cs336.stanford.edu/spring2025/" color="#087F8C">[S14] Stanford CS336: Language Modeling from Scratch (2025)</link>

没有系统基础时，先补 OS、网络与编程。只会框架命令通常不足以回答源码、并发和性能追问；无需把全部算法研究课程学完才开始系统项目。

AI INFRA / CAMPUS PREPARATION　·　04

专项路线：选一条做深

一个主方向 + 一项相邻能力，通常比四条线同时浅学更容易形成校招项目。

| 主线 | 专项知识 | 进阶内容 / 暂缓 |
| --- | --- | --- |
| 推理系统 | prefill / decode；KV Cache 与 PagedAttention；continuous batching、prefix cache；TTFT、TPOT、吞吐与 p95；vLLM 或 SGLang。 | 先跑通单 GPU 压测，再考虑 TP、PD 分离、投机解码与量化；量化后要检查质量。 |
| 训练系统 | DDP、梯度同步；FSDP / ZeRO 分片思想；DP / TP / PP；混合精度、梯度累积、checkpoint。 | 实测单机多 GPU；再学 NCCL、通信计算重叠、RDMA / RoCE 与大规模容错。 |
| 算子 / 编译器 | CUDA 或 Triton；coalescing、共享内存、归约、tiling、fusion、occupancy；数值误差与 profiling。 | 先写 reduction / softmax / matmul；再学 CUTLASS / CuTe、编译 IR、自动调优。 |
| 平台 / 集群 | Docker、K8s 对象与调度；GPU 资源、任务队列、配额、隔离；Prometheus / DCGM、日志与恢复。 | 进一步学 Operator、Kueue / Volcano、MIG、拓扑感知调度；无需先搭千卡集群。 |

不同学生的起点

**C++ / 系统基础较强：**优先做 Triton / CUDA 算子或推理 profiler 项目。
**Python / 深度学习基础较强：**先做推理压测或 DDP 实验，同时补 OS 和并发。
**后端 / 云原生项目较多：**先做资源调度与服务稳定性，再补 GPU 和模型执行。

工具边界要讲清

PagedAttention 关注 KV Cache 的管理与访问；FlashAttention 关注 attention 计算中的 I/O 优化。它们解决的层次不同。DDP 数据并行也不等于把模型参数分片；不要把各类并行、缓存和量化混为一种优化。

<link href="https://arxiv.org/abs/2506.21901" color="#087F8C">[S10] A Survey of LLM Inference Systems</link>　<link href="https://arxiv.org/abs/2407.20018" color="#087F8C">[S12] Efficient Training of LLMs on Distributed Infrastructures: A Survey</link>　<link href="https://docs.vllm.ai/en/latest/" color="#087F8C">[S15] vLLM 官方文档</link>　<link href="https://triton-lang.org/main/getting-started/tutorials/index.html" color="#087F8C">[S16] Triton 官方教程</link>　<link href="https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html" color="#087F8C">[S17] PyTorch Distributed Data Parallel 教程</link>

AI INFRA / CAMPUS PREPARATION　·　05

网上的人在讨论什么

以下是求职讨论的压缩综述与校招启示，均为转述；不复制完整帖子。

1. 个人面经：从概念继续追到实现

牛客的百融云创面经提到 reduction 按不同 shape 优化、vLLM 的进一步改进、FlashAttention、CUDA 内存模型、线程与锁，以及手写 LRU。**校招启示：**把项目准备成“实现细节 + 边界条件 + 为什么这样选”的说明，而不止记术语。该帖子为个人经历，并非所有公司的统一题库。

<link href="https://www.nowcoder.com/discuss/724396208503947264" color="#087F8C">[S04] 百融云创 AI Infra 面经（已口头 offer）</link>

2. 题目汇总：用来找盲点，答案仍需核对

牛客运营的汇总覆盖推理引擎、显存、训练并行及服务限流等话题。**校招启示：**做一张概念自测表，每题都配原理或实验；帖子中“吞吐提高数倍”这类概括不能作为你项目的实测结果。

<link href="https://www.nowcoder.com/discuss/891334000239734784" color="#087F8C">[S05] AI Infra 面试汇总（含回答思路）</link>

3. JD 学习路线：平台线重云原生，但样本有偏

GitHub 的个人汇总以 SRE / DevOps / 运维与 AI Infra 混合岗位为样本，强调 K8s、自动化、GPU 管理、RDMA 和可观测性。**校招启示：**平台方向值得参考；其中频次不能推广到推理内核或编译器岗位，更不能把 Go 或 K8s 当作所有 AI Infra 的第一要求。

<link href="https://github.com/jfang2048/SRE-Job-Description" color="#087F8C">[S06] SRE-Job-Description</link>

4. GPU 转行讨论：先确定自己的工程层次

Reddit 的讨论区分了部署 / 扩缩容、性能优化、算子及编译器等工作。有人指出一个人同时覆盖全部角色并不现实。**校招启示：**选一两项最想深入的能力，把 profiling、正确性和性能解释做扎实。匿名回复的热门趋势判断未独立核验。

<link href="https://www.reddit.com/r/CUDA/comments/1u7z83g/breaking_into_gpu_infrastructure_gpu_programming/" color="#087F8C">[S07] Breaking into GPU Infrastructure / GPU Programming Feels Overwhelming</link>

5. 从部署到系统优化：GPU 没跑满只是起点

一个有 LLM 服务实践的发帖者关注访存、batching、调度背压与实时延迟；另一个网络工程背景的求职帖讨论 GPU 节点、监控、模型存储和多 GPU 部署。**校招启示：**让项目回答一个具体系统问题，保留负载、资源与故障处理的证据。

<link href="https://www.reddit.com/r/kubernetes/comments/1tejfyz/interview_prep_for_ai_infra_role/" color="#087F8C">[S08] Interview prep for AI Infra role</link>　<link href="https://www.reddit.com/r/CUDA/comments/1t5txel/building_a_career_in_ai_infrastructure_and/" color="#087F8C">[S09] Building a career in AI infrastructure and inference engineering</link>

AI INFRA / CAMPUS PREPARATION　·　06

16 周校招准备安排

假设已有编程基础，每周投入约 10-15 小时；用于形成可展示作品，不是录用保证。

| 阶段 | 学习与实践 | 阶段验收 |
| --- | --- | --- |
| 第 1-3 周 / 补底座 | Python / C++、Linux、网络、常见算法；跑 PyTorch 小模型；做张量 shape、显存与耗时记录。 | 能解释模型一次前向；会排查进程 / 内存 / I/O；代码能复现。 |
| 第 4-5 周 / 理解 GPU | 学习内存层次、同步、profile；写 vector add / reduction；对比 CPU 与 GPU。 | 能说明慢在哪里；正确性测试覆盖不同 shape / dtype。 |
| 第 6-8 周 / 主项目基线 | 以推理为例：跑一个小模型服务，写请求负载，测 TTFT / TPOT / p95 / tokens/s 与显存。 | 有环境、原始日志、基准表；指标定义清楚，负载固定。 |
| 第 9-12 周 / 做专项改进 | 推理线对比 batching / cache；算子线改进 tiling / fusion；训练线做 DDP；平台线做调度 / 限流。 | 控制变量的前后对比；解释收益、代价、失败场景与结论边界。 |
| 第 13-14 周 / 读源码与整理 | 围绕一个功能读源码，画调用链；补 README、实验报告、架构图；做一个小修复或复现记录。 | 用 5 分钟讲清项目；能沿调用链解释一个实现点。 |
| 第 15-16 周 / 面试与投递 | 按目标 JD 补弱项；算法、系统设计、项目追问；投递校招 / 实习并迭代。 | 简历每个结果能追溯到数据；准备三个权衡与一个故障复盘。 |

如果你是零基础

可先额外安排 6-10 周补编程、OS、网络与 PyTorch，具体取决于现有能力。不要为赶进度略过正确性与基础概念。大学课程的完整作业量可能超过这里的时间，建议选择相关部分。

没有 GPU 的起步方式

CPU 可以做模型正确性、服务队列、Linux / 网络和源码学习。GPU 真实性能、CUDA 算子和多卡通信需要相应硬件验证；有条件时再用实验室 GPU 或按需租用。小模型是否放得下取决于权重、dtype、KV Cache、并发和上下文长度，不能只看参数量。

<link href="https://cs336.stanford.edu/spring2025/" color="#087F8C">[S14] Stanford CS336: Language Modeling from Scratch (2025)</link>

AI INFRA / CAMPUS PREPARATION　·　07

写进简历的三个项目

选一个作为主项目。学生可以从单机、小模型和有限范围开始。

项目 A：可复现的 LLM 推理性能报告

**问题：**不同请求长度与并发下，吞吐和延迟如何变化？
**实现：**固定模型、硬件和引擎版本，比较两种 batching 或 prefix cache 配置；记录请求长度分布、arrival rate、warm-up、输出长度与超时。
**交付：**启动脚本、负载脚本、原始日志、结果图、瓶颈分析；至少解释一次收益消失的条件。

**评估：**TTFT（首 token 等待）、TPOT（输出阶段每 token 时间）、p95 请求延迟、输出 tokens/s、峰值显存、失败率。对并发闭环测试与按到达率开环测试分别注明；量化等改变数值行为的优化应额外验证质量。

<link href="https://docs.vllm.ai/en/latest/" color="#087F8C">[S15] vLLM 官方文档</link>

项目 B：一个 Triton / CUDA 算子的优化过程

**问题：**选择 reduction、softmax 或矩阵乘法，解释时间花在哪里。
**实现：**从正确基线开始，改进访问合并、tiling 或 fusion；覆盖多个 shape、dtype 与数值误差。
**交付：**基线与优化版本、单元正确性、benchmark、profile 截图和原理图。测 GPU 计时要考虑异步执行，使用 CUDA events 或适当同步。

**避免：**只展示一个有利 shape，或比较不等价算法 / 精度后声称普遍加速。结果中注明计时是否包含数据传输与启动开销。

<link href="https://triton-lang.org/main/getting-started/tutorials/index.html" color="#087F8C">[S16] Triton 官方教程</link>　<link href="https://github.com/gpu-mode/lectures" color="#087F8C">[S18] GPU MODE lectures</link>

项目 C：小型 GPU 任务调度 / 推理服务平台

**问题：**资源不足、请求突增或进程失败时如何处理？
**实现：**做任务队列、配额、超时、重试、背压与状态持久化；增加基本监控，模拟服务崩溃或负载过高。平台线可接容器 / K8s；训练线可替换为 DDP checkpoint 恢复实验。
**交付：**架构图、接口、排队策略、故障演练和结果。没用真实 GPU 的部分标为模拟，不声称集群生产经验。

简历写法：用真实测量填写空位

“在 [GPU / 模型 / 引擎版本] 和 [负载] 下，针对 [瓶颈] 实现 [改进]，将 [指标] 从 [基线] 改为 [结果]；以 [验证方法] 确认正确性，并分析 [代价]。”不填未经测量的百分比。

AI INFRA / CAMPUS PREPARATION　·　08

已下载综述：怎么选读

原始公开英文 PDF；页数由本地文件校验。先看综述图与分类，再按项目定位细节。

推理系统综述 / 25 页

从算子、batching、调度到 KV Cache 管理，再看单副本 / 多副本、分离部署与 serverless。

**读完应能回答：**能否画出一次请求的执行路径？优化解决算力、带宽、容量还是调度问题？

本地文件：03_LLM_Inference_Systems_Survey_2506.21901.pdf

<link href="https://arxiv.org/abs/2506.21901" color="#087F8C">[S10] A Survey of LLM Inference Systems</link>

推理引擎综述 / 106 页

用作技术分类与引擎生态参考，按项目选择读；不建议校招初学者一次通读。

**读完应能回答：**不同引擎 / 方法的适用硬件、工作负载与限制是什么？

本地文件：04_Inference_Engines_Survey_2505.01658.pdf

<link href="https://arxiv.org/abs/2505.01658" color="#087F8C">[S11] A Survey on Inference Engines for Large Language Models</link>

分布式训练综述 / 42 页

优先看训练基础设施、并行策略、计算 / 通信 / 内存优化与可靠性。

**读完应能回答：**模型状态如何分布？何时通信？故障之后从哪里恢复？

本地文件：05_Distributed_Training_Survey_2407.20018.pdf

<link href="https://arxiv.org/abs/2407.20018" color="#087F8C">[S12] Efficient Training of LLMs on Distributed Infrastructures: A Survey</link>

课程与实作入口

| 资料 | 用途 |
| --- | --- |
| CMU Deep Learning Systems [S13] | 理解 autograd、算子、硬件和系统之间的关系。 |
| Stanford CS336 2025 [S14] | A1 补 Transformer 实现；A2 练 profiling、Triton 与分布式训练。 |
| vLLM / Triton / PyTorch [S15-S17] | 以官方文档作为环境配置、API 与实验实现的依据。 |
| GPU MODE lectures [S18] | 按需要选择 GPU 编程、kernel 和 profiling 原始讲座。 |

推荐阅读顺序：中文导读 → 推理系统综述的分类与示意图 → 官方教程的一个小实验 → 对应源码 / 论文。训练方向则把第三篇综述提前。论文覆盖时间不等于检索日期；具体 API 以实验版本的官方文档为准。

AI INFRA / CAMPUS PREPARATION　·　09

来源与阅读索引

全部于 2026-10-07 检索。点击标题打开原始来源；离线完整 URL 见 sources.md。

**S01 · 官方招聘**

<link href="https://talent.baidu.com/jobs/detail/GRADUATE/b9f68e95-00a5-4dcd-9c32-876865e79916" color="#087F8C">百度校园招聘：大模型推理基建相关岗位</link>

校园岗样本；C++/Python、GPU 算子、推理引擎、通信与性能优化。

**S02 · 官方招聘**

<link href="https://jobs.bytedance.com/en/position/7491726420784777480/detail" color="#087F8C">字节跳动：Compute Infrastructure / Orchestration &amp; Scheduling</link>

搜索索引可读，正文访问失败；仅作调度平台方向样本，未确认仍在招聘。

**S03 · 官方招聘**

<link href="https://jobs.ashbyhq.com/PrimeIntellect/297d925e-5a42-40bd-b02f-5c928d226f18/" color="#087F8C">Prime Intellect：GPU Infrastructure</link>

搜索索引可读，直开页面要求 JavaScript；为社招方向样本，非校招门槛。

**S04 · 个人面经 / 牛客**

<link href="https://www.nowcoder.com/discuss/724396208503947264" color="#087F8C">百融云创 AI Infra 面经（已口头 offer）</link>

2025-02-26；涉及 reduction、vLLM、FlashAttention、CUDA 内存及 LRU。

**S05 · 平台运营整理 / 牛客**

<link href="https://www.nowcoder.com/discuss/891334000239734784" color="#087F8C">AI Infra 面试汇总（含回答思路）</link>

面试话题索引；不是可验证的统一真题或标准答案。

**S06 · 个人 JD 汇总 / GitHub**

<link href="https://github.com/jfang2048/SRE-Job-Description" color="#087F8C">SRE-Job-Description</link>

混合 SRE、DevOps、AI Infra 样本；频次不代表全行业比例。

**S07 · 社区讨论 / Reddit**

<link href="https://www.reddit.com/r/CUDA/comments/1u7z83g/breaking_into_gpu_infrastructure_gpu_programming/" color="#087F8C">Breaking into GPU Infrastructure / GPU Programming Feels Overwhelming</link>

讨论岗位拆分、选择专长、GPU profiling；匿名经验。

**S08 · 社区讨论 / Reddit**

<link href="https://www.reddit.com/r/kubernetes/comments/1tejfyz/interview_prep_for_ai_infra_role/" color="#087F8C">Interview prep for AI Infra role</link>

网络工程背景转 AI Infra；GPU 节点、监控、存储和推理部署。

**S09 · 社区讨论 / Reddit**

<link href="https://www.reddit.com/r/CUDA/comments/1t5txel/building_a_career_in_ai_infrastructure_and/" color="#087F8C">Building a career in AI infrastructure and inference engineering</link>

从部署走向利用率、访存、调度、延迟优化；匿名经验。

证据口径：官方 JD 用来辨认职责；面经与社区只提供准备线索。这里没有抽样调查，不报告招聘量、薪资分布或录用率。对访问受限页面已单独说明。

AI INFRA / CAMPUS PREPARATION　·　10

论文、课程与官方文档

全部于 2026-10-07 检索。点击标题打开原始来源；离线完整 URL 见 sources.md。

**S10 · 论文综述 / arXiv**

<link href="https://arxiv.org/abs/2506.21901" color="#087F8C">A Survey of LLM Inference Systems</link>

原始公开 PDF 已下载；25 页。

**S11 · 论文综述 / arXiv**

<link href="https://arxiv.org/abs/2505.01658" color="#087F8C">A Survey on Inference Engines for Large Language Models</link>

原始公开 PDF 已下载；106 页。

**S12 · 论文综述 / arXiv**

<link href="https://arxiv.org/abs/2407.20018" color="#087F8C">Efficient Training of LLMs on Distributed Infrastructures: A Survey</link>

原始公开 PDF 已下载；42 页。

**S13 · 大学课程**

<link href="https://dlsyscourse.org/" color="#087F8C">CMU Deep Learning Systems</link>

自动微分、算子、硬件与系统；适合补系统基础。

**S14 · 大学课程**

<link href="https://cs336.stanford.edu/spring2025/" color="#087F8C">Stanford CS336: Language Modeling from Scratch (2025)</link>

已归档课程；重点选 A1 模型与 A2 系统，不必一次完成所有作业。

**S15 · 官方文档**

<link href="https://docs.vllm.ai/en/latest/" color="#087F8C">vLLM 官方文档</link>

部署、benchmark、缓存与并行；版本变化需记录实验版本。

**S16 · 官方文档**

<link href="https://triton-lang.org/main/getting-started/tutorials/index.html" color="#087F8C">Triton 官方教程</link>

从向量加法到矩阵乘与 fused attention。

**S17 · 官方文档**

<link href="https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html" color="#087F8C">PyTorch Distributed Data Parallel 教程</link>

DDP 实验入口；先确认训练正确性，再评估通信开销。

**S18 · 社区原始讲座材料**

<link href="https://github.com/gpu-mode/lectures" color="#087F8C">GPU MODE lectures</link>

GPU 编程与性能优化讲座材料，按兴趣选择。