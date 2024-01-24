import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
import pygame, sys, os, random, time

pygame.init()
# задаем размер экрана, заголовок и задний фон
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Menu')
BG = pygame.image.load('BG.jpg')
first_level_bg = pygame.image.load('first.jpg')
second_level_bg = pygame.image.load('second.jpg')
white = (255, 255, 255)
wall_list = pygame.sprite.Group()
PLAYER = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def roll_dice():
    dice_roll = random.randint(1, 6)
    print(f"Player rolled {dice_roll}")
    return dice_roll


def roll_dice_monster():
    dice_roll1 = random.randint(1, 6)
    print(f"Monster rolled {dice_roll1}")
    return dice_roll1


def battle_window():
    battle_screen = pygame.display.set_mode((800, 600))

    square_color = (0, 0, 0)

    battle_button_rect = pygame.Rect(450, 480, 207, 30)

    nobattle_button_rect = pygame.Rect(120, 480, 207, 30)

    font = pygame.font.Font(None, 36)
    button_text = font.render('бросить кости', True, (0, 0, 0))
    button_text2 = font.render('не бросать кости', True, (0, 0, 0))

    monster_images = [load_image('monster_walk.png'),
                      load_image('monster_walk1.png'),
                      load_image('monster_walk2.png'),
                      load_image('monster_walk3.png'),
                      load_image('monster_walk4.png'),
                      load_image('monster_walk5.png'), ]

    current_image = 0

    monster_total = 0

    x = 350
    y = 75

    speed = 1
    monser_win = False
    player_win = False
    flag = True
    attempts = 1
    player_total = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quiet")
                pygame.quit()
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (battle_button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]
                        and attempts <= 2 and flag):
                    battle_screen.fill((0, 0, 0))
                    dice_roll = roll_dice()
                    dice_roll_monster = roll_dice_monster()
                    font = pygame.font.Font(None, 36)

                    text = font.render("Игрок выбил {}".format(dice_roll), 1, (255, 255, 255))
                    battle_screen.blit(text, (500, 250))
                    player_total = dice_roll
                    print(attempts)
                    if monster_total <= player_total or attempts == 1:
                        text = font.render("Монстр выбил {}".format(dice_roll_monster), 1, (255, 255, 255))
                        battle_screen.blit(text, (100, 250))
                        monster_total = dice_roll_monster
                        print(attempts)
                    else:
                        text = font.render("Монстр решил не бросать кубики", 1, (255, 255, 255))
                        battle_screen.blit(text, (50, 250))
                    attempts += 1
                    player_total_text = font.render("Результат игрока {}".format(player_total), 1, (255, 255, 255))
                    battle_screen.blit(player_total_text, (500, 300))
                    monster_total_text = font.render("Результат монстра {}".format(monster_total), 1, (255, 255, 255))
                    battle_screen.blit(monster_total_text, (100, 300))
                if (nobattle_button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]
                        and player_total != 0 or attempts == 3):
                    if monster_total <= player_total and attempts < 3:
                        dice_roll_monster = roll_dice_monster()
                        try:
                            pygame.draw.rect(screen, square_color, pygame.Rect((50, 250), (300, 100)))
                            text = font.render("Монстр выбил {}".format(dice_roll_monster), 1, (255, 255, 255))
                        except:
                            pass
                        battle_screen.blit(text, (100, 250))
                        monster_total = dice_roll_monster
                        monster_total_text = font.render("Результат монстра {}".format(monster_total), 1,
                                                         (255, 255, 255))
                        battle_screen.blit(monster_total_text, (100, 300))



                    if monster_total > player_total:
                        monster_winner_text = font.render("Монстр победил", 1,
                                                          (255, 255, 255))
                        battle_screen.blit(monster_winner_text, (300, 375))
                        monser_win = True
                    elif player_total > monster_total:
                        player_winner_text = font.render("Игрок победил", 1,
                                                         (255, 255, 255))
                        battle_screen.blit(player_winner_text, (300, 375))
                        player_win = True
                    else:
                        nichia = font.render("Победителя нет", 1,
                                             (255, 255, 255))
                        battle_screen.blit(nichia, (300, 375))
                        player_win = True
                    flag = False


                    attempts += 1
        new_width, new_height = 100, 150
        raboty = 1
        try:
            if raboty == 1:
                resized_monster_image = pygame.transform.smoothscale(monster_images[current_image], (new_width, new_height))
                screen.blit(resized_monster_image.convert_alpha(), (x, y))
        except:
            pass

        current_image += 1
        if current_image >= len(monster_images):
            current_image = 0


        time.sleep(0.1)
        try:
            pygame.draw.rect(battle_screen, (255, 255, 255), battle_button_rect)
            battle_screen.blit(button_text, (466, 480))
        except:
            pass
        try:
            pygame.draw.rect(battle_screen, (255, 255, 255), nobattle_button_rect)
            battle_screen.blit(button_text2, (120, 480))
        except:
            pass
        winner_battle = pygame.Rect(300, 430, 217, 30)
        winner_text = font.render('продолжить игру', True, (0, 0, 0))
        if monser_win:
            pygame.draw.rect(battle_screen, (255, 255, 255), winner_battle)
            battle_screen.blit(winner_text, (300, 430))
            if (winner_battle.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]):
                return False
        elif player_win:
            pygame.draw.rect(battle_screen, (255, 255, 255), winner_battle)
            battle_screen.blit(winner_text, (300, 430))
            if (winner_battle.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]):
                return True
        pygame.display.flip()


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect(center=(x, y))
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.enemyes = pygame.sprite.Group()


