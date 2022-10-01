import sys, os
import time
from colored import fg, bg, attr

class logColorizer():
    def __init__(self):
        self.colors = {
            "default": fg("white"),
            "ERROR": fg("red"),
            "WARNING": fg("yellow"),
            "INFO": fg("white"),
            "DEBUG": fg("dark_gray"),
            "TRACE": fg("deep_pink_4c"),
            "reset": attr("reset")
        }

    def colorize(self, color, text):
        return self.colors[color] + text + self.colors['reset']
    
    def print(self, color, text):
        print(self.colorize(color, text))

COLOR = logColorizer()

try:
    PATH = sys.argv[1]
    file = sys.argv[2]
except IndexError:
    print("File error: No file specified")
    exit()

# PATH = sys.path[0]
# file = "test.log"

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
            # get all lines of the log file
            for line in f.readlines():
                logs.append(line)
            # get the last lineS of the log file
            logs = logs[len(pastLogs):]
            # enumerate the lines
            for l in logs:
                lvl = "default"
                # search the lvl of the line
                for key in COLOR.colors.keys():
                    if key in l.split(" "):
                        lvl = key
                # print the line
                COLOR.print(lvl, l.strip())
            # update the pastLogs
            pastLogs += logs
    else:
        print("File not found")
        time.sleep(2)
        sys.exit(1)
    time.sleep(0.1)