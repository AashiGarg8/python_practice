chai_order = "Tulsi"  # GLOBAL SCOPE

def chai_counter():
    chai_order = "lemon"  # ENCLOSING SCOPE

    def print_order():
        chai_order = "Ginger"  # LOCAL SCOPE
        print("Inner:", chai_order)

    print_order()
    print("Outer:", chai_order)

chai_counter()
print("Global:", chai_order)