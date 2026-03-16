class Chai:

    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

# ===THIS IS EXAMPLE OF DUPLICATION==== NO harm to use but you can see its cons
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

# ===THIS IS EXAMPLE OF EXPLICIT CALL==== OK OK
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

# ===supermethod=== BEST ONE
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(self, type_, strength) # super()
        self.spice_level = spice_level
# see how it simply your code and help in redundancy as well