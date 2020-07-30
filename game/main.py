

ff1()
ff2()

DEBUG = True


def gra():
    bohater = Postac("John", 100, 100)
    wrog = Postac("Demon", 100, 100)
    przedmiot = Przedmiot("Krucyfix", 10, 10)

    plansza = Plansza()
    polozenie_bohater = Polozenie(random.randint(1, 10), random.randint(1, 10), plansza)
    polozenie_wrog = Polozenie(random.randint(1, 10), random.randint(1, 10), plansza)
    polozenie_przedmiot = Polozenie(random.randint(1, 10), random.randint(1, 10), plansza)

    print("Rozpoczyna rozgrywkę: ")
    while True:
        if DEBUG:
            print(bohater, polozenie_bohater)
            print(wrog, polozenie_wrog)
            print(przedmiot, polozenie_przedmiot)

        komenda = input("W którą stronę idziesz? (g,d,l,p): ")
        try:
            getattr(polozenie_bohater, komenda)()
        except AttributeError:
            print("Wpisz poprawną komendę: ")
            continue

        if not polozenie_bohater.czy_na_planszy:
            print("Wypadłeś za planszę! Koniec!")
            break

        if polozenie_bohater == polozenie_przedmiot:
            print("Znalazłeś przedmiot!!!")
            bohater.daj_przedmiot(przedmiot)
            polozenie_przedmiot.x == -100

        if polozenie_bohater == polozenie_wrog:
            Postac.walka(bohater, wrog)

        print("Bohater na pozycji: ", polozenie_bohater)



gra()
