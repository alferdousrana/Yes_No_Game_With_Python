# Yes/No Game 🎮

A fun and interactive Python program built using Tkinter where the user is presented with a simple question: **"Do you like Python?"** 

The catch? You can click on **"Yes"**, but clicking on **"No"** is almost impossible, as the "No" button keeps moving when you hover over it! 😄

## Features
- Interactive GUI with Tkinter.
- A "No" button that hilariously avoids the mouse cursor.
- A "Yes" button that shows a thank-you message when clicked.


## Prerequisites
- Python 3.x
- Tkinter (comes pre-installed with Python)

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/alferdousrana/Yes_No_Game_With_Python.git
   cd yes-no-game
   ```
2. Run the script:
   ```bash
   python r-coding.py
   ```

## Code Overview
### Main Components
- **`on_yes_click` Function:** Displays a thank-you message when the "Yes" button is clicked.
- **`move_no_button` Function:** Randomly repositions the "No" button within the window when hovered over.

### Button Layout
- The **"Yes"** and **"No"** buttons are placed side by side initially.
- The **"No"** button moves to random positions upon hover.

### User Interface
- Clean and simple design created with Tkinter.
- Responsive buttons and interactive behavior.

## Example Output
1. The program asks, "Do you like Python?" 
2. If the user tries to hover over the "No" button, it moves to a random position.
3. Clicking "Yes" displays: **"Thank you for choosing Yes!"**

## Screenshot
![image](https://github.com/user-attachments/assets/f5552f05-1a66-49ce-8739-059153956643)


## Customization
Feel free to modify the code to:
- Change the question or button labels.
- Adjust the window size (`geometry` method in the script).
- Add more interactive elements!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy the game and share the laughter! 😄
