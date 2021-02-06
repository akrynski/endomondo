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
workout_items = []
workouts = []

klucze = []

os.chdir("C:\\Users\\Andrzej\\Downloads\\endomondo-2021-01-27\\Workouts\\")
os.system("dir /B /A:-D > .\\output.txt")


# noinspection PyShadowingNames
def czytaj_workout(_line):
    try:
        global aktualny_workout
        global workout_data
        print("Otwieram plik " + _line)
        if _line.strip() == "output.txt":
            return 0

        aktualny_workout = codecs.open(_line.strip(), 'r', 'utf-8', 'ignore')
        print("Json ładuje plik " + _line)
        workout_data = json.load(aktualny_workout)
        pola = len(workout_data)
        tmp = []
        for i in range(pola-1):
            #print(workout_data[i])
            tmp.append(workout_data[i])
            #print(workout_items[0])
        workouts.append([tmp])


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
        print("Odczytuję dane z dostarczonych przez Endomondo plików. Bądź cierpliwy, "
              "to może chwilę potrwać.", end='\n')
        print("Aktualny folder to ", os.getcwd(), end='\n')
        print(datetime.date.today())
        print(80 * '*')
        line = f.readline()
        while line != '':
            print("Opracowuję plik " + line.strip())
            czytaj_workout(line)
            line = f.readline()

    for i in range(len(workouts) - 1):
        #print(workout_items[klucz])
        for klucz, wartosc in workouts[i][0][0].items():
            print(workouts[i][0][0])
            if klucz not in klucze:
                klucze.append(klucz)
except (IOError, OSError):
    # print >> sys.stderr, "Error!", sys.exc_info()[0]
    print("Error!", sys.exc_info()[0], file=sys.stderr)
    f.close()
    sys.exit(1)
finally:
    f.close()
    #print(workouts[0][0])
    print(klucze)
