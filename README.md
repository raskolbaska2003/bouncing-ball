# Bouncing Ball

A small interactive Python project built with Pygame. Set a ball's velocity with a mouse gesture and watch it fall under gravity and bounce with decreasing speed.

## Features

- A ball moves inside a 1600 × 900 window.
- A left-button mouse gesture sets its direction and speed.
- Gravity accelerates the ball downward.
- Wall collisions reverse the corresponding velocity component and retain 85% of its magnitude.
- A small vertical velocity near the floor triggers a resting state.
- The selected velocity and per-frame vertical velocity are printed to the console.
- The frame rate is capped at 240 FPS.

## Requirements

- Python 3
- Pygame

## Installation and launch

Download or clone the repository, then open a terminal in the project folder:

```sh
cd bouncing-ball
python -m pip install pygame
python bounce_mechanic.py
```

Run the script from this folder so it can find `ball.png`. Keep the image alongside the Python file.

## Controls

1. Press the left mouse button inside the window to record the starting cursor position.
2. Move the cursor while holding the button.
3. Release the button inside the window to set the ball's velocity.

The gesture sets the initial velocity in the direction from the press position to the release position; gravity then changes its vertical component. A longer gesture produces a higher initial speed. Clicking directly on the ball is not required, and pressing the button does not stop its current movement. Another gesture can launch the ball again after it settles.

Close the window to exit.

## How it works

Each velocity component is calculated from the corresponding cursor displacement, divided by 4 and truncated to an integer:

```python
speed = [
    int((mouse_position_2[0] - mouse_position[0]) / x),
    int((mouse_position_2[1] - mouse_position[1]) / x),
]
```

Here, `x` is set to `4`. The resulting values represent pixels per frame. Gesture duration is not used in the calculation.

Before moving the image's rectangle, the program checks whether its next position would cross a window boundary. On a collision, it adjusts the position and multiplies the corresponding velocity component by `-k_bounce`, where `k_bounce = 0.85`.

Gravity adds `0.5` to the vertical velocity each frame when either the ball's bottom is more than 2 pixels above the floor or the absolute vertical velocity exceeds `0.5`:

```python
if ball.bottom < height - 2 or abs(speed[1]) > 0.5:
    speed[1] += 0.5
else:
    ball.bottom = height
    speed[1] = 0
```

Otherwise, the ball is placed exactly on the floor and its vertical velocity is set to zero. This resting rule does not reset horizontal velocity, so the ball may continue moving sideways.

After collision handling and gravity, the ball is moved and drawn against a cleared background, then the display is updated.

## Project structure

```text
bouncing-ball/
├── bounce_mechanic.py  # Event handling, movement, collisions, and rendering
├── ball.png           # Ball image required at runtime
└── README.md
```

## Current limitations

- Window dimensions are fixed.
- Movement and gravity depend on the actual frame rate. The rectangle uses integer coordinates, so small fractional movements can be lost.
- Collision checks use a single `if`/`elif` chain, so only one boundary is handled per frame. Corner collisions and large movements may behave unexpectedly.
- The floor-resting threshold can also stop a weak upward movement close to the floor.
- The image path is relative to the current working directory.

This learning project explores mouse events, velocity vectors, gravity, damped bouncing, rectangle-based collision detection, and a Pygame animation loop.
