import sys, os

# path = sys.argv[1]
path = sys.path[0]
# file = sys.argv[2]
file = "app.log"

def path(p:str, *args):
    for elm in args:
        p = os.path.join(p, elm)
    return p

