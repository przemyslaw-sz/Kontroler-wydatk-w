def pokaz_menu():
    print('\nMenu')
    print('1 - Dodawanie wydatku')
    print('2 - Pokaz liste wydatkow')
    print('3 - Suma wydanych pieniędzy')
    print('4 - Zakoncz dodawanie wydatkow')
wydatki = []
while True:
    pokaz_menu()
    wybor = input('Wybierz liczbe 1 - 4: ')
    if wybor == '1':
        wydatek = input('Co kupiles? ')
        while True:
            try:
                kwota = float(input('Ile zaplaciles za ' + wydatek + '? '))
                break
            except ValueError:
                print('Błędna wartość. Wpisz cenę np. 15.50.')
        nowy_wydatek = {'Nazwa: ': wydatek, 'Cena: ': kwota}
        wydatki.append(nowy_wydatek)
    elif wybor == '2':
        print(wydatki)
    elif wybor == '3':
        suma = sum(slownik.get('Cena: ', 0.0) for slownik in wydatki)
        print(suma)
    elif wybor == '4':
        print('Koniec dodawania')
        break
    else:
        print('Błąd')
        break 
              

    
