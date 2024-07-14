# Import the pygame module
# Import random for random numbers
import random
import time
import pygame
import pygame_menu
pygame.init()
# region
from pygame.locals import (
    K_DOWN,
    K_ESCAPE,
    K_LEFT,
    K_RIGHT,
    K_UP,
    KEYDOWN,
    K_RSHIFT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_q,
    K_e,
    K_KP0,
    QUIT,
    RLEACCEL,
)
# endregion

# region variables
# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
tilscore = 0
score = 0
score1 = "0"
score2 = "0"
tilend = 0
end = 1
rest1 = 0
tilrest = 0
rest12 = 0
tilrest2 = 0
pl1upward = 0.0
pl1xward = 0.0
pl2upward = 0.0
pl2xward = 0.0
jumped = 0
goup = 0.0
godown = 0.0
cooldown = 15
jumped2 = 0
goup2 = 0.0
godown2 = 0.0
cooldown2 = 15
shieldup = False
shieldup2 = False
Classic = pygame.image.load("Maps/Map6.png")
Second = pygame.image.load("Maps/moonmap.png")
Chasm = pygame.image.load("Maps/island_map.jpg")
Ocean = pygame.image.load("Maps/Map3.png")
Dusty = pygame.image.load("Maps/Map1.png")
victory = pygame.image.load("IkeSprite/Ike_victory.png")
victory = pygame.transform.scale(victory, (272,188))
victory2 = pygame.image.load("SonicSprite/Sonic_victory.png")
victory2 = pygame.transform.scale(victory2, (260,290))
tchcloud = False
tchcloud2 = False
t1 = 92
t2 = 425
t12 = 92
t22 = 425
attacking2 = False
attacking = False
right = False
right2 = False
what = 0
pl1damage = 0.0
pl2damage = 0.0
winner = 3
winnerstr = "0"
beenattack1 = 30
beenattack = 30
gamestate = 0
mapis = 1
diff = "0"
shielddown = 3
shielddown2 = 0
shielddownup = 0
shielddownup2 = 180
dashing = 0.0
is_dashed = False
dashmed = False
dashcharge = 0.0
dashing2 = False
dash = 30
isldash = False
# Define the Player object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
# endregion

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        if mapis == 4:
            self.surf = pygame.image.load("Assets/cloud2.png")
            self.rect = pygame.Rect((random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),random.randint(0, SCREEN_HEIGHT-200)),(100,75))
        else:
            self.surf = pygame.image.load("Assets/cloud.png")
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = pygame.Rect((random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),random.randint(0, SCREEN_HEIGHT-400)),(100,75))
        # The starting position is randomly generated
        

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()

