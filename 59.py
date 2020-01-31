class Error(Exception):
    pass
class aa(Error):
    pass
try:
   
   raise aa
  
except aa:
   print("duh")

