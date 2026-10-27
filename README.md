# rm-matrix
matrix-style particle animation inspired by RM (Kim Namjoon) of BTS, built with Python and Pygame.

Inspired by the iconic digital aesthetic of *The Matrix* and dedicated to RM (Kim Namjoon) of BTS, this project combines random character generation, particle positioning, and time-based animation to create a minimalist visual effect.

## Features

- **Matrix-style digital rain:** Random green characters fall against a black background, creating a classic cyberpunk aesthetic.
- **RM particle formation:** Hundreds of character particles move towards predefined positions to form a large RM pattern.
- **Dynamic characters:** The particles display randomly selected letters from `NAMJOON`, reinforcing the project's theme.
- **Time-based animation:** The morphing effect begins after a short delay and progresses smoothly over time.
- **Minimalist visual design:** A black background, bright green characters, and a monospaced font recreate the familiar Matrix look.

## Built With

- **Python**: Core programming language.
- **Pygame**: Window management, rendering, event handling, and animation.
- **Random**: Random character selection and particle positioning.

## How It Works

The animation combines two visual elements:

1. **Digital rain:** Random characters are rendered at different screen positions, producing a constantly changing Matrix-style background.
2. **Particle morphing:** Particles start at random positions and move towards target coordinates arranged according to a predefined RM pattern.

The morphing effect begins after 4 seconds and reaches its final interpolation stage after 8 seconds.

## Getting Started

### Prerequisites

Make sure you have Python 3 installed.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/alessandradibonito/rm-matrix.git
   ```

2. Navigate to the project directory:

   ```bash
   cd rm-matrix
   ```

3. Install Pygame:

   ```bash
   python -m pip install pygame
   ```

### Run the Project

Execute the Python script:

```bash
python main.py
```

Replace `main.py` with the name of your Python file if it differs.

A window will open displaying the animated Matrix-style rain and the RM particle effect. Close the window to exit.

## ⚙️ Configuration

You can customize the animation by modifying the constants at the beginning of the script.

| Setting | Default | Description |
|---|---:|---|
| `WIDTH` | `1200` | Window width in pixels |
| `HEIGHT` | `800` | Window height in pixels |
| `FPS` | `60` | Target frame rate |
| `FONT_SIZE` | `16` | Character font size |
| `GREEN` | `(0, 255, 120)` | Color of the characters |
| `BLACK` | `(0, 0, 0)` | Background color |
| `START_MORPH` | `4.0` | Time in seconds before morphing starts |
| `FULL_MORPH` | `8.0` | Time in seconds when interpolation reaches completion |

You can also edit `RAIN_TEXT` to change the characters used in the background rain or modify `RM_PATTERN` to experiment with different letter shapes.

## 📁 Project Structure

```text
rm-matrix/
├── main.py
└── README.md
```

The project currently uses a single Python script, keeping the implementation lightweight and easy to experiment with.

Future enhancements could include:

- Adding continuous downward movement to the Matrix rain.
- Creating a more fluid particle transition using easing functions.
- Introducing particle trails and fading effects.
- Adding more complex text or custom shapes.
- Allowing users to customize the colors, text, and animation timing.
- Improving the particle movement so the RM shape remains stable after forming.

## Purpose

This project is a small creative coding experiment exploring real-time graphics, randomisation, particle animation and visual effects with Python and Pygame.

It is also a way to combine programming with a personal appreciation for RM and the distinctive digital aesthetic of *The Matrix*.

## License

No license has been specified yet. If you want others to use, modify, or redistribute this project, consider adding an appropriate open-source license.

---

*Made with Python, Pygame, and a little Namjoon-inspired digital rain. 💚*


