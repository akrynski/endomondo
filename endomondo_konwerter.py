#! python3.9
# -*- coding: utf-8 -*-
# author: Andrzej Kryński
# licence: MIT
# date: 05-02-2021
#github access key: 044cb299a8c2d590a7d100d092b469ef0e2f0d3b
#delete it if u makake repo public !!!!!!!!!!!!!
import codecs, os, sys, datetime, json
from pathlib import Path


klucze = []
wartosci = []

os.chdir("C:\\Users\\Andrzej\\Downloads\\endomondo-2021-01-27\\Workouts\\")
os.system("dir /B /A:-D > .\\output.txt")

# noinspection PyShadowingNames
def czytaj_workout(_line):
    try:
        print("Otwieram plik " + _line.strip())
        if _line.strip() == "output.txt":
            return 0

        _aktualny_workout = codecs.open(_line.strip(), 'r', 'utf-8', 'ignore')
        print("Json ładuje plik " + _line)
        workout_data = json.load(_aktualny_workout)
        pola = len(workout_data)
        klucze = []
        for i in range(pola):
            klucz = [*workout_data[i]][0]
            if klucz not in klucze:
                klucze.append(klucz)
            wartosci.append({klucz: list(workout_data[i].values())})
        print('klucze: ',klucze)

        for i, v in enumerate(klucze):
            print("i=",i, "v=",v)
            if v != 'points':
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
            elif v == 'points':
                print('v==points: ',v)
                print(i)
                print('TU SĄ POINSY')
                print(10*'v')
                print('dla points index = ',i)#ale tu o 1 więcej - 15,16 itp
                location_dic_list = workout_data[i]['points']
                #continue
                for i,v in enumerate(location_dic_list):
                    print(i,'||||||||||||||||||||||||||||||\n')
                    for item in v:
                        if 'location' in item:
                            print('latitude', item['location'][0][0]['latitude'])
                            print('longitude', item['location'][0][1]['longitude'])
                        if 'distance_km' in item:
                            print('przebyty dystans: ', item['distance_km'], 'km')
                        if 'speed_kmh' in item:
                            print('Prędkość na odcinku: ', item['speed_kmh'],'km/h')
                print(10*'*')
            else:
                continue
        return workout_data
    #--------------------------------------------------------------------------------
    except(IOError, OSError):
        print('Błąd funkcji \'czytaj_workout\'!', sys.exc_info()[0], file=sys.stderr)
        sys.exit(1)

try:
    with codecs.open('./output.txt', 'r', 'utf-8', 'ignore') as f:
        print("Odczytuję dane z dostarczonych przez Endomondo plików. Cierpliwości, "
              "to może chwilę potrwać.", end='\n')
        print("Aktualny folder to ", os.getcwd(), end='\n')
        print(datetime.date.today())
        print(80 * '*')
        for line in f:
            line = ''
            line = f.readline()
            if line.strip() == "output.txt":
                print('EOF reached. Breaking')
                break
            if not line:
                break
            print("Opracowuję plik " + line.strip())
            czytaj_workout(line)
except():
    # print >> sys.stderr, "Error!", sys.exc_info()[0] #python <v.3
    print("Error!", sys.exc_info()[0], file=sys.stderr)
    f.close()
    sys.exit(1)
finally:
    f.close()


