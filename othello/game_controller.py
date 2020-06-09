class GameController:
    def __init__(self, p1, p2, bd, p1_turn=True):
        self.p1 = p1
        self.p2 = p2
        self.bd = bd
        self.p1_turn = p1_turn

    def p1_move(self, pos):
        """
        for player1:
        transfer the real position into board position
        if the position is legal
        put_tile and flip tile
        set the p1_turn to False at the end
        """
        UNIT = 100
        tran_pos = (pos[0]//UNIT, pos[1]//UNIT)
        if(self.p1_turn is True):
            if tran_pos in self.bd.occupy["empty"]:
                # check if the square already has a tile
                if self.bd.is_legal(tran_pos, self.p1.color,
                   self.p2.color) is True:
                    self.bd.put_tile(self.p1.color, tran_pos)
                    self.bd.flip(self.p1.color, tran_pos, self.p2.color)
                    self.bd.display(self.p1, self.p2)
                    print("p2's tern!")
                    self.p1_turn = False

    def p2_move(self):
        """
        for player2:
        if there is no auto-genarated(legal) position, check p1
            if there is also no legal position for player1, end the game
        if there is, make a move on this position, which is the best position
        """
        auto_pos = self.p2.check_next_step(self.bd, self.p1.color)
        if auto_pos is None:
            if self.check_p1() is False:
                self.bd.occupy["empty"] = []
                return
            else:
                print("p1's turn!")
                return
        self.bd.put_tile(self.p2.color, auto_pos)
        self.bd.flip(self.p2.color, auto_pos, self.p1.color)
        self.bd.display(self.p1, self.p2)
        print("p1's turn!")

    def check_res(self, width):
        """decide whether the game ends"""
        res = self.bd.check_who_wins()
        if res is not None:
            return res

    def check_p1(self):
        """check if there is any legal move for player1"""
        possible_pos = self.p1.check_legal_move_exist(self.bd, self.p2.color)
        return possible_pos
