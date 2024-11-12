import pygame
import sys
import time

# Pygame başlat
pygame.init()

# Ekran boyutları
WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Renkler
BACKGROUND_COLOR = (139, 169, 119)
PASTEL_PINK = (255, 182, 193)
BROWN = (80, 40, 10)
DARK_GRAY = (169, 169, 169)
OFFICE_COLOR = (200, 200, 200)
WHITE = (255, 255, 255)
TREE_GREEN = (34, 139, 34)
CURTAIN_COLOR_1 = (255, 215, 0)
CURTAIN_COLOR_2 = (255, 239, 204)
CORNICE_COLOR = (139, 69, 19)
ASPHALT_COLOR = (50, 50, 50)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
RED_OFF = (100, 0, 0)
YELLOW_OFF = (100, 100, 0)
GREEN_OFF = (0, 100, 0)
PINK = (255, 192, 203)
POOL_BLUE = (0, 191, 255)
STONE_LIGHT = (169, 169, 169)
STONE_DARK = (105, 105, 105)

# Yazı tipi ayarları
font = pygame.font.Font(None, 20)
garage_font = pygame.font.Font(None, 18)

# Arka plan görselini yükle ve ekran boyutuna göre ölçeklendir
construction_site = pygame.image.load("kazi_alani.png")
construction_site = pygame.transform.scale(construction_site, (500, 400))

# Dekorasyon Resimleri ve Pozisyonları
bench_man = pygame.image.load("bankta_oturan_adam.png")
worker = pygame.image.load("amele.png")
pickaxe = pygame.image.load("kazma.png")
veterinarian = pygame.image.load("veteriner.png")
trash_can = pygame.image.load("cop_kutusu.png")
crane = pygame.image.load("vinc.png")
tree_image = pygame.image.load("agac.png")

# Detaylı kamyon çizme fonksiyonu
def draw_truck(x, y):
    # Kamyon gövdesi
    pygame.draw.rect(WINDOW, (255, 140, 0), (x - 140, y, 140, 60), border_radius=8)

    # Tuğla şekilli yük
    for i in range(5):
        for j in range(2):
            brick_color = (210, 105, 30) if (i + j) % 2 == 0 else (180, 90, 20)
            pygame.draw.rect(WINDOW, brick_color, (x - 125 + i * 20, y + 10 + j * 10, 18, 8))

    # Saydam yük örtüsü
    overlay_surface = pygame.Surface((120, 30), pygame.SRCALPHA)
    overlay_surface.fill((200, 200, 200, 100))
    WINDOW.blit(overlay_surface, (x - 130, y + 10))

    # Kabin (sürücü bölümü)
    pygame.draw.rect(WINDOW, (255, 140, 0), (x, y + 10, 30, 50), border_radius=8)
    pygame.draw.polygon(WINDOW, (255, 140, 0), [(x, y + 10), (x + 30, y), (x + 30, y + 10)])

    # Kabin detayları (kapı ve pencere)
    pygame.draw.rect(WINDOW, WHITE, (x + 5, y + 20, 15, 20))
    pygame.draw.rect(WINDOW, WHITE, (x + 10, y + 15, 10, 15))

    # Kapı kolu
    pygame.draw.circle(WINDOW, SILVER, (x + 20, y + 30), 2)

    # Yan aynalar
    pygame.draw.circle(WINDOW, SILVER, (x - 5, y + 15), 3)
    pygame.draw.circle(WINDOW, SILVER, (x + 30, y + 15), 3)

    # Farlar
    pygame.draw.circle(WINDOW, WHITE, (x + 40, y + 15), 5)
    pygame.draw.circle(WINDOW, YELLOW, (x - 10, y + 15), 3)
    pygame.draw.circle(WINDOW, YELLOW, (x + 40, y + 15), 3)

    # Tekerlekler
    pygame.draw.circle(WINDOW, BLACK, (x + 15, y + 60), 10)
    pygame.draw.circle(WINDOW, BLACK, (x - 100, y + 60), 10)
    pygame.draw.circle(WINDOW, BLACK, (x - 60, y + 60), 10)

    pygame.draw.circle(WINDOW, WHITE, (x + 15, y + 60), 5)
    pygame.draw.circle(WINDOW, WHITE, (x - 100, y + 60), 5)
    pygame.draw.circle(WINDOW, WHITE, (x - 60, y + 60), 5)

    # Arka kısım detayları
    pygame.draw.rect(WINDOW, (255, 140, 0), (x - 140, y + 50, 140, 10))

    # Arka lambalar
    pygame.draw.circle(WINDOW, RED, (x - 135, y + 55), 3)
    pygame.draw.circle(WINDOW, RED, (x - 105, y + 55), 3)

