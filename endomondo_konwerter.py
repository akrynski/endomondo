#! python3.9
# -*- coding: utf-8 -*-
# author: Andrzej Kryński
# licence: MIT
# date: 05-02-2021
import codecs, os, sys, datetime, json

workout = None
line = None
aktualny_workout = None
workout_data = None
klucze = []
wartosci = []

os.chdir("C:\\Users\\Andrzej\\Downloads\\endomondo-2021-01-27\\Workouts\\")
os.system("dir /B /A:-D > .\\output.txt")


# noinspection PyShadowingNames
def czytaj_workout(_line):
    try:
        global aktualny_workout
        global workout_data
        global klucze
        print("Otwieram plik " + _line)
        if _line.strip() == "output.txt":
            return 0

        aktualny_workout = codecs.open(_line.strip(), 'r', 'utf-8', 'ignore')
        print("Json ładuje plik " + _line)
        workout_data = json.load(aktualny_workout)
        pola = len(workout_data)
        for i in range(pola):
            '''
            print("Klucz " + str(i) +" : ", *workout_data[i])
            kl = [*workout_data[i]]
            print(kl[0])
            '''
            '''
            keyclass = workout_data[i].keys()
            klucz = list(keyclass)[0]
            if klucz not in klucze:
                klucze.append(klucz)
            '''
            klucz = [*workout_data[i]][0]
            if klucz not in klucze:
                klucze.append(klucz)
            wartosci.append({klucz: list(workout_data[i].values())})



    except(IOError, OSError):
        print('Błąd funkcji \'czytaj_workout\'!', sys.exc_info()[0], file=sys.stderr)
        aktualny_workout.close()
        aktualny_workout = None
        sys.exit(1)
    finally:
        if aktualny_workout is not None:
            aktualny_workout.close()
            aktualny_workout = None
    return  # workout


try:
    with codecs.open('./output.txt', 'r', 'utf-8', 'ignore') as f:
        print("Odczytuję dane z dostarczonych przez Endomondo plików. Cierpliwości, "
              "to może chwilę potrwać.", end='\n')
        print("Aktualny folder to ", os.getcwd(), end='\n')
        print(datetime.date.today())
        print(80 * '*')
        line = f.readline()
        while line != '':
            print("Opracowuję plik " + line.strip())
            czytaj_workout(line)
            line = f.readline()

except (IOError, OSError):
    # print >> sys.stderr, "Error!", sys.exc_info()[0]
    print("Error!", sys.exc_info()[0], file=sys.stderr)
    f.close()
    sys.exit(1)
finally:
    f.close()
    #print("klucze: ", klucze)
    #print()

    for i in range(17):
        if list(workout_data[i].keys())[0] != 'points':
            '''
            print(list(workout_data[i].keys())[0])
            print(list(workout_data[i].values())[0])
            '''
            '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
            klucz = klucze[i]
            print(klucz)
            print(wartosci[i][klucz][0])
            '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
        else:
            location_dic = workout_data[i]['points']
            print(location_dic[0][0])
            print(location_dic[0][1])#dystans do pierwszego pktu
            latitude_dic = list((location_dic[0][0]).values())[0][0][0]
            longitude_dic = list((location_dic[0][0]).values())[0][0][1]
            print("latitude: ", latitude_dic['latitude'])
            print("longitude: ", longitude_dic['longitude'])

            #print(list(location_dic[0][0])[0])#0=napis klucza location
            print(location_dic[1][0])
            print(location_dic[0][1])  # dystans do drugiego pktu

            #print(*workout_data[1]) napis klucza source
