class Command:
   def __init__(self,a,b):
       self.a = a
       self.b = b
 
   def execute(self):
       raise Exception('Overwrite this one pls')

