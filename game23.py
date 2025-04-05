import pygame
import random
import time
import os


# Ініціалізація Pygame
pygame.init()
# Розміри екрану
WIDTH, HEIGHT = 600, 600

# Визначення кольорів
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BK = (0, 120, 0)

# Початкові змінні
money = 0
act_menu_active = False
running = True

# Налаштування вікна гри
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly")
# Шрифт
font = pygame.font.Font(None, 36)
# Шлях до папки з зображеннями
IMG_PATH = "assets/"

# Музика фонової мелодії
pygame.mixer.init()
pygame.mixer.music.load('assets/monopolu_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
# Завантаження зображень кубика (1-6)
diceImg = []
for i in range(1,7):
    diceImg.append(pygame.image.load(os.path.join(IMG_PATH+f"Frame 8-{i}.jpg")))
    diceImg[i-1] = pygame.transform.scale(diceImg[i-1], (50, 50))

# Завантаження і масштабування зображень для "плиток" (Tile)
bmw = pygame.image.load(os.path.join(IMG_PATH+"bmw.png"))
bmw = pygame.transform.scale(bmw, (60, 100))

birga = pygame.image.load(os.path.join(IMG_PATH+"img_3.png"))
birga = pygame.transform.scale(birga, (100, 100))

adidas = pygame.image.load(os.path.join(IMG_PATH+"img_4.png"))
adidas = pygame.transform.scale(adidas, (60, 100))

roshen = pygame.image.load(os.path.join(IMG_PATH+"img_5.png"))
roshen = pygame.transform.scale(roshen, (100, 60))

mak = pygame.image.load(os.path.join(IMG_PATH+"img_6.png"))
mak = pygame.transform.scale(mak, (60, 100))

start = pygame.image.load(os.path.join(IMG_PATH+"img_7.png"))
start = pygame.transform.scale(start, (100, 100))

kfc = pygame.image.load(os.path.join(IMG_PATH+"img_8.png"))
kfc = pygame.transform.scale(kfc, (60, 100))

mers = pygame.image.load(os.path.join(IMG_PATH+"img_9.png"))
mers = pygame.transform.scale(mers, (100, 60))

haribo = pygame.image.load(os.path.join(IMG_PATH+"img_10.png"))
haribo = pygame.transform.scale(haribo, (100, 60))

nike = pygame.image.load(os.path.join(IMG_PATH+"img_11.png"))
nike = pygame.transform.scale(nike, (100, 60))

pepsi = pygame.image.load(os.path.join(IMG_PATH+"img_12.png"))
pepsi = pygame.transform.scale(pepsi, (60, 100))

cola = pygame.image.load(os.path.join(IMG_PATH+"img_13.png"))
cola = pygame.transform.scale(cola, (100, 60))

samsa = pygame.image.load(os.path.join(IMG_PATH+"img_14.png"))
samsa = pygame.transform.scale(samsa, (100, 60))

apple = pygame.image.load(os.path.join(IMG_PATH+"img_15.png"))
apple = pygame.transform.scale(apple, (60, 100))

fora = pygame.image.load(os.path.join(IMG_PATH+"img_16.png"))
fora = pygame.transform.scale(fora, (100, 60))

atb = pygame.image.load(os.path.join(IMG_PATH+"img_17.png"))
atb = pygame.transform.scale(atb, (100, 60))

comfy = pygame.image.load(os.path.join(IMG_PATH+"img_18.jpg"))
comfy = pygame.transform.scale(comfy, (100, 60))

cit = pygame.image.load(os.path.join(IMG_PATH+"img_19.png"))
cit = pygame.transform.scale(cit, (100, 60))

steam = pygame.image.load(os.path.join(IMG_PATH+"img_20.png"))
steam = pygame.transform.scale(steam, (100, 60))

lays = pygame.image.load(os.path.join(IMG_PATH+"img_21.png"))
lays = pygame.transform.scale(lays, (100, 60))

epic = pygame.image.load(os.path.join(IMG_PATH+"img_22.png"))
epic = pygame.transform.scale(epic, (60, 100))

nice = pygame.image.load(os.path.join(IMG_PATH+"good_time.png"))
nice = pygame.transform.scale(nice, (100, 100))

bad = pygame.image.load(os.path.join(IMG_PATH+"bad_time.png"))
bad = pygame.transform.scale(bad, (100, 100))

luk = pygame.image.load(os.path.join(IMG_PATH+"img_23.png"))
luk = pygame.transform.scale(luk, (60, 100))

log = pygame.image.load(os.path.join(IMG_PATH+"img_24.png"))
log = pygame.transform.scale(log, (60, 100))

hup = pygame.image.load(os.path.join(IMG_PATH+"img_25.png"))
hup = pygame.transform.scale(hup, (60, 100))

net = pygame.image.load(os.path.join(IMG_PATH+"img_26.png"))
net = pygame.transform.scale(net, (60, 100))

meg = pygame.image.load(os.path.join(IMG_PATH+"img_27.png"))
meg = pygame.transform.scale(meg, (60, 100))

chill_zone = pygame.image.load(os.path.join(IMG_PATH+"chill_zone.png"))
chill_zone = pygame.transform.scale(chill_zone, (100, 100))





# === Клас плитки гри ===
class Tile:
    def __init__(self,number, x, y , weight, height, color):
        self.number = number
        self.posx = x
        self.posy = y
        self.weight = weight
        self.height = height
        self.color = color
        self.price = 100+50*self.number
        self.isitfree = None
        self.rent_paid = False
        self.Rect = pygame.Rect(self.posx, self.posy, self.weight, self.height)

    # Малює прямокутник плитки
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.Rect)

    # Малює плитку з картинкою і ціною
    def img_draw(self, surface, image):
        image = pygame.transform.scale(image, (self.weight, self.height))
        surface.blit(image, (self.posx, self.posy))
        pygame.draw.rect(surface, self.color, self.Rect, 3)

        if self.color != (250, 0, 0):
            price_font = pygame.font.Font(None, 24)
            price_text = price_font.render(f"{self.price}$", True, BK)
            text_x = self.posx + (self.weight - price_text.get_width()) // 2
            text_y = self.posy + self.height - price_text.get_height() - 5
            surface.blit(price_text, (text_x, text_y))


