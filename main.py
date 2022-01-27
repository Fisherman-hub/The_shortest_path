st_end_coordinate = (0, 2)
coordinates_of_points = ((2, 5), (5, 2), (6, 6), (8, 3))
len_shortest_path = 100000
for coordinate1 in coordinates_of_points:
    for coordinate2 in coordinates_of_points:
        for coordinate3 in coordinates_of_points:
            for coordinate4 in coordinates_of_points:
                list_of_coordinates = [st_end_coordinate, coordinate1, coordinate2,
                                       coordinate3, coordinate4, st_end_coordinate]
                if len(set(list_of_coordinates)) == 5:
                    len_of_way = 0
                    i = 0
                    text = str(st_end_coordinate)
                    while i != len(list_of_coordinates) - 1:
                        len_of_way += ((list_of_coordinates[i][0] - list_of_coordinates[i + 1][0]) ** 2 +
                                       (list_of_coordinates[i][1] - list_of_coordinates[i + 1][1]) ** 2) ** 0.5
                        text += '->{}[{}]'.format(list_of_coordinates[i+1], len_of_way)
                        i += 1
                    if len_shortest_path > len_of_way:
                        len_shortest_path = len_of_way
                        text_result = text
                    list_of_coordinates = []

print(text_result, len_shortest_path, sep='=')


