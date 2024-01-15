import pygame, random, sys, os, time

pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))

# Создание прямоугольника для кнопки
button_rect = pygame.Rect(350, 450, 100, 50)

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
    global dice_roll

    dice_roll = random.randint(1, 6)
    print(f"Player rolled {dice_roll}")
    return dice_roll


def roll_dice_monster():
    global dice_roll1
    dice_roll1 = random.randint(1, 6)
    print(f"Monster rolled {dice_roll1}")
    return dice_roll1


def battle_window():
    # Создание нового окна
    battle_screen = pygame.display.set_mode((800, 600))

    square_color = (0, 0, 0)

    # Создание прямоугольника для кнопки
    battle_button_rect = pygame.Rect(450, 480, 207, 30)  # Увеличиваем ширину и перемещаем кнопку направо

    # Создание кнопки не бросать кости
    nobattle_button_rect = pygame.Rect(120, 480, 207, 30)

    font = pygame.font.Font(None, 36)
    button_text = font.render('бросить кости', True, (0, 0, 0))
    button_text2 = font.render('не бросать кости', True, (0, 0, 0))

    # Загрузка изображений монстра
    monster_images = [load_image('monster_walk.png'),
                      load_image('monster_walk1.png'),
                      load_image('monster_walk2.png'),
                      load_image('monster_walk3.png'),
                      load_image('monster_walk4.png'),
                      load_image('monster_walk5.png'), ]

    # Индекс текущего изображения
    current_image = 0

    player_total = 0
    monster_total = 0

    # Координаты монстра
    x = 350
    y = 75

    # Скорость движения монстра
    speed = 1

    flag = True
    attemps = 1
    player_total = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if battle_button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and attemps <= 2 and flag:
                    battle_screen.fill((0, 0, 0))
                    dice_roll = roll_dice()
                    dice_roll_monster = roll_dice_monster()
                    font = pygame.font.Font(None, 36)

                    text = font.render("Игрок выбил {}".format(dice_roll), 1, (255, 255, 255))
                    battle_screen.blit(text, (500, 250))
                    player_total = dice_roll
                    print(attemps)
                    if monster_total <= player_total or attemps == 1:
                        text = font.render("Монстр выбил {}".format(dice_roll_monster), 1, (255, 255, 255))
                        battle_screen.blit(text, (100, 250))
                        monster_total = dice_roll_monster
                        print(attemps)
                    else:
                        text = font.render("Монстр решил не бросать кубики", 1, (255, 255, 255))
                        battle_screen.blit(text, (50, 250))
                    attemps += 1
                    player_total_text = font.render("Результат игрока {}".format(player_total), 1, (255, 255, 255))
                    battle_screen.blit(player_total_text, (500, 300))
                    monster_total_text = font.render("Результат монстра {}".format(monster_total), 1, (255, 255, 255))
                    battle_screen.blit(monster_total_text, (100, 300))
                if nobattle_button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and player_total != 0 or attemps == 3:
                    # Добавляем текст о результате боя
                    if monster_total <= player_total and attemps < 3:
                        dice_roll_monster = roll_dice_monster()
                        pygame.draw.rect(screen, square_color, pygame.Rect((50, 250), (300, 100)))
                        text = font.render("Монстр выбил {}".format(dice_roll_monster), 1, (255, 255, 255))
                        battle_screen.blit(text, (100, 250))
                        monster_total = dice_roll_monster
                        monster_total_text = font.render("Результат монстра {}".format(monster_total), 1,
                                                         (255, 255, 255))
                        battle_screen.blit(monster_total_text, (100, 300))

                    if monster_total > player_total:
                        monster_winner_text = font.render("Монстр победил", 1,
                                                         (255, 255, 255))
                        battle_screen.blit(monster_winner_text, (300, 375))
                    elif player_total > monster_total:
                        player_winner_text = font.render("Игрок победил", 1,
                                                          (255, 255, 255))
                        battle_screen.blit(player_winner_text, (300, 375))
                    else:
                        nichia = font.render("Победателя нет", 1,
                                                         (255, 255, 255))
                        battle_screen.blit(nichia, (300, 375))
                    flag = False

                    attemps += 1
        new_width, new_height = 100, 150  # Установите здесь нужные вам размеры
        resized_monster_image = pygame.transform.smoothscale(monster_images[current_image], (new_width, new_height))

        screen.blit(resized_monster_image.convert_alpha(), (x, y))

        current_image += 1
        if current_image >= len(monster_images):
            current_image = 0

        # Обновление экрана
        pygame.display.update()

        # Пауза
        time.sleep(0.1)

        # Отрисовка кнопки
        pygame.draw.rect(battle_screen, (255, 255, 255), battle_button_rect)
        battle_screen.blit(button_text, (466, 480))

        pygame.draw.rect(battle_screen, (255, 255, 255), nobattle_button_rect)
        battle_screen.blit(button_text2, (120, 480))

        # Обновление экрана
        pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                battle_window()

    # Отрисовка кнопки
    pygame.draw.rect(screen, (255, 255, 255), button_rect)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
