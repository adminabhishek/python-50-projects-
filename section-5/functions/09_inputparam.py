def make_chai(tea,milk ,suger):
    print(tea,milk,suger )

make_chai("darjeeling","yes","low") #postional
make_chai(tea="assam",suger="medium",milk ="no") #using keyword 


#args and kwargs very important topic

def special_chai(*ingredients,**extras):
    print("ingredients",ingredients)
    print("extraas",extras)

special_chai("cinnamon","cardmom",sweetner="honey",foam="yes")
