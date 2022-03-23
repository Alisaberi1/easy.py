a=int(input()) 
b=int(input()) 
c=int(input()) 
d=int(input()) 
list_name=a,b,c,d
while (a and b and c and d) <10e3:
  sum=0
  for r in list_name:
    sum+=r
  sum
  Average=sum/4
  Product=a*b*c*d
  Max=max(list_name)
  Min=min(list_name)
  break
print("Sum : %.6f"%sum,"\n"
      "Average : %.6f"%Average,"\n"
      "Product : %.6f"%Product,"\n"
      "Max : %.6f"%Max,"\n"
      "Min : %.6f"%Min)