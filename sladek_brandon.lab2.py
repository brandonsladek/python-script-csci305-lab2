# Import randint method from random module, used by RandomBot class below
from random import randint

# Global variable used by IterativeBot class below
moveNumber = -1

class Element:

    _name = ''

    # Constructor assigns name to created object
    def __init__(self, name=None):
        self._name = name

    def name(self):
        return self._name

    # This method will be implemented in all child classes
    def compareTo(self):
        raise NotImplementedError("Not yet implemented")


class Rock(Element):

    # The "other" parameter is the move to be compared to rock
    def compareTo(self, other):

        # Method will return two strings in a tuple
        string1 = ''
        string2 = ''

        # Assign strings to string variables based on the type of "other"
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

        # Invalid type of "other"
        else:
            return 'INVALID INPUT'
            
        return (string1, string2)


class Paper(Element):

    # The "other" parameter is the move to be compared to paper
    def compareTo(self, other):

        # Method will return two strings in a tuple
        string1 = ''
        string2 = ''

        # Assign strings to string variables based on the type of "other"
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

        # Invalid type of "other"
        else:
            return 'INVALID INPUT'
            
        return (string1, string2)


class Scissors(Element):

    # The "other" parameter is the move to be compared to scissors
    def compareTo(self, other):

        # Method will return two strings in a tuple
        string1 = ''
        string2 = ''

        # Assign strings to string variables based on the type of "other"
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

        # Invalid type of "other"
        else:
            return 'INVALID INPUT'
            
        return (string1, string2)


class Lizard(Element):

    # The "other" parameter is the move to be compared to lizard
    def compareTo(self, other):

        # Method will return two strings in a tuple
        string1 = ''
        string2 = ''

        # Assign strings to string variables based on the type of "other"
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

        # Invalid type of "other"
        else:
            return 'INVALID INPUT'
            
        return (string1, string2)


class Spock(Element):

    # The "other" parameter is the move to be compared to spock
    def compareTo(self, other):

        # Method will return two strings in a tuple
        string1 = ''
        string2 = ''

        # Assign strings to string variables based on the type of "other"
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

        # Invalid type of "other"
        else:
            return 'INVALID INPUT'
            
        return (string1, string2)


class Player:

    _name = ''

    # Constructor assigns name to created object
    def __init__(self, name=None):
        self._name = name

    def name(self):
        return self._name

    # This method will be implemented in all child classes
    def play(self):
        raise NotImplementedError("Not yet implemented")


class StupidBot(Player):

    def play(self):
        # Return rock every time
        return moves[0]


class RandomBot(Player):

    def play(self):
        # Number is to be a random integer between 0 and 4 inclusive
        number = randint(0,4)
        
        play = None
    
        if number == 0:
            # Set play equal to rock
            play = moves[0]
            
        elif number == 1:
            # Set play equal to paper
            play = moves[1]

        elif number == 2:
            # Set play equal to scissors
            play = moves[2]

        elif number == 3:
            # Set play equal to lizard
            play = moves[3]

        else:
            # Set play equal to spock
            play = moves[4]

        return play


class IterativeBot(Player):

    def play(self):
        global moveNumber
        # Increment moveNumber every time play method is called
        moveNumber = moveNumber + 1
        # The moves array only has indices 0-4 inclusive
        moveNumber = moveNumber % 5
        
        return moves[moveNumber]
        

class LastPlayBot(Player):

    play = None

    def play(self):
        for key in lastPlays:
            # Find key for opponent in dictionary
            if key != self.name():
                # If there hasn't been a previous move, return random move
                if lastPlays[key] == None:
                    index = randint(0,4)
                    play = moves[index]
                # lastPlays[key] returns the last move of the opponent
                else:
                    play = lastPlays[key]

        return play


