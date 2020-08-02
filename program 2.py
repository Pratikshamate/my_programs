import math

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

def getAngle(a, b, c):
    c=c[0]
    ang = math.degrees(math.atan2(float(c[1])-float(b[1]), float(c[0])-float(b[0])) - math.atan2(float(a[1])-float(b[1]), float(a[0])-float(b[0])))
    return ang + 360 if ang < 0 else ang

def getDiffAngle(a, b, c):
    a=a[0]
    ang = math.degrees(math.atan2(float(c[1])-float(b[1]), float(c[0])-float(b[0])) - math.atan2(float(a[1])-float(b[1]), float(a[0])-float(b[0])))
    return ang + 360 if ang < 0 else ang

def stringToList(s):
    list = []
    c = s.split("]")
    for i in range(len(c) - 1):
        if (c[i] != ""):
            p = c[i].split("[")
            d = (p[(len(p) - 1)])
            list.append(d.split(","))
    return (list)
def sublist(lst, n):
    sub=[] ; result=[]
    for i in lst:
        sub+=[i]
        if len(sub)==n: result+=[sub] ; sub=[]
    if sub: result+=[sub]
    return result

def shadow(a,s):
    sum=0
    if(len(a)==1):
        c = calculateDistance(float(a[0][0][0]),float(a[0][0][1]),float(a[0][1][0]),float(a[0][1][1]))
        d = calculateDistance(float(a[0][0][0]),float(a[0][0][1]),float(a[0][3][0]),float(a[0][3][1]))
        sum=c+d

    if (len(a) == 2):
        e = calculateDistance(float(a[0][0][0]), float(a[0][0][1]), float(a[0][1][0]), float(a[0][1][1]))
        f = calculateDistance(float(a[1][0][0]), float(a[1][0][1]), float(a[1][1][0]), float(a[1][1][1]))
        m = calculateDistance(float(a[0][0][0]), float(a[0][0][1]), float(a[0][3][0]), float(a[0][3][1]))
        n = calculateDistance(float(a[1][0][0]), float(a[1][0][1]), float(a[1][3][0]), float(a[1][3][1]))

        if(e<f):
            angle=360-getAngle(a[0][0], a[0][3], s)
            diff = calculateDistance(float(a[0][3][0]), 0, float(a[1][0][0]), 0)
            adj = (diff / math.tan(angle))
            if (adj < 0):
                if getAngle(a[1][3], a[1][0],s)<90:
                    sum = e + m + n
                else:
                    sum = e + m + n + f
            else:
                sum = f + m + n + adj

        else:
            angle= 360-getAngle(a[1][0], a[1][3], s)
            diff= calculateDistance(float(a[1][3][0]),0, float(a[0][0][0]), 0)
            adj= (diff/math.tan(angle))
            if(adj<0):
                if getAngle(a[0][3], a[0][0],s)<90:
                    sum = m + n + f
                else:
                    sum = e+ m + n + f
            else:

                sum = e + m + n + adj

    return sum

a=input()
b=stringToList(a)
c=input()

building= sublist(b,4)
sun=stringToList(c)

print (shadow(building,sun))