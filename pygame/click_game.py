character = Actor('character')
character.topright = 0, 10

WIDTH = 500
HEIGHT = character.height + 20

def draw():
    screen.clear()
    character.draw()

def update():
    character.left = character.left + 2
    if character.left > WIDTH:
        character.right = 0

def on_mouse_down(pos):
    if character.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")

def on_mouse_down(pos):
    if character.collidepoint(pos):
        sounds.eep.play()
        character.image = 'recording'

def set_character_hurt():
    character.image = 'recording'
    sounds.eep.play()
    clock.schedule_unique(set_character_normal, 1.0)
