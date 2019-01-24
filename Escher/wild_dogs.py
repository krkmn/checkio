def wild_dogs(coords):
    # replace this for solution
    numOfDogs = len(coords)

    catch_distance = []

    for i in range(numOfDogs):
        for j in range(i + 1, numOfDogs):
            y1 = coords[i][1]
            y2 = coords[j][1]
            x1 = coords[i][0]
            x2 = coords[j][0]

            if (x1 == x2):
                catches = [x[0] == x1 for x in coords].count(True)
                distance = x1
                catch_distance.append((catches, distance))
                continue

            if (y1 == y2):
                catches = [y[1] == y1 for y in coords].count(True)
                distance = y1
                catch_distance.append((catches, distance))
                continue

            k = (y2 - y1) / (x2 - x1)
            m = -x2 * k + y2

            line_equation = lambda x: k * x + m

            catches = [line_equation(i[0]) == i[1] for i in coords].count(True)

            ##cross line : y = t*x, t = -1/k
            ##cross_x = m/(t-k)
            ##cross_y = t*cross_x
            ##distance = cross_x**2+cross_y**2)**0.5

            t = -1 / k
            cross_x = m / (t - k)
            cross_y = t * cross_x
            distance = (cross_x ** 2 + cross_y ** 2) ** 0.5

            catch_distance.append((catches, distance))

if __name__ == '__main__':
    print("Example:")
    print(wild_dogs([(7, 122), (8, 139), (9, 156),
                     (10, 173), (11, 190), (-100, 1)]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156),
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
