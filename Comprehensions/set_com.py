#     {expression for item in iterable if condition}

favourite_chais = [
    "masala chai",
    "lemon tea",
    "green tea",
    "elaichi tea",
    "lemon tea",
    "green tea",
    "elaichi tea",

]
unique_chai1 = {chai for chai in favourite_chais}
unique_chai2 = {chai for chai in favourite_chais if len(chai) > 0}
print(unique_chai1) #{'green tea', 'lemon tea', 'masala chai', 'elaichi tea'}


recepies = {
    "Masala Chai" : ["ginger", "cardamom", "clove"],
    "Elaochi Chai" : ["ginger", "cardamom", "milk"],
    "Spicy Chai" : ["ginger", "black pepper", "clove"],

}

#            {expression for item in iterable if condition/or doesn't need or write more codes after it.}
            # expression = spices whatever you are trying to while thing is going to be an expression.
unique_spices = { spices for ingredients in recepies.values() for spices in ingredients }
print(unique_spices)
