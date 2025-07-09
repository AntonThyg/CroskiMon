class type:
    def __init__(self, name, effective, ineffective, noneffective):
        self.name=name
        self.effective=effective
        self.ineffective=ineffective
        self.noneffective=noneffective
    
    def get_name(self):
        return self.name
    
    def get_effective(self):
        return self.effective
    
    def get_ineffective(self):
        return self.ineffective
    
    def get_noneffective(self):
        return self.noneffective