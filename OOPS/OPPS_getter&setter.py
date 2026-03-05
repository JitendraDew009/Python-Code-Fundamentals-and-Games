# Getter and Setter decorator 
# In Python, we usually use the @property decorator for getters and @<property>.setter for setters. This way, you can access attributes like normal variables but still control how they’re calculated or updated.

class Student:
    def __init__(self, phy, chem, math):
        self._phy = phy      # use underscore to indicate "internal" variable
        self._chem = chem
        self._math = math

    @property
    def percentage(self):   # getter
        return round((self._phy + self._chem + self._math) / 3, 2)

    @property
    def phy(self):          # getter for phy
        return self._phy

    @phy.setter
    def phy(self, value):   # setter for phy
        if value < 0 or value > 100:
            raise ValueError("Marks must be between 0 and 100")
        self._phy = value

    # for chem 
    @property
    def chem(self):          # getter for chem
        return self._chem

    @chem.setter
    def chem(self, value):   # setter for chem
        if value < 0 or value > 100:
            raise ValueError("Marks must be between 0 and 100")
        self._chem = value
    
    #for math
    @property
    def math(self):          # getter for math
        return self._math

    @math.setter
    def math(self, value):   # setter for math
        if value < 0 or value > 100:
            raise ValueError("Marks must be between 0 and 100")
        self._math = value

s1 = Student(85, 87, 98)
print(s1.percentage)   # 90.0

s1.phy = 88            # setter updates phy
s1.chem = 90            # setter updates chem
s1.math = 99            # setter updates math
print(s1.percentage)   # 92.33 (recalculated automatically)