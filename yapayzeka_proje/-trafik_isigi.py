#TRAFİK IŞIĞI 

import pygame
import sys
import time

pygame.init()

# EKRAN
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trafik Isigi")

# RENKLER
KOYU_GRI = (50, 50, 50)  # YOL RENGİ
ACIK_GRI = (200, 200, 200)  # ŞERİT RENGİ
BEYAZ = (255, 255, 255)  # YOL KENARLARI VE TRAFİK IŞIĞI ÖNÜNDEKİ BEYAZ ÇİZGİ
KALDIRIM_GRI = (150, 150, 150)
KIRMIZI_ON = (255, 0, 0)
SARI_ON = (255, 255, 0)
YESIL_ON = (0, 255, 0)
KIRMIZI_OFF = (100, 0, 0)
SARI_OFF = (100, 100, 0)
YESIL_OFF = (0, 100, 0)

# YOL VE IŞIK ÖZELLİKLERİ
yol_width = 200
serit_width = 10
serit_gap = 30
kaldirim_width = (WIDTH - yol_width) // 2
isik_radius = 10






# KALDIRIM KISMINA AİT FONKSİYON
def draw_kaldirim():
    pygame.draw.rect(screen, KALDIRIM_GRI, (0, 0, kaldirim_width, HEIGHT))
    pygame.draw.rect(screen, KALDIRIM_GRI, (WIDTH - kaldirim_width, 0, kaldirim_width, HEIGHT))

    # TAŞLI GÖRÜNÜM
    for y in range(0, HEIGHT, 20):
        for x in range(0, kaldirim_width, 20):
            pygame.draw.rect(screen, (100, 100, 100), (x, y, 10, 10))
        for x in range(WIDTH - kaldirim_width, WIDTH, 20):
            pygame.draw.rect(screen, (100, 100, 100), (x, y, 10, 10))





# YOLA AİT FONKSİYON
def draw_yol():
    pygame.draw.rect(screen, KOYU_GRI, (kaldirim_width, 0, yol_width, HEIGHT))
    pygame.draw.line(screen, BEYAZ, (kaldirim_width, 0), (kaldirim_width, HEIGHT), 2)
    pygame.draw.line(screen, BEYAZ, (WIDTH - kaldirim_width, 0), (WIDTH - kaldirim_width, HEIGHT), 2)






# ŞERİT ÇİZGİLERİNE AİT FONKSİYON
def draw_serit_cizgileri():
    for y in range(0, HEIGHT, serit_gap * 2):
        pygame.draw.rect(screen, ACIK_GRI, (WIDTH // 2 - serit_width // 2, y, serit_width, serit_gap))






# TRAFİK IŞIĞININ ÖNÜNDEKİ BEYAZ ÇİZGİ
def draw_isik_cizgisi():
    pygame.draw.line(screen, BEYAZ, (kaldirim_width, HEIGHT // 2), (WIDTH - kaldirim_width, HEIGHT // 2), 5)





# TRAFİK IŞIĞINDA IŞIK RENGİNİN DEĞİŞİMİ
def draw_trafik_isigi(x, y, light_color):
    # Trafik ışığı çizimi
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 20, 60))
    pygame.draw.circle(screen, YESIL_OFF if light_color != "yesil" else YESIL_ON, (x + 10, y + 10), isik_radius)
    pygame.draw.circle(screen, SARI_OFF if light_color != "sari" else SARI_ON, (x + 10, y + 30), isik_radius)
    pygame.draw.circle(screen, KIRMIZI_OFF if light_color != "kirmizi" else KIRMIZI_ON, (x + 10, y + 50), isik_radius)






# TRAFİK IŞIĞI ZAMANLAYICISI
clock = pygame.time.Clock()
running = True
start_time = time.time()
light_color = "yesil"  # Trafik ışığı başlangıcı

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # IŞIK RENGİ DÖNGÜSÜ
    elapsed_time = (time.time() - start_time) % 36  # TOPLAM 36 SANİYE

    if elapsed_time < 20:
        light_color = "yesil"
    elif elapsed_time < 23:
        light_color = "sari"
    elif elapsed_time < 33:
        light_color = "kirmizi"
    else:
        light_color = "sari"
    #20 SANİYE YEŞİL, 3 SANİYE SARI, 10 SANİYE KIRMIZI, 3 SANİYE SARI, 20 SANİYE YEŞİL... OLACAK ŞEKİLDE...





    # EKRAN ARKA PLAN RENGİ
    screen.fill((255, 255, 255))






    # BİLEŞENLERİN ÇİZDİRİLMESİ
    draw_kaldirim()
    draw_yol()
    draw_serit_cizgileri()
    draw_isik_cizgisi()
    draw_trafik_isigi(kaldirim_width - 30, HEIGHT // 2 - 30, light_color)
    draw_trafik_isigi(WIDTH - kaldirim_width + 10, HEIGHT // 2 - 30, light_color)






    # DISPLAY
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
