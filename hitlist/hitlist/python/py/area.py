print("to find the areaa of:-")
print("1.rectnage")
print("2.triangle")
print("3.circle")
print("4.square")

choice=int(input("choice :1/2/3/4:-"))

if choice==1:
    L=float(input("enter the leanght:"))
    B=float(input("enter the btreath:"))
    area=float(L*B)
    print(f"the area of the rectangle:{L}x{B}={area}(sq m)")

elif choice==2:
     L=float(input("enter the leanght:"))
     H=float(input("enter the height:"))
     area=(L*H)/2
     print(f"the area of the triangle:{L}x{H}/2={area}(sq m)")

elif choice==3:
     r=float(input("enter the radiius:"))
     area=3.14*(r*r)
     print(f"the area of the circle:{r}x{r}x22/7={area}(sq m)")

else:
     s=float(input("enter the side:"))
     area=s*s
     print(f"the area of the square:{s}x{s}={area}(sq m)")




