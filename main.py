def startwith(start: int, mgraph: list) -> list:
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    print(nopass)
    dis = mgraph[start]
    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i
        nopass.remove(idx)
        passed.append(idx)
        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]: dis[i] = dis[idx] + mgraph[idx][i]
    return dis

if __name__ == '__main__':
    inf = 10086
    inputfile = open('net.in', 'r',encoding="utf-8")
    lines = inputfile.readlines()
    line_one = lines[0].replace('\n', '').split(' ')
    matrix_width = int(line_one[0])
    node_num = int(line_one[1])
    start_node = int(line_one[2])
    end_node = int(line_one[3])
    matrix = [[0 for i in range(matrix_width)] for j in range(matrix_width)]
    for i in range(matrix_width):
        for j in range(matrix_width):
            if(i != j):
                matrix[i][j] = inf
    for index in range(1, len(lines)):
        start, end, dis = lines[index].split(' ')
        matrix[int(start) - 1][int(end) - 1] = int(dis)
    distance = startwith(start_node-1, matrix)
    outputfile = open('net.out','w',encoding='utf-8')
    outputfile.writelines("叶思阳19121564"+'\n'+str(distance[end_node-1]))
