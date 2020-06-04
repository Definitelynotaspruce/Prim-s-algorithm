# Prim-s-algorithm
Minimum spanning tree algorithm

Minimalaus aprėpiančio medžio paieška naudojant Primo algoritmą

Programos veikimo principas:

1.  Viršūnės, nuo kurios vyks paieškos pradžia, nustatymas 
    (mano atveju tai yra 2-oji viršūnė, nes ji yra trečia nuo 
    pradžios skaičiuojant nuo 0).

2.  Duomenų nuskaitymas

3.  Skaičiavimai pagal Primo algoritmą:
    1)  Sukuriamas bool tipo masyvas "vertex", kuris saugo, 
        ar tam tikro indekso viršūnė jau aplankyta ar ne.
        Nustatoma aprėpiančiojo medžio paieškos pradžios viršūnė (vertex[2] = True).
        Surastų kraštinių skaičius prilyginamas 0 (edge_num  = 0).
        Nustatomas viršūnių skaičius ( vertex_num = len(Graph))
    2)  Kadangi minimaliame aprėpiančiajame medyje kraštiniu skaičius yra vienu mažesins nei viršūnių,
        paleidžiamas ciklas (while edge_num < vertex_num - 1).
    3)  Nustatomas mažiausias svoris (min = 1000) tam, kad vėliau galima būtų surasti už jį mažesnį.
        Taip pat deklaruojamas masyvas, kuris saugos briauną (iš kurios viršūnės į kurią keliauja bei jos svorį (minXYw = []))
        Paleidžiamas ciklas (for i in range(vertex_num)), kuris turi apeiti visų viršūnių indeksus.
    4)  Vyksta patikrinimo sąlyga (if vertex[i]), kuri suveikia teigiamai tik tada, kuomet viršūnė jau aplankyta (pirmuoju pradiniu atveju tai yra tik viršūnė 2)
    5)  Jeigu viršūnė jau aplankyta/iki jos trumpiausia briauna surasta, tuomet (slected[] = True),
        vyksta sekantis ciklas (for j in range(vertex_num)), kurio indeksas j kinta nuo 0 iki viršūnių skaičiaus.
    6)  Vyksta patikrinimo sąlyga (if (not vertex[j]) and Graph[i][j]), kuri tikrina, ar iki pasirinktos viršūnės jau nėra surasta briauna ir ar tokia briauna egzistuoja 
        iš paduotos gretimumo matricos.
        Jeigu abi šios sąlygos įgyvendintos, tikrinama, ar naujas svoris yra mažesnis už prieš tai nustatytą, jeigu taip,
        nustatomas naujas mažiausias svoris bei išsaugomos viršūnės su tuo svoriu (min = Graph[i][j], minXYw = [i, j, min])
    7)  Kuomet randama minimalaus aprėpiančio medžio briauna ciklas pažymi aplankytą viršūnę (vertex[minXYw[1]] = True)
        bei išsaugo tą atitinkamą briauną masyve (result.append(minXYw)). 
        Briaunų skaičius padidinamas 1 ( edge_num += 1).
    8)  Programa grįžta į pradinį ciklą (while edge_num < vertex_num - 1), taip randamos visos briaunos ir aplankomos visos viršūnės.
    9)  Grąžinamas rezultatų masyvas (return result).

4. Vyksta duomenų išvedimas:
    1)  Sukuriamas kintamasis minimalaus aprėpiančio medžio svoriui apskaičiuoti
        (sum = 0).
    2)  Išvedamas studento numeris bei pradžios viršūnė.
    3)  Išvedamos surastos briaunos (iš kurios viršūnės į kurią), taip pat sumuojami jų svoriai.
    4)  Išvedamas minimalaus aprėpiančio medžio svoris.
