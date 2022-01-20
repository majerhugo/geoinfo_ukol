import math, random
from matplotlib import pyplot

#definovanie funkcie pre import suradnic z textaku
def get_coord(input_file):

    #zoznam pre suradnice
    coord=[]
    
    with open(input_file) as f:
        lines=f.readlines()
        
        #zaciatok prveho riadku v textaku je nejaky vadny...
        lines[0]=lines[0][3:len(lines[0])]    

        for line in lines:
            line=line[:-2]
            line=line.split(";")
            line[0]=float(line[0])
            line[1]=float(line[1])        
            coord.append(line)
    return coord

#definovanie funkcie b_i, parametrom je vstupny dataset
def best_insertion(input):

    #dlzku Hamiltonovskej kruznice inicializujem ako 0
    w=0

    #list pre cestu
    path=[]

    #list indexov vsetkych uzlov
    l_ind = list(range(len(coord)-1))

    #kruznicu inicializujem 3 uzlami
    for i in range(3):
    
        #nahodny vyber z listu idexov
        u=random.choice(l_ind)

        #vybrany index zmazat
        l_ind.remove(u)

        #pridat ho do cesty
        path.append(u)

        #po druhej iteracii cyklu uz mam v zozname dva uzly, mozem pocitat vzdialenost
        if i > 0:
            w_k = math.sqrt((coord[path[i]][0] - coord[path[i-1]][0])**2 + (coord[path[i]][1] - coord[path[i -1]][1])**2)

            #pridavam ju do w
            w = w + w_k

    #do zoznamu cesty pridam znova startovny uzol, aby som dostal, resp. uzavrel kruznicu
    path.append(path[0])

    #pocitam vzdialenost medzi startovnym (resp. koncovym) uzlom a poslednym uzlom v ceste
    w = w + math.sqrt((coord[path[0]][0] - coord[path[-2]][0])**2 + (coord[path[0]][1] - coord[path[-2]][1])**2)

    #kym v zozname indexov nieco zostava
    while len(l_ind) > 0:

        #pomocna premenna do ktorej budem ukladat najkratsie prirastky dlzky kruznice
        w_min=float("inf")

        #miesto vlozenia do cesty
        index=-1

        #vyberam nahodne z listu vsetkych uzlov
        u=random.choice(l_ind)

        #ukladam suradnice vybraneho uzlu
        x = coord[u][0]
        y = coord[u][1]

        #pocitanie vzdialenosti aby som vedel kam vkladat vybrany uzol
        for i in range(len(path)-1):

            #vzdialenost medzi vybranym uzlom a i-tym uzlom
            w_k1 = math.sqrt((x - coord[path[i]][0])**2 + (y - coord[path[i]][1])**2)

            #vzdialenost medzi vybranym uzlom a (i-tym + 1) uzlom, pretoze uzol budem vkladat medzi 2 uzly
            w_k2 = math.sqrt((x - coord[path[i + 1]][0])**2 + (y - coord[path[i + 1]][1])**2)

            #vzdialenost medzi i-tym a (i-tym + 1) uzlom
            w_k3 = math.sqrt((coord[path[i]][0] - coord[path[i + 1]][0])**2 + (coord[path[i]][1] - coord[path[i + 1]][1])**2)

            #trojuholnikova nerovnost
            w_k4 = w_k1 + w_k2 - w_k3

            #ak je prirastok mensi 
            if w_k4 < w_min:

                #prepisem w_min
                w_min=w_k4

                #pozicia vlozenia do cesty
                index=i+1
    
        #k dlzke kruznice pridam danu vzdialenost
        w=w+w_min

        #do cesty na dane miesto vlozim ten (nahodne) vybrany uzol 
        path.insert(index, u)

        #odstranim vybrany uzol zo zoznamu vsetkych uzlov
        l_ind.remove(u)

    #vizualizacia

    #cesta
    x = []
    y = []
    for p in path:
        x.append(coord[p][0])
        y.append(coord[p][1])

    #uzly
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

#zavolanie funkcie na ziskanie suradnic
coord=get_coord(input_file)

#zavolanie funkcie b_i a vypisanie dlzky kruznice
print(best_insertion(coord))