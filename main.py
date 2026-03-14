import pygame


def main():
    print("Hello from pong!")
    
    pygame.init()
    
    
    WIN_SIZE = (420, 250)
    screen = pygame.display.set_mode(WIN_SIZE, flags=pygame.SCALED)
    clock = pygame.time.Clock()
    dt = 0
    running = True

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    
    while running:
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill("purple")

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        #clock.tick(60)  # limits FPS to 60
        
    pygame.quit()

if __name__ == "__main__":
    main()
