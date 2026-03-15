def chai_flavours(flavour = "Masala"):
    """Return the flaavour of chai.""" #multiline comment
    chai = "ginger"
    return flavour

print(chai_flavours.__doc__) # dunder doc work only down the line of  def functon.
print(chai_flavours.__name__) # dunder name work to find out the function name.


# ===========How to write actual industry level code==============
def genereate_bill(chai = 0, samosa = 0):
    """
    Calculate the total bill for chai and samosa
    :param chai : Number of chai cups (10 Rupees each)
    :param samosa : Number of samosa (15 Rupees each)
    : rturn : (total amount, thank yoy message as string)
            
    """
    total = chai*10 + samosa*15
    return total, "Thank You for Visiting Chai.com"

print(genereate_bill(2,5))