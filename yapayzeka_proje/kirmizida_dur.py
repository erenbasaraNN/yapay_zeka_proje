import pygame
import sys 
import random


# Pygame başlatma
pygame.init()

# Ekran boyutları
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Detaylı Taşlı Yol ve Kamyon")

# Renkler
sky_blue = (135, 206, 235)  # Gökyüzü rengi
asphalt_color = (50, 50, 50)  # Asfalt yol için koyu gri
stone_light = (169, 169, 169)  # Taşlı yol için açık gri
stone_dark = (105, 105, 105)  # Taşlı yol için koyu gri
black = (0, 0, 0)  # Tekerlekler için siyah
dark_grey = (40, 40, 40)  # Tekerlek gölgesi için koyu gri
silver = (192, 192, 192)  # Jant rengi
white = (255, 255, 255)  # Farlar, pencere çerçeveleri ve ön ızgara için beyaz
sun_yellow = (255, 223, 0)  # Güneş için sarı
yellow = (255, 255, 0)  # Sarı renk tanımlaması

red = (255, 0, 0)  # Kırmızı
green = (0, 255, 0)  # Yeşil
pink = (255, 192, 203)  # Pembe
purple = (128, 0, 128)  # Mor
orange = (255, 165, 0)  # Turuncu
brown = (165, 42, 42)  # Kahverengi
light_green = (144, 238, 144)  # Açık yeşil

# Trafik ışığı konumu
traffic_light_x = 370

# Trafik ışığı durumu
light_state = 'green'
light_timer = 0

# Taşlı yol için blok boyutları
block_width = 30
block_height = 15

# Gökyüzü nesneleri
sun_position = (700, 100)  # Güneş sabit konumda
clouds = [[random.randint(0, SCREEN_WIDTH), random.randint(50, 150)] for _ in range(5)]
birds = [[random.randint(0, SCREEN_WIDTH), random.randint(50, 200)] for _ in range(3)]

# Asfalt yolu çizme fonksiyonu
def draw_asphalt_road():
    pygame.draw.rect(window, asphalt_color, (0, 400, SCREEN_WIDTH, 100))
    for i in range(0, SCREEN_WIDTH, 100):  # Kesik çizgiler
        pygame.draw.rect(window, white, (i + 20, 445, 40, 10))

