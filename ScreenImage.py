import pyautogui
import time
import pygetwindow as gw

# Function to check if the mouse is over a specific button using image matching
def is_over_button(button_image_path, region_x_size=400, region_y_size=200):
    
    # Crea un screenshot y la guarda en el directorio
    #screenshot = pyautogui.screenshot()
    #screenshot.save('imgs/full_screen.png')

    #return pyautogui.locateOnScreen(button_image_path) is not None
    x, y = pyautogui.position()
    
    # Capture a small region around the mouse position
    region = (
        x - region_x_size // 2,
        y - region_y_size // 2,
        region_x_size,
        region_y_size
    )

    # Capture the region of interest
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('imgs/captured_screen.png')
    
    # Check if the button image is present in the captured region
    return pyautogui.locateOnScreen(button_image_path, region=region) is not None


# Example usage
# Replace 'button.png' with the path to the image of your button
#'./imgs/buttonGPT.png'
button_image_path = 'imgs/buttonGPT.png' 


# Move the mouse to the region of interest
pyautogui.moveTo(500, 500, duration=1)

# Set the region size
region_x_size = 200
region_y_size = 100

# Check if the mouse is over the button using image matching
if is_over_button(button_image_path, region_x_size, region_y_size):
    print("Mouse is over the button!")
else:
    print("Mouse is not over the button.")

# Optional: Add a delay before the script exits
time.sleep(2)
