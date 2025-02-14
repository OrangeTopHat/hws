class iterr:

   def __init__(self, data):
       self.data = data

   def __iter__(self):
       for item in self.data:
           yield item

iter = iterr([2, 3, 6, 81, 532])
for item in iter:
   print(item)