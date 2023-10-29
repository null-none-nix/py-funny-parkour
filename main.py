import pygame
import time
import sys
pygame.init()
pygame.mixer.init()
DEBUG = False


class LevelLoader(object):
    def __init__(self):
        self.output = None

    def load(self, path):
        print(path)
        with open(path, 'r', encoding='utf-8') as f:
            txt = f.readlines()
            # print(txt)
            idx = 0
            to_idx = -1
            self.output = [[], [], [], [], [], [], []]
            while True:
                try:
                    while not 'ST' in txt[idx]:
                        self.output[to_idx].append(eval(txt[idx][:-2]))
                        idx += 1
                    if idx < len(txt):
                        to_idx = int(txt[idx][2:])
                    idx += 1
                except:
                    print()
                    break

    def get_output(self):
        return self.output


class LevelGenerator(object):
    def __init__(self):
        self.data = None

    def load(self, path):
        with open(path) as f:
            pt = f.readlinse()
            pt.replace('\n', '')


width = 700
height = 500
screen_scale = 1
ll = LevelLoader()
ll.load(sys.path[0]+'/built-in levels.map')
const_gameblocks = ll.get_output()[0]
const_Finishs = ll.get_output()[1]
lt = ll.get_output()[2]
colors = ll.get_output()[3]
ltypes = ll.get_output()[4]
const_blocks2 = ll.get_output()[5]

db_w, db_h = 100, 72
screen = pygame.Surface((width, height))
stuff = pygame.Surface((db_w, db_h))
rscreen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('')
timeD = pygame.time.Clock()
x = y = l = f = speeds = times = js = xjs = 0
t = 1
s = C = 0
gamesblock = []
block1 = []
blocks = []
Finish = []
blocks2 = []
Finishs = []
color = []
Y = 0
g = False
tl = 5
tl2 = 8
tl3 = 2
tl4 = 1.5
moved = False
level_passed = False
time_start = time.time()
time_sum = 0
time_all = 0
speed = 0
for i in range(len(lt)):
    lt[i] = lt[i].upper()
