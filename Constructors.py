class Jordan:
    def __init__(self, model, colorway):
        # 1. INITIALIZATION
        self.model = model
        self.colorway = colorway
        print(f"Jordan {self.model} in {self.colorway} is ready!")

# Creating the object 
my_shoe = Jordan("Jordan 1", "Chicago")


# using a default value for size
class Jordan:
    def __init__(self, model, colorway, size=10):
        
        self.model = model
        self.colorway = colorway
        self.size = size
        print(f"Jordan {self.model} ({self.colorway}) created in size {self.size}.")


shoe1 = Jordan("Jordan 4", "Military Blue", 11)
shoe2 = Jordan("Jordan 1", "black")


