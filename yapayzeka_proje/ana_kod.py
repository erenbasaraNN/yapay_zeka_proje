import pygame
import sys
import time

pygame.init()

genislik=1000
yukseklik=800
pencere=pygame.display.set_mode((genislik,yukseklik))

#renkler
arkaplan = (139, 169, 119)
pastel_pink = (255, 182, 193)
brown = (80, 40, 10)
dark_gray = (169, 169, 169)
office_color = (200, 200, 200)
white = (255, 255, 255)
tree_green = (34, 139, 34)  # Ağaç yeşili
curtain_color_1 = (255, 215, 0)  # Altın sarısı perde
curtain_color_2 = (255, 239, 204)  # Krem rengi perde
cornice_color = (139, 69, 19)  # Kahverengi korniş
asphalt_color = (50, 50, 50)  # Asfalt yol için koyu gri
black = (0, 0, 0)  # Tekerlekler için siyah
silver = (192, 192, 192)  # Jant rengi
white = (255, 255, 255)  # Farlar, pencere çerçeveleri ve ön ızgara için white
yellow = (255, 255, 0)  # Sarı renk tanımlaması
red = (255, 0, 0)  # Kırmızı
green = (0, 255, 0)  # Yeşil
red_off = (100, 0, 0)
yellow_off = (100, 100, 0)
green_off = (0, 100, 0)
pink = (255, 192, 203)  # Pembe
havuz_mavisi= (0,191,255) # MERKEZ DAİRE
stone_light = (169, 169, 169)  # Taşlı yol için açık gri
stone_dark = (105, 105, 105)  # Taşlı yol için koyu gri


# Yazı tipi ayarları
font = pygame.font.Font(None, 20)
garage_font = pygame.font.Font(None, 18)

# Arka plan görselini yükle ve ekran boyutuna göre ölçeklendir
kazi_alani = pygame.image.load("kazi_alani.png")  # Arka plan resminin dosya adını doğru yaz
kazi_alani = pygame.transform.scale(kazi_alani, (500,400))  # Ekran boyutuna ölçeklendir

# Dekorasyon Resimleri ve Pozisyonları
bankta_oturan_adam=pygame.image.load("bankta_oturan_adam.png")
amele=pygame.image.load("amele.png")
kazma=pygame.image.load("kazma.png")
veteriner=pygame.image.load("veteriner.png")
cop_kutusu=pygame.image.load("cop_kutusu.png")
vinc=pygame.image.load("vinc.png")
agac=pygame.image.load("agac.png")


# Detaylı kamyon çizme fonksiyonu
def draw_truck(x, y):
    # Kamyon gövdesi (turuncu)
    pygame.draw.rect(pencere, (255, 140, 0), (x - 140, y, 140, 60), border_radius=8)  # Kamyon gövdesi
    
    # Tuğla şekilli yük (daha detaylı)
    for i in range(5):  # Tuğlaları çizmek için satırlar
        for j in range(2):  # İki satır tuğla
            brick_color = (210, 105, 30) if (i + j) % 2 == 0 else (180, 90, 20)  # Farklı renk tonları
            pygame.draw.rect(pencere, brick_color, (x - 125 + i * 20, y + 10 + j * 10, 18, 8))  # Tuğla blokları

    # Saydam yük örtüsü
    overlay_surface = pygame.Surface((120, 30), pygame.SRCALPHA)  # Saydam yüzey
    overlay_surface.fill((200, 200, 200, 100))  # Hafif saydam gri renk
    pencere.blit(overlay_surface, (x - 130, y + 10))  # Yük örtüsünü çiz

    # Kabin (sürücü bölümü)
    pygame.draw.rect(pencere, (255, 140, 0), (x, y + 10, 30, 50), border_radius=8)  # Kabin
    pygame.draw.polygon(pencere, (255, 140, 0), [(x, y + 10), (x + 30, y), (x + 30, y + 10)])  # Kabin üstü

    # Kabin detayları (kapı ve pencere)
    pygame.draw.rect(pencere, white, (x + 5, y + 20, 15, 20))  # Kapı
    pygame.draw.rect(pencere, white, (x + 10, y + 15, 10, 15))  # Pencere
    
    # Kapı kolu
    pygame.draw.circle(pencere, silver, (x + 20, y + 30), 2)  # Kapı kolu

    # Yan aynalar
    pygame.draw.circle(pencere, silver, (x - 5, y + 15), 3)  # Sol yan ayna
    pygame.draw.circle(pencere, silver, (x + 30, y + 15), 3)  # Sağ yan ayna

    # Farlar
    pygame.draw.circle(pencere, white, (x + 40, y + 15), 5)  # Sağ far
    pygame.draw.circle(pencere, yellow, (x - 10, y + 15), 3)  # Sol farın ışığı
    pygame.draw.circle(pencere, yellow, (x + 40, y + 15), 3)  # Sağ farın ışığı
    
    # Tekerlekler (3 tekerlek)
    pygame.draw.circle(pencere, (0, 0, 0), (x + 15, y + 60), 10)  # Ön tekerlek (kabinin altında)
    pygame.draw.circle(pencere, (0, 0, 0), (x - 100, y + 60), 10)  # Arka sol tekerlek (arka kasa ortasında)
    pygame.draw.circle(pencere, (0, 0, 0), (x - 60, y + 60), 10)   # Arka sağ tekerlek (arka kasa ortasında)
    
    pygame.draw.circle(pencere, (255, 255, 255), (x + 15, y + 60), 5)  # Ön tekerlek jant
    pygame.draw.circle(pencere, (255, 255, 255), (x - 100, y + 60), 5)  # Arka sol tekerlek jant
    pygame.draw.circle(pencere, (255, 255, 255), (x - 60, y + 60), 5)   # Arka sağ tekerlek jant

    # Arka kısım detayları
    pygame.draw.rect(pencere, (255, 140, 0), (x - 140, y + 50, 140, 10))  # Arka kapak
    
    # Arka lambalar (detaylar)
    pygame.draw.circle(pencere, red, (x - 135, y + 55), 3)  # Sol arka lamba
    pygame.draw.circle(pencere, red, (x - 105, y + 55), 3)  # Sağ arka lamba


