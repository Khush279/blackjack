# Khush Agarwala
# ICS 3UR
# June 18th, 2018
# Blackjack with a betting system

from random import randint
coins = 1000
def cardNew(deck):
    return deck[randint(0,len(deck)-1)]
def cardNumber(card):
    if card[:1] in ('J','Q','K','1'):
        return int(10)
    elif card[:1] in ('2','3','4','5','6','7','8','9'):
        return int(card[:1])
    elif card[:1] == 'A':
        print ("\n"+ str(card))
        num = input("Do you want this to be 1 or 11?\n>")
        while num !='1' or num !='11':
            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)
            else:
                num = input("Do you want this to be 1 or 11?\n>")
def cardExpel(deck,card):
    return deck.remove(card)
def deckTotal():
    cardNumber = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
    deck = []
    card_type = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    for i in card_type:
        for j in cardNumber:
            deck.append(j + ' of ' + i)
    return deck

replay = ''
print ("Welcome to Blackjack, the objective of the game is to beat the dealer by getting a card total as close to 21 as \npossible, without going over 21. King, Queen, and Jack all count as 10, while the other cards maintain their face \nvalue. You can choose whether you would like Ace to be worth 11 or 1 depending on how it suits you. After each\nround of cards flipped, you will be able to hit which means you would take the chance and draw another card, or\nyou can stand which means you can keep your current card value without drawing another card. You will start off\nthe game with 1000 coins and will choose how many you would like to bet each round. for every round you win the\ncoins bet will be added on to your total, and every round you lose the coins bet will be deducted. ")
while replay != 'EXIT':
    if coins == 0:
        print("You currently have no coins, which means you are unable to play Blackjack anymore. Thank you for playing.")
        quit()
    print ("\nYou currently have " + str(coins) + " coins")
    coinsBet = int(input("\nEnter the amount of coins you would like to bet\n"))
    while coinsBet > coins or coinsBet <= 0:
        coinsBet = int(input("Invalid Input!! Enter the amount of coins you would like to bet you currently have " + str(coins) + " coins \n"))
    print("\nYour cards are:")
    deckRefresh = deckTotal()
    card1 = cardNew(deckRefresh)
    cardExpel(deckRefresh,card1)
    card2 = cardNew(deckRefresh)
    cardExpel(deckRefresh,card2)
    print ("\n" + card1 + " and " + card2)
    value1 = cardNumber(card1)
    value2 = cardNumber(card2)
    total = value1 + value2
    print("with a total of " + str(total) )
    dealer_card1 = cardNew(deckRefresh)
    cardExpel(deckRefresh,dealer_card1)
    dealer_card2 = cardNew(deckRefresh)
    cardExpel(deckRefresh,dealer_card2)
    dealer_value1 = cardNumber(dealer_card1)
    dealer_value2 = cardNumber(dealer_card1)
    dealerCards = dealer_value1 + dealer_value2
    print ('\nThe dealer deals one card up and one card face down')
    print ("First a " + dealer_card1 + " and face down card.")
    if total == 21:
        print("Blackjack!")
    else:
        while total < 21:
            answer = input("Would you like to hit or stand? Type hit to hit and stand to stand\n ")
            if answer.lower() == 'hit':
                more_card = cardNew(deckRefresh)
                cardExpel(deckRefresh,more_card)
                more_value = cardNumber(more_card)
                total += int(more_value)
                print (more_card + " for a new total of " + str(total))
                if total > 21:
                    print("You lose!!!")
                    coins = coins - coinsBet
                    print ("You now have " + str(coins) + " coins.")
                    replay = input("Do you want to continue? Enter any key to continue or EXIT to leave\n")
                elif total == 21:
                    print("You win!!!")
                    coins = coins + coinsBet
                    print("You now have " + str(coins) + " coins.")
                    replay = input("Do you want to continue? Enter any key to continue or EXIT to leave\n")
                else:
                    continue
            elif answer.lower() == 'stand':
                print("The dealer's other card is ")
                print("a " + dealer_card2 + " for a total of " + str(dealerCards))
                if dealerCards < 17:
                    print("The dealer hits again.")
                    dealer_more = cardNew(deckRefresh)
                    more_dealer_value = cardNumber(dealer_more)
                    print("The card is a " + str(dealer_more))
                    dealerCards += int(more_dealer_value)
                    if dealerCards > 21 and total <=21:
                        print("The dealer went over 21! You win!")
                        coins = coins + coinsBet
                        print("You now have " + str(coins) + " coins.")
                    elif dealerCards < 21 and dealerCards > total:
                        print("the dealer has " + str(dealerCards) + " You lose.")
                        coins = coins - coinsBet
                        print("You now have " + str(coins) + " coins.")

                    else:
                        continue
                elif dealerCards == total:
                    print("You and the dealer have the same total, there is no winner")
                    print("You still have " + str(coins) + "coins.")
                elif dealerCards < total:
                    print("You win!")
                    coins = coins + coinsBet
                    print("You now have " + str(coins) + " coins.")
                else:
                    print("You Lose!")
                    coins = coins - coinsBet
                    print("You now have " + str(coins) + " coins.")
                replay = input("\nWould you like to continue? Enter any key to continue or EXIT to leave\n")
                break
print("You are walking away with " + str(coins) + " coins. Thank you for playing Blackjack!")