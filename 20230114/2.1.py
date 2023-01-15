if __name__ == "__main__":
    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
              "SanFrancisco", "Seoul", "Rome", "Paris",
              "Jeju", "NewYork", "Rome"]
    cache = []
    time = 0
    for city in cities:
        if not city in cache:
            if (len(cache) == 3):
                cache.pop(0)
            cache.append(city)
            #print(city)
            time += 5
        else:
            cache.pop(0)
            cache.append(city)
            print(city)
            time += 1

    print(time)