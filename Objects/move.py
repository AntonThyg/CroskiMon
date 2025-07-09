class move:
    def __init__(self, id, name, type, accuracy, power, pp):
        self.id=id
        self.name=name
        self.type=type
        self.accuracy=accuracy
        self.power=power
        self.pp=pp
    
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type
    
    def get_accuracy(self):
        return self.accuracy
    
    def get_power(self):
        return self.power
    
    def get_pp(self):
        return self.pp