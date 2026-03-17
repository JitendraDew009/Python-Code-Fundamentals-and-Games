# ===without static method===
# class ChaiUtils:
   
#     def clean_ingredients(self, text):
#         return [item.strip() for item in text.split(",")]
    
# raw = " water, milk , ginger , honey "

# # obj = ChaiUtils()
# # print(obj.clean_ingredients(raw)) #['water', 'milk', 'ginger', 'honey']

# ===With Static Method===
class ChaiUtils:
    @staticmethod #don't forget this decorator
    def clean_ingredients(text): #when you use decorator don't use self OK !
        return [item.strip() for item in text.split(",")]
    
raw = " water, milk , ginger , honey "

cleaned = ChaiUtils.clean_ingredients(raw)

print(cleaned) #['water', 'milk', 'ginger', 'honey']
