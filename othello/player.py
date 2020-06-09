class Player:
    def __init__(self, color):
        self.color = color

    def display(self, bd):
        """
        set color and draw tiles of the color
        transform the board position into realposition when drawing
        """
        UNIT = 100
        CENTER = 50
        WIDTH = 90
        if self.color == "black":
            c = 0
        elif self.color == "white":
            c = 1
        fill(c)
        for i in bd.occupy[self.color]:
            ellipse(i[0] * UNIT + CENTER, i[1] * UNIT + CENTER, WIDTH, WIDTH)

    def check_next_step(self, bd, opp_name):
        """
        find the best solution for player2(AI),
        which is the solution that can flip the largest number of black tiles
        return the best solution, if there's no legal solution, return None
        """
        best_point = None
        edge_list = []
        not_edge_list = []
        threshold = 5
        for y in range(bd.size):
            for x in range(bd.size):
                if (x, y) in bd.occupy["empty"]:
                    if bd.is_legal((x, y), self.color, opp_name):
                        length_directions = 8
                        flip_flag = [False] * length_directions
                        checked_direction = []
                        can_flip = 0
                        for i in range(1, bd.size):
                            if len(checked_direction) == length_directions:
                                break
                            d = bd.directions_generator(i, (x, y))
                            curr = []
                            for j in range(len(d)):
                                if j not in checked_direction:
                                    if d[j][0] in range(0, bd.size) and\
                                       d[j][1] in range(0, bd.size):
                                        con1 = d[j] in bd.occupy[self.color]
                                        con2 = d[j] in bd.occupy[self.color]
                                        if d[j] in bd.occupy["empty"]:
                                            checked_direction.append(j)
                                        elif not flip_flag[j] and con1:
                                            checked_direction.append(j)
                                        elif d[j] in bd.occupy[opp_name]:
                                            flip_flag[j] = True
                                        elif flip_flag[j] and con2:
                                            checked_direction.append(j)
                                            x_dist = abs(d[j][0] - x - 1)
                                            y_dist = abs(d[j][1] - y - 1)
                                            can_flip += max(x_dist, y_dist)
                        if self.is_at_edge((x, y), bd.size):
                            edge_list += [((x, y), can_flip)]
                        else:
                            not_edge_list += [((x, y), can_flip)]
        edge_list = sorted(edge_list, key=lambda x: x[1], reverse=True)
        not_edge_list = sorted(not_edge_list, key=lambda x: x[1], reverse=True)
        if len(edge_list) != 0 and len(not_edge_list) != 0:
            if (edge_list[0][1] - not_edge_list[0][1] <= threshold):
                best_point = edge_list[0][0]
            else:
                best_point = not_edge_list[0][0]
        elif len(edge_list) != 0 and len(not_edge_list) == 0:
            best_point = edge_list[0][0]
        elif len(edge_list) == 0 and len(not_edge_list) != 0:
            best_point = not_edge_list[0][0]
        return best_point

    def is_at_edge(self, loc, size):
        """check if the position is at the edge of board"""
        if loc[0] == 0 or loc[0] == size-1 or loc[1] == 0 or loc[1] == size-1:
            return True
        return False

    def check_legal_move_exist(self, bd, opp_name):
        """
        check if there is legal move for player1(human)
        return False if no, True if yes
        """
        for y in range(bd.size):
            for x in range(bd.size):
                if (x, y) in bd.occupy["empty"]:
                    if bd.is_legal((x, y), self.color, opp_name):
                        return True
        return False
