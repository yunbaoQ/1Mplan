(base) yun@yun-virtual-machine:~$ mkdir -p ~/ai-infra-day3
(base) yun@yun-virtual-machine:~$ ls
ai-infra-day3  Documents  miniconda3  Pictures  rknn  Templates
Desktop        Downloads  Music       Public    snap  Videos
(base) yun@yun-virtual-machine:~$ cd ai-infra-day3
(base) yun@yun-virtual-machine:~/ai-infra-day3$ pwd
/home/yun/ai-infra-day3

(base) yun@yun-virtual-machine:~/ai-infra-day3$ bash -c 'for n in {1..60}; do echo "step=$n"; sleep 5; done' > demo.log 2>&1 &
[1] 3909
(base) yun@yun-virtual-machine:~/ai-infra-day3$ c2_pid=$!
(base) yun@yun-virtual-machine:~/ai-infra-day3$ echo "$c2_pid"
3909

(base) yun@yun-virtual-machine:~/ai-infra-day3$ ps -p "$c2_pid" -o pid,ppid,stat,etime,args
    PID    PPID STAT     ELAPSED COMMAND
   3909    3688 S          01:28 bash -c for n in {1..60}; do echo "step=$n"; sl
(base) yun@yun-virtual-machine:~/ai-infra-day3$ tail -n 5 demo.log
step=18
step=19
step=20
step=21
step=22
(base) yun@yun-virtual-machine:~/ai-infra-day3$ tail -f demo.log
step=20
step=21
step=22
step=23
step=24
step=25
step=26
step=27
step=28
step=29
step=30
step=31
step=32
^C

(base) yun@yun-virtual-machine:~/ai-infra-day3$ kill "$c2_pid"
(base) yun@yun-virtual-machine:~/ai-infra-day3$ ps -p "$c2_pid" -o pid,stat,args
    PID STAT COMMAND
[1]+  Terminated              bash -c 'for n in {1..60}; do echo "step=$n"; sleep 5; done' > demo.log 2>&1

demo.log:
step=1
step=2
step=3
step=4
step=5
step=6
step=7
step=8
step=9
step=10
step=11
step=12
step=13
step=14
step=15
step=16
step=17
step=18
step=19
step=20
step=21
step=22
step=23
step=24
step=25
step=26
step=27
step=28
step=29
step=30
step=31
step=32
step=33
step=34
step=35
step=36
step=37
step=38
step=39
step=40
step=41
step=42
step=43
step=44
step=45
step=46
