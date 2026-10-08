# AI Infra 资料来源与下载索引

检索与下载日期：2026-10-07。面向学生 / 校招；优先级为导读建议，非就业统计。

## 原始公开 PDF 下载

下载未改写论文；metadata 与 SHA-256 见 originals/download_manifest.json。

- [A Survey of LLM Inference Systems](originals/03_LLM_Inference_Systems_Survey_2506.21901.pdf)：25 页；[原始 PDF](https://arxiv.org/pdf/2506.21901)；2.88 MiB。

- [A Survey on Inference Engines for Large Language Models: Perspectives on Optimization and Efficiency](originals/04_Inference_Engines_Survey_2505.01658.pdf)：106 页；[原始 PDF](https://arxiv.org/pdf/2505.01658)；2.34 MiB。

- [Efficient Training of Large Language Models on Distributed Infrastructures: A Survey](originals/05_Distributed_Training_Survey_2407.20018.pdf)：42 页；[原始 PDF](https://arxiv.org/pdf/2407.20018)；1.78 MiB。

## 网络讨论、招聘与学习资料

帖子以链接与简短转述收录；不保存全文转载。

### S01 百度校园招聘：大模型推理基建相关岗位

- 类型：官方招聘
- [访问原文](https://talent.baidu.com/jobs/detail/GRADUATE/b9f68e95-00a5-4dcd-9c32-876865e79916)
- 阅读提示：校园岗样本；C++/Python、GPU 算子、推理引擎、通信与性能优化。

### S02 字节跳动：Compute Infrastructure / Orchestration & Scheduling

- 类型：官方招聘
- [访问原文](https://jobs.bytedance.com/en/position/7491726420784777480/detail)
- 阅读提示：搜索索引可读，正文访问失败；仅作调度平台方向样本，未确认仍在招聘。

### S03 Prime Intellect：GPU Infrastructure

- 类型：官方招聘
- [访问原文](https://jobs.ashbyhq.com/PrimeIntellect/297d925e-5a42-40bd-b02f-5c928d226f18/)
- 阅读提示：搜索索引可读，直开页面要求 JavaScript；为社招方向样本，非校招门槛。

### S04 百融云创 AI Infra 面经（已口头 offer）

- 类型：个人面经 / 牛客
- [访问原文](https://www.nowcoder.com/discuss/724396208503947264)
- 阅读提示：2025-02-26；涉及 reduction、vLLM、FlashAttention、CUDA 内存及 LRU。

### S05 AI Infra 面试汇总（含回答思路）

- 类型：平台运营整理 / 牛客
- [访问原文](https://www.nowcoder.com/discuss/891334000239734784)
- 阅读提示：面试话题索引；不是可验证的统一真题或标准答案。

### S06 SRE-Job-Description

- 类型：个人 JD 汇总 / GitHub
- [访问原文](https://github.com/jfang2048/SRE-Job-Description)
- 阅读提示：混合 SRE、DevOps、AI Infra 样本；频次不代表全行业比例。

### S07 Breaking into GPU Infrastructure / GPU Programming Feels Overwhelming

- 类型：社区讨论 / Reddit
- [访问原文](https://www.reddit.com/r/CUDA/comments/1u7z83g/breaking_into_gpu_infrastructure_gpu_programming/)
- 阅读提示：讨论岗位拆分、选择专长、GPU profiling；匿名经验。

### S08 Interview prep for AI Infra role

- 类型：社区讨论 / Reddit
- [访问原文](https://www.reddit.com/r/kubernetes/comments/1tejfyz/interview_prep_for_ai_infra_role/)
- 阅读提示：网络工程背景转 AI Infra；GPU 节点、监控、存储和推理部署。

### S09 Building a career in AI infrastructure and inference engineering

- 类型：社区讨论 / Reddit
- [访问原文](https://www.reddit.com/r/CUDA/comments/1t5txel/building_a_career_in_ai_infrastructure_and/)
- 阅读提示：从部署走向利用率、访存、调度、延迟优化；匿名经验。

### S10 A Survey of LLM Inference Systems

- 类型：论文综述 / arXiv
- [访问原文](https://arxiv.org/abs/2506.21901)
- 阅读提示：原始公开 PDF 已下载；25 页。

### S11 A Survey on Inference Engines for Large Language Models

- 类型：论文综述 / arXiv
- [访问原文](https://arxiv.org/abs/2505.01658)
- 阅读提示：原始公开 PDF 已下载；106 页。

### S12 Efficient Training of LLMs on Distributed Infrastructures: A Survey

- 类型：论文综述 / arXiv
- [访问原文](https://arxiv.org/abs/2407.20018)
- 阅读提示：原始公开 PDF 已下载；42 页。

### S13 CMU Deep Learning Systems

- 类型：大学课程
- [访问原文](https://dlsyscourse.org/)
- 阅读提示：自动微分、算子、硬件与系统；适合补系统基础。

### S14 Stanford CS336: Language Modeling from Scratch (2025)

- 类型：大学课程
- [访问原文](https://cs336.stanford.edu/spring2025/)
- 阅读提示：已归档课程；重点选 A1 模型与 A2 系统，不必一次完成所有作业。

### S15 vLLM 官方文档

- 类型：官方文档
- [访问原文](https://docs.vllm.ai/en/latest/)
- 阅读提示：部署、benchmark、缓存与并行；版本变化需记录实验版本。

### S16 Triton 官方教程

- 类型：官方文档
- [访问原文](https://triton-lang.org/main/getting-started/tutorials/index.html)
- 阅读提示：从向量加法到矩阵乘与 fused attention。

### S17 PyTorch Distributed Data Parallel 教程

- 类型：官方文档
- [访问原文](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)
- 阅读提示：DDP 实验入口；先确认训练正确性，再评估通信开销。

### S18 GPU MODE lectures

- 类型：社区原始讲座材料
- [访问原文](https://github.com/gpu-mode/lectures)
- 阅读提示：GPU 编程与性能优化讲座材料，按兴趣选择。