# Ev (baslangic)
def draw_house(x, y):
    pygame.draw.rect(pencere, pastel_pink, (x, y, 100, 100))
    pygame.draw.polygon(pencere, brown, [(x, y), (x + 50, y - 50), (x + 100, y)])
    pygame.draw.rect(pencere, dark_gray, (x + 35, y + 50, 30, 50))  # Kapı
    
    # Pencereler
    pencere_size = 20
    left_pencere = pygame.draw.rect(pencere, black, (x + 10, y + 20, pencere_size, pencere_size), 2)  # Sol pencere
    right_pencere = pygame.draw.rect(pencere, black, (x + 70, y + 20, pencere_size, pencere_size), 2)  # Sağ pencere
    
    # Perdeler
    pygame.draw.rect(pencere, cornice_color, (left_pencere.x - 2, left_pencere.y - 5, pencere_size + 4, 5))  # Sol korniş
    pygame.draw.rect(pencere, cornice_color, (right_pencere.x - 2, right_pencere.y - 5, pencere_size + 4, 5))  # Sağ korniş
    pygame.draw.rect(pencere, curtain_color_1, (left_pencere.x + 2, left_pencere.y + 2, pencere_size - 4, pencere_size // 2))  # Sol perde
    pygame.draw.rect(pencere, curtain_color_2, (left_pencere.x + 2, left_pencere.y + pencere_size // 2 + 2, pencere_size - 4, pencere_size // 2))  # Sol alt perde
    pygame.draw.rect(pencere, curtain_color_1, (right_pencere.x + 2, right_pencere.y + 2, pencere_size - 4, pencere_size // 2))  # Sağ perde
    pygame.draw.rect(pencere, curtain_color_2, (right_pencere.x + 2, right_pencere.y + pencere_size // 2 + 2, pencere_size - 4, pencere_size // 2))  # Sağ alt perde


# Ağaç çizdirme fonksiyonu
def draw_tree(x, y):
    pygame.draw.rect(pencere, brown, (x, y, 15, 40))
    pygame.draw.polygon(pencere, tree_green, [(x - 25, y), (x + 7.5, y - 50), (x + 45, y)])

# Ofis (son)
def draw_office(x, y):
    pygame.draw.rect(pencere, office_color, (x, y, 100, 100))
    pygame.draw.rect(pencere, black, (x, y - 10, 100, 20))  # Düz çatı
    text = font.render("OFFICE", True, white)
    pencere.blit(text, (x + 25, y - 8))
    
    for i in range(3):
        pygame.draw.rect(pencere, black, (x + 18 + i * 25, y + 20, 15, 15), 2)  # Üst pencereler
    for i in range(3):
        pygame.draw.rect(pencere, black, (x + 18 + i * 25, y + 60, 15, 15), 2)  # Alt pencereler


# Kavşak Oluşturma

yol_width = 100
serit_width = 10
serit_gap = 45
yol_radius= 25
havuz_radius= 10
ic_line_radius= 10
dis_line_radius=15

def draw_kavsak():
    pygame.draw.circle(pencere,tree_green,(110,700),yol_radius,0) #kavşak
    pygame.draw.circle(pencere,white,(110,700),yol_radius,3)
    pygame.draw.circle(pencere,havuz_mavisi,(110,700),havuz_radius,0) #kavşak içinde havuz
    pygame.draw.circle(pencere,white,(110,700),ic_line_radius,2) #havuz etrafına çizgi


#YOLLAR
def draw_ust_yatay_road():
    pygame.draw.rect(pencere,asphalt_color,(100,50,900,yol_width))

def draw_alt_yatay_road():
    pygame.draw.rect(pencere,asphalt_color,(0,650,850,yol_width))

def draw_sol_dikey_road():
    pygame.draw.rect(pencere,asphalt_color,(50,150,yol_width,550))

def draw_sag_dikey_road():
    pygame.draw.rect(pencere,asphalt_color,(850,50,yol_width,600))

def draw_serit_cizgileri():
    for y in range(200,700, serit_gap * 2):
        pygame.draw.rect(pencere, white,(100, y, serit_width, serit_gap)) #sol dikey yol
    for y in range(100,650, serit_gap * 2):
        pygame.draw.rect(pencere, white,(900, y, serit_width, serit_gap)) #sağ dikey yol
    for x in range(0,850, serit_gap * 2):
        pygame.draw.rect(pencere,white,(x,700, serit_gap, serit_width)) #alt yatay yol
    for x in range(140,1000, serit_gap * 2):
        pygame.draw.rect(pencere,white,(x,100, serit_gap, serit_width)) #üst yatay yol


# Çapraz dar taşlı yol çizme fonksiyonu
def draw_diagonal_gravel_road():
    block_width = 15  # genişlik
    block_height = 6
    start_x = 100  # Yolun sol üst köşedeki başlangıç x konumu 
    start_y = 150  # Yolun sol üst köşedeki başlangıç y konumu 
    num_rows = (yukseklik + genislik) // block_height  # Sağ alt köşeye kadar gitmesi için satır sayısı

    for row in range(num_rows):
        for col in range(10):  # Yol 10 piksel kalınlıkta olacak
            # Renkleri sırayla seçili
            color = stone_light if (row + col) % 2 == 0 else stone_dark
            
            # Çapraz yol için x ve y konumlarını ayarlıyoruz
            x = start_x + col * block_width + row * (block_width // 1.6) #x ve y yolun bitiş konumları 1.7 ise eğimi
            y = start_y + row * block_height
            
            # Sağ alt köşeyi aşmamak için kontrol
            if x < 850 and y < 650:
                pygame.draw.rect(pencere, color, (x, y, block_width, block_height))


# Levhaları yükle
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


isik_radius = 10
# TRAFİK IŞIĞINDA IŞIK RENGİNİN DEĞİŞİMİ
def draw_trafik_isigi(x, y, light_color):
    # Trafik ışığı çizimi
    pygame.draw.rect(pencere, (0, 0, 0), (x, y, 20, 60))
    pygame.draw.circle(pencere, green_off if light_color != "yesil" else green, (x + 10, y + 10), isik_radius)
    pygame.draw.circle(pencere, yellow_off if light_color != "sari" else yellow, (x + 10, y + 30), isik_radius)
    pygame.draw.circle(pencere, red_off if light_color != "kirmizi" else red, (x + 10, y + 50), isik_radius)



line_height = 5 #yaya gecidi şeridinin genişliği
cizgiler_arasi_aralik = 5
line_width = 50
def draw_yatay_yaya_gecidi():
    # Çizgi boyutları
    for i in range(5,15): #bir yolun genişliği 5-15 aralığında yani 10 piksel
        yaya_gecidi = pygame.Rect(750, i * (line_height + cizgiler_arasi_aralik), line_width, line_height) #750 x eksenindeki konumu
        pygame.draw.rect(pencere, white if i % 2 == 0 else asphalt_color, yaya_gecidi)


def draw_dikey_yaya_gecidi():
    # Dikey yaya geçidi çizgilerini çiz
    for i in range(85,95): #bir yolun genişliği 85-95 aralığında yani 10 piksel
        yaya_gecidi = pygame.Rect(i * (line_height + cizgiler_arasi_aralik),300 , line_height, line_width) #300 y eksenindeki konumu
        pygame.draw.rect(pencere, white if i % 2 == 0 else asphalt_color, yaya_gecidi)


def draw_car(x, y, color):
    pygame.draw.rect(pencere, color, (x, y, 120, 40), border_radius=15)  # Araba gövdesi
    pygame.draw.polygon(pencere, color, [(x + 20, y), (x + 110, y), (x + 90, y - 20), (x + 40, y - 20)])  # Üst gövde
    pygame.draw.circle(pencere, white, (x + 120, y + 15), 5)  # Sağ ön far
    pygame.draw.circle(pencere, white, (x , y + 15), 5)  # Sol ön far
    pygame.draw.rect(pencere, white, (x + 50, y + 10, 30, 5))  # Ön ızgara
    pygame.draw.polygon(pencere, white, [(x + 15, y - 10), (x + 20, y - 5), (x + 15, y - 5)])  # Sol ayna
    pygame.draw.polygon(pencere, white, [(x + 110, y - 10), (x + 105, y - 5), (x + 110, y - 5)])  # Sağ ayna
    pygame.draw.rect(pencere, white, (x + 35, y - 15, 60, 15), border_radius=5)  # Ön cam
    pygame.draw.circle(pencere, silver, (x + 20, y + 30), 18)  # Sol tekerlek gölgesi
    pygame.draw.circle(pencere, black, (x + 20, y + 30), 15)  # Sol tekerlek lastiği
    pygame.draw.circle(pencere, silver, (x + 20, y + 30), 7)  # Sol jant
    pygame.draw.circle(pencere, silver, (x + 100, y + 30), 18)  # Sağ tekerlek gölgesi
    pygame.draw.circle(pencere, black, (x + 100, y + 30), 15)  # Sağ tekerlek lastiği
    pygame.draw.circle(pencere, silver, (x + 100, y + 30), 7)  # Sağ jant







#--------------------------------------------------------------------------------------------------------

# Bütün Fonksiyonları Çağırdığımız ve Ana Ekranı Oluşturduğumuz MAIN Fonksiyon

def main():
    pygame.display.update()
    # TRAFİK IŞIĞI ZAMANLAYICISI
    clock = pygame.time.Clock()
    start_time = time.time()
    light_color = "yesil"  # Trafik ışığı başlangıcı

    #NPC'ler


    # NPC Arabalar
    car_x_yellow = 50  # Sarı arabanın başlangıç pozisyonu
    car_y_yellow = 690  # Taşlı yol üzerinde olacak şekilde y konumu
    car_speed_yellow = 2  # Sarı arabanın hızı

    car_x_red = 1000  # Kırmızı arabanın başlangıç pozisyonu
    car_y_red = 40  # Asfalt yol üzerinde olacak şekilde y konumu
    car_speed_red = 2  # Kırmızı arabanın hızı (daha hızlı)

    kedi=pygame.image.load("kedi.png")
    kedi_x=0
    kedi_y=750
    kedi_speed=1


    npc_kopekli_abla_sol = pygame.image.load("npc_kopekli_abla_sol.png")
    npc_kopekli_abla_sag=pygame.image.load("npc_kopekli_abla_sag.png")

    npc_adam_on=pygame.image.load("npc_adam_on.png")
    npc_adam_arka=pygame.image.load("npc_adam_arka.png")


    # Karakter başlangıç pozisyonu ve hız

    npc_kopekli_abla_x=920
    npc_kopekli_abla_y=270
    npc_kopekli_abla_speed=0.5
    gidis_sol = True

    npc_adam_x=750
    npc_adam_y=0
    npc_adam_speed=0.5
    gidis_asagi=True



    #--------------------------------------------------------------------------------------------------------------


    #Ana Ekranı Çalıştırma ve Kapatma
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()

        #Arkaplan rengini uygula
        pencere.fill(arkaplan)

        # Kazı Alanındaki Yer Resmini Ekrana Yazdır
        pencere.blit(kazi_alani, (150, 150))  # Resmi (0, 0) konumuna yerleştir



        #--------------------------------------------------------------------------------------------------------------
        
        # Trafik Işığı Renk Döngüsü
        #20 SANİYE YEŞİL, 3 SANİYE SARI, 10 SANİYE KIRMIZI, 3 SANİYE SARI, 20 SANİYE YEŞİL... OLACAK ŞEKİLDE...
        elapsed_time = (time.time() - start_time) % 36  # TOPLAM 36 SANİYE

        if elapsed_time < 20:
            light_color = "yesil"
        elif elapsed_time < 23:
            light_color = "sari"
        elif elapsed_time < 33:
            light_color = "kirmizi"
        else:
            light_color = "sari"
        

        
        car_x_red -= car_speed_red
        car_x_yellow += car_speed_yellow
        kedi_x+=kedi_speed

        
        # NPCLER

        # NPC Arabalar ve Kedi
        if car_x_yellow > 800: # Sarı Araba Alttaki Yoldan Geçecek
            car_x_yellow = -100

        if car_x_red <100: # Kırmızı Araba Yukardaki Yoldan
            car_x_red=1100

        if kedi_x > genislik:
            kedi_x=-50


        # Sağdaki Dikey Yolda Yaya Geçidinden Geçen Köpekli Kadın
        if gidis_sol:
            npc_kopekli_abla=npc_kopekli_abla_sol
            npc_kopekli_abla_x -= npc_kopekli_abla_speed
            if npc_kopekli_abla_x < 800:  # Sol sınır
                gidis_sol = False
                npc_kopekli_abla=npc_kopekli_abla_sag
        else:
            npc_kopekli_abla_x += npc_kopekli_abla_speed
            if npc_kopekli_abla_x > 950:  # Sağ sınır
                gidis_sol = True
                npc_kopekli_abla=npc_kopekli_abla_sol


        # Üst Yatay Yolda Yaya Geçidinden Geçen Yalnız Yıkık Adam
        if gidis_asagi:
            npc_adam=npc_adam_on
            npc_adam_y += npc_adam_speed
            if npc_adam_y >100:  # Aşağı sınır
                gidis_asagi = False
                npc_adam=npc_adam_arka
        else:
            npc_adam_y -= npc_adam_speed
            if npc_adam_y <-75:  # Yukarı sınır
                gidis_asagi = True
                npc_adam=npc_adam_on





        # Fonksiyonları Ekrana Yazdırma

        draw_diagonal_gravel_road()
        draw_alt_yatay_road()
        draw_sol_dikey_road()
        draw_ust_yatay_road()
        draw_sag_dikey_road()
        draw_serit_cizgileri()
        draw_kavsak()
        pencere.blit(agac,(200, 570)) #alttaki ağaçlar
        pencere.blit(agac,(350, 570))
        pencere.blit(agac,(550, 570))
        pencere.blit(agac,(700, 570))
        pencere.blit(agac,(950, 250)) #sağdaki ağaçlar
        pencere.blit(agac,(950, 450))
        pencere.blit(agac,(0, 250)) #soldaki ağaçlar
        pencere.blit(agac,(0, 450))
        draw_trafik_isigi(950,350, light_color) #sağ dikey yoldaki trafik ışığı
        draw_trafik_isigi(150,590, light_color) #kavşaktaki trafik ışığı
        

        # Yaya Geçitlerini Ekle
        draw_yatay_yaya_gecidi()
        draw_dikey_yaya_gecidi()

        # NPC'leri Ekle
        pencere.blit(npc_kopekli_abla, (npc_kopekli_abla_x,npc_kopekli_abla_y))
        pencere.blit(npc_adam,(npc_adam_x,npc_adam_y))
        pencere.blit(kedi,(kedi_x,kedi_y))
        draw_car(car_x_yellow, car_y_yellow, yellow)  # Sarı araba
        draw_car(car_x_red, car_y_red, red)  # Kırmızı araba
        draw_truck(600,80)

        
 


        # Binaları Ekle
        draw_house(50, 50)
        draw_office(850,650)
    

        # Tabelaları Konumlarına Göre Yerleştir (şeffaflık ile)
        pencere.blit(yaya_gecidi_img, (700,100))
        pencere.blit(tali_yol_img, (730,530))
        pencere.blit(dur_img, (-60,700))
        pencere.blit(yol_calismasi_img, (350, 250)) #yolu kapatma tabelası
        pencere.blit(duba_img, (350,80))
        pencere.blit(donel_kasvak, (0,520))
        pencere.blit(yolcalismasi,(200, 120)) #yolda çalışma olduğunu gösteren 3lü tabela
        pencere.blit(yolengel, (400,300)) #taşlar
        
        # Dekorasyon Resimlerini ve Konumlarını Yükle
        pencere.blit(amele,(550,350))
        pencere.blit(bankta_oturan_adam,(450,580))
        pencere.blit(kazma,(400,400))
        pencere.blit(veteriner,(680,230))
        pencere.blit(cop_kutusu,(820,150))
        pencere.blit(vinc,(200,400))


        
        pygame.display.flip()
        clock.tick(60)
        
 
if __name__ == "__main__":
    main()