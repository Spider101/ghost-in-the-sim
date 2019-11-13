import pygame

class ScoreCard:
    def __init__(self):
        self.scores = [0, 0]
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def draw(self, window):
        win_width, _ = window.get_size()

        score_card = " : ".join(str(score) for score in self.scores)
        score = self.font.render(score_card, True, (255, 255, 255))
        score_container = score.get_rect()
        text_rec_width, text_rec_height = score_container.size
        score_container.center = (win_width - text_rec_width // 2, text_rec_height // 2)

        window.blit(score, score_container)


