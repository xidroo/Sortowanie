import math
import random
import time

import pygame
from Button import Button




pygame.init()
okno = pygame.display.set_mode([1000, 600])
obszar = pygame.Surface((1000, 400))

pygame.display.set_caption("Algorytmy sortujące")
timer = pygame.time.Clock()
FPS = 60
fontDUZA = pygame.font.SysFont('Comic Sans MS', 34)
fontDUZA1 = pygame.font.SysFont('Comic Sans MS', 30)

fontDUZA.set_underline(True)
fontMALA = pygame.font.SysFont('Comic Sans MS', 22)
fontMALUTKA = pygame.font.SysFont('Comic Sans MS', 14)
font10 = pygame.font.SysFont('Comic Sans MS', 10)
font7 = pygame.font.SysFont('Comic Sans MS', 7)
font5 = pygame.font.SysFont('Comic Sans MS', 6)

dodajB = Button('aquamarine3','aquamarine','black',"Więcej")
odejmijB = Button('aquamarine3','aquamarine','black',"Mniej")
zmienB = Button('aquamarine3','aquamarine','black',"Zmień algorytm")
startB = Button('aquamarine3','aquamarine','black',"START",55)
koniecB = Button('aquamarine3','aquamarine','black',"Koniec")
losujB = Button('aquamarine3','aquamarine','black',"Losuj nowe")

TRYB = 0
run = True

rozmiar = 10
aktywny = -1
aktywny2 = -1
lista = []
maxWartosc = 0
szerokosc = 0
wybranyAlgorytm = 1

def inicjujListe(rozmiar):
    lista.clear()
    global szerokosc, maxWartosc
    for i in range(1,rozmiar+1):
        lista.append(i)
    random.shuffle(lista)
    szerokosc = 950 / rozmiar
    szerokosc = int(szerokosc)
    roznica = 950 - (szerokosc * rozmiar)
    odstep = roznica / rozmiar
    szerokosc += odstep
    maxWartosc = max(lista)


def narysujListe(aktywny,aktywny2):
    obszar.fill('azure3')
    global szerokosc, maxWartosc

    x = 25
    for i in range(0,rozmiar):
        if i == aktywny:
            pygame.draw.rect(obszar,'red',(x + (szerokosc*i),math.floor((400 -(400*lista[i])/maxWartosc)),szerokosc-2,(400*lista[i])/maxWartosc ))
        elif i == aktywny2:
            pygame.draw.rect(obszar,'chartreuse3',(x + (szerokosc*i),math.floor((400 -(400*lista[i])/maxWartosc)),szerokosc-2,(400*lista[i])/maxWartosc ))
        else:
            pygame.draw.rect(obszar,'blue',(x + (szerokosc*i),math.floor((400 -(400*lista[i])/maxWartosc)),szerokosc-2,(400*lista[i])/maxWartosc ))
        if rozmiar in [ 10,20]:
            obszar.blit(fontMALA.render(str(lista[i]), True, 'white'), (x + (szerokosc*i)+9, math.floor((400 -(400*lista[i])/maxWartosc))))
        elif rozmiar in [30,40]:
            obszar.blit(fontMALUTKA.render(str(lista[i]), True, 'white'), (x + (szerokosc*i)+3, math.floor((400 -(400*lista[i])/maxWartosc))))
        elif rozmiar in [50,60]:
            obszar.blit(font10.render(str(lista[i]), True, 'white'), (x + (szerokosc*i)+1, math.floor((400 -(400*lista[i])/maxWartosc))))
        elif rozmiar in [70, 80]:
            obszar.blit(font7.render(str(lista[i]), True, 'white'),(x + (szerokosc * i)+1, math.floor((400 - (400 * lista[i]) / maxWartosc))))
        else:
            obszar.blit(font5.render(str(lista[i]), True, 'white'),(x + (szerokosc * i), math.floor((400 - (400 * lista[i]) / maxWartosc))))
    okno.blit(obszar, (0, 70))
    pygame.display.update()



def numerAlgorytmuNaNazwe(numerAlgorytmu):
    if numerAlgorytmu == 1:
        return "            NAIWNE"
    if numerAlgorytmu == 2:
        return "         BĄBELKOWE"
    if numerAlgorytmu == 3:
        return "        PRZEZ WYBÓR"
    if numerAlgorytmu == 4:
        return "  PRZEZ WSTAWIANIE"
    if numerAlgorytmu == 5:
        return "     PRZEZ SCALANIE"
    if numerAlgorytmu == 6:
        return "            SZYBKIE"
nazwaWybranegoAlgorytmu = numerAlgorytmuNaNazwe(wybranyAlgorytm)
inicjujListe(rozmiar)

trwaSortowanie = False
def sortowanieNaiwne(lista = []):
    aktywny = 0
    aktywny2 = 0
    global trwaSortowanie
    i = 0
    while i < (len(lista)-1):
        narysujListe(aktywny,aktywny2)
        time.sleep(0.1)
        if lista[i] > lista[i+1]:
            pomoc = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = pomoc
            aktywny = i
            i = 0
        else:
            i += 1
            aktywny2 =i

    trwaSortowanie = False

