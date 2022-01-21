import math, random
from matplotlib import pyplot

#creating function for getting coordinates from text file
def get_coord(input_file):

    #list for coordinates
    coord=[]
    
    with open(input_file) as f:
        lines=f.readlines()
        
        #the beginning of text file´s first row is corrupted...
        lines[0]=lines[0][3:len(lines[0])]    

        for line in lines:
            line=line[:-2]
            line=line.split(";")
            line[0]=float(line[0])
            line[1]=float(line[1])        
            coord.append(line)
    return coord

#creating function for b_i method, the parameter is the dataset containing coordinates
def best_insertion(input):

    #initializing the length of Hamilton cyrcle as 0
    w=0

    #list for the path
    path=[]

    #list of indices of all nodes indexov vsetkych uzlov
    l_ind = list(range(len(coord)-1))

    #initializing the cyrcle by 3 nodes
    for i in range(3):
    
        #random choice from list of indices
        u=random.choice(l_ind)

        #the chosen one delete from the list of indices
        l_ind.remove(u)

        #add it to the path
        path.append(u)

        #after second iteration there are 2 nodes in path, calculating the distance between them is possible
        if i > 0:
            w_k = math.sqrt((coord[path[i]][0] - coord[path[i-1]][0])**2 + (coord[path[i]][1] - coord[path[i -1]][1])**2)

            #updating w
            w = w + w_k

    #adding the starting node to the path again to create a cyrcle
    path.append(path[0])

    #update the length of the cyrcle by adding distance between the last node of the path and the starting one
    w = w + math.sqrt((coord[path[0]][0] - coord[path[-2]][0])**2 + (coord[path[0]][1] - coord[path[-2]][1])**2)

    #while the list of indices is not empty
    while len(l_ind) > 0:

        #variable, where the shortest increase of cyrcle´s length will be stored, initialized as Inf
        w_min=float("inf")

        #position of insertion to the path
        index=-1

        #random choice from the list of indices
        u=random.choice(l_ind)

        #storing the coordinates of the chosen node
        x = coord[u][0]
        y = coord[u][1]

        #calculating the distances to determine the insertion position of the chosen node
        for i in range(len(path)-1):

            #distance between the chosen node and i node
            w_k1 = math.sqrt((x - coord[path[i]][0])**2 + (y - coord[path[i]][1])**2)

            #distance betweeen the chosen node and i+1 node, because the node will be inserted between 2 nodes
            w_k2 = math.sqrt((x - coord[path[i + 1]][0])**2 + (y - coord[path[i + 1]][1])**2)

            #distance between i node and i+1 node
            w_k3 = math.sqrt((coord[path[i]][0] - coord[path[i + 1]][0])**2 + (coord[path[i]][1] - coord[path[i + 1]][1])**2)

            #triangle inequality
            w_k4 = w_k1 + w_k2 - w_k3

            #if the increase is smaller 
            if w_k4 < w_min:

                #overwrite w_min
                w_min=w_k4

                #position of insertion to the path
                index=i+1
    
        #adding the given distance to the cyrcle length
        w=w+w_min

        #inserting the node to the path to the given position 
        path.insert(index, u)

        #removing the chosen node from the list of indices
        l_ind.remove(u)

    #visualization

    #path
    x = []
    y = []
    for p in path:
        x.append(coord[p][0])
        y.append(coord[p][1])

    #nodes
    x_uzly = []
    y_uzly = []
    for c in coord:
        x_uzly.append(c[0])
        y_uzly.append(c[1])

    pyplot.scatter(x_uzly, y_uzly, c="red")
    pyplot.plot(x, y, c="black")
    pyplot.show()

    return w

#input_file = "C:\\SKOLA\\GEOINFO\\grafove_algoritmy\\ukol\\data\\peaks_male_karpaty.txt"
input_file="C:\\SKOLA\\GEOINFO\\grafove_algoritmy\\ukol\\data\\ba_bary.txt"

#calling function for get_coord
coord=get_coord(input_file)

#calling function b_i and printing the length of Hamilton cyrcle
print(best_insertion(coord))