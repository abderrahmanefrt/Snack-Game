import random
import curses

screen = curses.initscr()

curses.curs_set(0)
screenheight, screenwidhth = screen.getmaxyx()

window= curses.newwin(screenheight, screenwidhth , 0, 0)
window.keypad(1)

window.timeout(100)

snake_x = screenwidhth // 4
snake_y= screenheight // 2
snake =[
    [snake_y, snake_x]
    [snake_y, snake_x -1],
    [snake_y, snake_x-2], 
]

food = [screenheight // 2, screenwidhth // 2]
window.addch(food[0], food[1], curses.ACS_PI )

key=curses.KEY_RIGHT 

while True:
  next_key = window.getch
  key=key if next_key == -1 else next_key 

  if snake[0][0] in [0,screenheight] or \
      snake[0][1] in [0 , screenwidhth] or \
      snake[0] in snake[1:]:
    curses.endwin()
    quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0]+= 1
    if key == curses.KEY_UP:
       new_head[0]-= 1
       if key == curses.KEY_LEFT:
          new_head[1]-= 1
          if key == curses.KEY_RIGHT:
             new_head[1]+= 1


             snake.insert(0, new_head)
             if snake[0]==food:
                 food = None
                 while food is None:
                     nf =[
                         random.randint(1, screenheight -1),
                         random.randint(1, screenwidhth -1)
                         
                     ]
