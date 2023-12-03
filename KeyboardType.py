

import pyautogui
import time


if __name__ == "__main__":

    # Get the current mouse coordinates
    print("Move the mouse to the input box and get the coordinates.")
    time.sleep(5)  # Give the user time to position the mouse
    x, y = pyautogui.position()
    print(f"Coordinates: ({x}, {y})")

    # Optional: Add a delay before starting to type
    time.sleep(2)

    # Type "Hello, World" into the input box
    pyautogui.click(x, y)  # Click on the input box to focus it
    pyautogui.typewrite("Hello, World", interval=0.2)

    # Optional: Add a delay after typing
    time.sleep(2)

print("Done.")