print("骑行每公里5元(不满1公里按1公里计算)")
print("收费方式:满5公里收费1元，满10公里收费2元，满15公里收费3元，超过15公里收费4元")
km_cost=1
Riding_costs=0
_km=0
_flag=True
while _flag :
    distance=float(input("要驶过的距离（公里）:"))
    if distance<0:
        print("距离不能是负数!")
    elif (distance%1)!=0:
        distance=distance-(distance%1)+1
    _km+=distance
    if distance<=5:
        Riding_costs=km_cost*distance+Riding_costs
    elif distance<=10:
        Riding_costs=km_cost*5+km_cost*(distance-5)*2+Riding_costs
    elif distance<=15:
        Riding_costs=km_cost*5+km_cost*5*2+km_cost*(distance-10)*3+Riding_costs
    elif distance>15:
        Riding_costs=km_cost*5+km_cost*5*2+km_cost*5*3+km_cost*(distance-15)*4+Riding_costs
    _flag=int(input("输入0结束。输入1继续:")) 
    if _flag==0:
        _flag=False
    elif _flag==1:
        _flag=True
    else:
        print("错误!要求跟0或1")
        _flag=False
print("一共驶过",_km,"公里，需要收费",Riding_costs,"元")