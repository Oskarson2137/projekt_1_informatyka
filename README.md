# projekt_1_informatyka
 Projekt 1 z informatyki na GIK 4 semestr
 Program służy do transformacji współrzędnych. 
##### Dostępne transformacje:
- XYZ (geocentryczne) --> BLH (elipsoidalne)
- BLH --> XYZ
- XYZ --> NEUp (topocentryczne)
- BL --> PL2000
- BL --> PL1992

##### Dostępne elipsoidy:
- GRS80
- WGS84
- Krasowski

## Wymagania
- python 3.11.1 lub python 3.12.3
- biblioteka numpy
- biblioteka argparse

Program został napisany dla systemu operacyjnego Windows 10 i Windows 11
## Opis użycia programu
Program umożliwia podawanie argumentów przy wywołaniu za pomocą odpowiednich flag.
```sh
-p
```
Przyjmuje ścieżkę do pliku z danymi wejściowymi, jeśli plik jest w tym samym folderze co skrypt, to wystarczy nazwa pliku z rozszerzeniem.
```sh
-el
```
Przyjmuje nazwę elipsoidy. Dostępne: WGS84, GRS80 lub KRASOWSKI. Wielkość wpisywanych liter nie ma znaczenia.
```sh
-t
```
Przyjmuje nazwę wybranej transformacji. Dostępne: XYZ2BLH, BLH2XYZ, PL2000, PL1992, XYZ2NEUP. Wielkość wpisywanych liter nie ma znaczenia.
Przykładowe wywołanie:
```sh
skrypt.py -p plik_dane_XYZ2BLH.txt -el grs80 -t xyz2blh
```
Następnie wyświetli się poniższy komunikat o utworzeniu pliku z wynikami transformacji w folderze, w którym znajduje się skrypt.py.
```sh
Plik wynikowy zostal utworzony.
Jezeli chcesz wykonac kolejna transformacje wpisz TAK jesli chcesz zakonczyc ENTER:
```
 Ukaże się również informacja o tym czy użytkownik chce wykonać kolejną transformacje. Jeśli użytkownik naciśnie **ENTER** program zakończy działanie.
```sh
Jezeli chcesz wykonac kolejna transformacje wpisz TAK jesli chcesz zakonczyc ENTER:
Koniec programu
```
W przypadku kiedy użytkownik będzie chciał wykonać kolejną transformację, wpisująć **TAK**, program wyświetli informację o ponownym podaniu elipsoidy, pliku z danymi i transformacji do wykonania. Po podaniu tych wartości całość będzie wyglądać przykładowo w następujący sposób:
```sh
Jezeli chcesz wykonac kolejna transformacje wpisz TAK jesli chcesz zakonczyc ENTER: tak
Podaj nazwe elipsoidy: wgs84
Wklej sciezke do pliku txt z danymi: plik_dane_XYZ2NEUP.txt
Jaka transformacje wykonac?: xyz2neup
Plik wynikowy zostal utworzony.
Jezeli chcesz wykonac kolejna transformacje wpisz TAK jesli chcesz zakonczyc ENTER: nie
Koniec programu
```
Takie same komunikaty pojawią się także w momencie kiedy użytkownik nie poda, którejś z tych wartości przy wywoływaniu za pomocą flag.

```sh
skrypt.py -p plik_dane_XYZ2BLH.txt -t xyz2blh
Podaj nazwe elipsoidy:
```

## Opis przykładowych danych do transformacji
Wszystkie dane w plikach wejściowych i wyjściowych są oddzielone od siebie spacją.
#### BL --> PL2000/PL1992
- plik_dane_2000_92.txt

>52.2397 21.0222\
>50.0747 19.9550\
>54.3822 18.6486\
>51.1179 17.0485\
>51.7692 19.4650

Pierwsza wartość to szerokość geodezyjna[stopnie], a druga to długość geodezyjna[stopnie].

- plik_wynikowy_PL2000_grs80.txt

>5789569.282 7501516.378\
>5549251.755 7425200.576\
>6028187.860 6542138.361\
>5665196.423 6433382.104\
>5738237.349 6601119.540



Pierwsza wartość to współrzędna X[m], a druga to współrzędna Y[m].

#### BLH --> XYZ
- plik_dane_BLH2XYZ.txt

>60.4564 21.0463 89.000\
>51.1348 15.2441 200.00\
>34.1022 48.1900 14.00\
>56.1009 27.1345 134.00\
>50.4538 16.6590 96.00

Pierwsza wartość to szerokość geodezyjna[stopnie], druga to długość geodezyjna[stopnie], a trzecia to wysokość punktu[m].

- plik_wynikowy_BLH2XYZ_grs80.txt

>2942674.364 1132316.034 5525804.063\
>3869379.142 1054485.783 4943124.193\
>3524593.233 3940658.616 3555847.025\
>3173162.265 1626200.933 5270827.498\
>3898338.973 1166517.713 4895156.053


Pierwsza wartość to współrzędna X[m], druga to współrzędna Y[m], a trzecia to współrzędna Z[m].
#### XYZ --> BLH
- plik_dane_XYZ2BLH.txt

>2942674.363971118 1132316.033519957 5525804.063369009\
>3869379.142155471 1054485.783406856 4943124.193059502\
>3524593.232779779 3940658.615900714 3555847.024582718\
>3173162.265385987 1626200.933395217 5270827.497781216\
>3898338.972561540 1166517.713211751 4895156.052621000