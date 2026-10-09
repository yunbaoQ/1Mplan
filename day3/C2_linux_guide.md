# C-2：虚拟机中的路径、进程与日志实验

预算45分钟以内。你已打开虚拟机，先打开Linux终端。下面是教学操作步骤，由你在虚拟机执行；助手没有操作虚拟机，不据此记实操完成。不要求安装软件或重新部署模型。熟悉的命令可以直接解释并跳过重复练习。

## 1. 创建自己的练习目录（约5分钟）

在Linux终端执行，保持后续步骤在同一终端：
```bash
mkdir -p ~/ai-infra-day3
cd ~/ai-infra-day3
pwd
ls
```
记录pwd实际输出。~/ai-infra-day3是用户主目录下的路径，demo.log是相对此目录的路径，不是Windows工作区路径。

## 2. 启动一个后台练习进程（约5分钟）

以下程序每5秒写一行日志，最多运行约5分钟：
```bash
bash -c 'for n in {1..60}; do echo "step=$n"; sleep 5; done' > demo.log 2>&1 &
c2_pid=$!
echo "$c2_pid"
```
demo.log是此次练习输出文件，重复运行会覆盖旧练习日志。末尾&表示后台运行，$!取得刚启动的后台进程PID；赋值c2_pid=$!中等号两侧不加空格。>把标准输出写入文件，2>&1让错误输出也进入该文件。

## 3. 查询进程并看日志（约10分钟）

```bash
ps -p "$c2_pid" -o pid,ppid,stat,etime,args
tail -n 5 demo.log
```
记录进程查询实际输出：PID、父PID、状态、已运行时间、命令行。过几秒再次执行tail，观察step值变化。如果ps只剩表头或没有该PID，进程可能已结束；不能据此认为查询命令坏了，可以重新从第2步启动一次，并取得新PID。

可选实时查看：
```bash
tail -f demo.log
```
Ctrl+C停止这次tail查看，不会停止前面独立的后台演示进程。退出查看后仍在同一终端继续。

## 4. 停止自己刚启动的程序（约5分钟）

先用第3步ps确认该PID仍是刚才的演示bash，再执行：
```bash
kill "$c2_pid"
ps -p "$c2_pid" -o pid,stat,args
```
观察该行是否消失；如果已自然结束，则无需kill，不是失败。不随意终止其他进程，也不需要sudo。

## 5. 留一份自己的记录（约10—20分钟）

在Windows工作区day3/linux_deployment_notes.md保存：
- 虚拟机发行版（若知道）、本次练习目录绝对路径；
- 自己获得的PID，以及ps、日志的实际输出；
- 用自己的话解释相对/绝对路径、后台进程与PID、输出到终端和文件的区别；
- 可选补充此前端侧DeepSeek部署中使用过的命令与用途，已有证据可替代重复操作；
- 实际耗时与任何卡点。复制文字输出即可，不强制截图，不把教学示例写成自己的结果。

验收：能定位目录、查到自己进程、从日志确认输出、说明结束与查看日志的区别。收到指南不代表已经通过。

资料：[Bash后台命令](https://www.gnu.org/s/bash/manual/html_node/Lists.html)、[输出重定向](https://www.gnu.org/s/bash/manual/html_node/Redirections.html)、[ps手册](https://man7.org/linux/man-pages/man1/ps.1.html)。
