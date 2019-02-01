import turtle

from dsa.coloring_problem.draw_pen import Pen

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Maze')
wn.setup(700, 700)

neighbour_dict = dict()
color_dict = dict()

all_data = list()

map_colors = ['blue', 'orange', 'red', 'green']

coloring_map = [
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXX"
]


def setup_map(_map):
    for y in range(len(_map[0])):
        for x in range(len(_map)):
            character = _map[x][y]
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            all_data.append(str(x) + ' ' + str(y))
            color_dict.update({str(x) + ' ' + str(y): 'white'})
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()


def find_neighbours(x, y):
    adj_matrix_ = list()

    right_x = x
    right_y = y + 1

    adj_matrix_.append(str(right_x) + ' ' + str(right_y))

    left_x = x
    left_y = y - 1

    adj_matrix_.append(str(left_x) + ' ' + str(left_y))

    up_x = x - 1
    up_y = y

    adj_matrix_.append(str(up_x) + ' ' + str(up_y))

    down_x = x + 1
    down_y = y

    adj_matrix_.append(str(down_x) + ' ' + str(down_y))

    right_up_x = x - 1
    right_up_y = y + 1

    adj_matrix_.append(str(right_up_x) + ' ' + str(right_up_y))

    right_down_x = x + 1
    right_down_y = y + 1

    adj_matrix_.append(str(right_down_x) + ' ' + str(right_down_y))

    left_up_x = x - 1
    left_up_y = y - 1

    adj_matrix_.append(str(left_up_x) + ' ' + str(left_up_y))

    left_down_x = x + 1
    left_down_y = y - 1

    adj_matrix_.append(str(left_down_x) + ' ' + str(left_down_y))

    return adj_matrix_


def color_map():
    for data in all_data:
        neighbour_colors = list()
        temp = data.split(' ')

        x = int(temp[0])
        y = int(temp[1])

        neighbours = find_neighbours(x, y)

        for neighbour in neighbours:
            if neighbour in all_data:
                neighbour_colors.append(color_dict.get(neighbour))

        valid_colors = list(set(map_colors) - set(neighbour_colors))
        color = valid_colors[0]

        color_dict.update({data: color})
        screen_x = -288 + (y * 24)
        screen_y = 288 - (x * 24)
        pen.goto(screen_x, screen_y)
        pen.color(color)
        pen.stamp()


if __name__ == '__main__':

    pen_obj = Pen()
    pen = pen_obj.get_pen()

    setup_map(coloring_map)
    color_map()

    turtle.done()
    while True:
        pass
