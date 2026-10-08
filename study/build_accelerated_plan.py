from pathlib import Path
from datetime import date,timedelta
import json

ROOT=Path(__file__).resolve().parent
base=json.loads((ROOT/'daily_plan.json').read_text(encoding='utf-8'))
start=date(2026,10,7)
counts=[3,3,3,3,3,2,2]*5+[3,3,3,3,2,2,1]
assert len(counts)==42 and sum(counts)==112
plans=[];cursor=0
for index,count in enumerate(counts,1):
 blocks=base['days'][cursor:cursor+count];cursor+=count
 review=index%7==0
 plans.append({'day':index,'week':(index-1)//7+1,'date':(start+timedelta(days=index-1)).isoformat(),'baseline_days':[b['day'] for b in blocks], 'title':' / '.join(b['title'] for b in blocks),'blocks':blocks,'minimum_minutes':150 if review else 360,'target_minutes':180 if review else 390,'optional_minutes':60,'review_day':review,'daily_extras':['算法或面试基础：普通日 40-60 分钟，围绕当前薄弱点。','实验记录、口头解释与自测：20-30 分钟。','如基准学习块不足时间，用代码实现、边界检查、复现实验深化；不为凑时间增加无关内容。']})
out={'start_date':start.isoformat(),'end_date':plans[-1]['date'],'timezone':'Asia/Shanghai','duration_weeks':6,'baseline_days':112,'daily_days':42,'daily_budget':'普通日 6-7 小时，至多 1 小时选做；每第七天 2-3 小时复盘补缺。','mastery_rules':['已有能力通过简短解释和实际产出验收后可跳过，不重复刷时间。','同一天的多个学习块仍遵守先决条件；关键基础或正确性未过不能硬跳。','没有 GPU 时先做 CPU 正确性/模拟/源码，真实 GPU 与多卡性能验收保留为待验证。','若基础好且验收连续通过，可提前完成；42 天为冲刺目标，不是掌握保证。'],'resources':base['resources'],'days':plans}
(ROOT/'accelerated_plan.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# AI Infra 6 周冲刺每日安排',f"开始：{out['start_date']}；目标结束：{out['end_date']}；北京时间。",'将原 16 周的 112 个学习块压缩为 42 个日程；不是删除基础内容。普通日 6-7 小时，选做最多 1 小时，每第七天 2-3 小时复盘补缺。','## 推进规则','按验收推进，不按日历机械跳过。已掌握的内容可快速验收；未完成任务与疑问优先。缺 GPU 的真实性能暂不验收，不能当作已完成。若基础较弱、GPU 尚不可用或每日时间不足，目标日期相应调整。','## 推荐时间块','08:30-10:30 学习块 A；10:45-12:15 实践/算法；14:00-16:00 学习块 B；16:15-17:30 学习块 C/实验；20:00-20:30 自测与记录。按实际登录时间重新分配，晚登录不补堆 7 小时。','## 晚间汇报模板','日期 / 冲刺 Day：\n完成与产出：\n实际投入：\n卡点/疑问：\n超额完成：\n明日可用时间：']
for entry in plans:
 if entry['day']%7==1:lines.append(f"## 冲刺第 {entry['week']} 周")
 lines.append(f"### Day {entry['day']:02d} · {entry['date']} · {'复盘补缺日' if entry['review_day'] else '集中学习日'}\n\n覆盖原学习块：{', '.join(map(str,entry['baseline_days']))}；预算：约 {entry['target_minutes']//60} 小时 {entry['target_minutes']%60} 分钟。")
 for i,block in enumerate(entry['blocks'],1):
  resource=base['resources'][block['resource']]
  lines.append(f"**学习块 {i}：{block['title']}**\n\n- 学习：{block['learn']}\n- 实践：{block['practice']}\n- 验收产出：{block['deliverable']}\n- [资料入口]({resource})")
 lines.append('复盘日：保留本日基准主题，优先回顾与补缺；如两个主题无法在预算内完成，应顺延。' if entry['review_day'] else '当日补充：40-60 分钟算法/面试基础，20-30 分钟自测与实验记录；掌握快则提前学习下一日，卡点多则收缩范围。')
(ROOT/'6_week_sprint_plan.md').write_text('\n\n'.join(lines)+'\n',encoding='utf-8')
state=json.loads((ROOT/'progress.json').read_text(encoding='utf-8'))
state.update({'end_date':out['end_date'],'active_plan':'accelerated_plan.json','duration_weeks':6,'planned_day_cursor':1,'baseline_day_cursor':1,'available_minutes':390,'notes':'用户要求提高每日投入并尽快完成；启用 6 周冲刺。Day 1 在本轮聊天提供，尚无完成汇报。'})
(ROOT/'progress.json').write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'days':len(plans),'baseline_blocks':sum(len(x['blocks']) for x in plans),'start':out['start_date'],'end':out['end_date']},ensure_ascii=True))
