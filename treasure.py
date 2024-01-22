import random
import pygame
import pygame.locals

pygame.init()

WIDTH = 800
HEIGHT = 600

player_score = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Hunt")

coin_sprites = ['coin_11.jpg', 'coin_12.jpg']
scroll_sprite = 'scroll.jpg'
necklace_sprites = ['necklace_1.jpg', 'necklace_2.jpg', 'necklace_3.jpg']
gold_sprites = ['gold_1.jpg', 'gold_2.jpg']
diamond_sprites = ['diamond_1.jpg', 'diamond_2.jpg']


def show_reward_window(reward_name, reward_cost, reward_sprite):
    reward_text = f"Вы нашли {reward_name}!!\nВы зарабатываете {reward_cost} очков!!"

    reward_window = pygame.Surface((300, 200))
    reward_window.fill(BLACK)
    reward_window_rect = reward_window.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    font = pygame.font.Font(None, 30)
    text = font.render(reward_text, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    reward_image = pygame.image.load(reward_sprite)
    reward_image_rect = reward_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    screen.blit(reward_window, reward_window_rect)
    screen.blit(text, text_rect)
    screen.blit(reward_image, reward_image_rect)
    pygame.display.update()

    pygame.time.wait(2000)  # задержка на 2 секунды, можно, в целом, 3?


def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            exit()


def start_game():
    while True:
        event_handler()

        if player_reached_n():
            # выбор случайной стоимости
            reward_cost = random.choice([25, 100, 150, 250, 500])

            # определение названия и спрайта награды на основе стоимости
            if reward_cost == 25:
                reward_name = "coin"
                reward_sprite = random.choice(coin_sprites)
            elif reward_cost == 100:
                reward_name = "scroll"
                reward_sprite = scroll_sprite
            elif reward_cost == 150:
                reward_name = "necklace"
                reward_sprite = random.choice(necklace_sprites)
            elif reward_cost == 250:
                reward_name = "gold"
                reward_sprite = random.choice(gold_sprites)
            else:
                reward_name = "diamond"
                reward_sprite = random.choice(diamond_sprites)

            show_reward_window(reward_name, reward_cost, reward_sprite)
            player_score += reward_cost

# игрок может как найти сокровище, так и выйграть его в бою:
def player_reached_n():
    # вставить список координат сокровищ в лабиринте
    coords = []
    # fight = 1 когда произошел бой, добавить в функцию из fight.py
    fight = 1
    # result = 1 победа игрока, 0 = поражение, добавить в функцию из fight.py
    result = 1
    if any([pygame.mouse.get_pos() == i for i in coords]) or (fight and result):
        return True

start_game()
