import pygame, random, sys, os, time

pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))

# Создание прямоугольника для кнопки
button_rect = pygame.Rect(350, 450, 100, 50)


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

    # Создание прямоугольника для кнопки
    battle_button_rect = pygame.Rect(450, 480, 207, 30)  # Увеличиваем ширину и перемещаем кнопку направо

    # Создание кнопки не бросать кости
    nobattle_button_rect = pygame.Rect(120, 480, 207, 30)

    font = pygame.font.Font(None, 36)
    button_text = font.render('бросить кости', True, (0, 0, 0))
    button_text2 = font.render('не бросать кости', True, (0, 0, 0))

    # Загрузка изображений монстра
    monster_images = [pygame.image.load('pechenka1.jpg').convert_alpha(),
                      pygame.image.load('pechenka2.jpg').convert_alpha(),
                      pygame.image.load('pechenka3.jpg').convert_alpha(),
                      pygame.image.load('pechenka4.jpg').convert_alpha(),
                      pygame.image.load('pechenka5.jpg').convert_alpha(),
                      pygame.image.load('pechenka6.jpg').convert_alpha(), ]

    # Индекс текущего изображения
    current_image = 0

    player_total = 0
    monster_total = 0

    # Координаты монстра
    x = 350
    y = 75

    # Скорость движения монстра
    speed = 1

    flag = False
    flag_monstr = False

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not flag or not flag_monstr:
                mouse_pos = pygame.mouse.get_pos()
                if nobattle_button_rect.collidepoint(mouse_pos) and not flag or not flag_monstr:
                    # Добавляем текст о результате боя
                    result_text = font.render("Игрок выйграл в этой битве", 1, (255, 255, 255))
                    battle_screen.blit(result_text, (250, 350))
                    flag = True
                elif battle_button_rect.collidepoint(mouse_pos) and not flag or not flag_monstr:
                    battle_screen.fill((0, 0, 0))
                    dice_roll = roll_dice()
                    player_total += dice_roll
                    dice_roll_monster = roll_dice_monster()
                    monster_total += dice_roll_monster
                    font = pygame.font.Font(None, 36)
                    if monster_total > 6:
                        flag_monstr = True
                    if player_total > 6:
                        flag = True
                        text = font.render("Игрок выбил {}".format(dice_roll), 1, (255, 255, 255))
                        battle_screen.blit(text, (500, 250))
                    else:
                        text = font.render("Игрок выбил {}".format(dice_roll), 1, (255, 255, 255))
                        battle_screen.blit(text, (500, 250))
                    if monster_total <= 3:
                        text = font.render("Монстр выбил {}".format(dice_roll_monster), 1, (255, 255, 255))
                        battle_screen.blit(text, (100, 250))
                    else:
                        text = font.render("Монстр решил не бросать кубики", 1, (255, 255, 255))
                        battle_screen.blit(text, (50, 250))
                elif flag:
                    result_text = font.render("Монстр выйграл в этой битве", 1, (255, 255, 255))
                    battle_screen.blit(result_text, (250, 350))
                    break
                elif flag_monstr:
                    result_text = font.render("Игрок выйграл в этой битве", 1, (255, 255, 255))
                    battle_screen.blit(result_text, (250, 350))
                    break

            player_total_text = font.render("Общая сумма очков игрока: {}".format(player_total), 1, (255, 255, 255))
            battle_screen.blit(player_total_text, (420, 300))
            monster_total_text = font.render("Общая сумма очков монстра: {}".format(monster_total), 1, (255, 255, 255))
            battle_screen.blit(monster_total_text, (20, 300))
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