# === Клас гравця ===
class player:
    def __init__(self, color):
        self.money = 5000
        self.color = color
        self.pos = 0
        self.Rect = pygame.Rect(20, 20, 10, 15)
        self.my = []

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.Rect)

    def move(self, number, tiles, surface):  # Рух гравця по полю
        for i in range(number):
            if self.pos >= 27:
                self.pos -= 27
                self.pos += 1
            else:
                self.pos += 1
            if self.color == (250, 0, 0):
                x = 20 # 30 40 60
                y = 20 # 30 40 60
            if self.color == (0, 250, 0):
                x = 40 # 30 40 60
                y = 20 # 30 40 60
            if self.color == (0, 0, 250):
                x = 60  # 30 40 60
                y = 20  # 30 40 60
            if self.color == (250, 250, 0):
                x = 80 # 30 40 60
                y = 20 # 30 40 60
            self.Rect = pygame.Rect(tiles[self.pos].posx + x, tiles[self.pos].posy + y, 10, 15)
            self.draw(surface)

        # Нагорода за стартову плитку
        if self.pos == 7:
            self.money += 400

        # Штраф на певній плитці
        if self.pos == 21:
            if self.money >= 400:
                self.money -= 400
            else:
                self.money = 0

    # Виводить кількість грошей гравця
    def monkey(self, surface):
        text = font.render(f'money:{self.money}$', True, self.color)
        surface.blit(text,(110, 110))


# === Кнопки купівлі / продажу ===
buying = pygame.Rect(200, 230, 200, 40)
buytext = font.render('BUY TILE', True, WHITE)
def buy(surface):
    pygame.draw.rect(surface, RED, buying)
    surface.blit(buytext, (buying.x + 5, buying.y + 5))

selling = pygame.Rect(200, 300, 200, 40)
selltext = font.render('SELL TILE', True, WHITE)
def sell(surface):
    pygame.draw.rect(surface, RED, selling)
    surface.blit(selltext, (selling.x + 5, selling.y + 5))

