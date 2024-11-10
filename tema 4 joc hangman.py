import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
incercari_ramase = 6
litere_incercate = []
while incercari_ramase > 0 and "_" in progres:
    litera = input("introdu o litera pretty pls: ").lower()
    if len(litera) != 1 or not litera.isalpha():
        print("as prefera daca ai introduce o litera valida")
        continue
    if litera in litere_incercate:
        print(f"ai încercat litera '{litera}' deja, pune alta")
        continue
    litere_incercate.append(litera)
    if litera in cuvant_de_ghicit:
        print(f"ai ghicit litera '{litera}' din cuvant")

        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
    else:
        incercari_ramase -= 1
        print(f"HAHA, AI GRESIT, litera '{litera}' nu e in cuvant, mai ai {incercari_ramase} sanse de a ghici")

    print("cuvantul de ghicit: " + " ".join(progres))
    print(f"incercari ramase: {incercari_ramase}")
    print()

if "_" not in progres:
    print(f"wow, ai ghicit cuvantul: {cuvant_de_ghicit}")
else:
    print(f"looooseeer!! cuvantul pe care trebuia sa il ghicesti era: {cuvant_de_ghicit}. better luck next time haha")