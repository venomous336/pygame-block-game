import pygame
from surfaces import Player, Cone
from surfaces import Functions
from random import choice # choice only needed if I use random cone spawns


# everything will happen in the main function
def main():
    pygame.init()

    # defining some variables
    screen_w, screen_h, screen, title, start_time, score, high_list, mode = Functions.variables()
    
    if mode == "e":
        timer = 1800
    elif mode == "m":
        timer = 1650
    elif mode == "h":
        timer = 1500

    cone_list = Functions.cone_list_finder()

    cone_index = -1
    current_list = cone_list

    # font
    tnr = pygame.font.Font("python/Practice projects/game/tnr/times new roman.ttf", 50)

    # death screen text
    end_surf,end_rect,intro_surf,intro_rect = Functions.end_surfaces(tnr)

    # win surfaces
    win, congratulations_surf, congratulations_rect, crown_surf, crown_rect = Functions.win_surf(tnr, screen_w)
    
    # groups
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    cone_group = pygame.sprite.Group()

    # timers
    clock = pygame.time.Clock()

    cone_timer = pygame.USEREVENT
    pygame.time.set_timer(cone_timer, timer)

    run = True
    game_active = False
    while run:
        # event loop
        for event in pygame.event.get():
            # exit
            if event.type == pygame.QUIT:
                run = False

            if game_active:
                # if game active timer for spawning cones
                if event.type == cone_timer:

                    cone_index += 1

                    if cone_index >= len(current_list):
                        cone_index = 0

                    if current_list[cone_index] in ['r', 'l']:
                        if current_list[(cone_index + 1) % len(current_list)] == 'left' or current_list[(cone_index + 1) % len(current_list)] == 'right':
                            sec_index = 'middle'
                        elif current_list[(cone_index + 1) % len(current_list)] == 'middle':
                            if current_list[cone_index] == 'r':
                                sec_index = 'right'
                            elif current_list[cone_index] == 'l':
                                sec_index = 'left'

                        cone_index += 1
                        
                    else:
                        sec_index = ""

                    if sec_index:
                        cone_group.add(Cone(sec_index))

                    print(current_list[cone_index])
                    cone_group.add(Cone(current_list[cone_index]))

                # if game is active key presses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player.update(True)
                    
                    if event.key == pygame.K_LEFT:
                        player.update(False)
            
            # if game is inactive key presses
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                    game_active = True
                    win = False
                    start_time = pygame.time.get_ticks()


        if game_active:

            # display background
            Functions.backgrounds(screen_h, screen_w, screen)

            # display objects
            player.draw(screen)
            cone_group.draw(screen)

            # move cone 
            cone_group.update()

            # display score
            score = Functions.display_score(screen, start_time, tnr)

            # collision
            game_active = Functions.collision_sprite(player, cone_group)

            # check if win
            if Functions.if_win(score):
                win = True
                game_active = False
        
        # end screen
        else:
            if win:
                screen.fill("#FFFFFF")
                screen.blit(congratulations_surf,congratulations_rect)
                screen.blit(crown_surf,crown_rect)
                cone_group.empty()

            else:
                screen.fill("#6342f5")

                # clears cones when dead
                cone_group.empty()

                # click space to play text
                screen.blit(end_surf,end_rect)
                
                # display high score
                Functions.high_score(score, high_list, tnr, screen)

                # restart from the beginning of the loop
                current_list = cone_list
                cone_index = -1

                # end score display
                end_score_surf = tnr.render(f"Your score is: {score}!", True, "#000000")
                end_score_rect = end_score_surf.get_rect(midbottom=(screen_w/2, 200))
                screen.blit(end_score_surf, end_score_rect)

                # display intro text
                if score == 0: screen.blit(intro_surf, intro_rect)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

# out of loop
pygame.quit()