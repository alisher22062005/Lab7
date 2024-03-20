import pygame 

pygame.init()


def playing_next_music():
    global index
    if  index==len(songs)-1:
        index=0

    else:
        index=index+1
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()


def playing_previous_music():
    global index
    if index==0:
        index=len(songs)-1
    else:
        index=index-1
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

index=0
songs=["better_off_alone.mp3","kbtu.mp3"]
music=1
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))


while music:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            music=0
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                unpause_music()
            if event.key==pygame.K_DOWN:
                pause_music()
            if event.key==pygame.K_RIGHT:
                playing_next_music()
            if event.key==pygame.K_LEFT:
                playing_previous_music()
            if event.key==pygame.K_SPACE:
                stop_music()