class Player1(pygame.sprite.Sprite):
    def __init__(self,image1,image2):
        super(Player1, self).__init__()
        self.image1 = image1
        self.image1.set_colorkey((34, 177, 76), RLEACCEL)
        self.image1r = image1r
        self.image1r.set_colorkey((34, 177, 76), RLEACCEL)
        self.image2 = image2
        self.image2.set_colorkey((34, 177, 76), RLEACCEL)
        self.image2r = image2r
        self.image2r.set_colorkey((34, 177, 76), RLEACCEL)
        self.image3 = image3
        self.image3.set_colorkey((34, 177, 76), RLEACCEL)
        self.image3r = image3r
        self.image3r.set_colorkey((34, 177, 76), RLEACCEL)
        self.image4 = image4
        self.image4.set_colorkey((34, 177, 76), RLEACCEL)
        self.image4r = image4r
        self.image4r.set_colorkey((34, 177, 76), RLEACCEL)
        self.image5 = image5
        self.image5.set_colorkey((34, 177, 76), RLEACCEL)
        self.image5r = image5r
        self.image5r.set_colorkey((34, 177, 76), RLEACCEL)
        self.imagec = imagec
        self.imagec.set_colorkey((34, 177, 76), RLEACCEL)
        
        self.surf = self.image1
        self.rect = self.surf.get_rect()
        self.rect.move_ip(530, 0)
        
        
    

    # Move the sprite based on keypresses
    def update(self, pressed_keys):

        global pl1upward
        global pl1xward
        global pl2upward
        global pl2xward
        global jumped
        global cooldown
        global shieldup
        global entity
        global godown
        global attacking
        global right
        global what
        global pl2damage
        global winner
        global beenattack1
        global shielddown
        global dashing
        global is_dashed
        global dashmed
        cooldown = cooldown - 1
        if shielddown > 0:
            shielddown -= 1
        # if shieldup:
            # shielddown -= 1
        # else:
            # shielddown = 180
        if attacking:
            if beenattack1 >= 1:
                beenattack1 -= 1
        else:
            beenattack1 = 30
        goup = pl1upward - pl1upward * 2
        pl1upward -= 1
        if goup >= 0:
            goup = 0
        if pl1upward <= 0:
            pl1upward = 0
        if pl1xward > 0:
            pl1xward -= 1
        if pl1xward < 0:
            pl1xward += 1
        self.rect.move_ip(pl1xward, goup)
        
        global rest1
        attacking = False
        if pressed_keys[K_RSHIFT]:
            if shielddown == 0:
                if shieldup == False:
                    attacking = True
                    if beenattack1 >= 1:

                        if self.rect.colliderect(player2.rect):
                            attack.play()
                            if shieldup2f == False:
                                if is_dashed:
                                    pl2damage += dashing
                                    dashing = 0
                                    is_dashed = False
                                else:
                                    pl2damage += 0.5
                                if right:
                                    pl2xward = 20 + pl2damage
                                    pl2upward = 25 + pl2damage
                                else:
                                   pl2xward = -20 - pl2damage
                                   pl2upward = 25 + pl2damage
                        is_dashed = False
                        dashing = 0



        if attacking:
            if beenattack1 >= 1:
                what = 1
                if right:
                    self.surf = self.image5r
                else:
                    self.surf = self.image5
            else:
                if what == 1:
                    self.surf = self.image1
                    what = 0
            
               
        if rest1 == 1:
            rest1 = 0
            if shieldup == False:
                if attacking == False:
                    
                    if self.surf == self.image1:
                        self.surf = self.image2
                    else:
                        if self.surf == self.image1r:
                            self.surf = self.image2r
                        else:
                            if self.surf == self.image2r:
                                self.surf = self.image1r
                            else:
                                self.surf = self.image1

        if tchcloud == False:
            #gravity
            self.rect.move_ip(0, 7)
        else:
            if cooldown <= 0:
                jumped = 0
            
        if pressed_keys[K_UP]:
            
            
            if cooldown <= 0 and dashmed == False:
                
                cooldown = 15
                if jumped <= 1:
                    
                    if shieldup == False:
                        pl1upward = 25
                        jumped = jumped + 1
                        move_up_sound.play()
            
        shieldup = False
        if pressed_keys[K_DOWN]:
            shielddown = 60
            if tchcloud == False:
                self.rect.move_ip(0, 10)
            move_down_sound.play()
            if right:
                self.surf = self.image3r
            if right == False:
                self.surf = self.image3
            shieldup = True
        dashmed = False
        if pressed_keys[K_KP0]:
            if shieldup == False:
               
               self.surf = self.imagec
               dashing += 0.015
               if dashing > 0.9:
                   is_dashed = True
               dashmed = True
        
        if pressed_keys[K_LEFT]:
            right = False
            if attacking == False and dashmed == False:
                if self.surf == self.image1r:
                    self.surf = self.image1
                if self.surf == self.image2r:
                    self.surf = self.image2         
                if attacking:
                    self.surf = self.image5
                if shieldup == False:
                    self.rect.move_ip(-6, 0)
        
        if pressed_keys[K_RIGHT]:
            right = True
            if attacking == False and dashmed == False:
                if self.surf == self.image1:
                    self.surf = self.image1r            
                if self.surf == self.image2:
                    self.surf = self.image2r          
                if attacking:
                    self.surf = self.image5r
                if shieldup == False:

                    self.rect.move_ip(6, 0)
                else:
                    if attacking == False:
                        self.surf = self.image3r
            
        # Keep player on the screen
        if self.rect.left < -50:
            self.rect.left = -50
            winner = 2
            
        elif self.rect.right > SCREEN_WIDTH + 50:
            self.rect.right = SCREEN_WIDTH + 50
            winner = 2
        if self.rect.top >= 800:
            self.rect.top = 800
            winner = 2
        if mapis == 2 or mapis == 3:
            if self.rect.bottom >= SCREEN_HEIGHT+150:
                winner = 2
        else:
            if self.rect.bottom >= SCREEN_HEIGHT-80:
                self.rect.bottom = SCREEN_HEIGHT-80
                jumped = 0
        
