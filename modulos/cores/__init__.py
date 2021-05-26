def cor(c):
    if c == 8:
        return '\033[m'
    if c == 0:
        return '\033[30m'
    if c == 1:
        return '\033[31m'
    if c == 2:
        return '\033[32m'
    if c == 3:
        return '\033[33m'
    if c == 4:
        return '\033[34m'
    if c == 5:
        return '\033[35m'
    if c == 6:
        return '\033[36m'
    if c == 7:
        return '\033[37m'
def bg(b):
    if b == 8:
        return '\033[m'
    if b == 0:
        return '\033[40m'
    if b == 1:
        return '\033[41m'
    if b == 2:
        return '\033[42m'
    if b == 3:
        return '\033[43m'
    if b == 4:
        return '\033[44m'
    if b == 5:
        return '\033[45m'
    if b == 6:
        return '\033[46m'
    if b == 7:
        return '\033[47m'
def negr():
    return '\033[1m'
def sub():
    return '\033[4m'
def nega():
    return '\033[7m'
def sem():
        return '\033[m'