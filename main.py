import sys, os
import time

try:
    PATH = sys.argv[1]
    file = sys.argv[2]
except IndexError:
    print("File error: No file specified")
    exit()

pastLogs = []

file = os.path.join(PATH, file)

os.system("cls" if os.name == "nt" else "clear")
while 1:
    if os.path.exists(file):
        logs = []

        encode = "utf-8"
        try:
            open(file, "r", encoding=encode).readlines()
        except UnicodeDecodeError:
            encode = "ISO-8859-1"

        with open(file, "r", encoding=encode) as f:
            for line in f.readlines():
                logs.append(line)
            logs = logs[len(pastLogs):]
            for l in logs:
                print(l.strip())
            pastLogs += logs
    else:
        print("File not found")
        time.sleep(2)
        sys.exit(1)
    time.sleep(0.1)