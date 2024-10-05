print("Zadanie 1:")
słownik = {
    "Piekarnia" : ["Chleb", "Pączek" , "Bułki"],
    "Warzywniak" : ["Marchew", "Seler", "Rukola"]
}
łączna_liczba_produktów = 0
for i in słownik:
    produkty = słownik[i]
    print (f"Idę do {i} i kupuję tam: {produkty}")
    łączna_liczba_produktów = łączna_liczba_produktów + len(produkty)
print(f"W sumie kupuję {łączna_liczba_produktów} produktów.")
print()


print("Zadanie 2:")
lista=[]
for i in range(1, 101):
    lista.append(i)
lista_podzielnych_przez_5 = []
for i in lista:
    if i % 5 == 0:
        lista_podzielnych_przez_5.append(i)
print(lista_podzielnych_przez_5)
lista_do_szescianu = []
for i in lista_podzielnych_przez_5:
    lista_do_szescianu.append(i*i*i)
print(lista_do_szescianu)