import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ check for keydown events """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """ check for keyup events """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(
        ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """ work with keydown buttons of keyboard and mouse """
    # listen keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(
                ai_settings,
                screen,
                stats,
                play_button,
                ship,
                aliens,
                bullets,
                mouse_x,
                mouse_y
            )


def check_play_button(
        ai_settings,
        screen,
        stats,
        play_button,
        ship,
        aliens,
        bullets,
        mouse_x,
        mouse_y
):
    """ run new game if button entered """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # hide mouse
        pygame.mouse.set_visible(False)

        # statistic reset
        stats.reset_stats()
        stats.game_active = True

        # clear aliens and bullets lists
        aliens.empty()
        bullets.empty()

        # create new fleet and ship in center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(
        ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """ update screen and draw new screen """
    # for every loop draw new screen
    screen.fill(ai_settings.bg_color)

    # all bullets create on back ship and invaders
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Play button on screen, if game active == 0
    if not stats.game_active:
        play_button.draw_button()

    # draw the last screen
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """ update bullets position and remove old bullets """
    # update bullets position
    bullets.update()

    # remove out of screen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    """ check for collisions with bullets and aliens """
    # check for hit in alien
    # if hit -> del bullet and alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # remuve bullets and create new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """ add bullet if it possible (maximun) """

    # create new bullet and insert in group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """ calculate counts of aliens in row """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """ number of rows on the screen """
    available_space_y = (
        ai_settings.screen_height - (3 * alien_height) - ship_height)

    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """add alien and add in row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """ create aliens fleet """
    # add alien and calculate counts of aliens in row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    # create aliens fleet
    for row_number in range(number_rows):
        # create first aliens raw
        for alien_number in range(number_aliens_x):
            # create alien and add in row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """ when alien in the end of screen """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """turn down aliens fleet and revese moving"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ process alien-ship collision """
    if stats.ships_left > 0:
        # decrease ships_left
        stats.ships_left -= 1

        # clean aliens and bullets lists
        aliens.empty()
        bullets.empty()

        # create new fleet and ship in center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ check for aliens in bottom of screen """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            """ the same with alien-ship collision """
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """ update aliens positions in fleet """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

    # check for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
