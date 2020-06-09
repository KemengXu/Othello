import os


class Helper:
    def set_bg_and_line(self, size, width, hight):
        """set the background and lines"""
        G = 0.4
        STROKE = 2
        background(0, G, 0)
        strokeWeight(STROKE)
        for i in range(1, size):
            line(0, i * hight/size, width, i * hight/size)
        for i in range(1, size):
            line(i*width/size, 0, i*width/size, hight)

    def check_show_results(self, gc, width):
        """
        if there are no more legal moves on the board
        get and show the results
        """
        res = gc.check_res(width)
        if res:
            R = 0.85
            G = 0.6
            B = 0
            TEXTSIZE1 = 80
            TEXTSIZE2 = 50
            POSITION1 = 100
            POSITION2 = 150
            fill(R, G, B)
            textSize(TEXTSIZE1)
            text(res[0], width/2, width/2)
            r1 = "p1 has " + str(res[1]) + " tiles"
            r2 = "p2 has " + str(res[2]) + " tiles"
            textSize(TEXTSIZE2)
            text(r1, width/2, width/2 + POSITION1)
            text(r2, width/2, width/2 + POSITION2)
            final = str(max(res[1], res[2]))
            print("Game Over!" + " Winner has " + final + " tiles")
            return res
        return

    def record(self, res):
        """a record of players and scores, highest always on top"""
        answer = self.input('enter your name')
        if answer:
            print('hi ' + answer)
        elif answer == '':
            print('[empty string]')
        else:
            print(answer)  # Canceled dialog will print None
        try:
            f = open("scores.txt", "r+")
        except FileNotFoundError:
            print("Can't find file!")
            exit()
        content = f.read()
        print(content)
        f.seek(0)
        line = f.readline().strip()
        print(line)
        if line == "":
            f.write(str(answer) + " " + str(res[1]) + "\n")
            exit()
            return
        pos = line.rfind(" ")
        curr_max = int(line[pos + 1:])
        if res[1] >= curr_max:
            f.seek(0)
            f.write(str(answer) + " " + str(res[1]) + "\n" + content)
        else:
            f.write(str(answer) + " " + str(res[1]) + "\n")
        exit()

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def mouse_event(self, size, p1, p2, gc, bd):
        """after mouse press, get the real position and make move"""
        TOLERENT = 40
        UNIT = 100
        PLUS = 50
        middle = [UNIT*i + PLUS for i in range(size)]
        for i in middle:
            if abs(mouseX - i) < TOLERENT:
                for j in middle:
                    if abs(mouseY - j) < TOLERENT:
                        gc.p1_move((i, j))
