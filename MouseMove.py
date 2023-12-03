

try:
    import pyautogui
except ImportError:
    print("pyautogui package not found. Please install it using 'pip install pyautogui'.")
import time

print(pyautogui.position())

# Move to absolute position
pyautogui.moveTo(200, 100, duration=0.25)
pyautogui.moveTo(300, 100, duration=0.25)
pyautogui.moveTo(300, 200, duration=0.25)
pyautogui.moveTo(200, 200, duration=0.25)
pyautogui.moveTo(200, 100, duration=0.25)

# Move relative to current position
pyautogui.moveRel(100, 0, duration=0.25)
pyautogui.moveRel(0, 100, duration=0.25)
pyautogui.moveRel(-100, 0, duration=0.25)
pyautogui.moveRel(0, -100, duration=0.25)

# pyautogui.click(100, 100, button='left')
# pyautogui.click(200, 100, button='left')
# pyautogui.click(200, 200, button='left')
# pyautogui.click(100, 200, button='left')
# pyautogui.click(100, 100, button='left')


# Time to wait before moving the mouse
wait_time = 1

# Duration of the mouse movement
move_duration = 1

## Opcion 2: Mover mouse a coordenadas especificas
def move_mouse_to_coordinates(x, y):
    pyautogui.moveTo(x, y, duration=move_duration)
    print(f"Moved to ({x}, {y})")

if __name__ == "__main__":
    # Example coordinates (adjust as needed)
    target_x = 500
    target_y = 500

    # List of coordinates to visit
    coordinates = [
        (100, 100), 
        (200, 100), 
        (200, 200), 
        (100, 200), 
        (100, 100)
    ]

    # Move the mouse to the specified coordinates
    move_mouse_to_coordinates(target_x, target_y)

    # Move the mouse to each coordinate in the list
    for coord in coordinates:
        move_mouse_to_coordinates(coord[0], coord[1])
        time.sleep(wait_time)

    # Wait for a moment before the script exits
    time.sleep(wait_time)

print("Done.")