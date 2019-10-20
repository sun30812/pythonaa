# 가변 인수

def pnum(*args):
    for arg in args:
        print(arg)

pnum(1,2,2,2,1,2)