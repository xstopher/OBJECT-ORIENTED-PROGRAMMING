class Jordan:
    def __init__(self, model, colorway):
        self.model = model
        self.colorway = colorway
        
    def display(self):
    
        print(f"Now Wearing: {self.model} in the {self.colorway} colorway.") 
        
my_shoe = Jordan("Jordan 4", "Black Cat")
my_shoe.display()

