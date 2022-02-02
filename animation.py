import pygame


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False
        self.at_door = False

    def start_animation(self):
        self.animation = True

    def animate(self):
        if self.animation:
            if not self.at_door:
                self.current_image += 1
                if self.current_image == 6:
                    self.image = self.images[self.current_image]
                    self.animation = False
                    self.at_door = True
                else:
                    self.image = self.images[self.current_image]
            elif self.at_door:
                self.current_image -= 1
                if self.current_image == 0:
                    self.image = self.images[self.current_image]
                    self.animation = False
                    self.at_door = False
                else:
                    self.image = self.images[self.current_image]


def load_animation_images(sprite_name):
    images = []
    path = f'assets/{sprite_name}/{sprite_name}'
    for num in range(1, 9):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        print("loaded : " + str(image_path))
    return images


animations = {
    'chambre': load_animation_images('chambre')
}
