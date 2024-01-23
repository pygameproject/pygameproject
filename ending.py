# прости, не могу найти твой код, но уверена, что там есть подобное условие. просто вставь сюда его название
if end_event:
    end_text = f"Congratulations!\nYou finished the game with {player_score} points!!"

    end_window = pygame.Surface((300, 200))
    end_window.fill(BLACK)
    end_window_rect = end_window.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    font = pygame.font.Font(None, 30)
    text = font.render(end_text, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    screen.blit(end_window, end_window_rect)
    screen.blit(text, text_rect)

    pygame.display.update()
    # проверка на существование, если это не первая игра 
    try:
        with open('results.txt', 'r') as f:
            count = len(list(map(str.strip, f.readlines())))
    except FileNotFoundError:
        count = 0
    with open('results.txt', 'w') as f:
        f.write(f'Игра №{count}: вы заработали {player_score} очков')
