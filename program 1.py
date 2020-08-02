def point_inside_polygon(c,poly):

    x=float(c[0][0])
    y=float(c[0][1])
    n = len(poly)
    inside =False
    p1x=float(poly[0][0])
    p1y=float(poly[0][1])
    for i in range(n+1):
        p2x = float(poly[i % n][0])
        p2y = float(poly[i % n][1])
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside

def stringToList(s):
    polygon = []
    c = s.split("]")
    for i in range(len(c) - 1):
        if (c[i] != ""):
            p = c[i].split("[")
            d = (p[(len(p) - 1)])
            polygon.append(d.split(","))
    return (polygon)

c = [[3,2],[-2,-0.8],[0,1.2],[2.2,0],[2,4.5]]
p=[3,5]
polygon=[]

a=input()
b=input()
polygon=stringToList(a)
point=stringToList(b)
print (point_inside_polygon(point,polygon))
# poly = Polygon(coords)
#
# print (p1.within(poly))