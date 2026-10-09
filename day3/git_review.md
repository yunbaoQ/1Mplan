在文件加入暂存后后面的字母变成了A显示已添加索引
未暂存的文件有两个一个U表示未跟踪的，这是新添加的文件，并且未暂存
还有一个M表示已修改，就是原有文件进行了修改

并且还出现了一个commit_editmsg的文件：
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
# Your branch is ahead of 'origin/main' by 1 commit.
#   (use "git push" to publish your local commits)
#
# Changes to be committed:
#	new file:   day3/first_repeat.cpp
#	new file:   day3/word_count.py
#
# Changes not staged for commit:
#	modified:   day2/python_practice.ipynb
#	modified:   day3/today_2026-10-09.md
#	modified:   study/COACHING.md
#	modified:   study/daily_log.md
#	modified:   study/progress.json
#
# Untracked files:
#	.vscode/
#	day3/B2_guide.md
#	day3/Python_device_train.ipynb
#	day3/algorithm_first_repeat.md
#	day3/demo_result.json
#	day3/hardware_corrections.md
#	day3/input.txt
#	day3/result.json
#
最终原因是我在提交时未填写此次修改的名称

