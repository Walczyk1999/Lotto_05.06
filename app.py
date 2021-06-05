def selected_numbers():
    lista = []
    while len(lista) < 6:
        try:
            number = int(input("Podaj liczbę :"))
        except ValueError:
            print("To nie jest liczba. :(")
        if number not in lista and 0 < number <= 49:
            lista.append(number)
    print(lista)
    return lista


def lotto():
    import random
    lotto = []
    x = random.randint(1, 49)
    while len(lotto) < 6:
        x = random.randint(1, 49)
        lotto.append(x)
    print(lotto)
    return lotto


def play(a, b):
    list_difference = []

    for item in a:

        if item in b:
            list_difference.append(item)
    print(f"Udalo Ci sie trafić {len(list_difference)} liczby, Gratulacje")
    print(list_difference)


play(selected_numbers(), lotto())
