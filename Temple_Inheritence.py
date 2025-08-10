
class FamousTemple:
    temple = "Tirumala"

    def __init__(self):
        self.height = 9.9
        self.energy = "High Possitive"
        self.gods = ("Vishnu", "Varahaswamy")

    def Laddu(self):
        self.quanty = 200
        self.taste = "Excelent"
        self.ingredeants = ("SUgar", "Ghee", "Badam")
        print(self.taste)

class VillageTemple(FamousTemple):
    temple = "LakshmiTirumala"

    def __init__(self):
        FamousTemple.__init__(self)
        self.vheight=9.7
        self.venergy="Possitive"
        self.vgods = ["Vishnu","Lakshmi"]

    def display(self):
        print(self.height, self.energy, self.gods)
        print(self.vheight, self.venergy, self.vgods)

    def Laddu(self):
        self.quanty=100
        self.taste = "Ok"
        self.ingredeants = ("Sugar", "Rawa")
        print(self.taste)

venkatesh = VillageTemple()
venkatesh.display()
venkatesh.Laddu()
