def outer_func():
    chai_order='lemon'
    print('outer:',chai_order)
    def inner_func():
        chai_order='ginger'
        print("inner:",chai_order)
    inner_func()

outer_func()
chai_order='tulsi'
print("global:",chai_order)