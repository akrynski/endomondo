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
def czytaj_workout(_line, _www):
    try:
        _www.write("\n<h3 align = 'center'>Trening {0}</h3><br>\n".format(_line.strip('.json')))
        print("Otwieram plik " + _line.strip())
        if _line == "output.txt":
            return 0
        _aktualny_workout = codecs.open(_line, 'r', 'utf-8', 'ignore')
        print("Json ładuje plik " + _line)
        workout_data = json.load(_aktualny_workout)
        pola = len(workout_data)
        klucze = []# to nie deklaracja a czyszczenie - deque?

        for i,_ in enumerate(workout_data):
            klucz = [*workout_data[i]][0]
            if klucz not in klucze:
                klucze.append(klucz)
        _www.write("<div class='container-fluid' style='background-color: #cfc'>")
        for i, v in enumerate(klucze):
            #print("i=",i, "v=",v)
            if  v != 'points':
                #_www.write("<b>{0}</b> {1}<br>".format(list(workout_data[i].keys())[0], workout_data[i][v]))
                if v == 'message': #sprawdzamy wszystkie klucze więc użyć trzeba if w każdym sprawdzeniu?
                    _www.write("Uwagi do treningu:<br>{0}<br>".format(workout_data[i][v]))
                    '''print('index = ',i)
                    print('klucz = ',list(workout_data[i].keys())[0])# == v
                    print('wartość: ',workout_data[i][v])
                    print(10*'-')'''
                if v == 'sport':
                    _www.write("{0}: {1}<br>".format(v, workout_data[i][v]))
                if v == 'source':
                    _www.write("Dane pochodzą z {1}<br>".format(v, workout_data[i][v]))
                if v == 'distance_km':
                    _www.write("Pokonano dystans <b>{1:.2f}km</b><br>".format(v, workout_data[i][v]))
                if v == 'speed_avg_kmh':
                    _www.write("Średnia prędkość to <b>{1:.2f}km/h</b><br>".format(v, workout_data[i][v]))
                if v == 'speed_max_kmh':
                    _www.write("Prędkość maksymalna: <b>{1:.2f}km/h</b><br>".format(v, workout_data[i][v]))
                if v == 'altitude_min_m':
                    _www.write("Najmniejsze przewyższenie: <b>{1}m</b><br>".format(v, workout_data[i][v]))
                if v == 'altitude_max_m':
                    _www.write("Największe przewyższenie: <b>{1}m</b><br>".format(v, workout_data[i][v]))
                if v == 'duration_s':
                    _www.write("Trening trwał <b>{0}godz. {1}min.</b><br>".format(workout_data[i][v]//3600, (workout_data[i][v]%3600)//60 ))
                if v == 'comments':
                    print("SEKCJA COMMENTS")
                    comment_dic_list= workout_data[i]
                    comment_dic = list(comment_dic_list['comments'][0])
                    _www.write("Do treningu {0} dodał komentarz:<br>&nbsp&nbsp&nbsp<i>{1}</i><br>".format(comment_dic[0]['author'],comment_dic[2]['text'] ))
                    print('Autor: ',comment_dic[0]['author'])
                    print('text: ', comment_dic[2]['text'])
                    print(10*'-')
                elif v == 'routes':
                    print('SEKCJA ROUTES')
                    routes_dic_list = workout_data[i]
                    routes_dic = list(routes_dic_list['routes'][0])
                    print('name: ',routes_dic[1]['name']) # jeśli struktura tabeli wartości routes jest niezmienna
                                                          # mogę użyć stałych wskaźników tabeli ([0],[1])
                    print('identifier: ', routes_dic[0]['identifier'])
                    print(10*'-')
                    _www.write("Workout przebiegał śladem zapisanej trasy {0}<br>".format(routes_dic[1]['name']))
                elif v == "pictures":
                    print("SEKCJA PICTURES")
                    pictures_dic_list = workout_data[i]['pictures']
                    _www.write("<div class=box align='top' style = 'float: right;width: 40%;border: 5px solid gray;margin: 2;'>")
                    for i,v in enumerate(pictures_dic_list):

                        for item in v:
                            if 'picture' in item:
                                print('url: ', item['picture'][0][0]['url'])
                                _www.write("<img src=../{0} style='float:right;width:30%;height:30%;object-fit:scale-down;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);' alt='fotka'>".format(item['picture'][0][0]['url']))

                    print(10*'-')
                    _www.write("</div>")

                elif v == 'tags':
                    print("SEKCJA TAGS")
                    tagi = workout_data[i][v]
                    print('tagi:', tagi[0][0]['name'])
                    _www.write("Zapisane tagi: {0}".format(tagi[0][0]['name']))
                    print(10 * '-')
            elif v == 'points':
                print(i)
                print('TU SĄ POINSY')
                print(10*'v')
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
                _www.write("</div>")
                continue
        _www.write("</div>")
        return workout_data
    #--------------------------------------------------------------------------------
    except(IOError, OSError):
        print('Błąd funkcji \'czytaj_workout\'!', sys.exc_info()[0], file=sys.stderr)
        sys.exit(1)
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
h = codecs.open('./out.html', 'a', 'utf-8', 'ignore')
h.write("<!DOCTYPE html>\n<html lang='pl'>\n<head>\n<title>Przegląd treningów</title>\n<meta charset='utf-8' />\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n</head>\n<body>")
with codecs.open('./output.txt', 'r', 'utf-8', 'ignore') as f:
        print("Odczytuję dane z dostarczonych przez Endomondo plików. Cierpliwości, "
              "to może chwilę potrwać.", end='\n')
        print("Aktualny folder to ", os.getcwd(), end='\n')
        print(datetime.date.today())
        print(80 * '*')
        for wiersz in czytaj_wiersz(f):
            czytaj_workout(wiersz, h)
h.write("</body>\n</html>\n")
h.close()
