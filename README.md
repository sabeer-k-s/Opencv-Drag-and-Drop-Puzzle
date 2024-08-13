# Drag-and-Drop Image Puzzle with Hand Tracking

## Overview

This project is an interactive image puzzle game where users can solve a jumbled image by dragging and dropping its pieces into the correct order. The puzzle is built using OpenCV, and it leverages a hand tracking module to detect finger positions, allowing users to interact with the puzzle using hand gestures.

## Features

- **Drag-and-Drop Functionality:** Users can move image pieces by dragging them to the desired location using hand gestures.
- **Hand Tracking:** The project uses a hand tracking module to detect finger positions, enabling intuitive control over the puzzle pieces.
- **Puzzle Completion Detection:** The game recognizes when all pieces are correctly placed, signaling the successful completion of the puzzle.

## Technologies Used

- **OpenCV:** For image processing and displaying the puzzle.
- **Mediapipe:** For hand tracking and detecting finger positions.
- **Python:** The programming language used to implement the project.

## How It Works

1. **Image Loading and Splitting:**
   - The input image is divided into multiple pieces, which are then shuffled to create the puzzle.

2. **Hand Tracking:**
   - The hand tracking module detects the user's hand and tracks finger positions, which are used to drag and drop puzzle pieces.

3. **Piece Movement:**
   - Users can drag a puzzle piece by placing a finger over it and moving it to the desired position.
   
4. **Puzzle Solving:**
   - The program continuously checks the positions of all pieces. When all pieces are correctly arranged, the puzzle is considered solved.

## Setup and Installation

### Prerequisites

- Python3
- OpenCV
- Mediapipe

### Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/sabeer-k-s/Opencv-Drag-and-Drop-Puzzle.git
```

2. **Install the Required Packages:**

```bash
pip install opencv-python mediapipe
```

3. **Run the Program:**

```bash
python app.py
```

## Usage

- **Start the Game:** Run the `app.py` script to start the puzzle.
- **Control the Pieces:** Use your hand to drag and drop pieces into place.
- **Solve the Puzzle:** Arrange all pieces correctly to complete the puzzle.

## Demo

![Puzzle Demo](path/to/demo_image.png)

## Conclusion

This project demonstrates the integration of computer vision and gesture recognition in an interactive application. It showcases how hand tracking can be used to create engaging and intuitive user experiences.

---
