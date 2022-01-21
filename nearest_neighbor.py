import math
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

#creating function for n_n method, parameter is the dataset containing coordinates
def nearest_neighbor (input):

    #initializing status of all nodes as New 
    s=["N"]*(len(coord))

    #initializing the length of Hamilton cyrcle as 0
    w=0

    #index of the first node
    start=0

    #starting with first node, labelling it as Closed
    s[0]="C"

    #creating the path, starting with first node
    path=[start]

    #while exists node with status New in list s 
    while "N" in s:

        #variable, where the shortest distances of the following (next) node of path will be stored, initialized as Inf 
        min_w=float("inf")
    
        #index of the closest node
        u=-1

        #going through node after node, from 1 because 0 is the starting one
        for i in range(1, len(coord)):

            #if the given node has status New
            if s[i] == "N":

                #calculating the distance between the last node of cyrcle and the i node
                w_i = math.sqrt((coord[i][0] - coord[path[-1]][0])**2 + (coord[i][1] - coord[path[-1]][1])**2)

                #if the distance is shorter than the minimal, rewrite min_w and note the index of given node
                if w_i < min_w:
                    min_w=w_i
                    u=i
    
        #add the closest node to the path     
        path.append(u)

        #give status Closed to the added node
        s[u]="C"

        #update the length of the patrh (cyrcle)
        w = w + min_w

    #adding the starting node to the path again to get cyrcle
    path.append(path[0])

    #update the length of the cyrcle by adding distance between the last node of the path and the starting one
    w = w + math.sqrt((coord[0][0] - coord[path[-2]][0])**2 + (coord[0][1] - coord[path[-2]][1])**2)

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
    

#input_file="C:\\SKOLA\\GEOINFO\\grafove_algoritmy\\ukol\\data\\peaks_male_karpaty.txt"
input_file="C:\\SKOLA\\GEOINFO\\grafove_algoritmy\\ukol\\data\\ba_bary.txt"

#calling function for get_coord
coord=get_coord(input_file)

#calling function n_n and printing the length of Hamilton cyrcle
print(nearest_neighbor(coord))