import os
platformio_folder = "E:\user\Google Drive\MADNERD\github"

arduino_dirs = []
arduino_inos = []
if os.path.isdir(platformio_folder):
    for root, dirs, files in os.walk(platformio_folder):
        for name in files:
            if name.endswith(("platformio.ini")):
                arduino_dirs.append(root)
                arduino_inos_temp = root.split("\\")
                arduino_inos.append(arduino_inos_temp[len(arduino_inos_temp)-2])

print(arduino_dirs)
print(arduino_inos)

#cd "E:\user\Google Drive\MADNERD\github\leds*\arduino\" && platformio run
