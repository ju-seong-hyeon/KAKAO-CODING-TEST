

if __name__ == "__main__":
    m = 'ABCDEFG'
    fos = {'C#':'H', 'D#':'I', 'F#':'J', 'G#':'K', 'A#':'L'}
    for key, value in fos.items():
        m = m.replace(key, value)
    # m = m.replace('C#', 'H')
    print(m)
    a_max = 0
    musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    for music in musicinfos:
        ratio = 0
        sp = music.split(',')
        for key, value in fos.items():
            sp[3] = sp[3].replace(key, value)
        for i in range(len(m)):
            for j in range(len(sp[3])):
                if(m[i] == sp[3][j]):
                    ratio

