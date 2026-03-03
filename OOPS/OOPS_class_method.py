# Class Method is bound to the class & receives the class as an implicit forst agrument.
# Note - static method can't access pr modify class state & gerenally for utility.

# class Student:
    
#     @classmethod #decorator
#     def college (cls):
#         pass

class Person:
    name = "anonymus"

    #----THIS WILL ALSO WORK BUT
    # def changeName(self, name):
    #     Person.name = name # / self.name = name
        #
    #     # self.__class__.name = "jujutsu"
    
    @classmethod
    def changeName(cls, name):
        cls.name = name



p1 = Person()
p1.changeName("Jitendra Dewangan")
print(p1.name) # Jitendra Dewangan 
print(Person.name) #Jitendra Dewangan instead of anonymous