# Kenetlenen taşlı yolu çizme fonksiyonu
def draw_gravel_road():
    for row in range(500, 600, block_height):
        for col in range(0, SCREEN_WIDTH, block_width):
            color = stone_light if (row // block_height + col // block_width) % 2 == 0 else stone_dark
            offset = block_width // 2 if (row // block_height) % 2 == 0 else 0
            pygame.draw.rect(window, color, (col + offset, row, block_width, block_height))

# Gökyüzü nesnelerini çizme fonksiyonu
def draw_sky_elements():
    pygame.draw.circle(window, sun_yellow, sun_position, 40)  # Güneş
    for cloud in clouds:  # Bulutlar
        pygame.draw.ellipse(window, white, (cloud[0], cloud[1], 100, 50))
    for bird in birds:  # Kuşlar
        pygame.draw.arc(window, black, (bird[0], bird[1], 20, 10), 3.14, 0, 2)
        pygame.draw.arc(window, black, (bird[0] + 15, bird[1], 20, 10), 3.14, 0, 2)

# Trafik ışığı çizme fonksiyonu
def draw_traffic_light(x, y, state):
    pygame.draw.rect(window, black, (x + 7, y, 6, 40))  # Demir direk
    pygame.draw.circle(window, (255, 0, 0) if state == 'red' else (100, 0, 0), (x + 10, y + 10), 10)  # Kırmızı ışık
    pygame.draw.circle(window, (255, 165, 0) if state == 'yellow' else (200, 200, 0), (x + 10, y + 20), 10)  # Sarı ışık
    pygame.draw.circle(window, (0, 255, 0) if state == 'green' else (0, 100, 0), (x + 10, y + 30), 10)  # Yeşil ışık

    
# Detaylı kamyon çizme fonksiyonu
def draw_truck(x, y):
    # Kamyon gövdesi (turuncu)
    pygame.draw.rect(window, (255, 140, 0), (x - 140, y, 140, 60), border_radius=8)  # Kamyon gövdesi
    
    # Tuğla şekilli yük (daha detaylı)
    for i in range(5):  # Tuğlaları çizmek için satırlar
        for j in range(2):  # İki satır tuğla
            brick_color = (210, 105, 30) if (i + j) % 2 == 0 else (180, 90, 20)  # Farklı renk tonları
            pygame.draw.rect(window, brick_color, (x - 125 + i * 20, y + 10 + j * 10, 18, 8))  # Tuğla blokları

    # Saydam yük örtüsü
    overlay_surface = pygame.Surface((120, 30), pygame.SRCALPHA)  # Saydam yüzey
    overlay_surface.fill((200, 200, 200, 100))  # Hafif saydam gri renk
    window.blit(overlay_surface, (x - 130, y + 10))  # Yük örtüsünü çiz

    # Kabin (sürücü bölümü)
    pygame.draw.rect(window, (255, 140, 0), (x, y + 10, 30, 50), border_radius=8)  # Kabin
    pygame.draw.polygon(window, (255, 140, 0), [(x, y + 10), (x + 30, y), (x + 30, y + 10)])  # Kabin üstü

    # Kabin detayları (kapı ve pencere)
    pygame.draw.rect(window, white, (x + 5, y + 20, 15, 20))  # Kapı
    pygame.draw.rect(window, white, (x + 10, y + 15, 10, 15))  # Pencere
    
    # Kapı kolu
    pygame.draw.circle(window, silver, (x + 20, y + 30), 2)  # Kapı kolu

    # Yan aynalar
    pygame.draw.circle(window, silver, (x - 5, y + 15), 3)  # Sol yan ayna
    pygame.draw.circle(window, silver, (x + 30, y + 15), 3)  # Sağ yan ayna

    # Farlar
    pygame.draw.circle(window, white, (x + 40, y + 15), 5)  # Sağ far
    pygame.draw.circle(window, yellow, (x - 10, y + 15), 3)  # Sol farın ışığı
    pygame.draw.circle(window, yellow, (x + 40, y + 15), 3)  # Sağ farın ışığı
    
    # Tekerlekler (3 tekerlek)
    pygame.draw.circle(window, (0, 0, 0), (x + 15, y + 60), 10)  # Ön tekerlek (kabinin altında)
    pygame.draw.circle(window, (0, 0, 0), (x - 100, y + 60), 10)  # Arka sol tekerlek (arka kasa ortasında)
    pygame.draw.circle(window, (0, 0, 0), (x - 60, y + 60), 10)   # Arka sağ tekerlek (arka kasa ortasında)
    
    pygame.draw.circle(window, (255, 255, 255), (x + 15, y + 60), 5)  # Ön tekerlek jant
    pygame.draw.circle(window, (255, 255, 255), (x - 100, y + 60), 5)  # Arka sol tekerlek jant
    pygame.draw.circle(window, (255, 255, 255), (x - 60, y + 60), 5)   # Arka sağ tekerlek jant

    # Arka kısım detayları
    pygame.draw.rect(window, (255, 140, 0), (x - 140, y + 50, 140, 10))  # Arka kapak
    
    # Arka lambalar (detaylar)
    pygame.draw.circle(window, red, (x - 135, y + 55), 3)  # Sol arka lamba
    pygame.draw.circle(window, red, (x - 105, y + 55), 3)  # Sağ arka lamba
  

# Kamyon konumu
truck_x = 50
truck_y = 515  # Taşlı yolun ortasına yerleştir
truck_speed = 2  # Kamyon hızı
slow_speed = 1    # Kırmızı ışıkta yavaş hızı

# Oyun döngüsü
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(sky_blue)

    # Gökyüzü elemanlarını çiz
    draw_sky_elements()

    # Asfalt yolu ve taşlı yolu çiz
    draw_asphalt_road()
    draw_gravel_road()

    # Trafik ışığını güncelle
    if light_state == 'green':
        light_timer += 1
        if light_timer > 100:  # 100 frame (yaklaşık 4 saniye) sonra ışık sarıya döner
            light_state = 'yellow'
            light_timer = 0
    elif light_state == 'yellow':
        light_timer += 1
        if light_timer > 50:  # 50 frame (yaklaşık 1,6 saniye) sonra ışık kırmızıya döner
            light_state = 'red'
            light_timer = 0
    elif light_state == 'red':
        light_timer += 1
        if light_timer > 100:  # 150 frame (yaklaşık 5 saniye) sonra ışık yeşile döner
            light_state = 'green'
            light_timer = 0

    # Kamyonun hareketini kontrol et
    if truck_x == traffic_light_x:  # Eğer kamyon trafik ışığıyla aynı konumdaysa
        if light_state == 'red':
            pass  # Kırmızı ışıkta dur (konum değiştirme)
        else:
            truck_x += truck_speed  # Yeşil veya sarı ışıkta normal hızda hareket et
    else:  # Eğer kamyon trafik ışığının sağındaysa
        truck_x += truck_speed  # Kamyon trafik ışığının sağında, ışığın durumuna bakmadan hareket et

    # Kamyonun ekranın dışına çıkmasını kontrol et
    if truck_x > SCREEN_WIDTH:  # Ekranın sağ tarafını geçerse
        truck_x = -140  # Kamyonu yeniden başlat (soldan başla)

    # Trafik ışığını çiz
    draw_traffic_light(traffic_light_x, 360, light_state)

    # Kamyonu çiz
    draw_truck(truck_x, truck_y)

    # Ekranı güncelle
    pygame.display.flip()
    clock.tick(60)  # FPS'yi 60'da sabitle  