class HumanPlayer(Player):

    play = None
    
    def play(self):
        # User input variable, assign negative number to enter while loop at least once
        choice = -1

        # Display the move options
        print("(1) : Rock")
        print("(2) : Paper")
        print("(3) : Scissors")
        print("(4) : Lizard")
        print("(5) : Spock")

        # Continuously prompt user while input is invalid
        while ((choice is not int) and (choice < 1 or choice > 5)):
            
            # Read in user input
            try:
                choice = int(input("Enter your move: "))
            except ValueError:
                print("That's not an integer!")

            # If user input is invalid
            if choice < 1 or choice > 5:
                print("Invalid move. Please try again.")

        print()
        
        # Subtract 1 from choice since moves array starts at index 0
        play = moves[choice-1]

        return play


class MyBot(Player):

    play = None
    
    def pickRandomMove(self):
        # Number is to be a random integer between 0 and 4 inclusive
        number = randint(0,4)
        
        randomPlay = None
    
        if number == 0:
            # Set play equal to rock
            randomPlay = moves[0]
            
        elif number == 1:
            # Set play equal to paper
            randomPlay = moves[1]

        elif number == 2:
            # Set play equal to scissors
            randomPlay = moves[2]

        elif number == 3:
            # Set play equal to lizard
            randomPlay = moves[3]

        else:
            # Set play equal to spock
            randomPlay = moves[4]

        return randomPlay

    # MyBot play method chooses a random move out of a list of moves that the opponent hasn't used
    def play(self):
        # Pick random move if it is the first round
        if lastPlays[self.name()] == None:
            play = self.pickRandomMove()

        else:
            # If p1PlayList is for player calling method
            if p1PlayList[0] == self.name():
                listSize = len(p1PlayList)
                index = randint(1, listSize-1)
                # Chosen play is chosen randomly from the list of moves the opponent hasn't used
                if p1PlayList[index] is not None:
                    play = p1PlayList[index]
            else:
                listSize = len(p2PlayList)
                index = randint(1, listSize-1)
                if p2PlayList[index] is not None:
                    play = p2PlayList[index]

        return play
    
        
