import pygame
import pygame.draw

pygame.init()


#EKRAN
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kavsak Modeli")


#RENKLER
KOYU_GRI = (50, 50, 50)  # YOL RENGİ
ACIK_GRI = (200, 200, 200)  # ŞERİT RENGİ
BEYAZ = (255, 255, 255)  # YOL KENARLARI
CIM_YESILI= (0,128,0) # ÇİMENLER
HAVUZ_MAVISI= (0,191,255) # MERKEZ DAİRE


#EKRAN ARKA PLAN RENGİ
screen.fill(CIM_YESILI)


#BİLEŞEN ÖZELLİKLERİ
yol_width = 100
serit_width = 10
serit_gap = 30
yol_radius= 125
havuz_radius= 25
ic_line_radius= 25
dis_line_radius=85





#ŞERİT ÇİZGİLERİ

def draw_serit_cizgileri():
    for y in range(0,300, serit_gap * 2):
        pygame.draw.rect(screen, ACIK_GRI, (895, y, serit_width, serit_gap))
    for y in range(530,1500, serit_gap * 2):
        pygame.draw.rect(screen, ACIK_GRI,(895, y, serit_width, serit_gap))
    for x in range(0,750, serit_gap * 2):
        pygame.draw.rect(screen,ACIK_GRI,(x,395, serit_gap, serit_width))
    for x in range(1030,1500, serit_gap * 2):
        pygame.draw.rect(screen,ACIK_GRI,(x,395, serit_gap, serit_width))









#DİKEY YOL ÇİZİMİ

pygame.draw.rect(screen,KOYU_GRI,(850,0,yol_width,800))

#YATAY YOL ÇİZİMİ

pygame.draw.rect(screen,KOYU_GRI,(0,350,1000,yol_width))

#YOL KENARI ÇİZGİLERİ

pygame.draw.line(screen,BEYAZ,(800,350),(0,350),2)
pygame.draw.line(screen,BEYAZ,(900,450),(0,450),2)
pygame.draw.line(screen,BEYAZ,(1000,450),(1500,450),2)
pygame.draw.line(screen,BEYAZ,(1000,350),(1500,350),2)
pygame.draw.line(screen,BEYAZ,(950,0),(950,500),2)
pygame.draw.line(screen,BEYAZ,(850,0),(850,500),2)
pygame.draw.line(screen,BEYAZ,(850,300),(850,1000),2)
pygame.draw.line(screen,BEYAZ,(950,300),(950,1000),2)

#DAİRESEL YOLUN DIŞ ÇİZGİLERİ

pygame.draw.circle(screen,BEYAZ,(932,370),dis_line_radius,2)
pygame.draw.circle(screen,BEYAZ,(868,370),dis_line_radius,2)
pygame.draw.circle(screen,BEYAZ,(868,430),dis_line_radius,4)
pygame.draw.circle(screen,BEYAZ,(932,430),dis_line_radius,4)




#DAİRESEL YOL
pygame.draw.circle(screen,KOYU_GRI,(900,400),yol_radius,0)

#ORTADAKİ HAVUZ
pygame.draw.circle(screen,HAVUZ_MAVISI,(900,400),havuz_radius,0)

#HAVUZUN ETRAFINDAKİ BEYAZ ÇİZGİ
pygame.draw.circle(screen,BEYAZ,(900,400),ic_line_radius,2)




draw_serit_cizgileri()
#PENCERENİN AÇIK KALMA DÖNGÜSÜ
pygame.display.update()
durum= True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum= False
pygame.quit()