# Ev (başlangıç)
def draw_house(x, y):
    pygame.draw.rect(WINDOW, PASTEL_PINK, (x, y, 100, 100))
    pygame.draw.polygon(WINDOW, BROWN, [(x, y), (x + 50, y - 50), (x + 100, y)])
    pygame.draw.rect(WINDOW, DARK_GRAY, (x + 35, y + 50, 30, 50))

    # Pencereler
    window_size = 20
    left_window = pygame.draw.rect(WINDOW, BLACK, (x + 10, y + 20, window_size, window_size), 2)
    right_window = pygame.draw.rect(WINDOW, BLACK, (x + 70, y + 20, window_size, window_size), 2)

    # Perdeler
    pygame.draw.rect(WINDOW, CORNICE_COLOR, (left_window.x - 2, left_window.y - 5, window_size + 4, 5))
    pygame.draw.rect(WINDOW, CORNICE_COLOR, (right_window.x - 2, right_window.y - 5, window_size + 4, 5))
    pygame.draw.rect(WINDOW, CURTAIN_COLOR_1, (left_window.x + 2, left_window.y + 2, window_size - 4, window_size // 2))
    pygame.draw.rect(WINDOW, CURTAIN_COLOR_2, (left_window.x + 2, left_window.y + window_size // 2 + 2, window_size - 4, window_size // 2))
    pygame.draw.rect(WINDOW, CURTAIN_COLOR_1, (right_window.x + 2, right_window.y + 2, window_size - 4, window_size // 2))
    pygame.draw.rect(WINDOW, CURTAIN_COLOR_2, (right_window.x + 2, right_window.y + window_size // 2 + 2, window_size - 4, window_size // 2))

# Ağaç çizdirme fonksiyonu
def draw_tree(x, y):
    pygame.draw.rect(WINDOW, BROWN, (x, y, 15, 40))
    pygame.draw.polygon(WINDOW, TREE_GREEN, [(x - 25, y), (x + 7.5, y - 50), (x + 45, y)])

# Ofis (son)
def draw_office(x, y):
    pygame.draw.rect(WINDOW, OFFICE_COLOR, (x, y, 100, 100))
    pygame.draw.rect(WINDOW, BLACK, (x, y - 10, 100, 20))
    text = font.render("OFFICE", True, WHITE)
    WINDOW.blit(text, (x + 25, y - 8))

    for i in range(3):
        pygame.draw.rect(WINDOW, BLACK, (x + 18 + i * 25, y + 20, 15, 15), 2)
    for i in range(3):
        pygame.draw.rect(WINDOW, BLACK, (x + 18 + i * 25, y + 60, 15, 15), 2)

# Kavşak oluşturma
ROAD_WIDTH = 100
LANE_WIDTH = 10
LANE_GAP = 45
ROAD_RADIUS = 25
POOL_RADIUS = 10
INNER_LINE_RADIUS = 10

def draw_roundabout():
    pygame.draw.circle(WINDOW, TREE_GREEN, (110, 700), ROAD_RADIUS)
    pygame.draw.circle(WINDOW, WHITE, (110, 700), ROAD_RADIUS, 3)
    pygame.draw.circle(WINDOW, POOL_BLUE, (110, 700), POOL_RADIUS)
    pygame.draw.circle(WINDOW, WHITE, (110, 700), INNER_LINE_RADIUS, 2)

# Yollar
def draw_top_horizontal_road():
    pygame.draw.rect(WINDOW, ASPHALT_COLOR, (100, 50, 900, ROAD_WIDTH))

def draw_bottom_horizontal_road():
    pygame.draw.rect(WINDOW, ASPHALT_COLOR, (0, 650, 850, ROAD_WIDTH))

def draw_left_vertical_road():
    pygame.draw.rect(WINDOW, ASPHALT_COLOR, (50, 150, ROAD_WIDTH, 550))

def draw_right_vertical_road():
    pygame.draw.rect(WINDOW, ASPHALT_COLOR, (850, 50, ROAD_WIDTH, 600))

def draw_lane_lines():
    for y in range(200, 700, LANE_GAP * 2):
        pygame.draw.rect(WINDOW, WHITE, (100, y, LANE_WIDTH, LANE_GAP))
    for y in range(100, 650, LANE_GAP * 2):
        pygame.draw.rect(WINDOW, WHITE, (900, y, LANE_WIDTH, LANE_GAP))
    for x in range(0, 850, LANE_GAP * 2):
        pygame.draw.rect(WINDOW, WHITE, (x, 700, LANE_GAP, LANE_WIDTH))
    for x in range(140, 1000, LANE_GAP * 2):
        pygame.draw.rect(WINDOW, WHITE, (x, 100, LANE_GAP, LANE_WIDTH))

# Çapraz dar taşlı yol çizme fonksiyonu
def draw_diagonal_gravel_road():
    block_width = 15
    block_height = 6
    start_x = 100
    start_y = 150
    num_rows = (HEIGHT + WIDTH) // block_height

    for row in range(num_rows):
        for col in range(10):
            color = STONE_LIGHT if (row + col) % 2 == 0 else STONE_DARK
            x = start_x + col * block_width + row * (block_width // 1.6)
            y = start_y + row * block_height

            if x < 850 and y < 650:
                pygame.draw.rect(WINDOW, color, (x, y, block_width, block_height))

# Levhaları yükle
pedestrian_crossing_img = pygame.image.load("yayagecidi.png")
give_way_img = pygame.image.load("yolver.png")
stop_img = pygame.image.load("durlevhasi.png")
road_work_img = pygame.image.load("yolcalismasi.png")
cone_img = pygame.image.load("duba.png")
roundabout_img = pygame.image.load("donelkavsak.png")
exclamation_img = pygame.image.load("unlem.png")
road_work_sign_img = pygame.image.load("yolcalismasi2.png")
road_block_img = pygame.image.load("yolengel.png")

# Görsellerin boyutunu ayarla
scale_factor = 0.1
pedestrian_crossing_img = pygame.transform.scale(pedestrian_crossing_img, (int(pedestrian_crossing_img.get_width() * scale_factor), int(pedestrian_crossing_img.get_height() * scale_factor)))
give_way_img = pygame.transform.scale(give_way_img, (int(give_way_img.get_width() * scale_factor), int(give_way_img.get_height() * scale_factor)))
stop_img = pygame.transform.scale(stop_img, (int(stop_img.get_width() * 0.2), int(stop_img.get_height() * 0.2)))
road_work_img = pygame.transform.scale(road_work_img, (int(road_work_img.get_width() * scale_factor), int(road_work_img.get_height() * scale_factor)))
cone_img = pygame.transform.scale(cone_img, (int(cone_img.get_width() * scale_factor), int(cone_img.get_height() * scale_factor)))
roundabout_img = pygame.transform.scale(roundabout_img, (int(roundabout_img.get_width() * scale_factor), int(roundabout_img.get_height() * scale_factor)))
road_work_sign_img = pygame.transform.scale(road_work_sign_img, (int(road_work_sign_img.get_width() * 0.2), int(road_work_sign_img.get_height() * 0.2)))
road_block_img = pygame.transform.scale(road_block_img, (int(road_work_sign_img.get_width()), int(road_block_img.get_height() * 0.2)))

# Trafik ışığı fonksiyonu
LIGHT_RADIUS = 10

def draw_traffic_light(x, y, light_color):
    pygame.draw.rect(WINDOW, BLACK, (x, y, 20, 60))
    pygame.draw.circle(WINDOW, GREEN_OFF if light_color != "green" else GREEN, (x + 10, y + 10), LIGHT_RADIUS)
    pygame.draw.circle(WINDOW, YELLOW_OFF if light_color != "yellow" else YELLOW, (x + 10, y + 30), LIGHT_RADIUS)
    pygame.draw.circle(WINDOW, RED_OFF if light_color != "red" else RED, (x + 10, y + 50), LIGHT_RADIUS)

# Yaya geçidi çizme fonksiyonları
LINE_HEIGHT = 5
LINE_GAP = 5
LINE_WIDTH = 50

def draw_horizontal_pedestrian_crossing():
    for i in range(5, 15):
        crossing = pygame.Rect(750, i * (LINE_HEIGHT + LINE_GAP), LINE_WIDTH, LINE_HEIGHT)
        pygame.draw.rect(WINDOW, WHITE if i % 2 == 0 else ASPHALT_COLOR, crossing)

def draw_vertical_pedestrian_crossing():
    for i in range(85, 95):
        crossing = pygame.Rect(i * (LINE_HEIGHT + LINE_GAP), 300, LINE_HEIGHT, LINE_WIDTH)
        pygame.draw.rect(WINDOW, WHITE if i % 2 == 0 else ASPHALT_COLOR, crossing)

# Araba çizme fonksiyonu
def draw_car(x, y, color):
    pygame.draw.rect(WINDOW, color, (x, y, 120, 40), border_radius=15)
    pygame.draw.polygon(WINDOW, color, [(x + 20, y), (x + 110, y), (x + 90, y - 20), (x + 40, y - 20)])
    pygame.draw.circle(WINDOW, WHITE, (x + 120, y + 15), 5)
    pygame.draw.circle(WINDOW, WHITE, (x, y + 15), 5)
    pygame.draw.rect(WINDOW, WHITE, (x + 50, y + 10, 30, 5))
    pygame.draw.polygon(WINDOW, WHITE, [(x + 15, y - 10), (x + 20, y - 5), (x + 15, y - 5)])
    pygame.draw.polygon(WINDOW, WHITE, [(x + 110, y - 10), (x + 105, y - 5), (x + 110, y - 5)])
    pygame.draw.rect(WINDOW, WHITE, (x + 35, y - 15, 60, 15), border_radius=5)
    pygame.draw.circle(WINDOW, SILVER, (x + 20, y + 30), 18)
    pygame.draw.circle(WINDOW, BLACK, (x + 20, y + 30), 15)
    pygame.draw.circle(WINDOW, SILVER, (x + 20, y + 30), 7)
    pygame.draw.circle(WINDOW, SILVER, (x + 100, y + 30), 18)
    pygame.draw.circle(WINDOW, BLACK, (x + 100, y + 30), 15)
    pygame.draw.circle(WINDOW, SILVER, (x + 100, y + 30), 7)

# Ana fonksiyon
def main():
    pygame.display.update()
    clock = pygame.time.Clock()
    start_time = time.time()
    light_color = "green"

    # NPC Arabalar
    car_x_yellow = 50
    car_y_yellow = 690
    car_speed_yellow = 2
    original_car_speed_yellow = car_speed_yellow  # Orijinal hızı sakla


    car_x_red = 1000
    car_y_red = 40
    car_speed_red = 2
    original_car_speed_red = car_speed_red  # Kırmızı arabanın orijinal hızını sakla

    # Kedi
    cat_image = pygame.image.load("kedi.png")
    cat_x = 0
    cat_y = 750
    cat_speed = 1

    # NPC Karakterler
    npc_woman_left = pygame.image.load("npc_kopekli_abla_sol.png")
    npc_woman_right = pygame.image.load("npc_kopekli_abla_sag.png")
    # Köpekli kadının resim boyutlarını al
    npc_woman_image = npc_woman_left  # Resmin yönü fark etmez, boyutlar aynı
    npc_woman_width = npc_woman_image.get_width()
    npc_woman_height = npc_woman_image.get_height()


    npc_man_front = pygame.image.load("npc_adam_on.png")
    npc_man_back = pygame.image.load("npc_adam_arka.png")
    # NPC Adamın boyutları için resmin genişliği ve yüksekliği
    npc_man_image = npc_man_front
    npc_man_width = npc_man_image.get_width()
    npc_man_height = npc_man_image.get_height()


    npc_woman_x = 920
    npc_woman_y = 270
    npc_woman_speed = 0.5
    moving_left = True

    npc_man_x = 750
    npc_man_y = 0
    npc_man_speed = 0.5
    moving_down = True

    # Ana döngü
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Arka plan rengi
        WINDOW.fill(BACKGROUND_COLOR)

        # İnşaat alanı resmi
        WINDOW.blit(construction_site, (150, 150))

        # Trafik ışığı zamanlaması
        elapsed_time = (time.time() - start_time) % 36

        if elapsed_time < 20:
            light_color = "green"
        elif elapsed_time < 23:
            light_color = "yellow"
        elif elapsed_time < 33:
            light_color = "red"
        else:
            light_color = "yellow"

        car_x_red -= car_speed_red
        car_x_yellow += car_speed_yellow
        cat_x += cat_speed

        # NPC Arabalar ve Kedi
        if car_x_yellow > 800:
            car_x_yellow = -100

        if car_x_red < 100:
            car_x_red = 1100

        if cat_x > WIDTH:
            cat_x = -50

        # Köpekli kadın
        if moving_left:
            npc_woman = npc_woman_left
            npc_woman_x -= npc_woman_speed
            if npc_woman_x < 800:
                moving_left = False
                npc_woman = npc_woman_right
        else:
            npc_woman_x += npc_woman_speed
            if npc_woman_x > 950:
                moving_left = True
                npc_woman = npc_woman_left

        # Yalnız adam
        if moving_down:
            npc_man = npc_man_front
            npc_man_y += npc_man_speed
            if npc_man_y > 100:
                moving_down = False
                npc_man = npc_man_back
        else:
            npc_man_y -= npc_man_speed
            if npc_man_y < -75:
                moving_down = True
                npc_man = npc_man_front

        # Araba ve yaya için dikdörtgenler oluştur
        yellow_car_rect = pygame.Rect(car_x_yellow, car_y_yellow, 120, 40)  # Arabanın dikdörtgeni
        npc_man_rect = pygame.Rect(npc_man_x, npc_man_y, npc_man_width, npc_man_height)  # Yayanın dikdörtgeni
        # Kırmızı araba ve köpekli kadın için dikdörtgenler oluştur
        red_car_rect = pygame.Rect(car_x_red, car_y_red, 120, 40)  # Kırmızı arabanın dikdörtgeni
        npc_woman_rect = pygame.Rect(npc_woman_x, npc_woman_y, npc_woman_width, npc_woman_height)  # Köpekli kadının dikdörtgeni

        # Çarpışma kontrolü
        if yellow_car_rect.colliderect(npc_man_rect):
            car_speed_yellow = 0  # Araba durur
        else:
            car_speed_yellow = original_car_speed_yellow  # Araba hareket etmeye devam eder
        
        if red_car_rect.colliderect(npc_woman_rect) or red_car_rect.colliderect(npc_man_rect):
            car_speed_red = 0  # Kırmızı araba durur
        else:
            car_speed_red = original_car_speed_red  # Kırmızı araba hareket etmeye devam eder
        
        # Sarı arabanın pozisyonunu güncelle
        car_x_yellow += car_speed_yellow

        if car_x_yellow > 800:
            car_x_yellow = -100
        # Kırmızı arabanın pozisyonunu güncelle
        car_x_red -= car_speed_red

        if car_x_red < 100:
            car_x_red = 1100


        # Çizim fonksiyonlarını çağır
        draw_diagonal_gravel_road()
        draw_bottom_horizontal_road()
        draw_left_vertical_road()
        draw_top_horizontal_road()
        draw_right_vertical_road()
        draw_lane_lines()
        draw_roundabout()
        WINDOW.blit(tree_image, (200, 570))
        WINDOW.blit(tree_image, (350, 570))
        WINDOW.blit(tree_image, (550, 570))
        WINDOW.blit(tree_image, (700, 570))
        WINDOW.blit(tree_image, (950, 250))
        WINDOW.blit(tree_image, (950, 450))
        WINDOW.blit(tree_image, (0, 250))
        WINDOW.blit(tree_image, (0, 450))
        draw_traffic_light(950, 350, light_color)
        draw_traffic_light(150, 590, light_color)

        # Yaya geçitleri
        draw_horizontal_pedestrian_crossing()
        draw_vertical_pedestrian_crossing()

        # NPC'leri ekle
        WINDOW.blit(npc_woman, (npc_woman_x, npc_woman_y))
        WINDOW.blit(npc_man, (npc_man_x, npc_man_y))
        WINDOW.blit(cat_image, (cat_x, cat_y))
        draw_car(car_x_yellow, car_y_yellow, YELLOW)
        draw_car(car_x_red, car_y_red, RED)
        draw_truck(600, 80)

        # Binaları ekle
        draw_house(50, 50)
        draw_office(850, 650)

        # Levhaları ekle
        WINDOW.blit(pedestrian_crossing_img, (700, 100))
        WINDOW.blit(give_way_img, (730, 530))
        WINDOW.blit(stop_img, (-60, 700))
        WINDOW.blit(road_work_img, (350, 250))
        WINDOW.blit(cone_img, (350, 80))
        WINDOW.blit(roundabout_img, (0, 520))
        WINDOW.blit(road_work_sign_img, (200, 120))
        WINDOW.blit(road_block_img, (400, 300))

        # Dekorasyon resimleri
        WINDOW.blit(worker, (550, 350))
        WINDOW.blit(bench_man, (450, 580))
        WINDOW.blit(pickaxe, (400, 400))
        WINDOW.blit(veterinarian, (680, 230))
        WINDOW.blit(trash_can, (820, 150))
        WINDOW.blit(crane, (200, 400))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
