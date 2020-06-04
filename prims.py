def ReadGraphMatrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in lines:
            G = []
            for j in i.split():
                G.append(int(j))
            matrix.append(G)
    return matrix


def minimum_spanning_tree(Graph, start_num):
    result = []
    edge_num = 0
    vertex_num = len(Graph)
    vertex = [False] * vertex_num
    vertex[start_num] = True

    while edge_num < vertex_num - 1:
        min = 10000
        minXYw = []
        for i in range(vertex_num):
            if vertex[i]:
                for j in range(vertex_num):
                    if (not vertex[j]) and Graph[i][j]:
                        if min > Graph[i][j]:
                            min = Graph[i][j]
                            minXYw = [i, j, min]
        vertex[minXYw[1]] = True
        edge_num += 1
        result.append(minXYw)
    return result


def PrintResults(result, start_num):
    sum = 0
    with open("rezultatai.txt", "w") as file:
        file.write("Studento numeris 13, pradžios viršūnė " +
                   str(start_num) + " (skaičiuojant viską nuo 0)\n")
        file.write("Briaunos (iš kurios viršūnės į kurią): \n")

        for i in range(len(result)):
            file.write(str(result[i][0]) + "-" + str(result[i][1]) + "\t")
            sum += result[i][2]
        file.write("\nMinimalaus aprėpiančio medžio svoris - " + str(sum))


# nuo kurios viršūnės pradėti
num = 2
# nuskaitymas
# G = ReadGraphMatrix("duomenys.txt")
# duota svorine gretimumo matrica:
G = [[0,  98, 67, 30, 48, 44, 47, 30, 49, 83],
     [98, 0, 23, 22, 14, 22, 12, 29, 60, 39],
     [67, 23, 0	, 3, 53, 69, 77, 2	, 54, 47],
     [30, 22, 3	, 0, 56, 79, 90, 34, 50, 61],
     [48, 14, 53, 56, 0, 4	, 79, 46, 19, 22],
     [44, 22, 69, 79, 4, 0	, 37, 57, 76, 51],
     [47, 12, 77, 90, 79, 37, 0	, 30, 80, 81],
     [30, 29, 2, 34, 46, 57, 30, 0	, 12, 79],
     [49, 60, 54, 50, 19, 76, 80, 12, 0, 24],
     [83, 39, 47, 61, 22, 51, 81, 79, 24, 0]]

result = minimum_spanning_tree(G, num)
# duomenu isvedimas i faila
PrintResults(result, num)
