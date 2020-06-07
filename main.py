import pygame
import time

pygame.init()

display_width = 600
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)

turn = 'X'

small_text = pygame.font.Font("freesansbold.ttf", 80)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, location, turn, board, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = (x + (w / 2), y + (h / 2))
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        gameDisplay.blit(text_surf, text_rect)
        if click[0] == 1 and location is not None:
            board[location[0]][location[1]] = turn
            if action is not None:
                return True
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    return turn


def play_again_button(msg, x, y, w, h, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = (x + (w / 2), y + (h / 2))
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, w, h))
        gameDisplay.blit(text_surf, text_rect)
        if click[0] == 1:
            pygame.display.update()
            return True

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, w, h))


def buttons(turn, board):
    if board[0][0] is None:
        turn = button(turn, 0, 0, 200, 200, white, white, (0, 0), turn, board, None)
    if board[1][1] is None:
        turn = button(turn, 200, 200, 200, 200, white, white, (1, 1), turn, board, None)
    if board[2][2] is None:
        turn = button(turn, 400, 400, 200, 200, white, white, (2, 2), turn, board, None)
    if board[1][0] is None:
        turn = button(turn, 200, 0, 200, 200, white, white, (1, 0), turn, board, None)
    if board[2][1] is None:
        turn = button(turn, 400, 200, 200, 200, white, white, (2, 1), turn, board, None)
    if board[2][0] is None:
        turn = button(turn, 400, 0, 200, 200, white, white, (2, 0), turn, board, None)
    if board[0][1] is None:
        turn = button(turn, 0, 200, 200, 200, white, white, (0, 1), turn, board, None)
    if board[0][2] is None:
        turn = button(turn, 0, 400, 200, 200, white, white, (0, 2), turn, board, None)
    if board[1][2] is None:
        turn = button(turn, 200, 400, 200, 200, white, white, (1, 2), turn, board, None)
    return turn


def win(board):
    result = None
    for filled in ['X', 'O']:
        if board[0][0] == filled and board[0][1] == filled and board[0][2] == filled:
            result = True
        elif board[1][0] == filled and board[1][1] == filled and board[1][2] == filled:
            result = True
        elif board[2][0] == filled and board[2][1] == filled and board[2][2] == filled:
            result = True
        elif board[0][0] == filled and board[1][0] == filled and board[2][0] == filled:
            result = True
        elif board[0][1] == filled and board[1][1] == filled and board[2][1] == filled:
            result = True
        elif board[0][2] == filled and board[1][2] == filled and board[2][2] == filled:
            result = True
        elif board[0][0] == filled and board[1][1] == filled and board[2][2] == filled:
            result = True
        elif board[0][2] == filled and board[1][1] == filled and board[2][0] == filled:
            result = True
        if result is None:
            result = False
        if result:
            return filled


def cats_eye(board):
    count = 0
    for row in board:
        for item in row:
            if item is not None:
                count += 1
    if count == 9:
        return "catseye"


def game(turn):
    end = False
    board = [[None, None, None], [None, None, None], [None, None, None]]
    gameDisplay.fill(white)
    pygame.draw.line(gameDisplay, black, (200, 0), (200, 600), 5)
    pygame.draw.line(gameDisplay, black, (400, 0), (400, 600), 5)
    pygame.draw.line(gameDisplay, black, (0, 200), (600, 200), 5)
    pygame.draw.line(gameDisplay, black, (0, 400), (600, 400), 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass
        pygame.display.update()
        turn = buttons(turn, board)
        pygame.draw.line(gameDisplay, black, (200, 0), (200, 600), 5)
        pygame.draw.line(gameDisplay, black, (400, 0), (400, 600), 5)
        pygame.draw.line(gameDisplay, black, (0, 200), (600, 200), 5)
        pygame.draw.line(gameDisplay, black, (0, 400), (600, 400), 5)
        clock.tick(20)
        winner = win(board)
        catseye = cats_eye(board)
        if winner == 'X' or winner == 'O':
            print(f"\n{winner} won the game!")
            gameDisplay.fill(white)
            text_surf, text_rect = text_objects(f"{winner} won the game!", pygame.font.Font("freesansbold.ttf", 50))
            text_rect.center = (300, 300)
            gameDisplay.blit(text_surf, text_rect)
            pygame.display.update()
            time.sleep(1)
            break
        elif catseye == "catseye":
            print("\nCatseye!")
            gameDisplay.fill(white)
            text_surf, text_rect = text_objects("Catseye!", pygame.font.Font("freesansbold.ttf", 50))
            text_rect.center = (300, 300)
            gameDisplay.blit(text_surf, text_rect)
            pygame.display.update()
            time.sleep(1)
            break


game('X')