class Player2(pygame.sprite.Sprite):
    def __init__(self,images1,images2):
        super(Player2, self).__init__()
        self.images1 = images1
        self.images1.set_colorkey((34, 177, 76), RLEACCEL)
        self.images1r = images1r
        self.images1r.set_colorkey((34, 177, 76), RLEACCEL)
        self.images2 = images2
        self.images2.set_colorkey((34, 177, 76), RLEACCEL)
        self.images2r = images2r
        self.images2r.set_colorkey((34, 177, 76), RLEACCEL)
        self.images3 = images3
        self.images3.set_colorkey((34, 177, 76), RLEACCEL)
        self.images3r = images3r
        self.images3r.set_colorkey((34, 177, 76), RLEACCEL)
        self.imagesar = imagesar
        self.imagesar.set_colorkey((34, 177, 76), RLEACCEL)
        self.imagesa = imagesa
        self.imagesa.set_colorkey((34, 177, 76), RLEACCEL)
        self.surf = self.images1
        self.rect = self.surf.get_rect()
        self.rect.move_ip(50, 0)
        
    

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        global pl2upward
        global pl2xward
        global jumped2
        global cooldown2
        global shieldup2
        global entity
        global godown2
        global attacking2
        global right2
        global pl1upward
        global pl1xward
        global pl1damage
        global winner
        global beenattack
        global shielddown2
        global shieldup2f
        global dashing
        global dashmed
        global dashcharge
        global dashing2
        global dash
        global isldash
        if shielddown2 > 0:
            shielddown2 -= 1
        cooldown2 = cooldown2 - 1
        goup2 = pl2upward - pl2upward * 2
        if attacking2:
            if beenattack >= 1:
                beenattack -= 1
        else:
            beenattack = 30
        pl2upward -= 1
        if goup2 >= 0:
            goup2 = 0
        if pl2upward <= 0:
            pl2upward = 0
        if pl2xward > 0:
            pl2xward -= 1
        if pl2xward < 0:
            pl2xward += 1
        self.rect.move_ip(pl2xward, goup2)
        global rest12
        if rest12 == 1:
            if shieldup2f == False:
                rest12 = 0
                if self.surf == self.images1 or self.surf == self.images1r:
                    if right2:
                        self.surf = self.images2
                    else:
                        self.surf = self.images2r
                else:
                    if right2:
                        self.surf = self.images1
                    else:
                        self.surf = self.images1r

        if tchcloud2 == False:
            #gravity
            if dash > 0 and dash < 29 and dashing2 == False:
                right2 = right2
            else:
                self.rect.move_ip(0, 7)
        else:
            if cooldown2 <= 0:
                jumped2 = 0
        
        if pressed_keys[K_w]:
            
            
            if cooldown2 <= 0:
                
                cooldown2 = 15
                if jumped2 <= 1:
                    
                    if shieldup2f == False:
                        pl2upward = 25
                        
                        jumped2 = jumped2 + 1
                        move_up_sound.play()
        dashing2 = False
        if pressed_keys[K_s]:
            dash = 0
            
            if tchcloud2 == True:
                isldash = True
            dashing2 = True
            if dashcharge < 30:
                
                dashcharge += 0.5
            
               
        if dashing2 == False and dashcharge > 0 or dash > 0:
            
            if dashcharge > 0:
                dash = dashcharge / 2
            dashcharge = 0
            dash -= 1
            if isldash == True and tchcloud2 == False:
                
                isldash = False
                dash = 0
                if right2:
                    self.rect.move_ip(-20, 0)
                else:
                    self.rect.move_ip(20, 0)
            else:
                if right2:
                    self.rect.move_ip(20, 0)
                else:
                    self.rect.move_ip(-20, 0)
            if self.rect.colliderect(player1.rect):
                isldash = False
                print("collision")
                if shieldup == False:
                    dash = 0
                    pl1damage += 1.5
                    if right2:
                        pl1xward = 20 + pl1damage
                        pl1upward = 25 + pl1damage
                    else:
                       pl1xward = -20 - pl1damage
                       pl1upward = 25 + pl1damage
        shieldup2f = False
        if pressed_keys[K_e]:
            if dashing2 == False:
                shielddown2 = 30
                shieldup2f = True
                move_down_sound.play()
                self.surf = self.images3
                shieldup2f = True
                
            
                #shieldup2 = False
       
        if pressed_keys[K_a]:
            right2 = False
            if dashing2 == False:
                if self.surf == self.images1:
                    self.surf = self.images1r
                if self.surf == self.images2:
                    self.surf = self.images2r         
                if shieldup2f == False and attacking2 == False:
                    self.rect.move_ip(-9, 0)
        if pressed_keys[K_d]:
            right2 = True
            if dashing2 == False:
                if self.surf == self.images1r:
                    self.surf = self.images1           
                if self.surf == self.images2r:
                    self.surf = self.images2          
                if shieldup2f == False:
                    if attacking2 == False:
                        self.rect.move_ip(9, 0)
                
            
        attacking2 = False
        if pressed_keys[K_q]:
            if shielddown2 == 0:
                if shieldup2f == False:
                    attacking2 = True
                    if beenattack >= 1:
                        if self.rect.colliderect(player1.rect):
                            attack.play()
                            if shieldup == False:
                                pl1damage += 0.5
                                if dashmed:
                                    dashing = 0
                                if right2:
                                    pl1xward = 20 + pl1damage
                                    pl1upward = 25 + pl1damage
                                else:
                                   pl1xward = -20 - pl1damage
                                   pl1upward = 25 + pl1damage
                        if right2 == False:
                            self.surf = self.imagesar
                        if right2:
                            self.surf = self.imagesa
        #if mapis == 2:
            
        # Keep player on the screen
        if self.rect.left < -50:
            self.rect.left = -50
            winner = 1
        elif self.rect.right > SCREEN_WIDTH + 50:
            self.rect.right = SCREEN_WIDTH + 50
            winner = 1
        if self.rect.top >= 800:
            self.rect.top = 800
            winner = 1
        if mapis == 2 or mapis == 3:
            if self.rect.bottom >= SCREEN_HEIGHT+150:
                winner = 1
        else:
            if self.rect.bottom >= SCREEN_HEIGHT-80:
                self.rect.bottom = SCREEN_HEIGHT-80
                jumped2 = 0
        
