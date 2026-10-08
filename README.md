# AI Infra 学习与实践

面向校招的 AI Infra 学习记录，主线为推理系统，逐步补充 Python、Linux、Git、硬件基础、GPU 编程与分布式系统。

## 目录

- `day1/`、`day2/`：每日任务、个人练习、实验输出与验收反馈；后续沿用 `dayN/`。
- `study/6_week_sprint_plan.md`：当前六周冲刺参考计划，2026-10-07 至 2026-11-17；任务按真实完成情况调整。
- `study/16_week_daily_plan.md`：原十六周学习块安排。
- `study/progress.json`、`study/daily_log.md`：进度与每日复盘记录。
- `output/pdf/`：中文学习综述、思维导图、资料来源和公开英文综述原文。

普通学习日参考 6-7 小时，每第七日复盘补缺。完成文件不等于完成验收；环境、正确性与性能结论需要对应证据。

## 环境

当前实验使用 Conda 环境 `torch311`，已记录 PyTorch `2.11.0+cu128`、torchvision `0.26.0+cu128` 与 NVIDIA RTX 4070。实际设备、版本和运行结果以每日环境记录为准。Notebook 需要选择对应解释器。

## 日常 Git 使用

在项目根目录查看并提交学习成果：

```powershell
git status
git diff
git add day1 day2 study
git commit -m "Record learning progress"
git push
```

新增每日目录时，将 `git add` 中的目录改为当天目录。提交前确认包含的是需要保存的练习和笔记。仓库排除了临时渲染文件、缓存、环境目录、模型权重和重复的 ZIP 资料包。

## 资料说明

中文导读与思维导图为整理成果；`output/pdf/originals/` 为公开论文原始下载，来源与校验信息见该目录的 `download_manifest.json` 和 `output/pdf/sources.md`。个人笔记保留实际学习过程及修订记录。
