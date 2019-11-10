import pygame

from pong import Ball, Player, WIDTH, HEIGHT

def start_game(window):
    player1 = Player(True, 'Player 1')
    player2 = Player(False, 'Player2')
    ball = Ball(1, True)

    shouldRun = True
    while shouldRun:
        pygame.time.delay(200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shouldRun = False

        ball.update_coords([player1.paddle, player2.paddle])
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            player1.paddle.update_coords(1)
        elif keys[pygame.K_DOWN]:
            player1.paddle.update_coords(-1)
        elif keys[pygame.K_LEFT]:
            player2.paddle.update_coords(1)
        elif keys[pygame.K_RIGHT]:
            player2.paddle.update_coords(-1)
        
        window.fill((0,0,0))
        
        player1.paddle.draw(window)
        player2.paddle.draw(window)
        ball.draw(window)

        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
   
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('I am nice at ping pong')
    start_game(win)

    pygame.quit()
