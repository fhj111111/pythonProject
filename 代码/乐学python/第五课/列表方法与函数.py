lstStop = ['阳光路', '汉江路', '清凉门', '嫩江路', '五台山']
lstFlow = [34,45,88,62,21]
q=lstStop.insert(1,'汉江东路')
print(lstStop)
lstStop.remove('五台山')
print(lstStop)
start = lstStop.index('汉江路')
end = lstStop.index('嫩江路')
print(end - start)

lst = sorted(lstFlow)
l1 = lstFlow.index(lst[0])
l2 = lstFlow.index(lst[1])
print(lstStop[l1],lstStop[l2])