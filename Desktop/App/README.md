# Projet2
Projet2 | Corona Virus
Première version:

Flask est fonctionnel.
Attention!! Ne jamais modifier le nom du fichier "templates" et ajouter tous les fichiers .html ainsi que .css dans celui-ci sinon Flask ne s'y retrouve plus.
_________________

Pour installer Flask,
Rendez-vous sur le dossier "Projet2" si vous n'y ếtes pas déjà.
Tappez la commande python3 -m venv venv 
Si venv n'est pas déjà installé rajouté d'abord cette commande:
sudo apt-get install venv
. venv/bin/activate
pip install Flask
Attention, si pip n'est pas encore installé tappez:
#sudo apt-get install python3-pip
sudo apt-get install python-virtualenv
Ensuite, exportez l'app dans flask
export FLASK_APP=app.py
Enfin:
flask run
Et rendez-vous sur:
http://127.0.0.1:5000/
Attention si vous voulez relancer le serveur mais qu'il occupe encore le port 5000:
sudo lsof -t -i tcp:5000 | xargs kill -9
