mport random
while True:    
  moje_liczby = set()
  wylosowane_liczby = set()
  trafione_liczby  =  moje_liczby.intersection(wylosowane_liczby)
  ilosc_trafionych = 0
  
  print(""" Witaj w grze Lotto,podaj 6 wytypowanyh przez Ciebie liczb!""")
  print("\n")
  moje_liczby_length = len(moje_liczby)
  
  while moje_liczby_length != 6:
    pobierz_liczby  = int(input("Podaj swoje liczby:"))
    
    if int(pobierz_liczby) > 49:
      print("Podana liczba jest za duza podaj liczbe od 1 do 49")

    elif int(pobierz_liczby) == 0:
      print("Podana liczba jest za mala podaj liczbe od 1 do 49")
    
    else:
      moje_liczby.add(pobierz_liczby)
      moje_liczby_length+=1
  
  
  def losowanie():
    """
    Losuje 6 liczb i dodaje je do seta wylosowane liczby
    """
    licznik = 6
    while licznik > 0:
        liczba = random.randint(1,49) 
        if liczba in wylosowane_liczby:
          liczba = random.randint(1,49) 

        else:
          licznik = licznik-1
          wylosowane_liczby.add(liczba)

      
  def sprawdz_wynik():
    """
    Wypisuje trafione liczby, liczby podane przez użytkownika oraz ilosc trafionych liczb    
    
    """
    trafione_liczby = moje_liczby.intersection(wylosowane_liczby)
    ilosc_trafionych = len(trafione_liczby)
    
    if ilosc_trafionych == 6:
        print("Twoje liczby to",moje_liczby," a wylosowane liczby to",wylosowane_liczby)
        print("Gratulacje udało Ci się trafić 6")
        print("\n")

    elif ilosc_trafionych == 5:
        print("Twoje liczby to",moje_liczby," a wylosowane liczby to",wylosowane_liczby)
        print("Trafiłeś 5 liczb")
        print("\n")

    elif ilosc_trafionych == 4:
        print("Twoje liczby to",moje_liczby," a wylosowane liczby to",wylosowane_liczby)
        print("Trafiłeś 4 liczby")
        print("\n")

    elif ilosc_trafionych == 3:
        print("Twoje liczby to",moje_liczby," a wylosowane liczby to",wylosowane_liczby)
        print("Trafiłeś 3 liczby")
        print("\n")


    elif ilosc_trafionych == 2:
        print("Twoje liczby to",moje_liczby," a wylosowane liczby to",wylosowane_liczby)
        print("Trafiłeś 2 liczby")
        print("\n")

    elif ilosc_trafionych == 1:
        print("Twoje liczby to",moje_liczby," a wylosowane liczby to",wylosowane_liczby)
        print("Trafiłeś jedna liczbe")
        print("\n")
  
    else:
        print("Twoje liczby to",moje_liczby," a wylosowane liczby to",wylosowane_liczby)
        print("Próbuj dalej")
        print("\n")
        
  
  if __name__ == "__main__":
    losowanie()
    sprawdz_wynik()
