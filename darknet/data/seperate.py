import os
path = "images"
files = os.listdir(path)
s1 = ""
s2 = ""
f1 = open("1.txt", 'w')
f2 = open("2.txt", 'w')
i = 0
for f in files:
	i = i + 1
	if (i % 2 != 0):
		s1 += f + "\n"
	else:
		s2 += f + "\n"
f1.write(s1)
f2.write(s2)
f1.close()
f2.close()