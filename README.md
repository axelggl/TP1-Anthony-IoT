
# IoT : TP Moteurs & Capteur Ultrason



## Auteurs

- [@dadidodz](https://www.github.com/dadidodz)
- [@LeYapson](https://github.com/LeYapson/)
- [@axel_ggl](https://github.com/axel_ggl/)


## Prérequis


Afin de faire fonctionner ce programme, vous aurez besoin :

- 1 ESP-32
- 2 moteurs à courant continu avec réducteur
- 1 capteur ultrason (HC-SR04)
- 1 câble micro-USB mâle vers USB mâle permettant de transférer des données
- L'IDE Thonny

## Implémentation du code sur l'ESP-32

Afin d'implémenter le code sur notre carte, connectez tout d'abord votre carte ESP-32 à votre ordinateur.

Vous aurez besoin d'ouvrir votre IDE Thonny. Assurez-vous que les options "Files" et "Shell" soient activées dans la partie "View". En haut à gauche, cliquez sur "Run" puis "Configure Interpreter".

Une nouvelle fenêtre va s'ouvrir sur votre ordinateur. Dans l'onglet "Interpreter", choisissez l'interpréteur "MicroPython (ESP32)".

Par la suite, cliquez sur "Install or update MicroPython (esptool)" pour installer le tout sur votre ESP32. 

Dans la partie "Target Port", choisissez "CP2012 USB To UART Bridge Controller". Si cette option ne s'affiche pas, cela signifie que vous n'avez pas le driver correspondant, vous pouvez l'installer en suivant ces liens : 

- Windows : http://www.silabs.com/documents/public/software/CP210x_VCP_Windows_XP_Vista.zip
- Mac : http://www.silabs.com/Support%20Documents/Software/Mac_OSX_VCP_Driver_10_6.zip
- Linux : http://www.silabs.com/Support%20Documents/Software/Linux_2.6.x_VCP_Driver_Source.zip




Choisissez la famille MicroPython "ESP32", puis la variante "Espressif - ESP32 / WROOM", et puis installez.

Dans la partie à gauche de votre fenêtre, vous devriez avoir accès aux fichiers présents sur votre ordinateur, ainsi qu'à ceux sur votre ESP-32, c'est-à-dire "boot.py".

Faites un clic droit sur la partie "MicroPython Device" et sélectionnez "New file". Renommez-le "main.py", et recommencez cette opération une seconde fois en le renommant "motors.py", une troisième fois avec "captor.py" et ainsi de suite.

Copiez-collez le contenu de nos fichiers dans les nouveaux fichiers créés sur votre ESP-32. Sauvegardez vos fichiers en vous rendant sur ceux-ci et en faisant CTRL+S.

Vous pouvez lancer le programme en allant sur votre "main.py", et en cliquant sur le bouton vert en dessous de "View", permettant de lancer votre programme.
