f = open('目錄.txt', 'r', encoding = "utf-8")
for line in f:
    line = line.replace('\n', '') + '  '
    print(f"{line.replace('.', '')}")
f.close()