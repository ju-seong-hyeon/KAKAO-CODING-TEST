from collections import deque
if __name__ == "__main__":
    cacheSize = 3
    cities = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo',
              'Seoul', 'Jeju', 'Pangyo', 'Seoul']
    a = []
    a = deque(a)
    time = 0
    for city in cities:
        if a in city:
            a.pop()
            a.appendleft(city)
            time += 1
        else:
            if (len(a) == cacheSize):
                a.popleft()
            a.append(city)
            time += 5

    print(time)