block_control = 0
texts = {
    'A': [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1]],
    'B': [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 0]],
    'C': [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 1, 1, 1]],
    'D': [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 0]],
    'E': [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1]],
    'F': [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
    'G': [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 1]],
    'H': [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1]],
    'I': [[1, 1, 1, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [1, 1, 1, 0]],
    'J': [[1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [1, 0, 1, 0], [0, 1, 0, 0]],
    'K': [[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]],
    'L': [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1]],
    'M': [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1]],
    'N': [[1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1]],
    'O': [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]],
    'P': [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
    'Q': [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]],
    'R': [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]],
    'S': [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 0]],
    'T': [[1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]],
    'U': [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]],
    'V': [[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]],
    'W': [[1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]],
    'X': [[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]],
    'Y': [[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]],
    'Z': [[1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1]],
    ' ': [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    '0': [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
    '1': [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
    '2': [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
    '3': [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
    '4': [[1, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0]],
    '5': [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
    '6': [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
    '7': [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
    '8': [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
    '9': [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
    '.': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 0]]
}
lvsfs = []
lvns = []
nums = []
tfs = []
for i in range(len(lt)):
    sf = pygame.Surface((6*tl*len(lt[i]), 7*tl))
    for j in range(len(lt[i])):
        for k in range(len(texts[lt[i][j]])):
            for p in range(len(texts[lt[i][j]][k])):
                if texts[lt[i][j]][k][p]:
                    pygame.draw.rect(
                        sf, (colors[i][0]/2, colors[i][1]/2, colors[i][2]/2), (j*6*tl+p*tl, k*tl, tl, tl))
    lvsfs.append(sf)

timer_stuffs = {'CURRENT': (0x7f, 0xcf, 0x7f), 'USEFUL': (
    0, 0xff, 0), 'TOTAL': (0xff, 0, 0)}
for i in timer_stuffs:
    sf = pygame.Surface((round(6*tl4*len(i)), round(7*tl4)+1))
    for j in range(len(i)):
        for k in range(len(texts[i[j]])):
            for p in range(len(texts[i[j]][k])):
                if texts[i[j]][k][p]:
                    pygame.draw.rect(
                        sf, timer_stuffs[i], (round(j*6*tl4+p*tl4), round(k*tl4), round(tl4), round(tl4)))
    tfs.append(sf)
for i in range(len(colors)):
    stage = str(i+1)
    sf = pygame.Surface((4*tl2*len(stage), 5*tl2))
    for j in range(len(stage)):
        for k in range(len(texts[stage[j]])):
            for p in range(len(texts[stage[j]][k])):
                if texts[stage[j]][k][p]:
                    pygame.draw.rect(
                        sf, (colors[i][0]/2, colors[i][1]/2, colors[i][2]/2), (j*4*tl2+p*tl2, k*tl2, tl2, tl2))
    lvns.append(sf)
for stage in '0123456789.':
    sf = pygame.Surface((4*tl3*len(stage), 5*tl3))
    for j in range(len(stage)):
        for k in range(len(texts[stage[j]])):
            for p in range(len(texts[stage[j]][k])):
                if texts[stage[j]][k][p]:
                    pygame.draw.rect(sf, (0xff, 0xff, 0xff),
                                     (j*4*tl3+p*tl3, k*tl3, tl3, tl3))
    nums.append(sf)


def lv():
    screen.blit(lvns[Y], (350-3*tl2*len(str(Y+1)), 100-int(3*tl2)))


def main():
    global x, y, l, f, speeds, blocks, times, Finish, color, Y, blocks2, block_control
    global js, xjs, C, blocks2, g, moved, time_sum, level_passed, time_all, speed
    block_control = 18
    speed = 0
    time_all += now_time - time_start
    if Y == 0:
        time_all = time_sum = 0
    elif level_passed:
        time_sum += now_time - time_start
    level_passed = False
    g = 0
    if const_blocks2[Y] == None:
        blocks2 = [[-10000, -10000]]
        speeds = [1]
        js = [1]
        xjs = [1]
    else:
        blocks2 = []
        speeds = []
        js = []
        xjs = []
        for i in range(len(const_blocks2[Y])):
            blocks2.append([const_blocks2[Y][i][0], const_blocks2[Y][i][1]])
            speeds.append(const_blocks2[Y][i][2])
            js.append(const_blocks2[Y][i][3])
            xjs.append(0)
    x = y = 200
    l = 17
    f = C = 1
    color = colors[Y].copy()
    Finish = const_Finishs[Y].copy()
    blocks = const_gameblocks[Y].copy()
    times = 1
    moved = False


def block():
    global block1, color
    pygame.draw.rect(screen, color, (block1[0]-20, block1[1]-20, 40, 40))


def finish():
    global Finish
    pygame.draw.rect(screen, (0xff, 0, 0),
                     (Finish[0]-20, Finish[1]-20, 40, 40))


def block2():
    global blocks2, color
    for z in range(len(blocks2)):
        pygame.draw.rect(
            screen, color, (blocks2[z][0]-20, blocks2[z][1]-20, 40, 40))


def paddle():
    global x, y
    pygame.draw.rect(screen, (0, 0xff, 0xff), (x-15, y-15, 30, 30))


def title():
    screen.blit(lvsfs[Y], (350-3*tl*len(lt[Y]), 250-int(3.5*tl)))


def timer():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 150, 60))
    played_time = '%.3f' % (now_time-time_start)
    for i in range(len(played_time)):
        if played_time[i] in '0123456789':
            screen.blit(nums[int(played_time[i])], (5*tl3*i+5+70, 5))
        else:
            screen.blit(nums[10], (5*tl3*i+5+70, 5))
    played_time = '%.3f' % (time_sum+now_time-time_start)
    for i in range(len(played_time)):
        if played_time[i] in '0123456789':
            screen.blit(nums[int(played_time[i])], (5*tl3*i+5+70, 25))
        else:
            screen.blit(nums[10], (5*tl3*i+5+70, 25))
    played_time = '%.3f' % (time_all+now_time-time_start)
    for i in range(len(played_time)):
        if played_time[i] in '0123456789':
            screen.blit(nums[int(played_time[i])], (5*tl3*i+5+70, 45))
        else:
            screen.blit(nums[10], (5*tl3*i+5+70, 45))
    screen.blit(tfs[0], (5, 5))
    screen.blit(tfs[1], (5, 25))
    screen.blit(tfs[2], (5, 45))


tick_sum = 0
tick_start = time.time()
tick_end = time.time()
now_time = time.time()
fps = 72
mspfps = 1/fps
ssx = ssy = 0
now_fps = 72
neww, newh = width, height
max_fps = 72
min_wait = 1/max_fps
wait = 1/max_fps
all_start = time.time()
main()
while True:
    while time.time()-tick_end < wait:
        ...
    now_time = time.time()
    if not moved:
        time_start = now_time
    if not moved and Y == 0:
        time_all_start = now_time
    run_time = now_time-tick_end
    now_fps = now_fps * 0.9 + round(1/run_time) * 0.1
    # tick_cnt = round(run_time/mspfps)
    tick_cnt = 1
    tick_end += tick_cnt*mspfps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('avg tick ms: ', (time.time()-tick_start)/tick_sum*1000)
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            neww = event.size[0]
            newh = event.size[1]
            rscreen = pygame.display.set_mode((neww, newh), pygame.RESIZABLE)
            rscreen.fill((0, 0, 0))
            if neww / width < newh / height:
                screen_scale = neww / width
            else:
                screen_scale = newh / height
            ssx = (neww - width * screen_scale) // 2
            ssy = (newh - height * screen_scale) // 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Y += 1
                Y = min(Y, len(colors)-1)
                main()
            elif event.key == pygame.K_F1:
                DEBUG = not DEBUG
    for i in range(tick_cnt):
        if s == 0:
            main()
            s = 1
        switch = False
        for z in range(len(blocks2)):
            blocks2[z][0] += speeds[z]
            xjs[z] += speeds[z]
            if xjs[z] < min(js[z], 0) or xjs[z] > max(0, js[z]):
                speeds[z] = -speeds[z]
        if times == 0:
            times = 0
        tick_sum += 1
        c = pygame.key.get_pressed()
        if c[pygame.K_RIGHT] and c[pygame.K_SPACE] == 0 and C and not block_control:
            moved = True
            if ltypes[Y] in (1, 3):
                for z in range(len(blocks)//2):
                    blocks[z*2] -= 7
                Finish[0] -= 7
                for z in range(len(blocks2)):
                    blocks2[z][0] -= 7
            else:
                x += 7
        if c[pygame.K_LEFT] and c[pygame.K_SPACE] == 0 and C and not block_control:
            moved = True
            if ltypes[Y] in (1, 3):
                for z in range(len(blocks)//2):
                    blocks[z*2] += 7
                Finish[0] += 7
                for z in range(len(blocks2)):
                    blocks2[z][0] += 7
            else:
                x -= 7
        switch = False
        if ltypes[Y] in (2, 4):
            for z in range(len(blocks)//2):
                blocks[z*2+1] += 2
            Finish[1] += 2
            for z in range(len(blocks2)):
                blocks2[z][1] += 2
        for z in range(len(blocks)//2):
            if y + 20 >= blocks[z*2+1] - 20 and y + 10 <= blocks[z*2+1] and blocks[z*2] - 20 < x + 15 and blocks[z*2] + 20 > x - 15:
                switch = True
                times = -1
                y = blocks[z*2+1] - 35
                if ltypes[Y] in (3, 4):
                    blocks[z*2+1] += 3
        C = True
        for z in range(len(blocks2)):
            if (x + 15 >= blocks2[z][0] - 20) and (x - 15 <= blocks2[z][0] + 20) and (y + 15 >= blocks2[z][1] - 20) and (y - 15 <= blocks2[z][1] + 20):
                l = 0
                times = -1
                if ltypes[Y] in (1, 3):
                    for z2 in range(len(blocks)//2):
                        blocks[z2*2] -= speeds[z]
                    for z2 in range(len(blocks2)):
                        blocks2[z2][0] -= speeds[z]
                    Finish[0] -= speeds[z]
                y = blocks2[z][1] - 20
                x = blocks2[z][0]
                C = False
        if switch:
            l = 0
        if x > 685:
            x = 685
        if x < 15:
            x = 15
        if c[pygame.K_q] and Y > 0:
            Y -= 1
            main()
        if c[pygame.K_LEFT] and c[pygame.K_SPACE] and x > 15 and C and not block_control:
            moved = True
            if ltypes[Y] in (1, 3):
                for z in range(len(blocks) // 2):
                    blocks[z * 2] += 2
                Finish[0] += 2
                for z in range(len(blocks2)):
                    blocks2[z][0] += 2
            else:
                x -= 2
        if c[pygame.K_RIGHT] and c[pygame.K_SPACE] and x < 685 and C and not block_control:
            moved = True
            if ltypes[Y] in (1, 3):
                for z in range(len(blocks) // 2):
                    blocks[z * 2] -= 2
                Finish[0] -= 2
                for z in range(len(blocks2)):
                    blocks2[z][0] -= 2
            else:
                x += 2
        if (c[pygame.K_UP] or c[pygame.K_z]) and g == 0 and not block_control and times == -1:
            times = 1
            moved = True
        for z in range(len(blocks)//2):
            if blocks[z*2+1] + 20 > y - 15 and blocks[z*2+1] < y and times and blocks[z*2] - 20 < x + 15 and blocks[z*2] + 20 > x - 15:
                times = -1
        if Y == len(ltypes) - 1:
            time_start = time_all_start = now_time
        if Finish[1] + 20 > y - 15 and Finish[1] < y and Finish[0] - 20 < x + 15 and Finish[0] + 20 > x - 15:
            Y += 1
            level_passed = True
            main()
        if times == 1:
            y -= 17
        y += l
        if y < 550:
            if l < 50:
                l += 0.8
        else:
            main()
        block_control = max(0, block_control-1)
    screen.fill((0, 0, 0))
    title()
    lv()
    for z in range(len(blocks)//2):
        block1 = [blocks[z*2], blocks[z*2+1]]
        block()
    paddle()
    finish()
    block2()
    if Y == len(ltypes) - 1:
        screen.fill((0xff, 0xff, 0xff))
        pygame.draw.polygon(screen, (200, 200, 200), ((
            300, 150), (300, 250), (400, 200), (300, 150)))
        H = pygame.mouse.get_pressed()[0]
        if H:
            pygame.quit()
            sys.exit()
    timer()
    _screen = pygame.transform.scale(
        screen, (int(width*screen_scale), int(height*screen_scale)))
    _stuff = stuff.copy()
    stuff.fill((0, 0, 0))
    stuff.blit(_stuff, (-1, 0))
    now_fps = min(max(now_fps, 0), max_fps)
    if now_fps >= 30:
        limit_col = (0x3f, 0x7f, 0x3f)
    else:
        limit_col = (0x7f, 0x3f, 0x3f)
    pygame.draw.rect(stuff, limit_col, (db_w-1,
                                        round((max_fps-now_fps)/max_fps*db_h), db_w-1, db_h+1))
    stuff.set_at((db_w-1, round((max_fps-fps)/max_fps*db_h)),
                 (0xff, 0xff, 0xff))
    stuff.set_at((db_w-1, round((max_fps-60)/max_fps*db_h)), (0, 0xff, 0))
    stuff.set_at((db_w-1, round((max_fps-30)/max_fps*db_h)), (0xff, 0, 0))
    rscreen.blit(_screen, (ssx, ssy))
    if DEBUG:
        rscreen.blit(stuff, (neww-db_w, newh-db_h))
    pygame.display.update()