class Terrain(pygame.sprite.Sprite):
    def __init__(self):
        super(Terrain, self).__init__()
        self.surf = pygame.image.load("Assets/Terrain.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (f1,f2))
        # The starting position is randomly generated
        
        self.rect = self.surf.get_rect(center=(t1, t2,))
   
class Oak_tree(pygame.sprite.Sprite):
    def __init__(self):
        super(Oak_tree, self).__init__()
        self.surf = pygame.image.load("Assets/Oak_tree.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(center=(t1, t2,))

pygame.mixer.init()


# region Load images
# Setup the clock for a decent framerate
clock = pygame.time.Clock()
new_cloud = Cloud()
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bgd = pygame.image.load('Assets/deathscreen.jpg')
bgd = pygame.transform.scale(bgd, (1000,600))
image1 = pygame.image.load('IkeSprite/Ike_rest.png').convert()
image1 = pygame.transform.scale(image1, (68,96))
image1r = pygame.transform.flip(image1, True,False)
image2 = pygame.image.load('IkeSprite/Ike_rest2.png').convert()
image2 = pygame.transform.scale(image2, (68,96))
image2r = pygame.transform.flip(image2, True,False)
image3 = pygame.image.load('IkeSprite/Ike_shield.png').convert()
image3 = pygame.transform.scale(image3, (68,96))
image3r = pygame.transform.flip(image3, True,False)
image4 = pygame.image.load('IkeSprite/Ike_attack.png').convert()
image4 = pygame.transform.scale(image4, (104,120))
image4r = pygame.transform.flip(image4, True,False)
image5 = pygame.image.load('IkeSprite/Ike_dash.png').convert()
image5 = pygame.transform.scale(image5, (136,94))
image5r = pygame.transform.flip(image5, True,False)
imagec = pygame.image.load('IkeSprite/Ike_charging.png').convert_alpha()
imagec = pygame.transform.scale(imagec, (68,96))
#sonic
images1 = pygame.image.load('SonicSprite/Sonic_rest.png').convert()
images1 = pygame.transform.scale(images1, (52,48))
images1r = pygame.transform.flip(images1, True,False)
imagesa = pygame.image.load('SonicSprite/Sonic_attack.png').convert()
imagesa = pygame.transform.scale(imagesa, (52,48))
imagesar = pygame.transform.flip(imagesa, True,False)
images2 = pygame.image.load('SonicSprite/Sonic_rest2.png').convert()
images2 = pygame.transform.scale(images2, (52,48))
images2r = pygame.transform.flip(images2, True,False)
images3 = pygame.image.load('SonicSprite/Sonic_shield.png').convert()
images3 = pygame.transform.scale(images3, (52,48))
images3r = pygame.transform.flip(images3, True,False)
# Create custom events for adding a new enemy and cloud
# endregion

# region setup
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 4000)

# Create our 'player'
player1 = Player1(image1,image2)

clouds = pygame.sprite.Group()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
scoreText = pygame.font.SysFont('Comic Sans MS', 30)
scoreText2 = pygame.font.SysFont('Comic Sans MS', 30)
loat = pygame.font.SysFont('Comic Sans MS', 150)
# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites isused for renderings
all_sprites = pygame.sprite.Group()



# Load and play our background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("SoundFX/Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)

# Load all our sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("SoundFX/Rising_putter.mp3")
move_down_sound = pygame.mixer.Sound("SoundFX/Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("SoundFX/Collision.ogg")
death_sound = pygame.mixer.Sound("SoundFX/death.ogg")
attack = pygame.mixer.Sound("SoundFX/attack.mp3")
click = pygame.mixer.Sound("SoundFX/click.wav")
attack.set_volume(100)
click.set_volume(100)

# Set the base volume for all sounds
move_up_sound.set_volume(0.5)
move_down_sound.set_volume(0.5)
collision_sound.set_volume(0.5)
death_sound.set_volume(1)
pygame.display.set_caption("Fighting Game By Noah")
Icon = pygame.image.load("Assets/Smash_icon.png")
pygame.display.set_icon(Icon)
# Variable to keep our main loop running
# endregion

def set_map(diff,mainmap):
    global mapis
    mapis = mainmap
    click.play()
    
def checkcoll(player,island):
    if (player.rect.bottom <= island.rect.top + 20 and
            player.rect.right > island.rect.left and
            player.rect.top <= island.rect.bottom and
            player.rect.bottom >= island.rect.top and
            player.rect.left < island.rect.right ):
        return True
    else:
        return False
    
def start_the_game():
    global menuruns
    menuruns = False
    click.play()
    time.sleep(0.1)
def island():
    click.play()
    global mapis
    mapis = 2
def chasm():
    click.play()
    global mapis
    mapis = 3
def ocean():
    click.play()
    global mapis
    mapis = 4  
def dusty():
    click.play()
    global mapis
    mapis = 5
def classic():
    click.play()
    global mapis
    mapis = 1 
def quit():

    click.play()
    pygame.quit()
# region menu
controls = "Press ESC to open Menu "
controls1 = "Player1: arrow keys to move"
controls2 = "Ctrl to Charge up"
controls3 = "Down arrow key to shield"
controls4 = "Shift to attack"
controls5 = "Player2: WASD to move"
controls6 = "S to dash"
controls7 = "E to shield"
controls8 = "Q to attack"
control_menu = pygame_menu.Menu(title='Controls', width=1000, height=600,theme=pygame_menu.themes.THEME_BLUE)
control_menu.add.label(controls, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
control_menu.add.label(controls1, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
control_menu.add.label(controls2, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
control_menu.add.label(controls3, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
control_menu.add.label(controls4, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
control_menu.add.label(controls5, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
control_menu.add.label(controls6, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
control_menu.add.label(controls7, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
control_menu.add.label(controls8, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
settings_menu_theme = pygame_menu.themes.THEME_BLUE.copy()
settings_menu_theme.widget_font_size = 63
map_menu = pygame_menu.Menu('Choose map',SCREEN_WIDTH,SCREEN_HEIGHT,columns=3,rows=2,theme=settings_menu_theme)
map_menu.add.button('Return',pygame_menu.events.BACK,padding=(17, 0, 17, 0))
map_menu.add.image("Assets/Map6menu.png",padding=(0, 0, 0, 0),onselect=classic,selectable=True)
map_menu.add.image("Assets/moonmapmenu.png",padding=(0, 0, 0, 0),onselect=island,selectable=True)
map_menu.add.image("Assets/Map3menu.png",padding=(0, 0, 0, 0),onselect=ocean,selectable=True)
map_menu.add.image("Assets/Map1menu.png",padding=(0, 0, 0, 0),onselect=dusty,selectable=True)
map_menu.add.image("Assets/island_mapmenu.png",padding=(0, 0, 0, 0),onselect=chasm,selectable=True)
menu = pygame_menu.Menu(title='Fighting game', width=1000, height=600,theme=pygame_menu.themes.THEME_BLUE)
#menu.add.selector('Choose map', [("classic", 1), ('Island', 2), ('Chasm', 3), ('Ocean', 4)], onchange=set_map)
menu.add.button('Choose map', map_menu)
menu.add.button('Controls', control_menu)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', quit)
menuruns = True
player2 = Player2(images1,images2)
all_sprites.add(player2)
# endregion
# gameloop
while True:
    
    if winner != 3:
        for entity in all_sprites:
            entity.kill()
        for entity in clouds:
            entity.kill()
        # oak_tree.kill()
        # oak_tree2.kill()
        player2 = Player2(images1,images2)
    
    tchcloud = False
    tchcloud2 = False
    t1 = 92
    t2 = 425
    t12 = 92
    t22 = 425
    dash = 0

    #all_sprites.add(player1)
    pl1damage = 0
    pl2damage = 0
    dashing = 0
    pl1xward = 0
    pl2xward = 0
    winner = 3
    menuruns = True
    while menuruns:
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        if menu.is_enabled():
            menu.update(events)
            menu.draw(screen)
        # if map_menu.is_enabled():
            # map_menu.update(events)
            # map_menu.draw(screen)

        pygame.display.update()
    # Our main loop-------------------------------------------------------
    if mapis == 1:
        oak_tree = Oak_tree()
        t1 = 585
        t2 = 425
        oak_tree2 = Oak_tree()
        all_sprites.add(oak_tree)
        all_sprites.add(oak_tree2)
    if mapis == 2:
        t1 = 150
        t2 = 200
        f1 = 170
        f2 = 98
        terrain1 = Terrain()
        t1 = 850
        t2 = 300
        terrain2 = Terrain()
        t1 = 200
        t2 = 500
        terrain3 = Terrain()
        t1 = 600
        t2 = 470
        terrain4 = Terrain()
    

        #terrain3 = Terrain()
        #terrain4 = Terrain()
        all_sprites.add(terrain1)
        all_sprites.add(terrain2)
        all_sprites.add(terrain3)
        all_sprites.add(terrain4)
        #all_sprites.add(oak_tree2)
    if mapis == 3:
        t1 = 480
        t2 = 500
        f1 = 410
        f2 = 207
        terrain1 = Terrain()
        all_sprites.add(terrain1)
    if mapis == 5:
        t1 = 480
        t2 = 300
        f1 = 410
        f2 = 207
        terrain1 = Terrain()
        all_sprites.add(terrain1)
    if mapis != 3:
        player2.rect.x = 50
    else:
        player2.rect.x = 400
    player2.rect.y = 0
    player1.rect.x = 530
    player1.rect.y = 0
    running = True
    while running:
        
        # score:
        if winner != 3:
            running = False
        score12 = int(pl2damage)
        score2 = str(score12)
        text_surface = scoreText.render(score2, False, (255, 0, 0))
        score12 = int(pl1damage)
        score1 = str(score12)
        text_surface2 = scoreText2.render(score1, False, (255, 0, 0))


        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop
                if event.key == K_ESCAPE:
                    running = False

            # Did the user click the window close button? If so, stop the loop
            elif event.type == QUIT:
                pygame.quit()

            # Should we add a new enemy?

            # Should we add a new cloud?
            elif event.type == ADDCLOUD:
                # Create the new cloud, and add it to our sprite groups
                if mapis != 2:
                    new_cloud = Cloud()
                    clouds.add(new_cloud)
                    all_sprites.add(new_cloud)

        tilrest = tilrest + 1
        if tilrest == 15:
            tilrest = 0
            rest1 = 1
        tilrest2 = tilrest2 + 1
        if tilrest2 == 15:
            tilrest2 = 0
            rest12 = 1



        # Update the position of our enemies and clouds

        clouds.update()
        if mapis == 1:
            if (player1.rect.bottom <= oak_tree.rect.top + 20 and
                    player1.rect.right > oak_tree.rect.left and
                    player1.rect.top <= oak_tree.rect.bottom and
                    player1.rect.bottom >= oak_tree.rect.top and
                    player1.rect.left < oak_tree.rect.right ):
                tchcloud = True
            else:
                if (player1.rect.bottom <= oak_tree2.rect.top + 20 and
                    player1.rect.right > oak_tree2.rect.left and
                    player1.rect.top <= oak_tree2.rect.bottom and
                    player1.rect.bottom >= oak_tree2.rect.top and
                    player1.rect.left < oak_tree2.rect.right ):
                    tchcloud = True
                else:
                    tchcloud = False

            if (player2.rect.bottom <= oak_tree.rect.top + 20 and
                    player2.rect.right > oak_tree.rect.left and
                    player2.rect.top <= oak_tree.rect.bottom and
                    player2.rect.bottom >= oak_tree.rect.top and
                    player2.rect.left < oak_tree.rect.right ):
                tchcloud2 = True
            else:
                if (player2.rect.bottom <= oak_tree2.rect.top + 20 and
                    player2.rect.right > oak_tree2.rect.left and
                    player2.rect.top <= oak_tree2.rect.bottom and
                    player2.rect.bottom >= oak_tree2.rect.top and
                    player2.rect.left < oak_tree2.rect.right ):
                    tchcloud2 = True
                else:
                    tchcloud2 = False
        if mapis == 2:
            tchcloud = checkcoll(player1,terrain4)
            if checkcoll(player1,terrain4) == False:
                tchcloud = checkcoll(player1,terrain3)
                if checkcoll(player1,terrain3) == False:
                    tchcloud = checkcoll(player1,terrain2)
                    if checkcoll(player1,terrain2) == False:
                        tchcloud = checkcoll(player1,terrain1)
            tchcloud2 = checkcoll(player2,terrain4)
            if checkcoll(player2,terrain4) == False:
                tchcloud2 = checkcoll(player2,terrain3)
                if checkcoll(player2,terrain3) == False:
                    tchcloud2 = checkcoll(player2,terrain2)
                    if checkcoll(player2,terrain2) == False:
                        tchcloud2 = checkcoll(player2,terrain1)

        if mapis == 3:
            tchcloud = checkcoll(player1,terrain1)
            tchcloud2 = checkcoll(player2,terrain1)
        if mapis == 5:
            tchcloud = checkcoll(player1,terrain1)
            tchcloud2 = checkcoll(player2,terrain1)



        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player1.update(pressed_keys)
        player2.update(pressed_keys)
        # Fill the screen with sky blue
        if mapis == 1:
             screen.blit(Classic, (0, 0))
        if mapis == 2:
             screen.blit(Second, (0, 0))
        if mapis == 3:
             screen.blit(Chasm, (0, 0))
        if mapis == 4:
             screen.blit(Ocean, (0, 0))
        if mapis == 5:
             screen.blit(Dusty, (0, 0))
    
        screen.blit(text_surface, (10,10))
        screen.blit(text_surface2, (950,10))
        #all_sprites.draw(screen)
        # Draw all our sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        if attacking:
            screen.blit(player1.surf, (player1.rect.x - 46, player1.rect.y))
        else:
            screen.blit(player1.surf, player1.rect)
        screen.blit(player2.surf, player2.rect)

        # Check if any enemies have collided with the player


        # Flip everything to the display
        pygame.display.flip()

        # Ensure we maintain a 30 frames per second rate
        clock.tick(60)

    # region
    # At this point, we're done, so we can stop and quit the mixer
    end = 1
    tilend = 0
    while end == 1:
        clock.tick(60)
        if winner == 3:
            end = 0
            winner = 1
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop
                if event.key == K_ESCAPE:
                    end = 0

            # Did the user click the window close button? If so, stop the loop
            elif event.type == QUIT:
                pygame.quit()
        tilend += 1
        if tilend == 180:
            tilend = 0
            end = 0
            
            
        winnerstr = str(winner)
        text_surface = loat.render("player " + winnerstr + " won", False, (255, 255, 255))
        screen.blit(bgd, (0,0))
        if winner == 1:
            victory.set_colorkey((34, 177, 76), RLEACCEL)
            screen.blit(victory, (364,280))
        if winner == 2:
            victory2.set_colorkey((34, 177, 76), RLEACCEL)
            screen.blit(victory2, (364,280))
        screen.blit(text_surface, (0,0))
        pygame.display.flip()
    # endregion