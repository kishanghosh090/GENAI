class Chai:
    def __init__(self,type_,strength):
        self.type = type_
        self.strength = strength

class GingerChai(Chai):
    def __init__(self, type_, strength,spice_level):
        super().__init__(type_,strength)
        self.spiceLevel = spice_level
        