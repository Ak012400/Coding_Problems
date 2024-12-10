def GetLongestNum(Number):
   val=str(Number)
   sorted_number=list(val)
   lenth=len(sorted_number)
   if(int(sorted_number[0])==0 and int(sorted_number[1])==0 and int(sorted_number[2])%2 !=0):
      sorted_number=sorted_number[2:lenth]
      lenth=len(sorted_number)
   if(int(sorted_number[0])==0 and int(sorted_number[1])%2 !=0):
      sorted_number=sorted_number[1:lenth]
      lenth=len(sorted_number)
   for i in range(0,lenth-1):
      if(int(sorted_number[i])%2==0 and int(sorted_number[i+1])%2==0):
         if(int(sorted_number[i])<int(sorted_number[i+1])):
            sorted_number[i],sorted_number[i+1]=sorted_number[i+1],sorted_number[i]
            even=True
            k=1
            while((i-k+1)==0 or even):
              
               if((i-k+1)==0):
                 
                  even=False
               else:
                  if(int(sorted_number[i-k])%2==0 and int(sorted_number[i-k+1])%2==0):
                     if(int(sorted_number[i-k]) < int(sorted_number[i-k+1])):
                        sorted_number[i-k],sorted_number[i-k+1]=sorted_number[i-k+1],sorted_number[i-k]
                        k=k+1
                       
                     else:
                        even=False
                  else:
                     even=False
                     k=1  
                     
      elif(int(sorted_number[i])%2==1 and int(sorted_number[i+1])%2==1):
         sorted_number[i],sorted_number[i+1]=sorted_number[i+1],sorted_number[i]
         m=1
         Odd=True
         while((i-m+1)==0 or Odd):
               
               if((i-m+1)==0):
                  Odd=False
               else:
                  if(int(sorted_number[i-m])%2==1 and int(sorted_number[i-m+1])%2==1):
                     if(int(sorted_number[i-m]) < int(sorted_number[i-m+1])):
                        sorted_number[i-m],sorted_number[i-m+1]=sorted_number[i-m+1],sorted_number[i-m]
                        m=m+1
                     else:
                        Odd=False

                  else:
                     Odd=False
                     m=1
         
   return ''.join(sorted_number)   
val = "0098079640908"
val4=int(val)
print("value is -",GetLongestNum(val4))
#00  0098079640908 