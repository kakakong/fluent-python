# 測試str.join() return 1,2,3
a = ','.join(repr(i) for i in [1, 2, 3])
print(a)