# === Меню продажу плитки ===
def sell_tile_menu(surface, player):
    menu_width, menu_height = 300, 250
    menu_x, menu_y = (WIDTH - menu_width) // 2, (HEIGHT - menu_height) // 2
    menu_rect = pygame.Rect(menu_x, menu_y, menu_width, menu_height)

    pygame.draw.rect(surface, BLACK, menu_rect)
    pygame.draw.rect(surface, WHITE, menu_rect, 3)

    title_text = font.render("Select a tile to sell:", True, WHITE)
    surface.blit(title_text, (menu_x + 10, menu_y + 10))

    tile_buttons = []
    for index, tile_num in enumerate(player.my):
        tile = tiles[tile_num]
        tile_button = pygame.Rect(menu_x + 10, menu_y + 40 + index * 30, menu_width - 20, 25)
        pygame.draw.rect(surface, RED, tile_button)
        text = font.render(f"Tile {tile.number} - ${tile.price // 2}", True, WHITE)
        surface.blit(text, (tile_button.x + 5, tile_button.y + 5))
        tile_buttons.append((tile_button, tile))

    cancel_button = pygame.Rect(menu_x + 10, menu_y + 40 + len(player.my) * 30, menu_width - 20, 25)
    pygame.draw.rect(surface, RED, cancel_button)
    cancel_text = font.render("dont sell", True, WHITE)
    surface.blit(cancel_text, (cancel_button.x + 5, cancel_button.y + 5))
    tile_buttons.append((cancel_button, None))

    return tile_buttons

# === Логіка продажу плитки ===
def sell_tile(player, tile):
    if tile in tiles and tile.isitfree == player:
        tile.isitfree = None
        player.my.remove(tile.number)
        player.money += tile.price


# === Купівля плитки ===
def buytile(surface, player):
    current_tile = tiles[player.pos]
    if current_tile.color == (250, 0, 0):
        return
    if current_tile.isitfree is None and player.money >= current_tile.price:
        player.money -= current_tile.price
        player.my.append(current_tile.number)
        current_tile.isitfree = player
        current_tile.price = current_tile.price // 2
        check_mono(tiles, player)


# === Монополії: якщо всі 3 плитки з групи — збільшує ціну ===
monopoly = [[1, 2, 3],[4, 5, 6],[8, 9, 10],[11, 12, 13],[15, 16, 17],[18, 19, 20],[22, 23, 24],[25, 26, 27]]

def check_mono(all_tiles, player):
    for mono in monopoly:
        num = 0
        for t in mono:
            if all_tiles[t].isitfree == player:
                num+=1
        if num == 3 and all_tiles[mono[0]].ismono == False:
            for i in mono:
                all_tiles[i].price = all_tiles[i].price * 4
                all_tiles[i].ismono = True


# === Відображення маркерів власника ===
def drawmarker(surface):
    for tile in tiles:
        if tile.isitfree is not None:
            owner_color = tile.isitfree.color
            pygame.draw.circle(
                surface, owner_color,
                (tile.posx + tile.weight - 10, tile.posy + 10), 10
            )

# === Перевірка: чи гравець на чужій плитці ===
def isitown(player):
    current_tile = tiles[player.pos]
    if current_tile.isitfree and current_tile.isitfree != player and not current_tile.rent_paid:
        rent = current_tile.price
        if player.money >= rent:
            player.money -= rent
            current_tile.isitfree.money += rent
            current_tile.rent_paid = True
        else:
            game_over_text = font.render("you're bankrupt!", True, player.color)
            screen.blit(game_over_text, (200, 200))
            pygame.display.flip()
            pygame.time.wait(2000)
            players.remove(player)
            for tile in player.my:
                tiles[tile].isitfree = None
            player.my.clear()

# === Скидання флагів "оплачена оренда" ===
def reset_rent_flags():
    for tile in tiles:
        tile.rent_paid = False


dice_result = None
dice_player_color = None
last_dice_result = None
last_player_color = None
last_switch_time = time.time()

# === Кубик ===
def dice_roll(player_color):
    global dice_player_color
    if player_color != dice_player_color:
        num = random.randint(0,5)
    else:
        num = last_dice_result
    dicerect = diceImg[num].get_rect()
    dicerect.y = 150
    dicerect.x = 200
    dice_player_color = player_color
    return num, dicerect

