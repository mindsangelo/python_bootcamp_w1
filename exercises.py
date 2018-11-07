# 1. repeated-string problem
def  repeatedString(s, n):
    count_in_s = s.count("a")
    return (n//len(s))*count_in_s + s[0: n % len(s)].count('a')




# 2. Funny String
def funnyString(s):
   i=0
   j=0
   r = (s[::-1])
   while i<len(s)-1:
       if (abs(ord(s[i])-ord(s[i+1]))) == abs((ord(r[i])-ord(r[i+1]))):
           j+=1
       i+=1
  
   if (j==len(s)-1):
       return "Funny"
  
   else:
       return "Not Funny"


# 3.  Left Rotation
def rotLeft(a, d):
	new_index=0
	new_array = []    
	for i in range(0, len(a)):
    	new_index = (i + d) % len(a)
    	new_array.append(a[new_index])
    
	return new_array   	 



# 4. Frequency Queries
def freqQuery(querys):
   array =[]
   cont=0
   for i in range(0, len(querys), 2):
       if(querys[i]== 3):
           for j in range(len(array)):
               if array.count(array[j]) == querys[i+1]:
                   cont+= 1
           if cont > 0:
               array.append(1)
           else:
               array.append(0)
   return array

querys = [1,5,1,6,3,2,1,10,1,10,1,6,2,5,3,2]

res = freqQuery(querys)
print(res)





  
