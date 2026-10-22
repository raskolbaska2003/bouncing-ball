# Bouncing Ball

A small interactive Python project built with Pygame. Set a ball's velocity with a mouse gesture and watch it bounce off the window edges.

## Features

- A ball moves inside a 1600 × 900 window.
- A left-button mouse gesture sets its direction and speed.
- The ball reverses its horizontal or vertical velocity when it crosses a window boundary.
- The selected velocity is printed to the console.
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

The ball moves in the direction from the press position to the release position. A longer gesture produces a higher speed. Clicking directly on the ball is not required, and pressing the button does not stop its current movement.

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

Pygame moves the image's rectangle each frame. If it crosses a horizontal or vertical boundary, the corresponding velocity component changes sign. The background is cleared and the ball is drawn at its new position before the display is updated.

## Project structure

```text
bouncing-ball/
├── bounce_mechanic.py  # Event handling, movement, collisions, and rendering
├── ball.png           # Ball image required at runtime
└── README.md
```

## Current limitations

- Window dimensions are fixed.
- Movement depends on the actual frame rate.
- Collision handling reverses velocity without moving the ball back inside the window, which can cause problems with large movements near an edge.
- The image path is relative to the current working directory.

This learning project explores mouse events, velocity vectors, rectangle-based collision detection, and a Pygame animation loop.
