#pure and impure functions 
def pure_function(cups):
    return cups*10    #here theh output for the same input is always same 


#impure function 
total_chai=0

def impure_function(cups):
    global total_chai
    total_chai +=cups

#type 2
#recursive funtion 

def poure_chai(n):
    print(n)
    if n == 0:
        return "all cups poured"
    return poure_chai(n-1)

print(poure_chai(5))

#function type 3
#lambda funtion 

chai_type=["light","kadak","ginger","kadak"]

strong_chai=list(filter(lambda chai:chai!="kadak",chai_type))

print(strong_chai)