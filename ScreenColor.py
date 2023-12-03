import pyautogui
import time

# Function to check if the mouse is over a specific button based on pixel color
def is_over_button(button_color):
    x, y = pyautogui.position()
    pixel_color = pyautogui.pixel(x, y)
    return pixel_color == button_color

# Example usage
# Replace (x_button, y_button) with the coordinates of the button
x_button, y_button = 100, 100
button_color = (255, 0, 0)  # Replace with the expected RGB color of the button

# Move the mouse to the button
pyautogui.moveTo(x_button, y_button, duration=1)

# Check if the mouse is over the button based on pixel color
if is_over_button(button_color):
    print("Mouse is over the button!")
else:
    print("Mouse is not over the button.")

# Optional: Add a delay before the script exits
time.sleep(2)