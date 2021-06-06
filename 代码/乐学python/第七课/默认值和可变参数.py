# 默认函数
def hello(name,masj='你好'):
    print(name+' '+masj)
hello('Tom','早上好')
hello('Jack')


# 可变参数
def fun(nums):
    s=0
    cnt=0
    for i in  nums:
        s+=i
        cnt+=1
    return s,s/cnt
print(fun((3,5,8,9,0,4)))