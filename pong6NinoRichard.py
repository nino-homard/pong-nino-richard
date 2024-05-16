import pygame
from time import sleep
from random import randint, random

pygame.init()
endgame = False
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Random Pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

myfont = pygame.font.SysFont('monospace', 50)

print("pong6")
screen.fill(BLACK)
title = myfont.render("Single Player Pong:", False, WHITE)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2,
                    HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)


def loadingscreen():
  loadingfor = randint(2, 5)
  point = [".", "..", "..."]
  tips = [
      "If you lose, don't cry", "Try to press AltF4", "Try to become better",
      "Less cry more try", "Losing ? Skill issues ?", "rdm speed is wanted"
  ]
  p = 0
  for i in range(0, loadingfor):
    screen.fill(BLACK)
    title = myfont.render("Loading" + point[p], False, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2,
                        HEIGHT // 2 - title.get_height() * 2))
    title = myfont.render(tips[randint(0, len(tips)) - 1], False, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2,
                        HEIGHT // 1.2 - title.get_height() * 2))
    pygame.display.update()
    pygame.time.delay(2000)
    p += 1
    if p >= len(point):
      p = 0
  screen.fill(BLACK)


def timespeed(speed, score):
  if score <= 1:
    speed = 2
  else:
    speed += score // 20
  return speed


def paddlewidth(score, paddlewidth, lastestscore):
  if score != lastestscore:
    paddlewidth -= 5
  if paddlewidth <= 30:
    paddlewidth = 30
  return paddlewidth, score


def losescreen(score):
  endgame = True
  screen.fill(BLACK)
  title = myfont.render("Game Over", False, RED)
  screen.blit(title, (WIDTH // 2 - title.get_width() // 2,
                      HEIGHT // 2 - title.get_height() * 2))
  pygame.display.update()
  pygame.time.delay(2000)
  screen.fill(BLACK)
  title = myfont.render("Your score is : " + str(score - 1), False, RED)
  screen.blit(title, (WIDTH // 2 - title.get_width() // 2,
                      HEIGHT // 2 - title.get_height() * 2))
  pygame.display.update()
  pygame.time.delay(2000)

  while endgame:
    screen.fill(BLACK)
    title = myfont.render("Press space to replay", False, RED)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2,
                        HEIGHT // 2 - title.get_height() * 2 - 50))
    title = myfont.render("or Q to quit", False, RED)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2,
                        HEIGHT // 2 - title.get_height() * 2))
    pygame.display.update()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          endgame = False
          return endgame
        elif event.key == pygame.K_q:
          pygame.quit()
          quit()


while not endgame:
  endgame = False
  end = False

  loadingscreen()

  radius = 10
  x = WIDTH // 2
  y = radius * 2
  score = 1
  lastestscore = 1
  speed = 0.2
  pygame.draw.circle(screen, WHITE, (x, y), radius)

  paddle = {
      "width": 200,
      "height": 20,
      "color": BLUE,
      "x": 0,
      "y": HEIGHT,
      "speed": 0
  }
  paddle["x"] = WIDTH // 2 - paddle["width"] // 2
  paddle["y"] = HEIGHT - paddle["height"]
  paddle["speed"] = 7

  x_sens = y_sens = 1
  while x_sens == 0:
    if x_sens == 0:
      x_sens = y_sens

  pause = False

  while not end:
    speed = timespeed(speed, score)
    screen.fill(BLACK)

    pygame.draw.rect(
        screen, paddle["color"],
        (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

    pygame.draw.circle(screen, WHITE, (int(x), int(y)), radius)
    title = myfont.render("Score : " + str(score - 1), False, WHITE)
    screen.blit(title, (WIDTH - title.get_width(),
                        HEIGHT - title.get_height() - title.get_height() * 2))

    pygame.display.update()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        end = True
    key = pygame.key.get_pressed()

    if key[pygame.K_m]:
      auto = False

    if key[pygame.K_LEFT]:
      paddle["x"] -= paddle["speed"]
    if key[pygame.K_RIGHT]:
      paddle["x"] += paddle["speed"]

    if paddle["x"] <= 0:
      paddle["x"] = 0
    if paddle["x"] >= WIDTH - paddle["width"]:
      paddle["x"] = WIDTH - paddle["width"]

    if x >= WIDTH - radius or x - radius <= 0:
      x_sens = -x_sens + randint(-1, 1)
    if y - radius <= 0:
      y_sens = -y_sens + randint(-1, 1)

    if y >= paddle["y"] - radius and (x >= paddle["x"]
                                      and x <= paddle["x"] + paddle["width"]):
      y_sens = -y_sens
      score += 1

    if y >= HEIGHT:
      end = True

    paddle["width"], score = paddlewidth(score, paddle["width"], lastestscore)
    lastestscore = score

    x = x + x_sens * speed
    y = y + y_sens * speed

    pygame.time.delay(10)

  endgame = losescreen(score)

pygame.time.delay(2000)
pygame.quit()
