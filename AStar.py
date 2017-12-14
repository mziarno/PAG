from cmath import sqrt


def Astar(nodes, start_id, end_id):
    nodes_open = {}
    nodes_close = {}

    nodes_open[start_id] = nodes[start_id]

    while len(nodes_open) != 0:
        q = min(nodes_open, key=lambda node_id: nodes_open.get(node_id).f)
        del nodes_open[q]
        # print "Marcka"
        print len(nodes[q].neighbours)
        for neighbour in nodes[q].neighbours:
            if neighbour == end_id:
                print "znalezione"
            g = nodes[q].g + distance(nodes[q].x, nodes[q].y, nodes[neighbour].x, nodes[neighbour].y)
            h = distance(nodes[neighbour].x, nodes[neighbour].y, nodes[end_id].x, nodes[end_id].y)
            f = g + h
            # print f
            if neighbour in nodes_open:
                if nodes_open[neighbour].f < f:
                    continue
            if neighbour in nodes_close:
                if nodes_close[neighbour].f < f:
                    continue

            nodes[neighbour].f = f
            nodes[neighbour].g = g
            nodes[neighbour].h = h
            nodes[neighbour].parent = q

            nodes_open[neighbour] = nodes[neighbour]
            print len(nodes_open)

        nodes_close[q] = nodes[q]











def distance(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    d = sqrt(x**2 + y**2).real
    return d



