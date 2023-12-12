cx,cy= [float(d) for d in input().split()]
ax,ay= [float(d) for d in input().split()]
bx,by= [float(d) for d in input().split()]
if (cy-ay)/(by-ay)==(cx-ax)/(by-ay):
    print ("YES")
else:
    print("NO")

if (cx>ax and cy>ay) and (cy-ay)/(by-ay)==(cx-ax)/(by-ay):
    print ("YES")
else:
    print ("NO")
if (cx>ax and cy>ay) and (cx<bx and cy<by) and (cy-ay)/(by-ay)==(cx-ax)/(by-ay):
    print ("YES")
else:
    print ("NO")