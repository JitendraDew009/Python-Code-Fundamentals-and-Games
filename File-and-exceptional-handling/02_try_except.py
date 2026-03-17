chai_menu = {"masala" : 30, "ginger" : 40}

# chai_menu["elaichi"] #KeyError: 'elaichi'

try:
 chai_menu["elaichi"] #KeyError: 'elaichi'
except KeyError:
 print("The key doesn't exist")

print("Hello I need Chai")