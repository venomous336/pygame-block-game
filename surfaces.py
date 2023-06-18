import pygame
from math import floor


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((200,200))
        self.image.fill("#0366fc")
        self.rect = self.image.get_rect(midbottom=(300,1000))


    def pressed(self, right_or_left):
        if right_or_left: self.rect.x += 300
        else: self.rect.x -= 100

        if self.rect.x >= 600:
            self.rect.x = 500

        if self.rect.x <= 0:
            self.rect.x = 100

        self.rect = self.image.get_rect(midbottom=(self.rect.x,1000))


    def update(self, right_or_left):
        self.pressed(right_or_left)


class Cone(pygame.sprite.Sprite):
    def __init__(self, location):
        super().__init__()
        if location == "left":
            self.x_pos = 100
        elif location == "middle":
            self.x_pos = 300
        elif location == "right":
            self.x_pos = 500

        # self.image = pygame.Surface((screen_w/3,screen_h/5))
        # self.image.fill("#f28c33") 
        self.image = pygame.Surface((200,200))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(midtop=(self.x_pos,0))

    def move(self):
        self.rect.y += 5

        if self.rect.y > 1000:
            self.kill()

    def update(self):
        self.move()


class Functions:
    def variables():
        screen_w = 600 # /3 = 200
        screen_h = 1000
        screen = pygame.display.set_mode((screen_w, screen_h))
        title = pygame.display.set_caption("escape!")
        start_time = 0
        score = 0
        high_list = []
        mode = "e"

        return screen_w, screen_h, screen, title, start_time, score, high_list, mode

    def display_score(screen, start_time, tnr):
        cur_time = floor((pygame.time.get_ticks() - start_time) / 1000)
        score_surf = tnr.render(f"Score: {cur_time}", False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(300, 50))
        screen.blit(score_surf, score_rect)
        return cur_time

    def collision_sprite(player, cone):
        if pygame.sprite.spritecollide(player.sprite, cone, True):
            return False
        else:
            return True

    def backgrounds(screen_h, screen_w, screen):
        # left lane
        left_surf = pygame.Surface((screen_w/3,screen_h))
        left_surf.fill("#457a99")
        left_rect = left_surf.get_rect(bottomleft=(0,screen_h))
        screen.blit(left_surf,left_rect)

        # middle lane
        mid_surf = pygame.Surface((screen_w/3,screen_h))
        mid_surf.fill("#5a4599")
        mid_rect = left_surf.get_rect(bottomleft=(200,screen_h))
        screen.blit(mid_surf,mid_rect)

        # right lane
        right_surf = pygame.Surface((screen_w/3,screen_h))
        right_surf.fill("#8e4599")
        right_rect = left_surf.get_rect(bottomleft=(400,screen_h))
        screen.blit(right_surf,right_rect)

    def end_surfaces(tnr):
        end_surf = tnr.render("click space to play!", True, "#000000")
        end_rect = end_surf.get_rect(midbottom=(300, 800))

        intro_surf = tnr.render("play to increace your score!", True, "#000000")
        intro_rect = intro_surf.get_rect(midtop=(300,200))

        return end_surf,end_rect,intro_surf,intro_rect

    def high_score(score, high_list, tnr, screen):
        high_list.append(int(score))
        high_surf = tnr.render(f"Your high score is: {max(high_list)}", True, "#000000")
        high_rect = high_surf.get_rect(midbottom=(300, 400))
        screen.blit(high_surf, high_rect)

    def win_surf(tnr, width):
        congratulations_surf = tnr.render("Congratulations you won!", True, "#000000")
        congratulations_rect = congratulations_surf.get_rect(center=(width/2, 800))

        crown_surf = pygame.image.load("python/Practice projects/game/images/crown.png").convert()
        crown_rect = crown_surf.get_rect(center=(width/2,300))

        return False, congratulations_surf, congratulations_rect, crown_surf, crown_rect

    def if_win(score):
        if score >= 45: return True
        else: return False

    def cone_list_finder():
        return ["r", "right", "l","middle", "right", "left", "right", "l", "left", "left", "r", "right", "left", "l","middle", "right", "l","left","r","middle", "left", "right", "r","middle", "left", "middle", "r","right"]




