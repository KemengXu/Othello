#### Data Structure:       
    * I use tuple to represent the position(x_cordinate, y_cordinate)
    * I use dictionary to represnet the board, which stores the positions, the keys are : "black","white","empty", the values are lists of positions
## There are 4 classes in my design
* class ```Helper```: (In part1 I won't have this class, just put some of these functions in Processing)    
    to simplify pyde code, includes all helper functions:
    1. set_bg_and_line(): setting the background ans lines
    2. mouse_event(): what to do after detecting mousePressed
    3. check_show_results(): check if the game ends, if end, show result
    4. record(): prompt the player's name and store info in scores.txt


* class ```Player```:    
    self.color: "black" or "white"
    1. display() : set color and draw tiles of the color,
        transform the board position into realposition when drawing

    2. check_next_step(): find the best solution for player2(AI),
        which is the solution that can flip the largest number of black tiles
        return the best solution, if there's no legal solution, return None

    3. check_legal_move_exist(): check if there is legal move for player1(human)
        return False if no, True if yes


* class ```Board```:    
    self.size : int, 4 in part1, 8 in part2    
    self.occupy : a dictionary{    
            "black": [],    
            "white": [],    
            "empty": [(i, j)for j in range(size) for i in range(size)]    
        }    
    1. initial_tile(): put the middle 4 tiles, calculate their positions
        append to occupy["black"] and occupy["white"]
        remove from occupy["empty"]
    
    2. is_empty(): check if len(occupy["empty"]) == 0, if yes, return True
                                                        else, False

    3. put_tile(): alter the occupy dictionary with the mouse-clicked positon
        occupy[name].append(pos)
        occupy["empty"].remove(pos)
    
    4. flip(): flip after every put_tile, the input is already legal
        check all tiles around the new tile wheter they should flip
        and call the flip_execute function

    5. execute_flip(): execute the flip in different situatoions

    6. check_who_wins(): check who wins according to the number of tiles
        if self.is_empty() is True:
            if occupy["black"] > occupy["white"], black wins
            elif --------------- == --------------, Tie
            else, white wins
            return the result
    
    7. display(): call p1.display() and p2.display()

    8. is_legal(): decide if the input position is legal
        by checking if there will be at least one flip after the tile
    
    9. directions_generator(): generate a list of all positions around the input position


* class GameController:    
    self.p1 : Player("black")    
    self.p2 : Player("white")    
    self.bd : Board(size)    
    self.p1_turn : True    
    (In hw11, p1_move and p2_move will be put into only one method called update())    
    1. p1_move(): for player1:       
        transfer the real position into board position    
        if the position is legal    
        put_tile and flip tile   
        set the p1_tern to False at the end    
    2. p2_move(): for player2:    
        if there is no auto-genarated(legal) position, check p1    
        if there is also no legal position for player1, end the game    
        if there is, make a move on this position, which is the best position    
    3. check_res(): call bd.check_who_wins() decide whether the game ends
    4. check_p1(): call p1.check_legal_move_exist() check if there is any legal move for player1
#### In Processing: we define 3 functions: set() draw() and mousePressed() and some variables such as the width and hight
### The main flow of my driver is:     
    [check if there is any legal move for p1, if no, set p1_turn flag to be False] ==>>    
    [Get the position in mousePressed()] ==>> [send to GameController by mouse_event() in Helper] ==>>     
    [call p1_move, check if legal and p1_turn is True, if both yes, send to Board, tile and flip and display, set p1_turn False    
    if the position is illegal, do nothing and wait for another mousePressed()] ==>>    
    [if p1_turn is False, send to Player to generate an auto-position, if there exists an auto-position, tile and flip and display      
    if the position is none, check if there is legal move for player1, if no, end the game, if yes, let set p1_turn to be True] ==>>    
    [if the game end, check result, show result and store record, otherwise get back to the beginning of this flow!]    

