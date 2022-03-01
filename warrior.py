import pygame

level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1],
    [1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
level_1 = [[95, 161], [865, 927]]
level_2 = [31 * 16, 31 * 18]
level_3 = [[31, 97], [33 * 21, 31 * 25]]
level_4 = [[31 * 7, 31 * 9], [31 * 16, 31 * 18], [865, 927]]
level_5 = [[32 * 10, 32 * 12]]

pygame.display.set_caption("Warrior")
wood_box = pygame.image.load('wood_box.png')
ladder = pygame.image.load('ladder.png')
right_walk = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
              pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
              pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
left_walk = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
             pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
             pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
right_walk_boss = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                   pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                   pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R1E.png')]
left_walk_boss = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                  pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                  pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L1E.png')]
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()
width, height = 959, 609

pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


def base():
    pygame.init()
    size = 959, 609
    win = pygame.display.set_mode(size)
    pygame.display.set_caption("Warrior")
    win.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Warrior!", True, 'yellow')
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 25
    win.blit(text, (text_x, text_y))
    text_1 = font.render("level 1  or  level 2", True, 'yellow')
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 + 25
    win.blit(text_1, (text_x, text_y))
    pygame.draw.line(win, color='red', start_pos=(text_x + 85, text_y + 35), end_pos=(text_x + 105, text_y + 35),
                     width=5)
    pygame.draw.line(win, color='red', start_pos=(text_x + 265, text_y + 35), end_pos=(text_x + 285, text_y + 35),
                     width=5)
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            print('1')
            level_1_base()
        if keys[pygame.K_2]:
            print('2')
            level_2_base()
        pygame.display.update()
    pygame.quit()


def base_window_of_game(win, left, right, x, y):
    global count_of_walk, wood_box, up_x, floor
    pygame.init()
    size = 959, 609
    win = pygame.display.set_mode(size)
    win.fill('black')
    w_1 = -32
    h_1 = -32

    for i in level:
        h_1 += 32
        w_1 = -32
        for j in i:
            w_1 += 32
            if j == 1:
                win.blit(wood_box, (w_1, h_1))
            elif j == 2:
                win.blit(ladder, (w_1, h_1))

    if count_of_walk + 1 >= 27:
        count_of_walk = 0
    if up_x:
        if floor == 1:
            floor += 1
            up_x = False
        elif floor == 2:
            floor += 1
            up_x = False
        elif floor == 3:
            floor += 1
            up_x = False
        elif floor == 4:
            floor += 1
            up_x = False
        elif floor == 5:
            floor = 0
            up_x = False

    if left:
        win.blit(left_walk[count_of_walk // 3], (x, y))
        count_of_walk += 1
    elif right:
        win.blit(right_walk[count_of_walk // 3], (x, y))
        count_of_walk += 1
    else:
        win.blit(char, (x, y))
    if x == 875 and y == 32:
        win_of_warrior()

    pygame.display.update()


def base_window_of_game_2(win, left, right, x, y, left_e, right_e, x_e, y_e):
    global count_of_walk, count_of_walk_boss, up_x, floor, width, height, run
    win.fill('black')
    w_1 = -32
    h_2 = -32
    for i in level:
        h_2 += 32
        w_1 = -32
        for j in i:
            w_1 += 32
            if j == 1:
                win.blit(wood_box, (w_1, h_2))
            elif j == 2:
                win.blit(ladder, (w_1, h_2))

    if count_of_walk + 1 >= 27:
        count_of_walk = 0
    if count_of_walk_boss + 1 >= 27:
        count_of_walk_boss = 0
    if up_x:
        if floor == 1:
            floor += 1
            up_x = False
        elif floor == 2:
            floor += 1
            up_x = False
        elif floor == 3:
            floor += 1
            up_x = False
        elif floor == 4:
            floor += 1
            up_x = False
        elif floor == 5:
            floor = 0
            up_x = False

    if left:
        win.blit(left_walk[count_of_walk // 3], (x, y))
        count_of_walk += 1
    elif right:
        win.blit(right_walk[count_of_walk // 3], (x, y))
        count_of_walk += 1
    else:
        win.blit(char, (x, y))
    if left_e:
        win.blit(left_walk_boss[count_of_walk_boss // 3], (x_e, y_e))
        count_of_walk_boss += 1
    elif right_e:
        win.blit(right_walk_boss[count_of_walk_boss // 3], (x_e, y_e))
        count_of_walk_boss += 1
    if -16 <= x_e - x <= 16 and floor == 0:
        dead_of_warrior()
    if x == 875 and y == 32:
        win_of_warrior()

    pygame.display.update()


def level_1_base():
    global count_of_walk, up_x, up_x_down, floor
    pygame.init()
    size = 959, 609
    screen = pygame.display.set_mode(size)
    win = pygame.display.set_mode(size)
    run = True
    pygame.display.set_caption("Load Runner")
    x = 16
    up_x_down = x
    up_x = False
    floor = 1
    y = 608 - 96
    width = 64
    height = 64
    cord = 5
    left = False
    right = False
    count_of_walk = 0
    while run:
        clock.tick(27)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    if (level_1[0][0] <= x - 16 <= level_1[0][1] or level_1[0][0] <= x - 50 <= level_1[0][
                        1]) and floor == 1:
                        x += 32
                        count_of_walk = 0
                        y -= 96
                        up_x = True
                    if (level_1[1][0] <= x <= level_1[1][1] or level_1[1][0] <= x <= level_1[1][1]) and floor == 1:
                        x = level_1[1][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if level_2[0] <= x + 50 <= level_2[1] and floor == 2:
                        x = level_2[0] + 32
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if (level_3[1][0] <= x <= level_3[1][1] or level_3[1][0] <= x <= level_3[1][1]) and floor == 3:
                        x = level_3[1][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if (level_3[0][0] <= x <= level_3[0][1] or level_3[0][0] <= x <= level_3[0][1]) and floor == 3:
                        x = level_3[0][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if (level_4[0][0] <= x - 16 <= level_4[0][1] or level_4[0][0] <= x + 50 <= level_4[0][
                        1]) and floor == 4:
                        x += 32
                        count_of_walk = 0
                        y -= 96
                        up_x = True
                    if (level_4[1][0] <= x - 16 <= level_4[1][1] or level_4[1][0] <= x + 50 <= level_4[1][
                        1]) and floor == 4:
                        x = level_4[1][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if (level_4[2][0] <= x <= level_4[2][1] or level_4[2][0] <= x <= level_4[2][1]) and floor == 4:
                        x = level_4[2][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if (level_5[0][0] <= x <= level_5[0][1] or level_5[0][0] <= x <= level_5[0][1]) and floor == 5:
                        x = level_5[0][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x - 16 > cord:
            x -= cord
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 960 - width - cord - 16:
            x += cord
            right = True
            left = False
        else:
            right = False
            left = False
            count_of_walk = 0

        base_window_of_game(win, left, right, x, y)


def level_2_base():
    global count_of_walk, count_of_walk_boss, i, up_x, floor
    pygame.init()
    size = 959, 609
    win = pygame.display.set_mode(size)
    run = True
    pygame.display.set_caption("Warrior")
    x = 16
    x_e = 960 - 64
    y = 608 - 96
    y_e = 35
    width = 64
    height = 64
    vel = 5
    left = False
    right = False
    x_up_down = x
    up_x = False
    boss_left = True
    boss_right = True
    count_of_walk_boss = 0
    count_of_walk = 0
    floor = 1
    while run:
        clock.tick(27)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    if (level_1[0][0] <= x - 16 <= level_1[0][1] or level_1[0][0] <= x - 50 <= level_1[0][
                        1]) and floor == 1:
                        x += 32
                        count_of_walk = 0
                        y -= 96
                        up_x = True
                    if (level_1[1][0] <= x <= level_1[1][1] or level_1[1][0] <= x <= level_1[1][1]) and floor == 1:
                        x = level_1[1][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if level_2[0] <= x + 50 <= level_2[1] and floor == 2:
                        x = level_2[0] + 32
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if (level_3[1][0] <= x <= level_3[1][1] or level_3[1][0] <= x <= level_3[1][1]) and floor == 3:
                        x = level_3[1][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if (level_3[0][0] <= x <= level_3[0][1] or level_3[0][0] <= x <= level_3[0][1]) and floor == 3:
                        x = level_3[0][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if (level_4[0][0] <= x - 16 <= level_4[0][1] or level_4[0][0] <= x + 50 <= level_4[0][
                        1]) and floor == 4:
                        x += 32
                        count_of_walk = 0
                        y -= 96
                        up_x = True
                    if (level_4[1][0] <= x - 16 <= level_4[1][1] or level_4[1][0] <= x + 50 <= level_4[1][
                        1]) and floor == 4:
                        x = level_4[1][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if (level_4[2][0] <= x <= level_4[2][1] or level_4[2][0] <= x <= level_4[2][1]) and floor == 4:
                        x = level_4[2][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
                    if (level_5[0][0] <= x <= level_5[0][1] or level_5[0][0] <= x <= level_5[0][1]) and floor == 5:
                        x = level_5[0][0]
                        y -= 96
                        count_of_walk = 0
                        up_x = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x - 16 > vel:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 960 - width - vel - 16:
            x += vel
            right = True
            left = False
        else:
            x_up_down = x
            right = False
            left = False
            count_of_walk = 0
        if x_e < 50:
            boss_left = False
            boss_right = True
        elif x_e > 890:
            boss_left = True
            boss_right = False
        if boss_left:
            x_e -= vel
            boss_left = True
            boss_right = False
        if boss_right:
            x_e += vel
            boss_right = True
            boss_left = False
        base_window_of_game_2(win, left, right, x, y, boss_left, boss_right, x_e, y_e)


def dead_of_warrior():
    pygame.init()
    size = 959, 609
    win = pygame.display.set_mode(size)
    win.fill('black')
    font = pygame.font.Font(None, 50)
    text = font.render("YOU ARE LOST...", True, 'orange')
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    win.blit(text, (text_x, text_y))
    text2 = font.render("press any key to continue", True, 'orange')
    text_x = width // 2 - text.get_width() // 2 - 45
    text_y = height // 2 - text.get_height() // 2 + 25
    win.blit(text2, (text_x, text_y))
    pygame.display.update()
    dead_run = True
    while dead_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead_run = False
            if event.type == pygame.KEYDOWN:
                base()
    pygame.quit()


def win_of_warrior():
    pygame.init()
    size = 959, 609
    win = pygame.display.set_mode(size)
    win.fill('black')
    font = pygame.font.Font(None, 50)
    text = font.render("YOU ARE WIN...", True, (255, 200, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    win.blit(text, (text_x, text_y))
    text2 = font.render("press any key to continue", True, 'orange')
    text_x = width // 2 - text.get_width() // 2 - 45
    text_y = height // 2 - text.get_height() // 2 + 25
    win.blit(text2, (text_x, text_y))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                base()
    pygame.quit()


run = True
while run:
    base()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        level_1_base()
    if keys[pygame.K_2]:
        level_2_base()

pygame.quit()
