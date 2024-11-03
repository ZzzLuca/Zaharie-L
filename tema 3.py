meniu = ["papanasi"] * 10 +["ceafa"] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"] # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"] # coada FIFO
tavi = ["tava"] * 7 # stiva LIFO
istoric_comenzi = []
while studenti:
    comanda = comenzi.pop()
    student = studenti.pop()
    tavi.pop()
    istoric_comenzi.append(comanda)
    cati_papanasi_exista = meniu.count("papanasi") - istoric_comenzi.count("papanasi")
    cata_ceafa_exista = meniu.count("ceafa") - istoric_comenzi.count("ceafa")
    cat_guias_exista = meniu.count("guias") - istoric_comenzi.count("guias")
    print (f"{student} a comandat {comanda}")
    if cat_guias_exista > 0:
        print("au ramas {cat_guias_exista} portii de guias")
    if cat_guias_exista < 0:
        print("nu mai este guias")
    if cati_papanasi_exista > 0:
        print("au ramas {cati_papanasi_exista} papanasi")
    if cati_papanasi_exista < 0:
        print("nu mai sunt papanasi")
    if cata_ceafa_exista > 0:
        print("au ramas {cata_ceafa_exista} bucati de ceafa")
    if cata_ceafa_exista < 0:
        print("nu mai este ceafa")

    print(f"mai sunt {len(tavi)} tavi")
    print(f"au fost comandate {istoric_comenzi.count("papanasi")}portii de papanasi, {istoric_comenzi.count("ceafa")} cefe,
          {istoric_comenzi.count("guias")} portii de guias")
    def vanzari():
        vanzari_ceafa = preturi[1][1] * istoric_comenzi.count("ceafa")
        vanzari_guias = preturi[2][1] * istoric_comenzi.count("guias")
        vanzari_papanasi = preturi [0][1] * istoric_comenzi.count("papanasi")
        print(f"venitul cantinei este de {vanzari_ceafa + vanzari_papanasi + vanzari_guias} lei")
    def costuri():
        for portie in preturi:
            pret = portie[1]
            if pret <= 7:
                print(f"portiile care costa cel mult 7 lei: {portie[0]}")
    vanzari()
    costuri()
    