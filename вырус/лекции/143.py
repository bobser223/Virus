ox,oy,ax,ay,bx,by,cx,cy= [float(d) for d in input().split()]
abx=bx-ax
aby=by-ay
aox=ox-ax
aoy=oy-ay
bcx=cx-bx
bcy=cy-by
box=ox-bx
boy=oy-by
cax=ax-cx
cay=ay-cy
coy=oy-cy
cox=ox-cx
#ab*ao
a=abx*aoy-aby*aox
#bc*bo
b=bcx*boy-bcy*box
#ca*co
c=cax*coy-cay*cox
if (a <=0 and b<=0 and c<=0) or (a>=0 and b>=0 and c>=0):
    print (1)
else:
    print (0)
# if (c and a and b)<0 or (c and a and b)>0:
#     print (1)
# elif ((a or c or b)==0) and (((a and c ) or (a and b) or (b and c)) >0 or ((a and c ) or (a and b) or (b and c)) <0):
#     print (1)
# else:
#     print (0)

