from operator import itemgetter


def get_start_vertex(point, rectangles):
    values = list(filter(
        lambda x: x[0] <= point[0] < x[1] and point[2] <= x[2] and point != x and not (
            point[0] == x[0] and point[2] == x[2]
        ),
        rectangles)
    )
    if values:
        return None
    else:
        return point[0], point[2]


def get_end_vertex(point, rectangles):
    higher_values = list(filter(lambda x: x[0] <= point[1] < x[1] and point[2] <= x[2] and point != x, rectangles))
    if higher_values:
        return None
    else:
        lower_values = list(filter(lambda x: x[0] <= point[1] < x[1] and point[2] > x[2] and point != x, rectangles))
        if lower_values:
            max_value = max(lower_values, key=itemgetter(2))[2]
            return point[1], max_value
        else:
            return point[1], 0


def get_vertices(rectangles):
    vertices = []
    for i in rectangles:
        start_vertex = get_start_vertex(i, rectangles)
        if start_vertex:
            vertices.append(start_vertex)
        end_vertex = get_end_vertex(i, rectangles)
        if end_vertex:
            vertices.append(end_vertex)
    vertices = list(set(vertices))
    return vertices


if __name__ == '__main__':
    input_list = [(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)]
    print(get_vertices(input_list))
