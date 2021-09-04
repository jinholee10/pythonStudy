x1, y1, R1 = map(int, input().split())
x2, y2, R2 = map(int, input().split())
d2 = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
e2 = (R1+R2) * (R1+R2)
if d2 < e2:
    print("YES")
else:
    print("NO")
