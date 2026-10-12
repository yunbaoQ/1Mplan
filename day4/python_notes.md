使用python word_count_try.py能够发现result.json出现，并且其中有相关的字词。
修改时间查看：
PS C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4> Set-Location -LiteralPath 'C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4'
PS C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4> Get-Item -LiteralPath .\result.json | Select-Object Name, LastWriteTime

Name        LastWriteTime      
----        -------------      
result.json 2026/10/10 20:38:36

PS C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4> python -c "import word_count_try; print('导入完成')"
导入完成
使用python -c "import word_count_try; print('导入完成')"后能发现修改时间未变。所以它不启动main。
PS C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4> Get-Item -LiteralPath .\result.json | Select-Object Name, LastWriteTime

Name        LastWriteTime      
----        -------------      
result.json 2026/10/10 20:38:36


PS C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4> python -c "import word_count_try; print(word_count_try.word_count('AI ai'))"
{'ai': 2}

所以python -c "import word_count_try"实际就是导入了整个函数库，而并没有使用它。而python word_count_try.py则是调用了其main，主要是因为后面加了:
if __name__ == '__main__':
    main()
我尝试过将其注释，发现：
PS C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4> python word_count_try.py
PS C:\Users\IPIC-ZQY\Desktop\codex\AI-infra\day4> Get-Item -LiteralPath .\result.json | Select-Object Name, LastWriteTime

Name        LastWriteTime      
----        -------------      
result.json 2026/10/10 20:38:36
main未启动。