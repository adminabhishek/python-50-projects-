# you are building a simple ap that registers users 
# you wqant to separate concerns :geting input,validating it,and saving it 

# taske:
# register_user() that calls :
# get_input()
# validate_input()
# save_to_db()

def get_input():
    print("getting input")
def validate_input():
    print("validating user info ")

def save_to_db():
    print("saving to database ")
def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("user registration is complete ")
    
register_user()

