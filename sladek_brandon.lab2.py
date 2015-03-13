from random import randint


class Element:

    _name = ''
    
    def __init__(self, name=None):
        self._name = name

    def name(self):
        return self._name

    def compareTo(self):
        raise NotImplementedError("Not yet implemented")


class Rock(Element):

    def compareTo(self, other):
        
        string1 = ''
        string2 = ''

        if type(other) is Rock:
            string1 = 'Rock equals Rock'
            string2 = 'Tie'

        elif type(other) is Paper:
            string1 = 'Paper covers Rock'
            string2 = 'Lose'
            
        elif type(other) is Scissors:
            string1 = 'Rock crushes Scissors'
            string2 = 'Win'
 
        elif type(other) is Lizard:
            string1 = 'Rock crushes Lizard'
            string2 = 'Win' 
            
        elif type(other) is Spock:
            string1 = 'Spock vaporizes Rock'
            string2 = 'Lose'

        else:
            return 'INVALID INPUT'
            
        return (string1, string2)


class Paper(Element):

    def compareTo(self, other):
        
        string1 = ''
        string2 = ''

        if type(other) is Rock:
            string1 = 'Paper covers Rock'
            string2 = 'Win'

        elif type(other) is Paper:
            string1 = 'Paper equals Paper'
            string2 = 'Tie'
            
        elif type(other) is Scissors:
            string1 = 'Scissors cut Paper'
            string2 = 'Lose'
 
        elif type(other) is Lizard:
            string1 = 'Lizard eats Paper'
            string2 = 'Lose' 
            
        elif type(other) is Spock:
            string1 = 'Paper disproves Spock'
            string2 = 'Win'

        else:
            return 'INVALID INPUT'
            
        return (string1, string2)


class Scissors(Element):

    def compareTo(self, other):
        
        string1 = ''
        string2 = ''

        if type(other) is Rock:
            string1 = 'Rock crushes Scissors'
            string2 = 'Lose'

        elif type(other) is Paper:
            string1 = 'Scissors cut Paper'
            string2 = 'Win'
            
        elif type(other) is Scissors:
            string1 = 'Scissors equal Scissors'
            string2 = 'Tie'
 
        elif type(other) is Lizard:
            string1 = 'Scissors decapitate Lizard'
            string2 = 'Win' 
            
        elif type(other) is Spock:
            string1 = 'Spock smashes Scissors'
            string2 = 'Lose'

        else:
            return 'INVALID INPUT'
            
        return (string1, string2)


class Lizard(Element):

    def compareTo(self, other):
        
        string1 = ''
        string2 = ''

        if type(other) is Rock:
            string1 = 'Rock crushes Lizard'
            string2 = 'Lose'

        elif type(other) is Paper:
            string1 = 'Lizard eats Paper'
            string2 = 'Win'
            
        elif type(other) is Scissors:
            string1 = 'Scissors decapitate Lizard'
            string2 = 'Lose'
 
        elif type(other) is Lizard:
            string1 = 'Lizard equals Lizard'
            string2 = 'Tie' 
            
        elif type(other) is Spock:
            string1 = 'Lizard poisons Spock'
            string2 = 'Win'

        else:
            return 'INVALID INPUT'
            
        return (string1, string2)


class Spock(Element):

    def compareTo(self, other):
        
        string1 = ''
        string2 = ''

        if type(other) is Rock:
            string1 = 'Spock vaporizes Rock'
            string2 = 'Win'

        elif type(other) is Paper:
            string1 = 'Paper disproves Spock'
            string2 = 'Lose'
            
        elif type(other) is Scissors:
            string1 = 'Spock smashes Scissors'
            string2 = 'Win'
 
        elif type(other) is Lizard:
            string1 = 'Lizard poisons Spock'
            string2 = 'Lose' 
            
        elif type(other) is Spock:
            string1 = 'Spock equals Spock'
            string2 = 'Tie'

        else:
            return 'INVALID INPUT'
            
        return (string1, string2)


class Player:

    _name = ''
    
    def __init__(self, name=None):
        self._name = name

    def name(self):
        return self._name

    def play(self):
        raise NotImplementedError("Not yet implemented")


class StupidBot(Player):

    def play(self):
        return moves[0]


class RandomBot(Player):

    def play(self):
        number = randint(0,4)
        play = None
    
        if number == 0:
            play = moves[0]
            
        elif number == 1:
            play = moves[1]

        elif number == 2:
            play = moves[2]

        elif number == 3:
            play = moves[3]

        else:
            play = moves[4]

        return play


class IterativeBot(Player):

    moveNumber = -1
    
    def play(self):
        global moveNumber
        moveNumber = moveNumber + 1
        moveNumber = moveNumber % 5
        return moves[moveNumber]
        

class LastPlayBot(Player):
    pass


class HumanPlayer(Player):

    def play(self):
        
        choice = -1

        print("(1) : Rock")
        print("(2) : Paper")
        print("(3) : Scissors")
        print("(4) : Lizard")
        print("(5) : Spock")
            
        while (choice < 1 or choice > 5):
            
            choice = int(input("Enter your move: "))

            if choice < 1 or choice > 5:
                print("Invalid move. Please try again.")
        
        return moves[choice-1]


class MyBot(Player):
    pass


class Main:

    global moves

    rock = Rock('Rock')
    paper = Paper('Paper')
    scissors = Scissors('Scissors')
    lizard = Lizard('Lizard')
    spock = Spock('Spock')

    moves = [rock, paper, scissors, lizard, spock]

    p1 = HumanPlayer('HumanPlayer')
    p2 = HumanPlayer('AnotherHumanPlayer')
    p1move = p1.play()
    p2move = p1.play()
    print(p1move.compareTo(p2move))
    
