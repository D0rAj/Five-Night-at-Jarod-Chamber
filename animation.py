import pygame


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, sprite_name2):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.images2 = animations.get(sprite_name2)
        self.animation = False
        self.at_door = False
        self.at_bed = False
        self.go_door = False
        self.go_bed = False

    def start_animation(self, quel):
        if quel == 'porte':
            self.go_door = True
        elif quel == 'lit':
            self.go_bed = True
        self.animation = True

    def animate(self):
        if self.animation:
            if self.go_door:
                if not self.at_bed:
                    if not self.at_door:
                        self.current_image += 1
                        if self.current_image == 6:
                            self.image = self.images[self.current_image]
                            self.go_door = False
                            self.animation = False
                            self.at_door = True
                        else:
                            self.image = self.images[self.current_image]
                    elif self.at_door:
                        self.current_image -= 1
                        if self.current_image == 0:
                            self.image = self.images[self.current_image]
                            self.go_door = False
                            self.animation = False
                            self.at_door = False
                        else:
                            self.image = self.images[self.current_image]
            elif self.go_bed:
                if not self.at_door:
                    if not self.at_bed:
                        self.current_image += 1
                        if self.current_image == 2:
                            self.image = self.images2[self.current_image]
                            self.go_bed = False
                            self.animation = False
                            self.at_bed = True
                        else:
                            self.image = self.images2[self.current_image]
                    elif self.at_bed:
                        self.current_image -= 1
                        if self.current_image == 0:
                            self.image = self.images2[self.current_image]
                            self.go_bed = False
                            self.animation = False
                            self.at_bed = False
                        else:
                            self.image = self.images2[self.current_image]


def load_animation_images(sprite_name, nbr_sprite):
    images = []
    path = f'assets/{sprite_name}/{sprite_name}'
    for num in range(1, nbr_sprite):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        print("loaded : " + str(image_path))
    return images


animations = {
    'chambre': load_animation_images('chambre', 9),
    'lit': load_animation_images('lit', 6)
}
