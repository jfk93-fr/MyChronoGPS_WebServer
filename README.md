# MyChronoGPS_WebServer

	**MyChronoGPS_WebServer** est un complément de **MyChronoGPS** (https://github.com/jfk93-fr/MyChronoGPS)
	Permet de voir des sessions ou des circuits récupérés à partir des téléchargements issus de MyChronoGPS.
	Utile pour analyser les données sans utiliser MyChronoGPS
	et pour partager ou utiliser des sessions de roulage.
	
# Installation

	MyChronoGPS_WebServer est un serveur web écrit en Python.
	Je n'ai pas réussi à en faire une commande .exe pour Windows avec pyinstaller !
	
	Récupérer le code sur https://github.com/jfk93-fr/MyChronoGPS_WebServer/archive/refs/heads/main.zip
	ou par git clone https://github.com/jfk93-fr/MyChronoGPS_WebServer.git
	
# Windows

	. Prérequis : Python installé sur le PC.
	
	Télécharger et installer l'archive .zip dans un dossier
	Ouvrir une fenêtre invite de commande
	Se placer dans le dossier d'installation de MyChronoGPS_WebServer
	Saisir la commande suivante :
	
	>python MyChronoGPS_WebServer.py
	
# Linux

	Installer MyChronoGPS_WebServer
	Ouvrir une fenêtre Terminal
	Passer les commandes :
	
	>git clone https://github.com/jfk93-fr/MyChronoGPS_WebServer.git
	>cd MyChronoGPS_WebServer
	>sudo chmod -R 0777 $HOME/MyChronoGPS_WebServer

# Lancement MyChronoGPS_WebServer

	Ouvrir une fenêtre Terminal

	Se placer dans le dossier MyChronoGPS_WebServer
	>cd $HOME/MyChronoGPS_WebServer
	
	Passer la commande :
	>python3 MyChronoGPS_WebServer.py

# Utilisation
	
	Ouvrir le navigateur internet se placer dans la barre d'adresse et saisir l'URL suivante :
	
	>localhost:8080
	
	(A partir d'un autre PC, remplacer `localhost` par l'adresse ip du PC où tourne MyChronoGPS_WebServer)
	
	La fenêtre d'accueil de MyChronoGPS_WebServer devrait apparaitre.
