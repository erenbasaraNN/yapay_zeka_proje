import pygame
import sys
import math

# Pygame'i başlatma
pygame.init()

# Ekran boyutları
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kuzeybatı Köşesinde Ev ve Araba Garajı")

# Renkler
pastel_pink = (255, 182, 193)
brown = (139, 69, 19)
dark_gray = (169, 169, 169)
light_gray = (200, 200, 200)
black = (0, 0, 0)
road_color = (105, 105, 105)
road_line_color = (255, 255, 255)  # Beyaz yol çizgisi
building_color = (150, 150, 150)
small_building_color = (200, 200, 200)
white = (255, 255, 255)
green = (34, 139, 34)  # Ağaç yeşili
curtain_color_1 = (255, 215, 0)  # Altın sarısı perde
curtain_color_2 = (255, 239, 204)  # Krem rengi perde
cornice_color = (139, 69, 19)  # Kahverengi korniş

# Yazı tipi ayarları
font = pygame.font.Font(None, 20)
garage_font = pygame.font.Font(None, 18)

# Ev çizim fonksiyonu
def draw_house(x, y):
    pygame.draw.rect(screen, pastel_pink, (x, y, 100, 100))
    pygame.draw.polygon(screen, brown, [(x, y), (x + 50, y - 50), (x + 100, y)])
    pygame.draw.rect(screen, dark_gray, (x + 35, y + 50, 30, 50))  # Kapı
    
    # Pencereler
    window_size = 20
    left_window = pygame.draw.rect(screen, black, (x + 10, y + 20, window_size, window_size), 2)  # Sol pencere
    right_window = pygame.draw.rect(screen, black, (x + 70, y + 20, window_size, window_size), 2)  # Sağ pencere
    
    # Perdeler
    pygame.draw.rect(screen, cornice_color, (left_window.x - 2, left_window.y - 5, window_size + 4, 5))  # Sol korniş
    pygame.draw.rect(screen, cornice_color, (right_window.x - 2, right_window.y - 5, window_size + 4, 5))  # Sağ korniş
    pygame.draw.rect(screen, curtain_color_1, (left_window.x + 2, left_window.y + 2, window_size - 4, window_size // 2))  # Sol perde
    pygame.draw.rect(screen, curtain_color_2, (left_window.x + 2, left_window.y + window_size // 2 + 2, window_size - 4, window_size // 2))  # Sol alt perde
    pygame.draw.rect(screen, curtain_color_1, (right_window.x + 2, right_window.y + 2, window_size - 4, window_size // 2))  # Sağ perde
    pygame.draw.rect(screen, curtain_color_2, (right_window.x + 2, right_window.y + window_size // 2 + 2, window_size - 4, window_size // 2))  # Sağ alt perde

# Araba Garajı çizim fonksiyonu
def draw_garage(x, y):
    pygame.draw.rect(screen, black, (x, y, 80, 60))
    pygame.draw.rect(screen, dark_gray, (x + 10, y + 20, 60, 40))
    
    # "GARAGE" yazısını ekle ve üstte hizala
    text = garage_font.render("GARAGE", True, white)
    text_rect = text.get_rect(center=(x + 40, y + 10))
    screen.blit(text, text_rect)

# Ağaç çizim fonksiyonu
def draw_tree(x, y):
    pygame.draw.rect(screen, brown, (x, y, 15, 40))
    pygame.draw.polygon(screen, green, [(x - 25, y), (x + 7.5, y - 50), (x + 45, y)])

# Çapraz yol çizim fonksiyonu
def draw_diagonal_road(start_x, start_y, length, angle):
    end_x = start_x + length * math.cos(math.radians(angle))
    end_y = start_y - length * math.sin(math.radians(angle))
    pygame.draw.line(screen, road_color, (start_x, start_y), (end_x, end_y), 80)
    
    # Beyaz kesik çizgiler
    num_lines = 30  # Kesik çizgi sayısını artırdık
    for i in range(num_lines):
        line_x = start_x + (end_x - start_x) * (i / num_lines)
        line_y = start_y + (end_y - start_y) * (i / num_lines)
        if i % 2 == 0:
            pygame.draw.line(screen, road_line_color, (line_x, line_y), 
                             (line_x + 20 * math.cos(math.radians(angle)), line_y - 20 * math.sin(math.radians(angle))), 3)  # Daha küçük kesik çizgiler
    
    return end_x, end_y

# Büyük işyeri binası çizim fonksiyonu
def draw_large_building(x, y):
    pygame.draw.rect(screen, building_color, (x, y, 120, 150))
    pygame.draw.rect(screen, black, (x, y - 20, 120, 20))  # Düz çatı
    text = font.render("OFFICE", True, white)
    screen.blit(text, (x + 25, y - 18))
    
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, black, (x + 15 + i * 30, y + 20 + j * 40, 15, 15), 2)

# Küçük işyeri binası çizim fonksiyonu
def draw_small_building(x, y):
    pygame.draw.rect(screen, small_building_color, (x, y, 80, 100))
    pygame.draw.rect(screen, black, (x, y - 10, 80, 20))  # Düz çatı
    text = font.render("OFFICE", True, white)
    screen.blit(text, (x + 7, y - 8))
    
    for i in range(3):
        pygame.draw.rect(screen, black, (x + 10 + i * 25, y + 20, 15, 15), 2)  # Üst pencereler
    for i in range(3):
        pygame.draw.rect(screen, black, (x + 10 + i * 25, y + 60, 15, 15), 2)  # Alt pencereler

# Ana döngü
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        draw_house(50, 50)
        draw_garage(160, 90)

        road_end_x, road_end_y = draw_diagonal_road(200, 160, 780, -45)

        draw_large_building(road_end_x + 10, road_end_y - 80)
        draw_small_building(road_end_x + 150, road_end_y - 30)

        draw_garage(road_end_x - 90, road_end_y + 10)

        # Evin önüne sabit ağaçlar ekle (aralarında daha fazla mesafe)
        draw_tree(80, 250)   # 1. ağaç
        draw_tree(120, 380)   # 2. ağaç
        draw_tree(190, 580)  # 3. ağaç

        # Yolun diğer tarafına 5 simetrik ağaç ekle
        draw_tree(400, 170)  # 1. simetrik ağaç
        draw_tree(480, 290)  # 2. simetrik ağaç
        draw_tree(650, 390)  # 3. simetrik ağaç
        draw_tree(840, 210)  # 4. simetrik ağaç
        draw_tree(680, 270)  # 5. simetrik ağaç

        pygame.display.flip()

if __name__ == "__main__":
    main()
