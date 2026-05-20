class conta: 

    def __init__(self):
        self.saldo = 0.0
        
    def Saca(self,valor):
        self.saldo -= valor 
    
    def deposita(self,saldo):
        self.saldo += saldo

    def calculaRendimento(self):
        return self.saldo *0.1 


 