class Main:

    # Welcome the user
    print("\nWelcome to Rock, Paper, Scissors, Lizard, Spock, implemented by Brandon Sladek.")
    
    # Instantiate five possible moves
    rock = Rock('Rock')
    paper = Paper('Paper')
    scissors = Scissors('Scissors')
    lizard = Lizard('Lizard')
    spock = Spock('Spock')

    # Global array to easily return a specific move
    global moves

    # Fill moves array with five possible moves
    moves = [rock, paper, scissors, lizard, spock]

    # Global dictionary to keep track of opponent's last play (for LastPlayBot only)
    global lastPlays

    # lastPlays will contain two entries that get updated every round with each bot's move
    lastPlays = {}

    # Global lists to keep track of each player's move history
    global p1PlayList
    global p2PlayList
    p1PlayList = []
    p2PlayList = []

    anotherGame = 1

    # Repeat while user wants to play another game
    while (anotherGame == 1):

        print("\nNEW GAME\n")

        # Prompt user to pick two players for simulated match
        print("Please choose two players:")
        print("\t(1) HumanPlayer")
        print("\t(2) StupidBot")
        print("\t(3) RandomBot")
        print("\t(4) IterativeBot")
        print("\t(5) LastPlayBot")
        print("\t(6) MyBot")

        print()

        # Set player integers to 0 to initially enter while loop 
        player1 = 0
        player2 = 0

        # Read in user input while input is invalid 
        while ((player1 < 1 or player1 > 6) or (player2 < 1 or player2 > 6)):
            try:
                player1 = int(input("Select player 1: "))
            except ValueError:
                print("That's not an integer!")
            try:
                player2 = int(input("Select player 2: "))
            except ValueError:
                print("That's not an int!")

            if player1 < 1 or player1 > 6:
                print("Invalid choice for player1. Please try again.")
            if player2 < 1 or player2 > 6:
                print("Invalid choice for player2. Please try again.")
            
        # Instantiate player1 bot
        if player1 == 1:
            player1 = HumanPlayer('HumanPlayer')
        elif player1 == 2:
            player1 = StupidBot('StupidBot')
        elif player1 == 3:
            player1 = RandomBot('RandomBot')
        elif player1 == 4:
            player1 = IterativeBot('IterativeBot')
        elif player1 == 5:
            player1 = LastPlayBot('LastPlayBot')
        else:
            player1 = MyBot('MyBot')

        # Instantiate player2 bot, ensure players have different names
        if player2 == 1:
            if player1.name() == "HumanPlayer":
                player2 = HumanPlayer('AnotherHumanPlayer')
            else:
                player2 = HumanPlayer('HumanPlayer')
        elif player2 == 2:
            if player1.name() == "StupidBot":
                player2 = StupidBot('AnotherStupidBot')
            else:
                player2 = StupidBot('StupidBot')
        elif player2 == 3:
            if player1.name() == "RandomBot":
                player2 = RandomBot('AnotherRandomBot')
            else:
                player2 = RandomBot('RandomBot')
        elif player2 == 4:
            if player1.name() == "IterativeBot":
                player2 = IterativeBot('AnotherIterativeBot')
            else:
                player2 = IterativeBot('IterativeBot')
        elif player2 == 5:
            if player1.name() == "LastPlayBot":
                player2 = LastPlayBot('AnotherLastPlayBot')
            else:
                player2 = LastPlayBot('LastPlayBot')
        else:
            if player1.name() == "MyBot":
                player2 = MyBot('AnotherMyBot')
            else:
                player2 = MyBot('MyBot')

        # Update PlayLists with bot name to keep track of which list is for which bot
        p1PlayList.append(player1.name())
        p2PlayList.append(player2.name())

        # Fill lists with all possible moves, will remove moves as opponent calls them
        p1PlayList.extend([moves[0], moves[1], moves[2], moves[3], moves[4]])
        p2PlayList.extend([moves[0], moves[1], moves[2], moves[3], moves[4]])

        print()

        # Update lastPlays dictionary with bot names, bots still haven't made any moves
        lastPlays = {player1.name() : None, player2.name() : None}
        
        # Print player types in match
        print("%s vs %s. Go!" % (player1.name(), player2.name()))
        
        print()

        # Variables to hold player scores
        player1Score = 0
        player2Score = 0

        # Iterate through each of five rounds, printing results each round
        for i in range(5):
            print("Round %d:" % (i+1))

            # Each bot makes a move
            p1move = player1.play()
            p2move = player2.play()

            # Save compareTo tuple to result variable
            try:
                # Check if moves are instances of Element class
                if isinstance(p1move, Element) and isinstance(p2move, Element):
                    result = p1move.compareTo(p2move)
            except AttributeError:
                print("  Attribute Error...")
            
            # Update lastPlays dictionary with each bot's previous move
            lastPlays[player1.name()] = p1move
            lastPlays[player2.name()] = p2move

            # Update PlayLists
            if p2move in p1PlayList:
                # Remove opponent's play from PlayList
                p1PlayList.remove(p2move)

            if p1move in p2PlayList:
                p2PlayList.remove(p1move)

            try:
                # Check if moves are instances of Element class
                if isinstance(p1move, Element) and isinstance(p2move, Element):
                    print("  Player 1 chose",p1move.name())
                    print("  Player 2 chose",p2move.name())
            except AttributeError:
                print("  AttributeError...")
            
            print(" ",result[0])

            # Give point to winner if there is one
            if result[1] == 'Win':
                print("  Player 1 won the round")
                player1Score += 1
            elif result[1] == 'Lose':
                print("  Player 2 won the round")
                player2Score += 1
            else:
                print("  Round was a tie")
                
            print()
        # End of for loop

        # Print the final score of the game
        print("The score is:")
        print("\tPlayer 1: %d\n\tPlayer 2: %d\n" % (player1Score, player2Score))

        # Print the winner of the game
        if player1Score > player2Score:
            print("Player 1 (%s) WON THE GAME!" % (player1.name()))
        elif player1Score < player2Score:
            print("Player 2 (%s) WON THE GAME!" % (player2.name()))
        else:
            print("GAME WAS A DRAW.")

        # Ask user if they want to play another game
        answer = input("\nWould you like to play another game? (yes or no)   ")

        if answer == "no":
            anotherGame = 0

    # Good manners
    print("\nGoodbye.")
        
