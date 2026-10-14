from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): 
        pass

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height, self.x, self.y, frame_width // 2, frame_height // 2)
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0, 7)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 20
        self.size = random.randint(0,1)
        if self.size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
    def update(self):
        self.y += 5
    def draw(self):
        self.image.draw(self.x, self.y)
        


def reset_world():
    global running
    running = True

    # World list 초기화
    global world
    world = []

    # 땅 객체를 생성하고 WORLD list에 추가
    global grass
    grass = Grass()
    world.append(grass)

    # 팀을 생성하고 WORLD list에 추가
    global team
    team = [Boy() for i in range(10)]
    world += team

    global zombie
    zombie = Zombie()
    world.append(zombie)

    global balls
    balls = [Ball() for i in range(20)]
    world += balls
def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




open_canvas()

reset_world()

while running:
    update_world()
    handle_events()
    render_world()
    delay(0.05)


close_canvas()
