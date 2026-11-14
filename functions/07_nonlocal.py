def chai_counter():
    chai_order = "Tulsi"  # Enclosing variable

    def update_order():
        nonlocal chai_order
        chai_order = "Ginger"

    update_order()
    print("Outer:", chai_order)

chai_counter()