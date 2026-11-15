#building simple app that register users
# seperate concerns : getting input , validating it and saving it.
#Task : write register_user() that calls: get_input(), validate_input(), save_to_db()
# 
def get_input():
    print("get user info")

def validate_input():
    print("Validating the user info")

def save_to_db():
    print("saving to database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User Registration complete")


register_user()

