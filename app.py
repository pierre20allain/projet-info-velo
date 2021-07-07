from repr_graph_prog import repr_entr
from planning import fct_planning
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from PIL import Image

from classes import Individu, Endurance, Sprint, Tempo, Sweet_spot, Capacite_aerobie, Capacite_anaerobie, Seuil, Recup_active
from programmevelo import fct_entrainement_ftp_max, fct_entrainement_ftp_min


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# On lie le site aux différentes bases de données
def get_db_connection():
    conn = sqlite3.connect('personnes.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_db_connection2():
    conn = sqlite3.connect('entrainements.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_username(username):
    conn = get_db_connection()
    username = conn.execute('SELECT * FROM personnes WHERE username = ?',
                        (username,)).fetchone()
    conn.close()
    if username is None:
        abort(404)
    return username


"""
def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?',
                        (user_id,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user
"""
# Page de base, ne contenant que la barre de navigation
@app.route('/')
def index():
    return render_template('base1.html')


# Page d'inscription
@app.route('/login',methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        age = request.form['age']
        pma = request.form['pma']
        lthr = request.form['lthr']
        ftp = request.form['ftp']
        duree = request.form['duree']
        username = request.form['username']
        mdp = request.form['mdp']
        jour = request.form['jour']
        


        
        # On demande à l'utilisateur de remplir toutes les données
        if not (nom and prenom and age and (pma or lthr or ftp) and duree and username and mdp and jour) :
            flash('Il faut remplir toutes les informations')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO personnes (nom, prenom, age, pma, lthr, ftp, duree, username, mdp, jour) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                         (nom, prenom, age, pma, lthr, ftp, duree, username, mdp, jour))
            conn.commit()
            conn.close()
            return redirect(url_for('planning', username=username))

    #conn = get_db_connection()
    #users = conn.execute('SELECT * FROM personnes').fetchall()
    #conn.close()
    return render_template('inscription.html')

# Connexion
@app.route('/connexion',methods=['GET'])
def do_admin_login():
    if request.method == 'POST':
        username = request.form['username']
        mdp = request.form['mdp']

        conn = get_db_connection()
        conn.execute("SELECT mdp FROM personnes WHERE username = ?", username)
        result = eval(conn.fetchone()) #il y aura un problème quand fetchone retournera None mais jsp comment faire

        if not (username and mdp) :
            flash('Il faut remplir toutes les informations')
        
        else :
            if result == mdp:        
                session['logged_in'] = True
            else:
                flash('wrong username or password!')
            conn.close()
            return redirect(url_for('planning', username=username))

    return render_template('connexion.html')

"""
# Deconnexion
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))
"""

# A destination de l'administrateur de la page pour simplifier l'ajout d'entrainements
@app.route('/entreeEntrainement',methods=('GET', 'POST'))
def login_training():
    if request.method == 'POST':
        label = request.form['label']
        seance = request.form['seance']
        duree = request.form['duree']
        repetitions = request.form['repetitions']
        intensite = request.form['intensite']


        if not (label and seance and duree and repetitions and intensite) :
            flash('Il faut remplir toutes les informations')
        else:
            conn = get_db_connection2()
            conn.execute('INSERT INTO entrainements (label, seance, duree, repetitions, intensite) VALUES (?, ?, ?, ?, ?)',
                         (label, seance, duree, repetitions, intensite))
            conn.commit()
            conn.close()
            return redirect(url_for('accueil'))

    #conn = get_db_connection()
    #users = conn.execute('SELECT * FROM personnes').fetchall()
    #conn.close()
    return render_template('entreeEntrainement.html')

#Page du planning des entraînements
@app.route('/planning/<username>', methods=('GET', 'POST'))
def planning(username):

    planning = fct_planning(username)

    repr_entr(planning)

    return render_template('planning.html', username=username)

