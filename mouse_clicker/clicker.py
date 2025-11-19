import pyautogui
import time
import subprocess
import sys

#pip install opencv-python pip install pillow pyscreeze opencv-python

print("Starting in 3 seconds...")
time.sleep(3)

# URL to open
url = "https://web.dixiponto.com.br/"

# Launch Firefox with a dedicated profile
firefox_process = subprocess.Popen([
    "firefox",
    "-no-remote",
    "-P", "automation",
    "--new-window",
    url
])

# Wait for Firefox to load the page
print("Waiting 10 seconds for page to load...")
time.sleep(10)


# Try to locate the "USUARIO" button on screen
image_path = "/home/j/bin/mouse_clicker/usuario.png"
print(f"Looking for button: {image_path}")

try:
    button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if button_location is None:
        print("USUARIO button not found!")
        sys.exit(1)

    # Get center of the button and click
    button_center = pyautogui.center(button_location)
    pyautogui.moveTo(button_center.x, button_center.y, duration=0.5)
    pyautogui.click()
    print(f"Clicked on 'USUARIO' button at {button_center}")
    time.sleep(1)
    pyautogui.write('juliocezar')
except Exception as e:
    print(f"Error locating button: {e}")

# Wait 5 seconds
time.sleep(5)


# Try to locate the "SENHA" button on screen
image_path = "/home/j/bin/mouse_clicker/senha.png"
print(f"Looking for button: {image_path}")

try:
    button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if button_location is None:
        print("SENHA button not found!")
        sys.exit(1)

    # Get center of the button and click
    button_center = pyautogui.center(button_location)
    pyautogui.moveTo(button_center.x, button_center.y, duration=0.5)
    pyautogui.click()
    print(f"Clicked on 'SENHA' button at {button_center}")
    time.sleep(1)
    pyautogui.write('Mopa2022.')
except Exception as e:
    print(f"Error locating button: {e}")

# Wait 5 seconds
time.sleep(5)


# Try to locate the "UNIDADE" button on screen
image_path = "/home/j/bin/mouse_clicker/unidade.png"
print(f"Looking for button: {image_path}")

try:
    button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if button_location is None:
        print("UNIDADE button not found!")
        sys.exit(1)

    # Get center of the button and click
    button_center = pyautogui.center(button_location)
    pyautogui.moveTo(button_center.x, button_center.y, duration=0.5)
    pyautogui.click()
    print(f"Clicked on 'UNIDADE' button at {button_center}")
    time.sleep(1)
    pyautogui.write('plennus-tecnologia')
except Exception as e:
    print(f"Error locating button: {e}")

# Wait 5 seconds
time.sleep(5)

# Try to locate the "ENTRAR" button on screen
image_path = "/home/j/bin/mouse_clicker/entrar.png"
print(f"Looking for button: {image_path}")

try:
    button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if button_location is None:
        print("ENTRAR button not found!")
        sys.exit(1)

    # Get center of the button and click
    button_center = pyautogui.center(button_location)
    pyautogui.moveTo(button_center.x, button_center.y, duration=0.5)
    pyautogui.click()
    print(f"Clicked on 'ENTRAR' button at {button_center}")
except Exception as e:
    print(f"Error locating button: {e}")

# Wait 5 seconds
time.sleep(5)

# Try to locate the "BATIDA DE PONTO" button on screen
image_path = "/home/j/bin/mouse_clicker/batida-de-ponto.png"
print(f"Looking for button: {image_path}")

try:
    button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if button_location is None:
        print("BATIDA DE PONTO button not found!")
        sys.exit(1)

    # Get center of the button and click
    button_center = pyautogui.center(button_location)
    pyautogui.moveTo(button_center.x, button_center.y, duration=0.5)
    pyautogui.click()
    print(f"Clicked on 'BATIDA DE PONTO' button at {button_center}")
except Exception as e:
    print(f"Error locating button: {e}")


# Wait 5 seconds
time.sleep(5)

# Try to locate the "REGISTRAR PONTO" button on screen
image_path = "/home/j/bin/mouse_clicker/registrar-ponto.png"
print(f"Looking for button: {image_path}")

try:
    button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if button_location is None:
        print("REGISTRAR PONTO button not found!")
        sys.exit(1)

    # Get center of the button and click
    button_center = pyautogui.center(button_location)
    pyautogui.moveTo(button_center.x, button_center.y, duration=0.5)
    pyautogui.click()
    print(f"Clicked on 'REGISTRAR PONTO' button at {button_center}")
except Exception as e:
    print(f"Error locating button: {e}")

print("Done! Closing firefox")

# Wait 30 seconds
time.sleep(30)

# Send SIGTERM to the Firefox process we launched
firefox_process.terminate()

# Wait a few seconds to make sure it closes
try:
    firefox_process.wait(timeout=5)
except subprocess.TimeoutExpired:
    # Force kill if it didn’t close
    firefox_process.kill()
