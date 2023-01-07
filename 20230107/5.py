dict = {'zero' : '0', 'one':'1', 'two':'2','three':'3','four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
s = "one4seveneight"
ans = ""
cur = ""
st = 0
end = 0
for i in range(len(s)):
    if('a'<=s[i]<='z'):
        cur += s[i]
    else:
        ans += s[i]
    if(cur in dict.keys()):
        v = dict[cur]
        ans += str(v)
        cur = ""
print(ans)