class Board:
    def __init__(self, size):
        self.occupy = {
            "black": [],
            "white": [],
            "empty": [(i, j)for j in range(size) for i in range(size)]
        }
        self.size = size

    def initial_tile(self):
        """to put 4 initial tiles in the middle"""
        center = self.size//2
        w1 = (center - 1, center - 1)
        w2 = (center, center)
        b1 = (center - 1, center)
        b2 = (center, center - 1)
        del_set = {w1, w2, b1, b2}
        self.occupy["white"] += [w1, w2]
        self.occupy["black"] += [b1, b2]
        for i in del_set:
            self.occupy["empty"].remove(i)

    def is_empty(self):
        """check if there are spaces for more tiles"""
        if len(self.occupy["empty"]) == 0:
            return True
        return False

    def put_tile(self, name, tran_pos):
        """alter the occupy dictionary with the mouse_clicked positon"""
        self.occupy[name].append(tran_pos)
        self.occupy["empty"].remove(tran_pos)

    def flip(self, name, tran_pos, opp_name):
        """
        flip after every put_tile, the input is already legal
        check all tiles around the new tile wheter they should flip
        and call the flip_execute function
        """
        length_directions = 8
        flip_flag = [False] * length_directions
        checked_direction = []
        can_flip = [0] * length_directions
        for i in range(1, self.size):
            if len(checked_direction) == length_directions:
                break
            d = self.directions_generator(i, tran_pos)
            curr = []
            for j in range(len(d)):
                if j not in checked_direction:
                    if d[j][0] in range(0, self.size) and\
                       d[j][1] in range(0, self.size):         # on board
                        if d[j] in self.occupy["empty"]:
                            checked_direction.append(j)
                        elif not flip_flag[j] and d[j] in self.occupy[name]:
                            checked_direction.append(j)
                        elif d[j] in self.occupy[opp_name]:
                            flip_flag[j] = True
                        elif flip_flag[j] and d[j] in self.occupy[name]:
                            self.execute_flip(d[j], name, tran_pos, opp_name)
                            checked_direction.append(j)
                            can_flip[j] += 1

    def execute_flip(self, curr, name, tran_pos, opp_name):
        """execute the flip in different situatoions"""
        diff_x = curr[0] - tran_pos[0]
        diff_y = curr[1] - tran_pos[1]
        step_x = 0 if diff_x == 0 else int(diff_x / abs(diff_x))
        step_y = 0 if diff_y == 0 else int(diff_y / abs(diff_y))
        if step_x == 0:
            x = curr[0]
            for y in range(tran_pos[1] + step_y, curr[1], step_y):
                self.occupy[name].append((x, y))
                self.occupy[opp_name].remove((x, y))
        elif step_y == 0:
            y = curr[1]
            for x in range(tran_pos[0] + step_x, curr[0], step_x):
                self.occupy[name].append((x, y))
                self.occupy[opp_name].remove((x, y))
        else:
            x = tran_pos[0] + step_x
            y = tran_pos[1] + step_y
            while x != curr[0]:      # should not use for{for}, because
                # we want (0,0) -> (1, 1), not (0, 0)->(0,1)->(1, 0)->(1, 1)
                self.occupy[name].append((x, y))
                self.occupy[opp_name].remove((x, y))
                x += step_x
                y += step_y

    def check_who_wins(self):
        """check who wins according to the number of tiles"""
        res = []
        if self.is_empty() is True:
            r1 = len(self.occupy["black"])
            r2 = len(self.occupy["white"])
            if r1 > r2:
                res.append("You win")
            elif r1 == r2:
                res.append("Tie!!!!!")
            else:
                res.append("AI wins!")
            res += [r1, r2]
            return res
        return

    def display(self, p1, p2):
        """draw tiles on board"""
        p1.display(self)
        p2.display(self)

    def is_legal(self, pos, name, opp_name):
        """
        decide if the input position is legal
        by checking if there will be at least one flip after the tile
        """
        length_directions = 8
        opp_flag = [False] * length_directions
        impossible_direction = set()
        for i in range(1, self.size):
            if len(impossible_direction) == length_directions:
                break
            d = self.directions_generator(i, pos)
            for j in range(length_directions):
                if j not in impossible_direction:
                    if d[j][0] in range(0, self.size) and\
                       d[j][1] in range(0, self.size):
                        if d[j] in self.occupy[name] and opp_flag[j]:
                            return True
                        elif d[j] in self.occupy[name] and not opp_flag[j]:
                            impossible_direction.add(j)
                        elif d[j] in self.occupy["empty"]:
                            impossible_direction.add(j)
                        elif d[j] in self.occupy[opp_name]:
                            opp_flag[j] = True
        return False

    def directions_generator(self, i, pos):
        """generate a list of all positions around the input position"""
        w = (pos[0], pos[1] - i)
        e = (pos[0], pos[1] + i)
        n = (pos[0] - i, pos[1])
        s = (pos[0] + i, pos[1])
        nw = (pos[0] - i, pos[1] - i)
        ne = (pos[0] - i, pos[1] + i)
        sw = (pos[0] + i, pos[1] - i)
        se = (pos[0] + i, pos[1] + i)
        directions = [w, e, n, s, nw, ne, sw, se]
        return directions
