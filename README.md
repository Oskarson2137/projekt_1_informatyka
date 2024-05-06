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