class Treasure(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([10, 10])  # размер сокровища
        self.image.fill(white)  # цвет сокровища

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load('monsrtrtr.png')
        self.index = 0

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, weight, height):
        super().__init__()

        self.image = pygame.Surface([weight, height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# используем файл, в котором записаны нужные нам цвета и шрифты
def get_font(size):
    return pygame.font.Font("font.ttf", size)


# экран, где пользователь выбирает уровень
def play():
    pygame.display.set_caption('Play')

    while True:
        SCREEN.fill('black')

        # задаем новый заголовок
        play_mouse_pos = pygame.mouse.get_pos()
        play_text = get_font(100).render('CHOOSE LEVEL', True, '#b68f40')
        play_rect = play_text.get_rect(center=(640, 100))

        # создаем новые кнопки
        first_button = Button(image=pygame.image.load('rect.png'), pos=(640, 340),
                              text_input='FIRST LEVEL', font=get_font(40), base_color='#d7fcd4', hovering_color='White')
        second_button = Button(image=pygame.image.load('rect.png'), pos=(640, 540),
                               text_input='SECOND LEVEL', font=get_font(40), base_color='#d7fcd4',
                               hovering_color='White')

        SCREEN.blit(play_text, play_rect)
        for button in [first_button, second_button]:
            button.change_color(play_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_button.check_for_input(play_mouse_pos):
                    first_level()
                elif second_button.check_for_input(play_mouse_pos):
                    second_level()

        pygame.display.update()


def first_level():
    pygame.display.set_caption('First level')
    wall_list = pygame.sprite.Group()
    PLAYER = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    monser_list = pygame.sprite.Group()

    wall_coord = [
        [0, 0, 10, 720],
        [10, 0, 1270, 10],
        [1270, 10, 10, 710],
        [10, 710, 1270, 10],
        [10, 110, 768, 10],
        [878, 10, 10, 240],
        [248, 250, 640, 10],
        [110, 220, 10, 350],
        [10, 570, 110, 10],
        [238, 250, 10, 350],
        [420, 360, 10, 350],
        [430, 360, 530, 10],
        [520, 460, 10, 250],
        [530, 460, 530, 10],
        [1050, 92, 10, 378],
        [1200, 92, 10, 478],
        [770, 570, 500, 10]
    ]
    for coord in wall_coord:
        wall = Wall(coord[0], coord[1], coord[2], coord[3])
        wall_list.add(wall)
        all_sprites.add(wall)

    player = Player(50, 50, 'yodo.png')
    PLAYER.add(player)
    all_sprites.add(player)
    player.walls = wall_list
    clock = pygame.time.Clock()
    fps = 60
    speed = 3
    running = True

    for _ in range(5):
        monster = Monster(random.randint(10, 1260), random.randint(10, 710))
        while pygame.sprite.spritecollideany(monster, wall_list) or any(
                pygame.sprite.collide_rect(monster, m) for m in all_sprites if isinstance(m, Monster)):
            monster.rect.x = random.randint(10, 1260)
            monster.rect.y = random.randint(10, 710)
        monser_list.add(monster)
        all_sprites.add(monster)

    while running:
        SCREEN.blit(first_level_bg, (0, 0))
        SCREEN.blit(player.image, player.rect)
        all_sprites.draw(SCREEN)
        pygame.display.update()
        monser_battle = pygame.sprite.spritecollide(player, monser_list, True)
        if monser_battle:
            battle_window()
            pygame.display.set_mode((1200, 1700))
            continue
        # bloock_hit_list = pygame.sprite.spritecollide(player, wall_list, False)
        # if bloock_hit_list:
        #    running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rect.x -= speed
            if player.rect.x < 0:
                player.rect.x = 0
        elif keys[pygame.K_RIGHT]:
            player.rect.x += speed
            if player.rect.x > 1260:
                player.rect.x = 1260
        elif keys[pygame.K_DOWN]:
            player.rect.y += speed
            if player.rect.y > 710:
                player.rect.y = 710
        elif keys[pygame.K_UP]:
            player.rect.y -= speed
            if player.rect.y < 0:
                player.rect = 10

        clock.tick(fps)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def second_level():
    pygame.display.set_caption('Second level')
    wall_coord = [
        [0, 0, 10, 720],
        [10, 0, 1270, 10],
        [1270, 10, 10, 710],
        [10, 710, 1270, 10],
        [60, 80, 10, 210],
        [70, 110, 378, 10],
        [448, 60, 10, 60],
        [458, 60, 150, 10],
        [608, 60, 10, 200],
        [70, 170, 428, 10],
        [498, 120, 10, 60],
        [508, 120, 50, 10],
        [670, 10, 10, 300],
        [120, 310, 560, 10],
        [760, 60, 10, 310],
        [850, 60, 10, 310],
        [770, 60, 420, 10],
        [1190, 60, 10, 310],
        [1020, 360, 170, 10],
        [950, 150, 10, 450],
        [150, 450, 1160, 10],
        [60, 450, 10, 190],
        [70, 545, 350, 10],
        [420, 545, 10, 165],
        [770, 650, 10, 60],
        [770, 640, 400, 10],
        [1170, 640, 10, 70]
    ]
    for coord in wall_coord:
        wall = Wall(coord[0], coord[1], coord[2], coord[3])
        wall_list.add(wall)
        all_sprites.add(wall)

    player = Player(35, 40, 'yodo.png')
    player.walls = wall_list
    PLAYER.add(player)
    all_sprites.add(player)
    player.walls = wall_list
    clock = pygame.time.Clock()
    fps = 60
    speed = 3
    running = True
    for _ in range(5):
        monster = Monster(random.randint(10, 1260), random.randint(10, 710))
        while pygame.sprite.spritecollideany(monster, wall_list) or any(
                pygame.sprite.collide_rect(monster, m) for m in all_sprites if isinstance(m, Monster)):
            monster.rect.x = random.randint(10, 1260)
            monster.rect.y = random.randint(10, 710)
        all_sprites.add(monster)
    while running:
        SCREEN.blit(second_level_bg, (0, 0))
        SCREEN.blit(player.image, player.rect)
        all_sprites.draw(SCREEN)
        pygame.display.update()
        player.walls = wall_list
        bloock_hit_list = pygame.sprite.spritecollide(player, wall_list, False)
        if bloock_hit_list:
            running = False
        clock = pygame.time.Clock()
        fps = 60
        speed = 3

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rect.x -= speed
            if player.rect.x < 0:
                player.rect.x = 0
        elif keys[pygame.K_RIGHT]:
            player.rect.x += speed
            if player.rect.x > 1260:
                player.rect.x = 1260
        elif keys[pygame.K_DOWN]:
            player.rect.y += speed
            if player.rect.y > 710:
                player.rect.y = 710
        elif keys[pygame.K_UP]:
            player.rect.y -= speed
            if player.rect.y < 0:
                player.rect = 10
        clock.tick(fps)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


# лавное меню, при нажатии единственной кнопки "Play" появляется "новый" экран (старый заполняется черным цветом, появляются новые кнопки)
def main_menu():
    pygame.display.set_caption('Menu')

    while True:
        SCREEN.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = get_font(100).render('MAIN MENU', True, '#b68f40')
        menu_rect = menu_text.get_rect(center=(640, 100))

        play_button = Button(image=pygame.image.load('rect.png'), pos=(640, 340),
                             text_input='PLAY', font=get_font(75), base_color='#d7fcd4', hovering_color='White')
        SCREEN.blit(menu_text, menu_rect)

        for button in [play_button]:
            button.change_color(menu_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    play()

        pygame.display.update()


main_menu()
