def time_Cal(in_Time, out_Time):
    print(in_Time)
    print(out_Time)
    in_Time = in_Time.split(":")
    out_Time = out_Time.split(":")
    in_TimeMin = int(in_Time[0]) * 60 + int(in_Time[1])
    out_TimeMin = int(out_Time[0]) * 60 + int(out_Time[1])
    for_Time = out_TimeMin - in_TimeMin
    val = 0
    v = 0
    if(for_Time <= fees[0]):
        # res.append(fees[1])
        val = fees[1]
    else:
        for_Time -= fees[0]
        val += fees[1]
        v = for_Time // fees[2]
        val += v * fees[3]
        v = for_Time % fees[2]
        if(v != 0):
            val += fees[3]
    print(val)
    res.append(val)

if __name__ == "__main__":
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    # records.sort()
    # res = [14600, 34400, 5000]
    res = []
    in_Record = {}
    out_Record = []
    for i in records:
        record = i.split(" ")
        if record[2] == 'IN':
            in_Record[record[1]] = record[0]
        else:
            time_Cal(in_Record[record[1]], record[0])

    print(res)

    #         out_Record.append((record[0], record[1]))
    # print(in_Record)
    # print(out_Record)
