from cmath import sqrt


def Astar(nodes, start_id, end_id):
    nodes_open = {}
    nodes_close = {}
    path = []

    nodes_open[start_id] = nodes[start_id]
    while len(nodes_open) != 0:
        q = min(nodes_open, key=lambda node_id: nodes_open.get(node_id).f)
        # print q
        # print nodes[start_id].parent
        del nodes_open[q]
        for neighbour_id in nodes[q].neighbours:
            if neighbour_id == start_id:
                continue
            if neighbour_id == end_id:
                print "znalezione"
                nodes[neighbour_id].parent = q
                # print nodes[start_id].parent
                while nodes[neighbour_id].parent != 0:
                    path.append(neighbour_id)
                    neighbour_id = nodes[neighbour_id].parent
                    # print neighbour_id
                path.append(neighbour_id)
                return path

            g = nodes[q].g + distance(nodes[q].x, nodes[q].y, nodes[neighbour_id].x, nodes[neighbour_id].y)
            h = distance(nodes[neighbour_id].x, nodes[neighbour_id].y, nodes[end_id].x, nodes[end_id].y)
            f = g + h
            if neighbour_id in nodes_open:
                if nodes_open[neighbour_id].f < f:
                    continue
            if neighbour_id in nodes_close:
                if nodes_close[neighbour_id].f < f:
                    continue

            nodes[neighbour_id].f = f
            nodes[neighbour_id].g = g
            nodes[neighbour_id].h = h
            nodes[neighbour_id].parent = q

            nodes_open[neighbour_id] = nodes[neighbour_id]

        nodes_close[q] = nodes[q]


def distance(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    d = sqrt(x**2 + y**2).real
    return d



