import math
from matplotlib import pyplot

#definopvanie funkcie pre import suradnic z textaku
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

#definovanie funkcie n_n, parametrom je vstupny dataset
def nearest_neighbor (input):

    #stav vsetkych uzlov inicializujem ako nespracovane (new) 
    s=["N"]*(len(coord))

    #dlzku Hamiltonovskej kruznice inicializujem ako 0
    w=0

    #index prveho uzlu
    start=0

    #zacinam prvym uzlom, oznacim ho ako closed
    s[0]="C"

    #tvorim cestu, zacinam prvym uzlom (s indexom 0)
    path=[start]

    #pokym existuje nespracovany uzol v zozname s
    while "N" in s:

        #pomocna premenna do ktorej budem ukladat najkratsie vzdialenosti nasledujuceho uzlu kruznice, inicializujem nekonecnom
        min_w=float("inf")
    
        #index najblizsieho uzlu
        u=-1

        #prechadzame uzol po uzle, od 1 lebo 0 je startovny
        for i in range(1, len(coord)):

            #pokial dany uzol je nespracovany
            if s[i] == "N":

                #pocitanie vzdialenosti medzi poslednym (aktualnym) uzlom tvoriacim kruznicu a urcitym i-tym uzlom
                w_i = math.sqrt((coord[i][0] - coord[path[-1]][0])**2 + (coord[i][1] - coord[path[-1]][1])**2)

                #ak ich vzdialenosti je mensia ako ta minimalna, prepisem min_w a poznamenam si index daneho bodu
                if w_i < min_w:
                    min_w=w_i
                    u=i
    
        #do cesty pridam najblizsi uzol     
        path.append(u)

        #pridany uzol oznacim ako closed
        s[u]="C"

        #k dlzke kruznice pridam danu vzdialenost
        w = w + min_w

    #do zoznamu cesty pridam znova startovny uzol, aby som dostal, resp. uzavrel kruznicu
    path.append(path[0])

    #pripocitam vzdialenost medzi startovnym (a koncovym) uzlom kruznice a poslednym uzlom v ceste
    w = w + math.sqrt((coord[0][0] - coord[path[-2]][0])**2 + (coord[0][1] - coord[path[-2]][1])**2)

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
    

#input_file="C:\\SKOLA\\GEOINFO\\grafove_algoritmy\\ukol\\data\\peaks_male_karpaty.txt"
input_file="C:\\SKOLA\\GEOINFO\\grafove_algoritmy\\ukol\\data\\ba_bary.txt"

#zavolanie funkcie na ziskanie suradnic
coord=get_coord(input_file)

#zavolanie funkcie n_n a vypisanie dlzky kruznice
print(nearest_neighbor(coord))