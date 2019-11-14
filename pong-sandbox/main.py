import pygame

from pong import Pong

def start_game(window, game):

    move_up, move_down = -1, 1
    shouldRun = True
    while shouldRun:
        pygame.time.delay(200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shouldRun = False

        game.update_ball_coords()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            game.update_player_coords(game.player1, move_up)
        elif keys[pygame.K_DOWN]:
            game.update_player_coords(game.player1, move_down)
        elif keys[pygame.K_LEFT]:
            game.update_player_coords(game.player2, move_up)
        elif keys[pygame.K_RIGHT]:
            game.update_player_coords(game.player2, move_down)
        
        window.fill((0,0,0))
        
        game.draw(window)
        #  player1.paddle.draw(window)
        #  player2.paddle.draw(window)
        #  ball.draw(window)

        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
   
    pong = Pong(['Player 1', 'Player 2'])

    win = pygame.display.set_mode(tuple(pong.screen_dims))
    pygame.display.set_caption('I am nice at ping pong')
    start_game(win, pong)

    pygame.quit()
