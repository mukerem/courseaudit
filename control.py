f = open("input", 'r')
w = open("output", 'w')
y = open("format", "w")
tot = dict()
for i in f.readlines():
    x = i.strip().split()
    a = x[0]
    d = x[-1]
    b = " ".join(x[1: -2])
    c = int(x[-2][0])
    w.write("%s %s %d %s\n" % (a,b,c,d))
    y.write('("%s", "%s", %d, "%s"),\n' % (a,b,c,d))
w.close()
y.close()
f.close()