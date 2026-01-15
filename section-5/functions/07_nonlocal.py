def update_order():
    chai_type='ginger'
    def kitchen():
        nonlocal chai_type
        chai_type='kesar'
    kitchen()
    print("after kitchen updated:",chai_type)
update_order()