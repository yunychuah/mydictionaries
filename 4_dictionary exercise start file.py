# This program uses a dictionary as a deck of cards.
import random
def main():
    # Create a deck of cards.
    card_deck = create_deck() #contains the dictionary of cards
    #needed to give create_deck a var b/c def create_deck is a value returning function

    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))

    # Deal the cards.
    
    #have to give it two parameters unlike the line 5 create_deck
    #bottom says def deal_cards(deck,number) which means it has to have 2 and not just () like above
    deal_cards(card_deck, num_cards) #dont need to create a variale like in line 5 b/c it def deal_cards is not a value returning function

# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3, 
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck

# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck, number):
    # Initialize an accumulator for the hand value.
    hand_value = 0
    
    # DATA VALIDATION
    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck (52).
    if number > len(deck): #says if number is greater than the length of our dictionary, which is deck rn
        number = len(deck) #set the number to length of deck of cards

    # Deal the cards and accumulate their values.
    #pop item will not work so use alternate solution, print out name of the cards and then value of the cards

    #for card in range(number):
        #card = random.choice(list(deck)) #will create a list for all the keys
        #print(card)
        #value = deck[card]
        #hand_value += value

    for cards in range(number):
        card = random.choice(list(deck))
        print(card)
        hand_value += deck[card]

    # Display the value of the hand.
    print(hand_value)
    
    

# Call the main function.
main()
