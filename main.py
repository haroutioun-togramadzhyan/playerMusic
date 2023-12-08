import pygame
import sys
import os


pygame.init()
screen = pygame.display.set_mode((720, 260))
clock = pygame.time.Clock()
fps = 60
running = True


objects = []


font = pygame.font.SysFont(None, 25)


class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def play_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


def stop_music():
    pygame.mixer.music.stop()


def play_next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()


def play_previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()


def myFunction():
    print('Button Pressed')

#ICI CHANGEZ LES COVERS DES MUSIQUES!
thumbnails = [
    pygame.image.load("Covers\epic_cover.jpg"),
    pygame.image.load("Covers\happy_cover.jpg"),
    pygame.image.load("Covers\jazzy_cover.jpg"),
]

Button(600, 100, 100, 50, 'Next', play_next_track)
Button(480, 100, 100, 50, 'Play/Pause', play_pause)
Button(150, 100, 100, 50, 'Stop', stop_music)
Button(30, 100, 100, 50, 'Previous', play_previous_track)


current_track = 0
#ICI AJOUTEZ OU SUPPRIMEZ VOS MUSIQUES!
music_files = ["Musiques\epic_music.mp3", "Musiques\happy_music.mp3", "Musiques\jazzy_music.mp3"]

pygame.mixer.init()
pygame.mixer.music.load(music_files[current_track])
pygame.mixer.music.play()




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((10, 10, 10))


    screen.blit(thumbnails[current_track], (220, 0))

    for obj in objects:
        obj.process()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
