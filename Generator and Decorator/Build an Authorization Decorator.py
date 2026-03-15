from functools import wraps

def require_admin(func):

    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied, Only admin")
            return None # very optional line
        else:
            return func(user_role)
    return wrapper
        
@require_admin
def open(role):
    print("Acess granted, Welcome to my world")

open("user") # Access denied, Only admin
open("admin") # Acess granted, Welcome to my world