x = 0
y = 0
# === Створення ігрового поля (tiles) ===
tiles = []
for i in range(130):
    if i==0:
        tiles.append(Tile(i, x, 0, 100, 100, (250, 0, 0)))
        x += 100 + 5
        y += 100 + 5
    elif i <= 3:
        tiles.append(Tile(i, x , 0, 60, 100, (0, 250, 0)))
        x += 60 + 5
    elif i <= 6:
        tiles.append(Tile(i, x, 0, 60, 100, (0, 0, 250)))
        x += 60 + 5
    elif i <= 7:
        tiles.append(Tile(i, x, 0, 100, 100, (250, 0, 0)))
        #x += 100 + 5
    elif i <= 10:
        tiles.append(Tile(i, x, y, 100, 60, (0, 250, 250)))
        y += 60 + 5
    elif i <= 13:
        tiles.append(Tile(i, x, y, 100, 60, (250, 0, 250)))
        y += 60 + 5
    elif i <= 14:
         tiles.append(Tile(i, x, y, 100, 100, (250, 0, 0)))
         x -= 65
    elif i <= 17:
         tiles.append(Tile(i, x, y, 60, 100, (25, 80, 50)))
         x -= 60 + 5
    elif i <= 20:
         tiles.append(Tile(i, x, y, 60, 100, (98, 180, 150)))
         x -= 60 + 5
    elif i <= 21:
         tiles.append(Tile(i, 0, y, 100, 100, (250, 0, 0)))
         x = 0
         y = 495 - 65
    elif i <= 24:
        tiles.append(Tile(i, x, y, 100, 60, (120, 78, 250)))
        y -= 65
    elif i <= 27:
        tiles.append(Tile(i, x, y, 100, 60, (110, 250, 150)))
        y -= 65




# === Гравці ===
r = player((250, 0, 0))
g = player((0, 250, 0))
#b = player((0, 0, 250))
#y = player((250, 250, 0))


players = [r, g]

current_player_index = 0
current_player = players[current_player_index]

tile_selection_active = False
selected_tile_buttons = []

# === Основний ігровий цикл ===
while running:
    current_time = time.time()
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Натискання лівої кнопки миші
            if buying.collidepoint(event.pos):  # Якщо натиснули на кнопку
                current_tile = tiles[current_player.pos]
                if current_tile.isitfree:
                    isitown(current_player)
                else:
                    buytile(screen, current_player)
            if selling.collidepoint(event.pos):
                tile_selection_active = True
                selected_tile_buttons = sell_tile_menu(screen, current_player)
            elif tile_selection_active:
                for button, tile in selected_tile_buttons:
                    if button.collidepoint(event.pos):
                        sell_tile(current_player, tile)
                        tile_selection_active = False
                        break
    screen.fill(BLACK)
    # Кнопки R (кинути кубик) та S (перехід ходу)
    key = pygame.key.get_pressed()
    if key[pygame.K_r]:
        dice_result = dice_roll(current_player.color)
    if dice_result is not None and current_player.color == dice_player_color:
        num, dice_rect = dice_result
        last_dice_result = num
        screen.blit(diceImg[num], dice_rect)
        if  last_player_color != dice_player_color:
            current_player.move(last_dice_result + 1, tiles, screen)
            last_player_color = current_player.color
    if key[pygame.K_s] and (current_time - last_switch_time) >= 2:
        current_player_index = (current_player_index + 1) % len(players)
        current_player = players[current_player_index]
        dice_result = None
        dice_player_color = None
        last_switch_time = current_time
        reset_rent_flags()
    # Малювання плиток і зображень
    for i in range(len(tiles)):
        tiles[i].draw(screen)
    tiles[0].img_draw(screen, start)
    tiles[1].img_draw(screen, bmw)
    tiles[2].img_draw(screen, adidas)
    tiles[3].img_draw(screen, mak)
    tiles[4].img_draw(screen, kfc)
    tiles[5].img_draw(screen, pepsi)
    tiles[7].img_draw(screen,nice)
    tiles[6].img_draw(screen, apple)
    tiles[8].img_draw(screen, roshen)
    tiles[9].img_draw(screen, mers)
    tiles[10].img_draw(screen, haribo)
    tiles[11].img_draw(screen, nike)
    tiles[12].img_draw(screen, cola)
    tiles[13].img_draw(screen, samsa)
    tiles[14].img_draw(screen,chill_zone)
    tiles[26].img_draw(screen, fora)
    tiles[27].img_draw(screen, atb)
    tiles[25].img_draw(screen, comfy)
    tiles[24].img_draw(screen, cit)
    tiles[23].img_draw(screen, steam)
    tiles[22].img_draw(screen, lays)
    tiles[21].img_draw(screen,bad)
    tiles[20].img_draw(screen, epic)
    tiles[19].img_draw(screen, luk)
    tiles[18].img_draw(screen, log)
    tiles[17].img_draw(screen, hup)
    tiles[16].img_draw(screen, net)
    tiles[15].img_draw(screen, meg)
    drawmarker(screen)
    # Малювання гравців, грошей, інтерфейсу
    for player in players:
        player.draw(screen)


    current_player.monkey(screen)
    buy(screen)
    sell(screen)
    if tile_selection_active:
        selected_tile_buttons = sell_tile_menu(screen, current_player)


    pygame.display.flip()
