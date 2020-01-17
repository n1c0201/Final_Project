import pygame
import time
from enum import IntEnum
import cardImage as ci
from random import *
from button import Button
from deck import Deck

pygame.init()
 
display_width = 1600
display_height = 900

background_image = pygame.image.load(r'C:\Users\Nicholas Arthur\Desktop\python\Final Project\background.jpg')
background_image = pygame.transform.scale(background_image, (1600, 900))

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0, 200, 0)
lightgreen = (0, 255, 0)
lightred = (255, 0, 0)
 
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Blackjack')
clock = pygame.time.Clock()
 
#list of cards in the initial deck, and decks of the player and the player2

player1Cards = []
player2Cards = []
temp_deck = []
full_deck = []

#assigning a card value to an integer value
class Card_value (IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11

#assigning each symbol/suit with a integer value
class Suit (IntEnum):
    SPADES = 0
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3

#defining the cards with a value and a symbol/suit
class Playing_Cards:
    def __init__(self, card_value, card_suit):
        self.value = card_value
        self.suit = card_suit

#making a new full set of cards
def make_deck():
    for suit in Suit:
        for value in Card_value:
            temp_deck.append(Playing_Cards(Card_value(value), Suit(suit)))


#defining a text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#defining a text message display
def message_display(text):
    largeText = pygame.font.Font('impact.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)

def win_screen_p1():
    message_display("Player 1 Wins")
    del player1Cards[:]
    del player2Cards[:]

def win_screen_p2():
    message_display("Player 2 Wins")
    del player1Cards[:]
    del player2Cards[:]

def tie_screen():
    message_display("Tie")
    del player1Cards[:]
    del player2Cards[:]

#screen for the intro screen of the game
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        gameDisplay.blit(background_image,(0,0))
        largeText = pygame.font.Font('impact.ttf',115)
        TextSurf, TextRect = text_objects("Blackjack", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button_deal = Button("Deal", 400, 600, 250, 125, green, lightgreen, main_game)
        button_deal.make_button()

        button_quit = Button("Exit", 950, 600, 250, 125, red, lightred, quit)
        button_quit.make_button()
        pygame.display.update()
        clock.tick(15)

#function for the main game
def main_game():
    make_deck()
    full_deck = Deck(temp_deck)
    full_deck.initial_deal(player1Cards)
    full_deck.initial_deal(player2Cards)
    counterp1 = 2
    counterp2 = 2
    start = True
    xp1 = 550
    yp1 = 400
    w = 250
    h = 125
    xp2 = 850
    yp2 = 400
    gameDisplay.fill(white)

    gameDisplay.blit(background_image,(0,0))
    totalp1 = player1Cards[0].value + player1Cards[1].value
    totalp2 = player2Cards[0].value + player2Cards[1].value
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #displays the image of the cards that were in the initial hand
        for cards in range(2):
            gameDisplay.blit(ci.getCardImage(player1Cards, cards), (650 + (200*cards), (600)))
            gameDisplay.blit(ci.getCardImage(player2Cards, cards), (650 +(200*cards) , 40))
            pygame.display.flip()
        mouse2 = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        #button for dealing a single card to player one or player 2
        if xp1 + w > mouse2[0] > xp1 and yp1 + h > mouse2[1] > yp1:
            pygame.draw.rect(gameDisplay, lightgreen, (xp1, yp1, w, h))
            if click[0] == 1:
                full_deck.deal_card(player1Cards)
                gameDisplay.blit(ci.getCardImage(player1Cards, -1), (650 + 200 * counterp1, 600))
                counterp1 += 1
                totalp1 += player1Cards[-1].value
                pygame.display.update()

        else:
            pygame.draw.rect(gameDisplay, green, (xp1, yp1, w, h))
        

        if xp2 + w > mouse2[0] > xp2 and yp2 + h > mouse2[1] > yp2:
            pygame.draw.rect(gameDisplay, lightgreen, (xp2, yp2, w, h))
            if click[0] == 1:
                full_deck.deal_card(player2Cards)
                gameDisplay.blit(ci.getCardImage(player2Cards, -1), (650 + 200 * counterp2, 40))
                counterp2 += 1
                totalp2 += player2Cards[-1].value

        else:
            pygame.draw.rect(gameDisplay, green, (xp2, yp2, w, h))
        #text for button of Hit P1 and Hit P2
        smallText = pygame.font.SysFont("impact.ttf",50)
        textSurf, textRect = text_objects("Hit P1", smallText)
        textRect.center = ( (xp1+(w/2)), (yp1+(h/2)) )
        gameDisplay.blit(textSurf, textRect)

        textSurf2, textRect2 = text_objects("Hit P2", smallText)
        textRect2.center = ( (xp2+(w/2)), (yp2+(h/2)) )
        gameDisplay.blit(textSurf2, textRect2)
        pygame.display.update()

        #winning conditions
        print(totalp2)
        if totalp1 > 21:
            start = False
            win_screen_p2()
        if totalp2 > 21:
            start = False
            win_screen_p1()
        if totalp1 == 21 and totalp1 == totalp2:
            start = False
            tie_screen()
        pygame.display.flip()

game_intro()