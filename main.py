s = input()
s = s.split()
for i in range(4):
    s[i] = int(s[i])
if (s[1] - s[0]) == (s[2]-s[1]):
    s.append(s[3]+(s[1]-s[0]))
elif(s[1]/s[0]) == (s[2]/s[1]):
    s.append(int(s[3]*(s[1]/s[0])))
print(s)
for j in range(5):
    s[j] = str(s[j])
print(s)    
#print(" ".join(s))