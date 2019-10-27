# 딕셔너리 가지고 놀기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = {1:'one',2:'two'}

x.update(e=50)
print(x)
y.update(zip([3,4],['thr', 'four']))
print(y)

x.setdefault('a',99)
print(x)
x.update(a=99)
print(x)
y.update({1: 'ONE', 3: 'THREE'})
print(y)
