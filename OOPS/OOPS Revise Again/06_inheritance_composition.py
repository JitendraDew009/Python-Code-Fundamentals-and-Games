class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai): #here we inherit BaseChai in MasalaChai class.
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


class ChaiShop:
    chai_cls = BaseChai # this is compostion : keep the refernce of base chai. 
    
    def __init__(self):
       self.chai = self.chai_cls("Regular")
        #here we are holding all the ref in self.chai


    def serve(self):
       print(f"Serving {self.chai.type} chai in the shop") 
       self.chai.prepare()
        # And this object can be used anywhere in the class.

class FancyChaiShop(ChaiShop): #here is example of inherit 
    chai_cls = MasalaChai #and composition as well

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()