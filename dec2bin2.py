def dec2bin(num):
  result = ""
  while num > 0:
    if num % 2 == 1:
      result = "1" + result 
    else:  
      result = "0" + result 
    num = num/2 
  return result 
   
