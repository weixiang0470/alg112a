def neighbour(x,h):
    nb_list=[]
    x2=x+h
    x3=x-h
    nb_list.append(x2)
    nb_list.append(x3)
    return nb_list
def nn(x,fc):
    if fc >10 : 
        fc=0
        return
    
    print(x,fc)
    fc+=1
    nb_list = neighbour(x,0.01)
    for nb in range(len(nb_list)):
        nn(nb_list[nb],fc)

nn(0,0)