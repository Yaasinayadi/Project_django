# 🖥️ School Management System

Application web de gestion scolaire développée avec Django. Ce projet permet la gestion centralisée des étudiants, enseignants, matières, emplois du temps, examens, et plus encore.

## 📋 Présentation du Projet

Cette application a été conçue pour simplifier la gestion quotidienne d'une école en offrant :

- **Gestion des Étudiants** : Ajout, modification, suppression et consultation des informations des étudiants.
- **Gestion des Enseignants** : Suivi des enseignants et de leurs matières.
- **Gestion des Matières** : Organisation des matières enseignées.
- **Emplois du Temps** : Création et gestion des emplois du temps.
- **Gestion des Examens** : Planification des examens et suivi des résultats.
- **Gestion des Congés** : Ajout et suivi des jours fériés.

## 🛠️ Technologies Utilisées

- **Backend** : Django 4.x (Python 3.10+)
- **Frontend** : Templates Django + CSS + JavaScript Vanilla
- **Base de données** : SQLite (par défaut, extensible à PostgreSQL/MySQL)
- **Authentification** : Système d'authentification intégré de Django avec gestion des rôles (CustomUser).

## 📦 Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python 3.10 ou supérieur
- pip (gestionnaire de paquets Python)
- Un environnement virtuel (recommandé)
- Git

## ⚙️ Installation et Configuration

### 1. Cloner le projet

```bash
git clone https://github.com/Yaasinayadi/Project_django
cd Project_django
```

### 2. Créer et activer un environnement virtuel

Sous Windows :

```bash
python -m venv env
env\Scripts\activate
```

Sous macOS/Linux :

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations

Accédez au répertoire principal de l'application :

```bash
cd school
python manage.py migrate
```

### 5. Initialiser la base de données (Fixtures)

Le projet est fourni avec un fichier `db.sqlite3` contenant déjà un jeu de données complet. Toutefois, vous pouvez réinitialiser ou charger les données de test avec :

```bash
python manage.py loaddata seed_data.json
```

### 6. Lancer le serveur de développement

Toujours depuis le dossier `school`, lancez le serveur :

```bash
python manage.py runserver
```

L'application sera accessible à l'adresse : **http://127.0.0.1:8000**

## 🔑 Identifiants de Test

- **Administrateur** : Login = `admin` | Mot de passe = `admin123`
- **Enseignant (Exemple)** : Login = `youssef.alaoui` | Mot de passe = `password123`

(Note : Les mots de passe par défaut générés par le script `seed_data.py` sont `password123`.)

## 👥 Fonctionnalités par Rôle

| Rôle         | Permissions                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **Admin**    | Gestion complète du système, utilisateurs, étudiants, enseignants, etc.    |
| **Enseignant** | Gestion des matières, emplois du temps, et suivi des étudiants.            |
| **Étudiant** | Consultation des emplois du temps, résultats d'examens, et informations.   |

## 📁 Structure du Projet

Le projet suit l'architecture MVT (Model-View-Template) de Django :

- `requirements.txt` / `README.md` / `Rapport PFM Django.pdf` : Fichiers à la racine.
- `school/` : Dossier principal contenant le projet Django.
- `home_auth/` : Application gérant l'authentification et les rôles personnalisés.
- `faculty/` : Application pour la gestion des enseignants, départements et matières.
- `student/` : Application pour la gestion des étudiants et de leurs parents.
- `templates/` : Contient les fichiers HTML pour l'interface utilisateur.
- `static/` : Contient les fichiers CSS, JavaScript et images.
- `media/` : Contient les fichiers téléversés.
- `seed_data.json` : Fixture des données de test.
- `db.sqlite3` : Base de données SQLite par défaut.

## 🎥 Démonstration Vidéo

Une démonstration complète du projet est disponible ici :
[Voir la vidéo de démonstration](https://drive.google.com/drive/folders/1ZWrjEWfqHJVaHiqxvMlaQ_8CbOy_NLZV?usp=sharing)

## 👨‍💻 Contributeurs

Ce projet a été développé par l'équipe suivante dans le cadre du module de Développement web avancé - Back end (Python) :

- **CHRIAA Zakariae**
- **AYADI Yassine**

## 📄 Documentation Complémentaire

Pour plus de détails sur l'architecture (Diagramme UML) et les fonctionnalités du projet, consultez le rapport complet dans le fichier `Rapport PFM Django.pdf`.