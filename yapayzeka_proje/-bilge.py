import pygame

"""# Pygame'i başlat
pygame.init()

# Ekran boyutu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trafik Levhalari ve Dubalar")

# Renkler
WHITE = (255, 255, 255)

# Background
background = pygame.image.load('Anayol.png')

# Görselleri yükle
yaya_gecidi_img = pygame.image.load("yayagecidi.png")
tali_yol_img = pygame.image.load("yolver.png")
dur_img = pygame.image.load("durlevhasi.jpg")
yol_calismasi_img = pygame.image.load("yolcalismasi.png")
duba_img = pygame.image.load("duba.png")

# Görsellerin boyutunu ayarla
scale_factor = 0.1  # Görsellerin boyutunu küçültmek için bir ölçek faktörü
yaya_gecidi_img = pygame.transform.scale(yaya_gecidi_img, (int(yaya_gecidi_img.get_width() * scale_factor), int(yaya_gecidi_img.get_height() * scale_factor)))
tali_yol_img = pygame.transform.scale(tali_yol_img, (int(tali_yol_img.get_width() * scale_factor), int(tali_yol_img.get_height() * scale_factor)))
dur_img = pygame.transform.scale(dur_img, (int(dur_img.get_width() * scale_factor), int(dur_img.get_height() * scale_factor)))
yol_calismasi_img = pygame.transform.scale(yol_calismasi_img, (int(yol_calismasi_img.get_width() * scale_factor), int(yol_calismasi_img.get_height() * scale_factor)))
duba_img = pygame.transform.scale(duba_img, (int(duba_img.get_width() * scale_factor), int(duba_img.get_height() * scale_factor)))

# Trafik levhalarını yerleştir
def draw_signs():
    screen.blit(yaya_gecidi_img, (100, 100))       # Yaya geçidi levhası
    screen.blit(tali_yol_img, (200, 200))          # Tali yol levhası
    screen.blit(dur_img, (300, 100))               # Dur levhası
    screen.blit(yol_calismasi_img, (400, 300))     # Yol çalışması levhası
    screen.blit(duba_img, (500, 400))              # Duba

# Ana döngü
running = True
while running:
   
    # Trafik levhalarını çiz
    draw_signs()

    # Olayları kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ekranı güncelle
    pygame.display.flip()

# Pygame'i kapat
pygame.quit() """



# Pygame'i başlat
pygame.init()

# Ekran boyutunu ayarla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("LevhalarCalisma")

# Arka plan görselini yükle ve ekran boyutuna göre ölçeklendir
try:
    background_img = pygame.image.load("background.jpg")  # Arka plan resminin dosya adını doğru yaz
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Ekran boyutuna ölçeklendir
except pygame.error:
    print("Arka plan resmi yüklenemedi. Lütfen dosya yolunu kontrol edin.")
    pygame.quit()

# Görselleri yükle
yaya_gecidi_img = pygame.image.load("yayagecidi.png")
tali_yol_img = pygame.image.load("yolver.png")
dur_img = pygame.image.load("durlevhasi.png")
yol_calismasi_img = pygame.image.load("yolcalismasi.png")
duba_img = pygame.image.load("duba.png")
donel_kasvak = pygame.image.load("donelkavsak.png")
unlem = pygame.image.load("unlem.png")
yolcalismasi = pygame.image.load("yolcalismasi2.png")
yolengel = pygame.image.load("yolengel.png")


# Görsellerin boyutunu ayarla
scale_factor = 0.1  # Görsellerin boyutunu küçültmek için bir ölçek faktörü
yaya_gecidi_img = pygame.transform.scale(yaya_gecidi_img, (int(yaya_gecidi_img.get_width() * scale_factor), int(yaya_gecidi_img.get_height() * scale_factor)))
tali_yol_img = pygame.transform.scale(tali_yol_img, (int(tali_yol_img.get_width() * scale_factor), int(tali_yol_img.get_height() * scale_factor)))
dur_img = pygame.transform.scale(dur_img, (int(dur_img.get_width() * 0.2), int(dur_img.get_height() * 0.2)))
yol_calismasi_img = pygame.transform.scale(yol_calismasi_img, (int(yol_calismasi_img.get_width() * scale_factor), int(yol_calismasi_img.get_height() * scale_factor)))
duba_img = pygame.transform.scale(duba_img, (int(duba_img.get_width() * scale_factor), int(duba_img.get_height() * scale_factor)))
donel_kasvak = pygame.transform.scale(donel_kasvak, (int(donel_kasvak.get_width() * scale_factor), int(donel_kasvak.get_height() * scale_factor)))
yolcalismasi = pygame.transform.scale(yolcalismasi, (int(yolcalismasi.get_width() * 0.2), int(yolcalismasi.get_height() * 0.2)))
yolengel = pygame.transform.scale(yolengel, (int(yolcalismasi.get_width() * 1), int(yolengel.get_height() * 0.2)))

# Ana döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Arka planı çiz
    screen.blit(background_img, (0, 0))  # Resmi (0, 0) konumuna yerleştir

     # Tabelaların yerlerini ayarla
    yaya_gecidi_pos = (200, 30)
    tali_yol_pos = (160, 160)
    dur_pos = (430, 180)
    yol_calismasi_pos = (400, 300)
    duba_pos = (350, 10)
    donel_kasvak_pos = (200, 400)
    yolcalismasi_pos = (400,30)
    yolengel_pos = (380,400)
    

    # Tabelaları yerleştir (şeffaflık ile)
    screen.blit(yaya_gecidi_img, yaya_gecidi_pos)
    screen.blit(tali_yol_img, tali_yol_pos)
    screen.blit(dur_img, dur_pos)
    screen.blit(yol_calismasi_img, yol_calismasi_pos)
    screen.blit(duba_img, duba_pos)
    screen.blit(donel_kasvak, donel_kasvak_pos)
    screen.blit(yolcalismasi,yolcalismasi_pos)
    screen.blit(yolengel, yolengel_pos)
    

    # Ekranı güncelle
    pygame.display.flip()

# Pygame'i kapat
pygame.quit()
