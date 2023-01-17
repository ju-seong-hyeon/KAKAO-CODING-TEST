import math
from collections import defaultdict
def Cal_Min(Time):
    t = Time.split(":")
    return int(t[0]) * 60 + int(t[1])

def Cal_Fee(v):
    val = 0
    if(v <= fees[0]):
        val = fees[1]
    else:
        v -= fees[0]
        val += fees[1]
        mn = v / fees[2]
        mn = math.ceil(mn)
        val += mn * fees[3]
    return val

if __name__ == "__main__":
    fees = 	[1, 461, 1, 10]
    records = ["00:00 1234 IN"]
    fee_Record = defaultdict(int)
    In_Record = defaultdict(int)

    for i in records:
        record = i.split()
        if record[2] == 'IN':
            In_Record[record[1]] = Cal_Min(record[0])
        else:
            outTime = Cal_Min(record[0])
            fee_Record[record[1]] += (outTime - In_Record[record[1]])
            In_Record[record[1]] = -1
    print(In_Record)
    for key, value in In_Record.items():
        if(value != -1):
            last_Time = Cal_Min("23:59")
            fee_Record[key] += (last_Time - value)
    arr = []
    brr = []
    for key, value in fee_Record.items():
        v = Cal_Fee(value)
        arr.append((key, v))
    arr.sort()
    for i in arr:
        brr.append(i[1])
    print(brr)