# Crear VENV de app que mueve mouse


Genere distintos scripts para probar las funcionalidades de python
- MouseMove.py (mueve el mouse a coordenadas especificas)
- KeyboardType.py (tipea lo que necesites)
- ScreenColor.py (obtiene el color de un pixel)
- ScreenImage.py (indica si hay un botón o imagen presente en una región específica [y captura la pantalla])

## Crear un entorno virtual

```bash 
python -m venv mouse_move
```

## Activar el entorno virtual

```bash
cd mouse_move
Scripts/activate
``` 

## Instalar paquetes

```bash
pip install pyautogui
```

## Crear Python Script MouseMove.py

```python
    import pyautogui
    import time

    print(pyautogui.position())

    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    pyautogui.moveTo(100, 100, duration=0.25)

    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)

    pyautogui.click(100, 100, button='left')
    pyautogui.click(200, 100, button='left')
    pyautogui.click(200, 200, button='left')
    pyautogui.click(100, 200, button='left')
    pyautogui.click(100, 100, button='left')

    ## Opcion 2: Mover mouse a coordenadas especificas
    def move_mouse_to_coordinates(x, y):
        pyautogui.moveTo(x, y, duration=1)

    if __name__ == "__main__":
        # Example coordinates (adjust as needed)
        target_x = 500
        target_y = 500

        # Move the mouse to the specified coordinates
        move_mouse_to_coordinates(target_x, target_y)

        # Wait for a moment before the script exits
        time.sleep(2)
```



## Ejecutar un script

```bash
python MouseMove.py
```

## Desactivar el entorno virtual

```bash
deactivate
```

## Crear archivo requirements.txt

```bash
pip freeze > requirements.txt
```

## Crear archivo README.md

```bash
touch README.md
```

## Crear archivo .gitignore

```bash
touch .gitignore
```

## Crear repositorio en GitHub

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin

git push -u origin main
```



