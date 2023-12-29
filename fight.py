import pygame, random, sys, os, time

pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))

# Создание прямоугольника для кнопки
button_rect = pygame.Rect(350, 450, 100, 50)



def roll_dice():
    dice_roll = random.randint(1, 6)
    print(f"Player rolled {dice_roll}")
    return dice_roll


def battle_window():
    # Создание нового окна
    battle_screen = pygame.display.set_mode((800, 600))

    # Создание прямоугольника для кнопки
    battle_button_rect = pygame.Rect(450, 480, 175, 30)  # Увеличиваем ширину и перемещаем кнопку направо

    font = pygame.font.Font(None, 36)
    button_text = font.render('бросить кости', True, (0, 0, 0))

    # Загрузка изображений монстра
    monster_images = [pygame.image.load('pechenka1.jpg').convert_alpha(), pygame.image.load('pechenka2.jpg').convert_alpha(),
                      pygame.image.load('pechenka3.jpg').convert_alpha(), pygame.image.load('pechenka4.jpg').convert_alpha(),
                      pygame.image.load('pechenka5.jpg').convert_alpha(), pygame.image.load('pechenka6.jpg').convert_alpha(),]

    # Индекс текущего изображения
    current_image = 0

    # Координаты монстра
    x = 350
    y = 75

    # Скорость движения монстра
    speed = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if battle_button_rect.collidepoint(mouse_pos):
                    battle_screen.fill((0, 0, 0))
                    dice_roll = roll_dice()
                    font = pygame.font.Font(None, 36)
                    text = font.render("Игрок выбил {}".format(dice_roll), 1, (255, 255, 255))
                    battle_screen.blit(text, (500, 250))
                    text = font.render("Монстр выбил {}".format(dice_roll), 1, (255, 255, 255))
                    battle_screen.blit(text, (100, 250))

                    # Добавляем текст о результате боя
                    result_text = font.render("Игрок выйграл в этой битве", 1, (255, 255, 255))
                    battle_screen.blit(result_text, (250, 350))

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
        battle_screen.blit(button_text, (450, 480))

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
