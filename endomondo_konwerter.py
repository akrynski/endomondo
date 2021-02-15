#! python3.9
# -*- coding: utf-8 -*-
# author: Andrzej Kryński
# licence: MIT
# date: 05-02-2021
#github access key: 044cb299a8c2d590a7d100d092b469ef0e2f0d3b
#delete it if u makes repo public !!!!!!!!!!!!!
import codecs, os, sys, datetime, json

klucze = []

os.chdir("C:\\Users\\Andrzej\\Downloads\\endomondo-2021-01-27\\Workouts\\")
os.system("dir /B /A:-D > .\\output.txt")

def czytaj_wiersz(plik):
    for wiersz in plik:
        wiersz = plik.readline()
        wiersz = wiersz.strip()
        if wiersz == "output.txt":
            print("Koniec pliku \(EOF\).")
            break
        if not wiersz:
            break
        yield wiersz
# noinspection PyShadowingNames
def czytaj_workout(_line):
    try:
        print("Otwieram plik " + _line.strip())
        if _line == "output.txt":
            return 0
        _aktualny_workout = codecs.open(_line, 'r', 'utf-8', 'ignore')
        print("Json ładuje plik " + _line)
        workout_data = json.load(_aktualny_workout)
        pola = len(workout_data)
        klucze = []# to nie deklaracja a czyszczenie - deque?
        '''for i in range(pola):
            klucz = [*workout_data[i]][0]
            if klucz not in klucze:
                klucze.append(klucz)
            wartosci.append({klucz: list(workout_data[i].values())})
        print('klucze: ',klucze)'''
        for i,_ in enumerate(workout_data):
            klucz = [*workout_data[i]][0]
            if klucz not in klucze:
                klucze.append(klucz)
            #wartosci.append(v[klucz])
        #print(wartosci)

        for i, v in enumerate(klucze):
            #print("i=",i, "v=",v)
            if  v != 'points':
                print('index = ',i)
                print('klucz = ',list(workout_data[i].keys())[0])
                print('wartość: ',workout_data[i][v])
                print(10*'-')
                if v == 'comments':
                    print("SEKCJA COMMENTS")
                    comment_dic_list= workout_data[i]
                    comment_dic = list(comment_dic_list['comments'][0])
                    print('Autor: ',comment_dic[0]['author'])
                    print('text: ', comment_dic[2]['text'])
                    print(10*'-')
                elif v == 'routes':
                    print('SEKCJA ROUTES')
                    routes_dic_list = workout_data[i]
                    routes_dic = list(routes_dic_list['routes'][0])
                    print('name: ',routes_dic[1]['name'])
                    print('identifier: ', routes_dic[0]['identifier'])
                    print(10*'-')
                elif v == "pictures":
                    print("SEKCJA PICTURES")
                    pictures_dic_list = workout_data[i]['pictures']
                    for i,v in enumerate(pictures_dic_list):
                        for item in v:
                            #print(item)
                            if 'picture' in item:
                                print('url: ', item['picture'][0][0]['url'])
                    print(10*'-')
                elif v == 'tags':
                    print("SEKCJA TAGS")
                    tagi = workout_data[i][v]
                    print('tagi:', tagi[0][0]['name'])
                    print(10 * '-')
            elif v == 'points':
                print(i)
                print('TU SĄ POINSY')
                #print('v==points: ',v)
                print(10*'v')
                #print('dla points index = ',i)#ale tu o 1 więcej - 15,16 itp
                location_dic_list = workout_data[i]['points']
                print("Jeśli nie widać lokacji, to zakomentuj dyrektywę CONTINUE w linii 92\n")
                continue
                for i,v in enumerate(location_dic_list):
                    print(i,'||||||||||||||||||||||||||||||\n')
                    for item in v:
                        if 'location' in item:
                            print('latitude', item['location'][0][0]['latitude'])
                            print('longitude', item['location'][0][1]['longitude'])
                        if 'distance_km' in item:
                            print('przebyty dystans: ', item['distance_km'], 'km')
                        if 'speed_kmh' in item:
                            #print('Prędkość na odcinku: ', item['speed_kmh'],'km/h')
                            print(' '.join(["Prędkość na odcinku: ", str(item['speed_kmh']), 'km/h']))
                print(10*'*')
            else:
                continue
        return workout_data
    #--------------------------------------------------------------------------------
    except(IOError, OSError):
        print('Błąd funkcji \'czytaj_workout\'!', sys.exc_info()[0], file=sys.stderr)
        sys.exit(1)
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
with codecs.open('./output.txt', 'r', 'utf-8', 'ignore') as f:
        print("Odczytuję dane z dostarczonych przez Endomondo plików. Cierpliwości, "
              "to może chwilę potrwać.", end='\n')
        print("Aktualny folder to ", os.getcwd(), end='\n')
        print(datetime.date.today())
        print(80 * '*')
        for wiersz in czytaj_wiersz(f):
                czytaj_workout(wiersz)
