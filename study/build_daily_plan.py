from pathlib import Path
from datetime import date, timedelta
import json

ROOT=Path(__file__).resolve().parent
START=date(2026,10,7)
weeks=[
('编程、环境与能力盘点',[
('环境与能力盘点','记录 Python/C++、Linux、算法、PyTorch 的现有水平，以及每天可投入时间；列出 CPU、内存、GPU 和可用开发环境','用已有 Python 运行一个脚本；已有 Git 则建立练习目录并保存笔记，无需先购买 GPU','baseline.md：基础、硬件、时间与一个可运行脚本'),
('Python 数据结构与复杂度','复习 list、dict、set、deque 及常用操作的复杂度','实现词频统计与固定容量队列，补三个边界输入','python_basics.py + 复杂度说明'),
('Python 文件与实验记录','练习 pathlib、JSON、CSV、异常处理和日志','将昨天程序改为可读取输入并输出 JSON 结果','输入样例、结果文件与异常处理说明'),
('Linux 进程与文件','学习进程、权限、目录、标准输入输出；使用现有 Linux/WSL 或学校环境','观察一个自己运行的进程，记录 PID、CPU、内存和退出方式','linux_process.md；缺环境则记录安装需求，不强制当天安装'),
('C++ 内存与 RAII','复习对象生命周期、引用、指针、vector、unique_ptr 与 RAII','实现一个小型缓存或资源管理示例；暂时不会 C++ 就先读懂示例并写伪代码','cpp_raii.cpp 或带解释的伪代码'),
('算法：哈希与 LRU','学习哈希表、双向链表、LRU 淘汰过程','用熟悉语言实现 LRU，覆盖空容量、更新和淘汰','LRU 实现与边界用例'),
('第 1 周复盘','回看本周产出，闭卷解释 Python 数据结构、进程和 RAII','补一个最薄弱的点，整理下周可投入时间','周复盘：完成、遗留、疑问、调整'),
]),
('操作系统、网络与并发',[
('进程、线程与同步','理解进程/线程、锁、死锁与共享状态','实现线程安全计数或用最小示例复现竞态','并发示例 + 正确性解释'),
('内存与 I/O','学习虚拟内存、页缓存、文件描述符、缓冲','比较分块读文件与一次读入的时间和内存；使用小文件','memory_io.md + 简单测量'),
('TCP、HTTP 与 RPC','画一次 HTTP 请求路径，理解连接、超时和连接复用','用本地客户端/服务端请求，记录状态码与耗时','请求路径图 + 本地请求日志'),
('生产者消费者队列','学习有界队列、吞吐、背压和等待','实现有限容量生产者消费者队列，观察队列积压','queue_demo.py + 队列长度记录'),
('超时、重试与幂等','区分超时、重试和重复执行；理解退避','为本地模拟服务加入超时、有限重试与幂等键','故障模拟记录 + 重试策略'),
('延迟分布与系统排障','理解平均值、p50、p95、失败率；区分服务时间与排队时间','模拟突发负载并记录延迟，解释尾延迟来源','负载脚本 + 延迟表'),
('第 2 周复盘','闭卷说明死锁、背压、幂等与 p95','用昨天日志讲一次定位过程，补一项薄弱知识','周复盘 + 一张系统排障流程图'),
]),
('PyTorch 与模型执行',[
('张量、shape 与 dtype','学习张量维度、广播、dtype、stride 与设备','做矩阵乘、转置、reshape 的小实验并标注 shape','tensor_shapes.py + shape 表'),
('autograd 与训练循环','理解计算图、梯度、优化器和清零','用 CPU 跑一个极小训练循环，检查 loss 与梯度','train_tiny.py + loss 记录'),
('线性层与模型状态','理解参数、梯度、优化器状态和张量字节数','估算一个小模型参数内存，并与实际张量大小核对','模型状态与内存估算表'),
('Attention 基本实现','理解 Q/K/V、缩放点积、softmax、因果 mask','实现小规模 attention，检查 shape 与 mask','attention_toy.py + 正确性检查'),
('Transformer 前向路径','画 embedding、attention、MLP、residual、norm 的执行路径','阅读或运行一个小 Transformer，标注关键张量','forward_path.md + 执行示意图'),
('prefill 与 decode','理解自回归生成、prefill、decode 与 KV Cache 的目的','用小例子计算有/无缓存时重复工作的区别','prefill_decode.md + 计算示例'),
('第 3 周复盘','闭卷解释一次训练步骤和一次生成步骤','检查模型基础是否能支撑推理项目；补一个概念','周复盘 + 三分钟模型执行讲解'),
]),
('GPU 架构与 profiling',[
('GPU 内存层次','学习 global/shared/register、SM、warp、block','将模型执行步骤映射到数据搬运与计算；无 GPU 时先做示意图','gpu_memory_map.md'),
('并行与访存','理解线程索引、访问合并、分支发散与 occupancy','手推一个向量加法的线程分配和访存模式','vector_add_layout.md'),
('异步执行与正确计时','理解 kernel launch、stream、同步与 CUDA events','有 GPU 时比较不同计时方式；无 GPU 时标出测量设计','gpu_timing.md + 可运行计时脚本或伪代码'),
('算力与带宽瓶颈','理解算术强度与 roofline 的概念','估算向量加法/矩阵乘的数据访问与 FLOPs','bottleneck_estimates.md'),
('第一次 profile','学习 PyTorch profiler；区分 CPU 调度、算子和拷贝','对小模型收集 profile；CPU 环境注明不能推出 GPU 结论','profile trace + 初步瓶颈说明'),
('CPU/GPU 数据搬运','学习拷贝、同步、pinned memory 的概念','分析一段重复搬运代码；有 GPU 才做真实对比','transfer_analysis.md'),
('第 4 周复盘','闭卷解释访存、异步计时与瓶颈判断','整理可用 GPU 条件；未获得 GPU 时列出后续待验证项','周复盘 + 硬件验证清单'),
]),
('Triton/CUDA 小算子实践',[
('向量加法正确基线','选择 Triton 或 CUDA 一种入口；阅读官方向量加法教程','实现/逐行解释 vector add，检查不同长度和边界','vector_add + correctness 记录'),
('归约基线','理解并行 reduction 与中间结果','实现/解释 sum reduction，检查多种 shape','reduce_baseline + shape 用例'),
('归约访存优化','学习 block size、访问合并与减少重复访存','只改变一个参数或策略，对比正确性和计时','reduce_results.csv + 单变量结论'),
('Softmax 与融合','理解 softmax 数值稳定性及 fusion 减少搬运','实现小型 softmax；对比参考结果与误差','softmax + 误差记录'),
('矩阵乘 tiling','学习分块、数据复用与边界处理','跑/解释官方小矩阵乘教程，画 tile 关系','matmul_layout.md + 示例结果'),
('算子基准报告','固定硬件、dtype、shape、warm-up 与计时口径','整理基线与改进；无 GPU 时明确全部性能为待验证','kernel_report.md'),
('第 5 周复盘','闭卷解释优化为何有效、何时无效','整理一个算子项目小故事，选择推理作为后续主项目','周复盘 + 算子项目说明'),
]),
('LLM 推理服务基线',[
('选择小模型与实验环境','核对可用显存、dtype、上下文与并发需求，选择可运行模型','记录模型来源/许可、引擎与驱动版本；没 GPU 先用 CPU 验证流程','environment.md + 资源估算'),
('跑通一次离线推理','用固定输入运行模型，记录输出、参数和启动步骤','保存可复现脚本与依赖；不先优化性能','offline_inference.py + 固定样例'),
('启动本地推理服务','阅读 vLLM 官方服务文档，理解启动参数与接口','在具备支持的环境运行服务；否则完成客户端与模拟服务','service_start + API 样例'),
('流式输出与首 token','理解流式响应、TTFT 与客户端测量边界','实现流式客户端，标注开始、首 token 和结束时间','stream_client.py + 时间记录'),
('显存与上下文实验','固定其他条件，对比少量上下文长度/输出长度','记录显存或设计待验证实验，不运行超出资源的配置','memory_context.csv + 解释'),
('基线配置冻结','整理模型、硬件、软件、输入和计时口径','建立 baseline 配置与一次可重复运行入口','baseline_config.json + README'),
('第 6 周复盘','确认推理链路、版本和基线是否可复现','补环境/服务阻塞，决定下周能做真实还是模拟压测','周复盘 + 项目状态'),
]),
('压测与指标体系',[
('定义性能指标','明确 TTFT、TPOT、端到端延迟、吞吐和失败率','写指标定义与采集位置，避免混用请求/s 与 token/s','metrics.md'),
('设计请求负载','定义输入/输出长度、请求数和随机种子','生成固定负载集，注明 tokenizer 与 token 长度','workload.jsonl + 负载统计'),
('闭环并发压测','理解固定并发客户端的限制','测试小范围并发梯度，收集原始请求日志','closed_loop.py + 原始日志'),
('开环到达率压测','理解 arrival rate、排队与超载','实现受控到达率请求生成器，设置时间与请求上限','open_loop.py + 到达率日志'),
('分位数与图表','计算 p50/p95、TTFT、TPOT 和吞吐','画延迟/吞吐随负载变化的图，记录失败和超时','结果图 + 指标表'),
('warm-up 与重复实验','分析冷启动、warm-up、抖动与重复测量','重复小规模基线，记录差异和可复现条件','repeatability.md'),
('第 7 周复盘','用结果解释饱和点与尾延迟','检查负载公平性、原始数据和指标定义，补一个测量缺陷','周复盘 + baseline_report.md'),
]),
('KV Cache、batching 与缓存',[
('KV Cache 内存估算','理解层数、KV head、dtype、序列长度与并发对缓存大小的影响','为当前模型估算 KV Cache，并注明近似条件','kv_memory_estimate.md'),
('PagedAttention','理解逻辑 token 块、物理块和块表','画请求增长/释放时缓存块的变化，与 FlashAttention 区分','paged_attention_diagram.md'),
('Continuous batching','理解请求加入/结束时的动态批处理','做一个玩具调度仿真，比较静态批与动态合批','batching_simulation.py'),
('Prefix cache','理解共享前缀、命中率与失效条件','构造共享/不共享前缀负载，保存公平对比设计','prefix_workloads + 实验设计'),
('缓存配置对比','固定负载、模型与硬件，比较缓存开/关','记录 TTFT、吞吐、显存与命中指标；无 GPU 标为待实测','prefix_cache_results.csv'),
('项目基线总结','汇总不同长度和并发下的结果与瓶颈','写一个失败或收益消失场景；不泛化单一 workload','inference_baseline_report.md'),
('第 8 周复盘','闭卷解释 PagedAttention、FlashAttention、batching 与 prefix cache 的边界','选一个最有依据的瓶颈作为下阶段优化目标','周复盘 + 优化假设'),
]),
('推理主项目：验证一个优化',[
('写优化假设','明确瓶颈证据、预期收益和代价','只选择一项 batching/cache/调度参数改动，定义对照实验','optimization_hypothesis.md'),
('实施最小改动','记录参数/代码改动与回退办法','先验证正确性，再运行低负载冒烟','最小改动 + 验证记录'),
('长度梯度实验','对短/中/长输入与输出做控制变量实验','保留原始数据，不只选有利案例','length_sweep.csv'),
('负载梯度实验','对多个并发或 arrival rate 做公平比较','测吞吐、延迟、失败率和显存','load_sweep.csv'),
('权衡与失败案例','分析提高吞吐是否损害 TTFT/p95 或资源占用','复现一个收益有限或变差的条件','tradeoffs.md'),
('结果与因果解释','结合 profile 与日志解释改动作用位置','整理 baseline/优化图表并注明限制','optimization_report_v1.md'),
('第 9 周复盘','检查假设是否被数据支持','必要时否定原假设；安排一个小的后续实验','周复盘 + 下一步假设'),
]),
('推理进阶与相邻能力',[
('FlashAttention 原理','理解 attention I/O、分块与在线 softmax','画数据搬运对比，不把它等同于 KV Cache 分页','flash_attention_notes.md'),
('图与启动开销','学习 CUDA Graph 与 CPU/GPU 同步开销的作用条件','从 profile 判断项目是否涉及启动开销；无证据不强行加图','launch_overhead_analysis.md'),
('量化与质量','理解权重/激活量化、dtype 与质量代价','设计小型质量样例与等价性检查，不只比较速度','quantization_evaluation_plan.md'),
('投机解码概念','理解草稿生成、验证与接受率','画一次验证过程，解释接受率和草稿开销的关系','speculative_decode.md'),
('Tensor Parallel 概念','理解线性层切分和集合通信位置','画单卡/双卡执行差异；没有双卡不声称多卡性能','tp_execution_map.md'),
('选择一项可行进阶实验','按当前 GPU 与基础只选择前述一项适用实验','若都不适用则继续打磨第 9 周主优化的边界测试','进阶实验或边界测试报告'),
('第 10 周复盘','能解释四种优化适用条件与代价','决定哪些保留在简历主线，哪些仅作理解','周复盘 + 项目范围'),
]),
('训练通信基础：小型 DDP',[
('DDP 与状态分类','理解参数、梯度、优化器状态和数据并行','画一次 DDP 梯度同步时序','ddp_timeline.md'),
('跑通分布式正确性','阅读 PyTorch DDP 官方教程','有多 GPU 跑小实验；否则用 CPU gloo 验证进程通信并注明局限','ddp_tiny.py + 环境说明'),
('AllReduce 与通信','理解 collective 的数学结果和通信路径','手推 2-4 个 rank 的梯度聚合，检查训练结果','allreduce_example.md'),
('FSDP 与 ZeRO 思想','区分参数/梯度/优化器状态分片','画 DDP 与分片状态对比，估算内存','sharding_table.md'),
('checkpoint 与恢复','保存并恢复模型、优化器、步数与随机状态','对比连续训练与恢复训练的小规模结果','checkpoint_demo.py + 恢复记录'),
('计算通信重叠','理解 bucket、等待和并行策略权衡','从 trace/文献示意定位通信；无法实测时写验证方案','communication_analysis.md'),
('第 11 周复盘','闭卷解释 DDP、FSDP、ZeRO、TP、PP 的区别','将训练知识与推理项目边界连起来，补一个薄弱点','周复盘 + 并行策略图'),
]),
('服务稳定性与平台基础',[
('容器与可复现环境','理解镜像、容器、挂载和 GPU runtime','整理现有服务的依赖/启动配置；可用时构建小镜像','部署说明或 Dockerfile'),
('资源队列与配额','学习请求队列上限、超时、取消和资源配额','为模拟/真实服务加入有限队列，测试取消与超载','queue_policy.md + 用例'),
('监控与告警','选择请求率、失败率、延迟、队列和 GPU/内存指标','给服务增加最小指标输出与日志关联','metrics endpoint 或监控样例'),
('故障恢复实验','明确自己服务的崩溃、重启和状态丢失场景','仅对练习服务演练一次失败与恢复，保留时间线','failure_recovery.md'),
('K8s 与 GPU 调度概念','理解 Pod、Deployment、Service、requests/limits、GPU 资源','画单服务部署与 GPU 任务排队图，已有集群时再运行','k8s_deployment_notes.md'),
('稳定性报告','说明限流、背压、恢复如何影响主项目指标','整理两种故障场景与恢复结果','reliability_report.md'),
('第 12 周复盘','以系统设计方式讲服务、队列、资源与失败处理','清理未验证的生产规模声称，列出项目实际边界','周复盘 + 架构图'),
]),
('阅读源码与系统解释',[
('选一个源码入口','固定引擎版本，选择调度、KV Cache 或指标采集中的一个小功能','找到实际入口与关键类/函数，记录 commit 或版本','source_entry.md'),
('追一条调用链','沿入口到核心处理路径阅读，标注状态变化','画调用链与数据结构，不要求通读整个仓库','call_chain.md'),
('连接源码与实验','将第 8-9 周的一项观察映射到源码机制','记录对应函数、条件和实验现象，区分推测与已验证','source_to_experiment.md'),
('最小复现','为一个边界或异常输入构造最小复现','记录预期、实际、版本和触发条件；没有 bug 也可做行为验证','minimal_repro + 说明'),
('小改进或文档澄清','选择自己能验证的日志、测试、文档或小修复','在练习分支准备可审阅改动；无需现在向他人发消息','diff + 验证记录'),
('复核解释','重新检查调用链、实验与结论一致性','写五分钟源码讲解，标注尚未理解的部分','source_walkthrough.md'),
('第 13 周复盘','闭卷沿调用链解释一次请求/一次调度','汇总阅读收益与待补点，收敛项目说明','周复盘 + 源码问答'),
]),
('交付、报告与简历材料',[
('README 可复现入口','为陌生读者写环境、安装、运行、负载和复现步骤','从干净目录/环境验证一条小规模复现路径','README.md + 复现日志'),
('数据与图表审核','检查单位、坐标、分位数、负载和 baseline 公平性','让每张结果图追溯到原始数据与脚本','final_figures + 数据索引'),
('报告成稿','写问题、方案、实验、结果、代价与局限','保留失败实验与否定假设，不制造提升数字','final_report.md'),
('项目讲解三种长度','准备 30 秒、3 分钟、10 分钟介绍','录音或写逐字提纲，突出自己的实现和判断','project_pitch.md'),
('简历项目条目','用真实环境、负载与结果写两条简历描述','逐条检查是否能被代码/日志支持','resume_project_bullets.md'),
('开源贡献准备','如有可验证小改动，整理补丁、复现和验证说明','检查目标项目 CONTRIBUTING；准备草稿，发布前按当时授权处理','contribution_draft.md'),
('第 14 周复盘','验收项目代码、报告、图表和讲解完整性','列出面试最可能追问的五个缺口','周复盘 + 面试缺口表'),
]),
('面试基础与岗位匹配',[
('目标岗位矩阵','选 5-10 个官方校招/实习 JD，确认方向与招聘状态','记录共同要求、差距、截止时间和官方链接','target_jobs.md'),
('算法：链表与缓存','练习 LRU、链表或队列中的两道目标难度题','解释复杂度与边界，避免只记题解','算法代码 + 自评'),
('OS 与并发问答','闭卷回答进程/线程、锁、死锁、内存与 I/O','针对一个错误回答用小实验补证','os_interview_notes.md'),
('网络与分布式问答','回答超时、重试、幂等、背压、尾延迟','设计一个过载推理服务，说明故障处理','system_design_draft.md'),
('GPU 与模型问答','回答访存、同步、prefill/decode、KV Cache 与 batching','用自己 profile 或结果支撑至少三个回答','gpu_inference_qa.md'),
('项目压力追问','回答为何这样做、替代方案、失败条件、自己贡献和测量可靠性','找出无法回答的两点，补材料','project_questions.md'),
('第 15 周复盘','模拟 30 分钟技术面并自评','根据目标岗位调整最后一周重点，不盲目新增大项目','周复盘 + 最后一周重点'),
]),
('模拟面试、投递与结项',[
('简历终审','检查技术栈、项目结果、措辞与校招匹配','输出一版可投递简历内容；删掉不实或无法解释的内容','resume_final_notes.md'),
('模拟面试一','进行算法/基础/项目综合模拟','记录回答漏洞、时间分配与追问','mock_interview_1.md'),
('针对性补弱','只处理昨日最重要的两个知识或项目缺口','做一个小练习或补充实验验证','gap_fixes.md'),
('推理系统设计模拟','设计不同长度和负载的推理服务，讨论缓存、batching、限流与监控','讲清性能目标和取舍，不泛化模型/硬件','inference_design_final.md'),
('投递材料与跟踪','核验官方申请页面、简历版本与项目链接','准备或按用户当时授权完成投递，建立状态表','application_tracker.md'),
('模拟面试二','围绕目标岗位进行最后一次模拟','比较第一次表现，整理入职/实习还需补的点','mock_interview_2.md'),
('16 周结项与后续','汇总完成、项目证据、仍未完成内容与求职反馈','形成下一阶段建议；提醒计划到期，不自动延长','final_review.md'),
]),
]
assert len(weeks)==16 and all(len(days)==7 for _,days in weeks)
resources={
 'guide':'../output/pdf/01_AI_Infra_Campus_Guide_CN.pdf',
 'sources':'../output/pdf/sources.md',
 'pytorch':'https://docs.pytorch.org/tutorials/',
 'ddp':'https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html',
 'triton':'https://triton-lang.org/main/getting-started/tutorials/index.html',
 'vllm':'https://docs.vllm.ai/en/latest/',
 'cs336':'https://cs336.stanford.edu/spring2025/',
 'dlsys':'https://dlsyscourse.org/',
 'gpu_mode':'https://github.com/gpu-mode/lectures',
}
plan=[]
for w,(theme,days) in enumerate(weeks,1):
 for d,(title,learn,practice,deliverable) in enumerate(days,1):
  num=(w-1)*7+d
  resource='guide' if w<=2 else 'pytorch' if w==3 else 'gpu_mode' if w==4 else 'triton' if w==5 else 'vllm' if 6<=w<=10 else 'ddp' if w==11 else 'sources' if w>=15 else 'guide'
  plan.append({'day':num,'week':w,'weekday_in_plan':d,'baseline_date':(START+timedelta(days=num-1)).isoformat(),'theme':theme,'title':title,'learn':learn,'practice':practice,'deliverable':deliverable,'minutes':60 if d==7 else 110,'resource':resource,'optional':'若必做已完成，花 15-20 分钟做一题算法或深入一个相关概念；不是追加必做。' if d!=7 else '可休息，或整理下周一项问题。'})
