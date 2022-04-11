import src.barcodescanner as barcodescanner
import src.db as db





class FridgeKnight():

    def __init__(self):
        print("Starting listener")
        self.UPC_Read()
        
        
    def scan(self):
        return(barcodescanner.scan())

    def UPC_Read(self):
        upc=self.scan()
        return upc

    def dbVersion(self):
        

    
        
        
    

