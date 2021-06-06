"""
整数类型 int
浮点数类型 float
复数类型  complex
"""



print(pow(2,10))
import sys
print(sys.float_info)
for i in range(1):
    monts = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    n = input('请输入月份数（1-12）：')
    pos = (int(n)-1)*3
    monthAbbrev = monts[pos:pos+3]
    print( '月份简写是'+monthAbbrev+'.')


