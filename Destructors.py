class Jordan:
    def __init__(self, model):
        self.model = model
        print(f"{self.model} is now in your collection.")
   
    def __del__(self):
         print(f"Cleanup: {self.model} has been removed from memory.")
#create the object
my_grail = Jordan("Jordan 11")
#Delete the object
del my_grail



class Jordan:
    def __init__(self, model, colorway):
        
        self.model = model
        self.colorway = colorway
        print(f"Jordan {self.model} '{self.colorway}' added to inventory.")

    def __del__(self):
       
        print(f"Inventory Cleanup: {self.model} '{self.colorway}' has been deleted.")

#create the oject
limited_pair = Jordan("Jordan 4", "Black Cat")
#Delete the object 
del limited_pair