def sortowanieBabelkowe(lista = []):
    aktywny = 0
    aktywny2 = -1
    global trwaSortowanie
    zmiana = True
    granica = len(lista)-1
    while zmiana:
        print(lista)
        zmiana = False
        for i in range(granica):
            narysujListe(granica+1, i)
            time.sleep(0.1)
            if lista[i] > lista[i+1]:
                pomoc = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = pomoc
                zmiana = True
        granica-=1

    trwaSortowanie = False

def sortowanieWybor(lista =[]):
    aktywny = 0
    aktywny2 = -1
    global trwaSortowanie
    for i in range(len(lista)):
        min = lista[i]
        pozycja = i
        aktywny = i-1
        for j in range(i,len(lista)):
            narysujListe(aktywny, j)
            time.sleep(0.1)
            if lista[j] < min:
               min = lista[j]
               pozycja = j


        pomoc = lista[i]
        lista[i] = lista[pozycja]
        lista[pozycja] = pomoc


    trwaSortowanie = False


def sortowanieWstawianie(lista = []):
    global trwaSortowanie
    for i in range(1, len(lista)):
        j = i
        pomoc = lista[i]
        while lista[j-1] > pomoc and j > 0:
            narysujListe(i+1, j)
            time.sleep(0.1)
            lista[j] = lista[j-1]
            j-=1
        lista[j] = pomoc

    trwaSortowanie = False


def scalanie(p, s, k, lista=[]):
    kopia = []
    for liczba in lista:
        kopia.append(liczba)

    i = p
    j = s + 1
    q = p

    while i <= s and j <= k:
        if kopia[i] < kopia[j]:
            lista[q] = kopia[i]
            i += 1
        else:
            lista[q] = kopia[j]
            j += 1
        q += 1
        narysujListe(-1, q)
        time.sleep(0.1)

    while i <= s:
        lista[q] = kopia[i]
        i += 1
        q += 1

def sortowanieScalanie(p,k,lista=[]):
    global trwaSortowanie
    if p < k:
        s = (p+k)//2
        sortowanieScalanie(p,s,lista)
        sortowanieScalanie(s+1,k,lista)
        scalanie(p,s,k,lista)

    trwaSortowanie = False


def szybkieCpp(lista, poczatek , koniec):
    global trwaSortowanie
    j = poczatek
    podzial = lista[koniec]

    for i in range(poczatek,koniec):
        narysujListe(koniec, i)
        time.sleep(0.1)
        if (lista[i] < podzial):
            pom = lista[i]
            lista[i] = lista[j]
            lista[j] = pom
            j+=1


    lista[koniec] = lista[j]
    lista[j] = podzial

    if (poczatek < j - 1):
        szybkieCpp(lista, poczatek, j - 1)

    if (j + 1 < koniec):
        szybkieCpp(lista, j + 1, koniec)
    trwaSortowanie = False

while run:
    timer.tick(FPS)
    okno.fill('azure3')
    klawisze = pygame.key.get_pressed()
    myszPozycja = pygame.mouse.get_pos()
    myszKlik = pygame.mouse.get_pressed()


    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            run = False

    if klawisze[pygame.K_ESCAPE]: run = False
    if TRYB == 0:
        okno.blit(fontDUZA.render("Wizualizacja algorytmów sortujących", True, 'black'),(190,6))

        koniecB.render(okno,895,510,100,50)
        zmienB.render(okno,690,490,200,50)
        startB.render(okno,690,543,200,50)
        if koniecB.clik():
            run = False

        okno.blit(fontMALA.render("Ilość liczb: " + str(rozmiar), True, 'black'), (20, 500))
        okno.blit(fontDUZA1.render("SORTOWANIE", True, 'black'), (380, 490))
        okno.blit(fontDUZA1.render(nazwaWybranegoAlgorytmu, True, 'black'), (310, 535))
        dodajB.render(okno, 195, 490, 100, 50)
        odejmijB.render(okno, 195, 543, 100, 50)
        losujB.render(okno, 20, 543, 160, 50)
        if losujB.clik():
            inicjujListe(rozmiar)
        if dodajB.clik() and rozmiar < 100:
            rozmiar += 10
            inicjujListe(rozmiar)
        if odejmijB.clik() and rozmiar > 10:
            rozmiar -= 10
            inicjujListe(rozmiar)
        if zmienB.clik():
            wybranyAlgorytm += 1
            if wybranyAlgorytm > 6:
                wybranyAlgorytm = 1
            nazwaWybranegoAlgorytmu = numerAlgorytmuNaNazwe(wybranyAlgorytm)

        if startB.clik() and not trwaSortowanie:
            trwaSortowanie = True
            koniecB.nieAktywny = True
            pygame.display.update()
            if wybranyAlgorytm == 1:
                sortowanieNaiwne(lista)
            if wybranyAlgorytm == 2:
                sortowanieBabelkowe(lista)
            if wybranyAlgorytm == 3:
                sortowanieWybor(lista)
            if wybranyAlgorytm == 4:
                sortowanieWstawianie(lista)
            if wybranyAlgorytm == 5:
                sortowanieScalanie(0,rozmiar-1,lista)
            if wybranyAlgorytm == 6:
               szybkieCpp(lista, 0,rozmiar-1)

        if not trwaSortowanie:
            koniecB.nieAktywny = False
            narysujListe(aktywny,aktywny2)


    pygame.display.update()

pygame.quit()