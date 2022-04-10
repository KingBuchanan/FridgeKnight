import src.barcodescanner as barcodescanner





class FridgeKnight():

    def __init__(self):
        print("Starting listener")
        self.scan()
        
        
    def scan(self):
        print(barcodescanner.scan())
        
        
    