(ROOT/'daily_plan.json').write_text(json.dumps({'start_date':START.isoformat(),'end_date':plan[-1]['baseline_date'],'timezone':'Asia/Shanghai','main_track':'推理系统；算子、训练与平台作相邻能力','resources':resources,'days':plan},ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# AI Infra 16 周每日学习安排','开始：2026-10-07；结束：2027-01-26；时区：Asia/Shanghai。共 112 个基准学习日。','普通日约 90-120 分钟，复盘日约 60 分钟；已有编程基础的学生，以推理系统为主线。每天实际任务根据汇报调整，基准日期不强制赶进度。','## 使用方式','晨间最多安排 2-3 项必做，给出时长、资料入口、明确产出；选做单列。晚间在本聊天汇报完成项、产出、疑问和超额内容。','缺 GPU 的前几周仍可做基础、CPU 正确性和测量设计；真实性能必须在相应硬件上验证。','## 汇报模板','日期 / 学习日：\n完成：\n产出或结果：\n耗时：\n卡点/疑问：\n超额完成：\n明日可用时间：']
for entry in plan:
 if entry['weekday_in_plan']==1:lines.append(f"## 第 {entry['week']} 周：{entry['theme']}")
 lines.append(f"### Day {entry['day']:03d} · {entry['baseline_date']} · {entry['title']}\n\n- 学习：{entry['learn']}\n- 实践：{entry['practice']}\n- 验收：{entry['deliverable']}\n- 预算：约 {entry['minutes']} 分钟；[资料入口]({resources[entry['resource']]})\n- 选做：{entry['optional']}")
(ROOT/'16_week_daily_plan.md').write_text('\n\n'.join(lines)+'\n',encoding='utf-8')
state={'timezone':'Asia/Shanghai','start_date':START.isoformat(),'end_date':plan[-1]['baseline_date'],'planned_day_cursor':1,'completed_days':[],'partial_days':{},'blockers':[],'extra_completed':[],'available_minutes':110,'reported_dates':[],'morning_sent_dates':['2026-10-07'],'evening_sent_dates':[],'last_processed_report':None,'next_day_draft':None,'notes':'Day 1 于创建计划的本轮聊天提供；尚未收到用户学习成果，不能视为完成。'}
if not (ROOT/'progress.json').exists():(ROOT/'progress.json').write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
if not (ROOT/'daily_log.md').exists():(ROOT/'daily_log.md').write_text('# 每日学习记录\n\n## 2026-10-07：计划启动 / Day 1 已分配\n\n未收到学习进度汇报，完成状态未知。\n',encoding='utf-8')
print(json.dumps({'days':len(plan),'start':START.isoformat(),'end':plan[-1]['baseline_date'],'total_minutes':sum(x['minutes'] for x in plan)},ensure_ascii=True))
