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
        for i in range(pola):
            klucz = [*workout_data[i]][0]
            if klucz not in klucze:
                klucze.append(klucz)
            wartosci.append({klucz: list(workout_data[i].values())})

        for i, v in enumerate(klucze):  # za tagiem points jest jeszcze w tym pliku tag comments!!!, którego nie czytamy
            #if list(workout_data[i].keys())[0] != 'points':
            if v != 'points' and i < pola:
                print('index = ',i)
                print('słownik = ',workout_data[i])
                print('klucz = ',list(workout_data[i].keys())[0])
                #klucz = klucze[i]
                print('k-v: ', i,': ',v)#wartosci[i][v][0])
                print(10*'-')
            #elif list(workout_data[i].keys())[0] == 'points':
            elif v == 'points':
                print(i)
                print('TU SĄ POINSY')
                print(10*'v')

                location_dic = workout_data[i]['points']
                print('location: ', location_dic[0][0])
                print('location\'s timestamp: ', location_dic[0][1])  # location timestamp
                latitude_dic = list((location_dic[1][0]).values())[0][0][0]
                longitude_dic = list((location_dic[1][0]).values())[0][0][1]
                print("-->latitude: ", latitude_dic['latitude'])
                print("-->longitude: ", longitude_dic['longitude'])
                #print(f"-->the last tag (workout_data[-1]): {workout_data[-1]}")#->tu jest location!!!
                for data in workout_data:
                    location_dic = data.get('points')
                    print(f"latitude: {latitude_dic.get('latitude')}")
                    print(f"longitude: {longitude_dic.get('longitude')}")
                    # print(f"comments: ", [*workout_data[17]][0])
                    #print(f"comments: {data.get('comments')}")

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
        #line = f.readline()
        #while line:
        line = ''
        for line in f:
            line = f.readline()
            print("Opracowuję plik " + line.strip())
            #workout = None
            czytaj_workout(line)


except(IOError, OSError):
    # print >> sys.stderr, "Error!", sys.exc_info()[0]
    print("Error!", sys.exc_info()[0], file=sys.stderr)
    f.close()
    sys.exit(1)

finally:
    f.close()
    print('At the end I print all keys')
    for i, v in enumerate(klucze):
        print(i,v)

