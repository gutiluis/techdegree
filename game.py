from cards import Card
import random # use different patterns every time. for the method called set_cards


class Game:
    def __init__(self):
        # size 4. need 4 column names. grid is 4x4
        self.size = 4
        # show grid
        # size 4. 4 column names. 8 types of cards. each used 2 twice
        self.card_options = ['Add', 'Boo', 'Cat', 'Dev',
                             'Egg', 'Far', 'Gum', 'Hut']
        self.columns = ['A', 'B', 'C', 'D'] # 4 columns
        # create empty list to hold card instances
        self.cards = []
        # grid locations
        self.locations = []
        # loop through columns rows to create all the possible locations in the grid. to add to the list
        # for loop to loop through each column
        for column in self.columns:
            # loop through a range from 1 to 4
            # range start stop step parameters
            # for num in starting at 1. ends in 5. 5 is the self.size of our grid plus 1
            for num in range(1, self.size + 1):
                self.locations.append(f"{column}{num}") # missing instance. 
                # has words and locations
            # missing putting together using the cards. using import card
            
# no more arguments. only self
    def set_cards(self):
        # when giving a card a random location. do not use the same location again
        used_locations = []
        # create cards by looping through card_options. create cards for each word
        for word in self.card_options:
        # need to loop 2 cards for every word. 16 cards
        # the placeholder is not really needed
        # missing logic to grab a location and create and append our card
            for i in range(2): # ready to set up to grab a card and then do something twice
        # data type. or structure to remove duplicates. sets
        # convert 2 lists, locations and used_locations, into sets and subtract. ending with locations that haven't been used
        # 
                available_locations = set(self.locations) - set(used_locations)
                # convert back into a list. to use random on it
                # this works because subtracting the sets removes the duplicates. only available locations are left
                random_location = random.choice(list(available_locations))
                # randomly choose one location
                used_locations.append(random_location)
                # create card instance. pass in the word and its location.
                # append 
                card = Card(word, random_location)
                self.cards.append(card)

# find all the cards given in the given row. add spaces or the word
# in order to create the grid. create the rows
    def create_row(self, num): # pass the row number to know which row to create
# find all the cards with one in their location
# either cards if they have been guessed or empty spaces
        row = []
        # loop through the columns so we can find the matching locations for the row
        for column in self.columns:
            # loop through the cards
            for card in self.cards:
                # find the ones that are located in this row
                # where is the card object showing the attributes. it has attributes
                if card.location == f'{column}{num}': # current column and row number
        # check for matches
                    if card.matched:
                # append the word to the row
                        row.append(str(card)) # string of the card. making sure word gets appended
                        # append empty spaces the same size as the word
                    else: # 3 spaces
                        row.append('   ') # spaces keep grid nice and neat
             # return row
        return row
            
        
# create grid method. create the header. use the row method to create all 4 rows and print them out to the console
# use the create row to create the grid in the console
    def create_grid(self):
        # print the header
        # create a template using comments to show what this will look like
        # |  A  |  B  |  C  |  D  |
        # use join to print our the header with spaces
        # print pipes in between each header
        # leave a space for the row number
        # add all columns with pipeline and join
        # columns are single letter
        header = ' |  ' + '  |  '.join(self.columns) + '  |'# column names are a single letter while words 3
        # the header is the beginning of the game grid
        print(header) # create the rows by looping through a range
        # start at one and end at four
        for row in range(1, self.size + 1):
        # make a print_row variable
        # this row will be printed to the console
        # start the row with the row number
            print_row = f'{row}| '
        # call the row method and pass in the row we're currently on
            get_row = self.create_row(row)
        # add to the print_row variable. jand oin all the words or spaces
            print_row += ' | '.join(get_row) + ' |'
            print(print_row)
        
        
        # location guesses the player will input
        # check if two given locations have mathing cards
    def check_match(self, loc1, loc2): # 2 locations
    # empty list to hold 2 cards to loop through the cards to find the two that match the given locations
        cards = []
        for card in self.cards:
            if card.location == loc1 or card.location == loc2:
          # when the cards have been found that match the locations
          # append the match to the list
                cards.append(card)
        if cards[0] == cards[1]:
        # set the matched attribute to True and return True
            cards[0].matched = True
            cards[1].matched = True
            return True # return a false positive if no match of card and location
        else:
            for card in cards:
                print(f'{card.location}: {card}')
            return False
          
    def check_win(self):
        # loop through all cards
        for card in self.cards: # if cards match. attribute is false
            if card.matched == False:
            # return False. there's one card who's matched attribute. otherwise return True    
                return False    
        return True
          
        # tackle player input to make sure it's a correct location
    def check_location(self, time): # time argument. to know if this is the first or second guess
        # prompt for a location guess
        while True: # prompt until they provide one that exists in the grid
            # get input and use the time. let the player know what guess this is
            guess = input(f"What's the location of your {time} card? ")
            # check if the guess is in the location
            # return the check if it is a location
            if guess.upper() in self.locations: # make sure to get the match
                return guess.upper()
            else:
                print("That's not a valid location. It should look like this: A1") # if no match. let the player know their guess isn't valid
        
        
    def start_game(self):
        game_running = True
        # print game header
        print("Memory Game")
        # create the cards by calling the set_cards method
        self.set_cards()
        # create the while loop using game_running
        while game_running:
            # print the grid for the player they can guess
            self.create_grid()
                # ask for the guess. and pass first
            # this 2 lines of code will give matches
            guess1 = self.check_location("first")
            guess2 = self.check_location("second")
            if self.check_match(guess1, guess2):
            # if match. print-show result won game
                if self.check_win():
                    print("Congrats!! You have guessed them all!")
                    # print the grid 
                    self.create_grid()
                    # stop the while loop if they weren't a match
            # game running to False since the game is over
                    game_running = False
            else:
                    # if no match. let the player know
                    # use input to give a change to the player and see what the cards were
                    # before the grid is printed again
                input("Those cards are not a match. Press enter to continue")
                    # end of while loop. only when game_running has been set to False
        print("GAME OVER")
            
            
        # check for a win
        # make sure the player’s location input is a real 
        # run the game

if __name__ == "__main__":
    game = Game() # instance attributes
    game.start_game()
    game.set_cards() # create cards
    # print the words inside the grid
    game.cards[0].matched = True # grab first few cards in the list. switch their matched attribute to true
    game.cards[1].matched = True
    game.cards[2].matched = True
    game.cards[3].matched = True
    #print(game.create_row(1)) # call the create_row each row. the create_row is the third
    #print(game.create_row(2))
    #print(game.create_row(3))
    #print(game.create_row(4))
    game.create_grid()
    # see all cards
    #for card in game.cards:
        #print(card)