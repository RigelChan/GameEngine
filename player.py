import pygame


class Player:
    
    DIRECT_DICT = {pygame.K_a: (-1, 0), pygame.K_d: ( 1, 0), pygame.K_w: ( 0,-1), pygame.K_s: ( 0, 1)}
    # This direction dictionary lets us map keys to player speed.
    
    SIZE = (100, 100)  # Constant size we don't need to change this; so a class variable is used.
    
    def __init__(self, pos, speed):
        self.image = self.make_image()
        self.rect = self.image.get_rect(center=pos)  # Setting the center of the rect to be the pos parameter.
        # Applying list typecasting allowing us to use 
        # float positions for more precise movement.
        self.true_rect = list(self.rect.center)  # Creating a rect co-ord list.
        self.speed = speed  # Creating a speed attribute.
        
    def make_image(self):
        image = pygame.Surface(Player.SIZE).convert_alpha()  # Creating a player surface.
        image.fill(0,0,0,0)  # Adding transparency under the rect to prevent square looking overlaps.
        rect = image.get_rect()  # Fetching the rect
        pygame.draw.ellipse(image, pygame.Color("black"), rect)  # Drawing an ellipse.
        pygame.draw.ellipse(image, pygame.Color("tomato"), rect.inflate(-12, -12))  # Drawing an ellipse around the other one.
        return image  # Returning the image to the function caller.
    
    def update(self, keys, dt, screen_rect):
        for key in DIRECT_DICT:  # Looping through the keys in the direction dictionary.
            if keys[key]:
                self.true_pos[0] += DIRECT_DICT[key][0]*self.speed*dt
                self.true_pos[1] += DIRECT_DICT[key][1]*self.speed*dt
        self.rect.center = self.true_pos  # Re-setting the position after every frame.
        self.clamp(screen_rect)  # Calling the clamp method.
    
    def clamp(self, screen_rect):
        if not screen_rect.contains(self.rect):
            self.rect.clamp_ip(screen_rect)
            self.true_pos = list(self.rect.center)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)