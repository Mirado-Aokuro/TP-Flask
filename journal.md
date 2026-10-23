I - Mission 1 — Faire tourner Flask

1. Lancer flask --app app run. Modifier le texte, sauvegarder, recharger la page. Observe : la
modification apparaît-elle ?

-> ca ne modifie rien 

(.venv) PS E:\tp2-fask-taches> flask --app app run        
 * Serving Flask app 'app'
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [23/Oct/2026 00:07:58] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [23/Oct/2026 00:07:59] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [23/Oct/2026 00:08:49] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [23/Oct/2026 00:08:51] "GET / HTTP/1.1" 200 -


2. Arrêter le serveur (Ctrl + C), relancer avec flask --app app run --debug et refaire l'essai.
Observe : que dit le terminal au moment où vous sauvegardez ?

(.venv) PS E:\tp2-fask-taches> flask --app app run --debug
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 956-468-667
127.0.0.1 - - [23/Oct/2026 00:09:25] "GET / HTTP/1.1" 200 -
 * Detected change in 'E:\\tp2-fask-taches\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 956-468-667
127.0.0.1 - - [23/Oct/2026 00:12:49] "GET / HTTP/1.1" 200 -


4. Lancer simplement flask run --debug, sans --app. Observe : pourquoi cela fonctionne-t-il ?

-> Cela fonctionne car flask détecte et charge automatiquement l'application à partir du fichier par défaut comme app.py présent dans le dossier de travail.

(.venv) PS E:\tp2-fask-taches> flask run --debug
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 956-468-667


* Explique. À quoi sert l'option --debug ? Pourquoi ne faut-il jamais l'utiliser en production ? Pourquoi --
app est-il facultatif ici ?

L'option --debug active le mode débogage de Flask et permet de relancer automatiquement en cas de modification du code. L'option --app sert à indiquer à Flask quel fichier contient mon application , elle est facultative si le fichier principal s'appelle app.py car Flask cherche automatiquement par défaut dans les noms de fichiers du dossier utiliser.




II - Mission 2 — Jouer avec les URL

 1. Visiter /taches/2. Observe : qu'affiche la page ? Est-ce normal ?

Tâche introuvable

-> C'est normal que la page affiche "Tâche introuvable" car l'ID de l'URL est capturé comme une chaîne de caractères "2" et ne correspond pas aux nombres entiers "2" de votre liste.

2. Ajouter print(type(id), id) au début de la fonction et revisiter la page. Observe le terminal

Tâche introuvable

(.venv) PS E:\tp2-fask-taches> flask --app app run --debug
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 956-468-667
127.0.0.1 - - [23/Oct/2026 00:34:53] "GET /taches/2 HTTP/1.1" 200 -
 * Detected change in 'E:\\tp2-fask-taches\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 956-468-667
<class 'str'> 2
127.0.0.1 - - [23/Oct/2026 00:35:22] "GET /taches/2 HTTP/1.1" 200 -


3. Remplacer <id> par <int:id>. Visiter /taches/2, puis /taches/abc. Observe.

-> avec le premier ca montre : Installer Flask


-> le deuxieme avec Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.


voila ce qu'on a vu dans le terminal : 127.0.0.1 - - [23/Oct/2026 00:35:22] "GET /taches/2 HTTP/1.1" 200 -
 * Detected change in 'E:\\tp2-fask-taches\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 956-468-667
<class 'int'> 2
127.0.0.1 - - [23/Oct/2026 00:38:11] "GET /taches/2 HTTP/1.1" 200 -
127.0.0.1 - - [23/Oct/2026 00:38:50] "GET /taches/abc HTTP/1.1" 404 -


4. Visiter /taches/2/, avec une barre oblique à la fin. Observe.

127.0.0.1 - - [23/Oct/2026 00:40:13] "GET /taches/2/ HTTP/1.1" 404 -
127.0.0.1 - - [23/Oct/2026 00:40:35] "GET /taches/2/ HTTP/1.1" 404 -
127.0.0.1 - - [23/Oct/2026 00:40:36] "GET /taches/2/ HTTP/1.1" 404 -
127.0.0.1 - - [23/Oct/2026 00:40:36] "GET /taches/2/ HTTP/1.1" 404 -
127.0.0.1 - - [23/Oct/2026 00:40:37] "GET /taches/2/ HTTP/1.1" 404 -
127.0.0.1 - - [23/Oct/2026 00:40:37] "GET /taches/2/ HTTP/1.1" 404 -


5. Visiter /taches/99. Ouvrir les outils du navigateur (F12, onglet Réseau) et recharger. Observe : quel
est le code de la réponse, 200 ou 404 ?

-> code 202








III - Mission 3 — Afficher les tâches

1. Afficher la page. Observe : sous quelle forme la liste apparaît-elle ?

Mes tâches
[{'id': 1, 'titre': 'Réviser les décorateurs', 'priorite': 'haute', 'terminee': False}, {'id': 2, 'titre': 'Installer Flask', 'priorite': 'normale', 'terminee': True}, {'id': 3, 'titre': 'Lire la doc Jinja2', 'priorite': 'basse', 'terminee': False}]


2. Remplacer le paragraphe par une boucle : {% for t in taches %}<li>{{ t.titre }}</li>{%
endfor %} dans une liste <ul>. Observe : t.titre fonctionne alors que t est un dictionnaire.

Mes tâches
Réviser les décorateurs
Installer Flask
Lire la doc Jinja2


3. Ajouter {{ loop.index }} devant chaque titre. Tester ensuite au moins trois filtres choisis dans la
liste officielle (par exemple upper, length, sort(attribute="titre")). Observe et note ceux qui
fonctionnent.

Mes tâches
1 ) Réviser les décorateurs
2 ) Installer Flask
3 ) Lire la doc Jinja2


upper :

1 ) RÉVISER LES DÉCORATEURS
2 ) INSTALLER FLASK
3 ) LIRE LA DOC JINJA2

lenght :

1 ) 23
2 ) 15
3 ) 18

sort(attribute="titre") :

Mes taches (Total : [{'id': 2, 'titre': 'Installer Flask', 'priorite': 'normale', 'terminee': True}, {'id': 3, 'titre': 'Lire la doc Jinja2', 'priorite': 'basse', 'terminee': False}, {'id': 1, 'titre': 'Réviser les décorateurs', 'priorite': 'haute', 'terminee': False}])


4. Barrer les tâches terminées avec {% if t.terminee %} et la balise <s>, ou avec une classe CSS

1 ) RÉVISER LES DÉCORATEURS
2 ) INSTALLER FLASK #il est barrer
3 ) LIRE LA DOC JINJA2


IV - Mission 4 — Un menu commun


1. Créer templates/base.html avec la structure HTML complète, un menu <nav> et un bloc {%
block contenu %}{% endblock %}. Faire hériter taches.html de base.html. Afficher le code
source de la page (Ctrl + U). Observe.

<!DOCTYPE html>
<html lang="fr">
<head>
    
    
    <link rel="stylesheet" href="style.css" />
    
    <style type="text/css">
        .important { color: #336699; }
    </style>

</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Accueil</a></li>
            <li><a href="/">Tâches</a></li>
        </ul>
    </nav>
    <div id="content">

<h1>Mes tâches</h1>
<ul>
    
        <li >1 ) RÉVISER LES DÉCORATEURS</li>
    
        <li style="text-decoration: line-through;">2 ) INSTALLER FLASK</li>
    
        <li >3 ) LIRE LA DOC JINJA2</li>
    
</ul>

</div>
</body>
</html>


2. Dans taches.html, écrire une phrase en dehors de tout bloc. Observe.

-> elle est ignoré et non afficher


3. Dans base.html, mettre un bloc dans <title> : {% block titre %}Mes tâches{% endblock
%}. Le redéfinir dans taches.html, puis essayer {{ super() }} à l'intérieur. Observe.

-> le titre chnage

4. Créer static/style.css avec une règle simple, par exemple body { font-family: sansserif; }, et la lier dans base.html avec url_for('static', filename='style.css'). Visiter
directement /static/style.css. Observe.

-> on voit le code : 

body {
    font-family: sans-serif;
    background-color: skyblue;
}


5. Dans le menu, ajouter un lien vers url_for('ajouter'). Observe l'erreur : la route ajouter
n'existe pas encore. Retirer le lien jusqu'à la mission 5.             >

* sur la page :

BuildError
werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'ajouter'. Did you mean 'tache' instead?

Traceback (most recent call last)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1536, in __call__
return self.wsgi_app(environ, start_response)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1514, in wsgi_app
response = self.handle_exception(e)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1511, in wsgi_app
response = self.full_dispatch_request()
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 919, in full_dispatch_request
rv = self.handle_user_exception(e)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 917, in full_dispatch_request
rv = self.dispatch_request()
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 902, in dispatch_request
return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
File "E:\tp2-fask-taches\app.py", line 18, in index
return render_template("taches.html", taches=taches)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\templating.py", line 151, in render_template
return _render(app, template, context)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\templating.py", line 132, in _render
rv = template.render(context)
File "E:\tp2-fask-taches\.venv\lib\site-packages\jinja2\environment.py", line 1295, in render
self.environment.handle_exception()
File "E:\tp2-fask-taches\.venv\lib\site-packages\jinja2\environment.py", line 942, in handle_exception
raise rewrite_traceback_stack(source=source)
File "E:\tp2-fask-taches\templates\taches.html", line 1, in top-level template code
{% extends "base.html" %}
File "E:\tp2-fask-taches\templates\base.html", line 14, in top-level template code
<li><a href="{{ url_for('ajouter') }}">Ajouter</a></li>
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1121, in url_for
return self.handle_url_build_error(error, endpoint, values)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1110, in url_for
rv = url_adapter.build(  # type: ignore[union-attr]
File "E:\tp2-fask-taches\.venv\lib\site-packages\werkzeug\routing\map.py", line 901, in build
raise BuildError(endpoint, values, method, self)

* sur terminal :

127.0.0.1 - - [23/Oct/2026 02:22:46] "GET / HTTP/1.1" 500 -
Traceback (most recent call last):
  File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1536, in __call__
    return self.wsgi_app(environ, start_response)
  File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1514, in wsgi_app
    response = self.handle_exception(e)
  File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
  File "E:\tp2-fask-taches\app.py", line 18, in index
    return render_template("taches.html", taches=taches)
  File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\templating.py", line 151, in render_template
    return _render(app, template, context)
  File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\templating.py", line 132, in _render
    rv = template.render(context)
  File "E:\tp2-fask-taches\.venv\lib\site-packages\jinja2\environment.py", line 1295, in render
    self.environment.handle_exception()
  File "E:\tp2-fask-taches\.venv\lib\site-packages\jinja2\environment.py", line 942, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "E:\tp2-fask-taches\templates\taches.html", line 1, in top-level template code
    {% extends "base.html" %}
  File "E:\tp2-fask-taches\templates\base.html", line 14, in top-level template code
    <li><a href="{{ url_for('ajouter') }}">Ajouter</a></li>
  File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1121, in url_for
    return self.handle_url_build_error(error, endpoint, values)
  File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1110, in url_for
    rv = url_adapter.build(  # type: ignore[union-attr]
  File "E:\tp2-fask-taches\.venv\lib\site-packages\werkzeug\routing\map.py", line 901, in build
    raise BuildError(endpoint, values, method, self)
werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'ajouter'. Did you mean 'tache' instead?
127.0.0.1 - - [23/Oct/2026 02:22:46] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 -
127.0.0.1 - - [23/Oct/2026 02:22:46] "GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 -
127.0.0.1 - - [23/Oct/2026 02:22:47] "GET /?__debugger__=yes&cmd=resource&f=console.png&s=B9IxfMVDckkLr5vS1tcR HTTP/1.1" 200 -
127.0.0.1 - - [23/Oct/2026 02:22:47] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 -


6. Renommer le dossier templates en template. Observe, puis remettre le bon nom.

lorsqu'on enleve le s :

TemplateNotFound
jinja2.exceptions.TemplateNotFound: taches.html

Traceback (most recent call last)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1536, in __call__
return self.wsgi_app(environ, start_response)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1514, in wsgi_app
response = self.handle_exception(e)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1511, in wsgi_app
response = self.full_dispatch_request()
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 919, in full_dispatch_request
rv = self.handle_user_exception(e)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 917, in full_dispatch_request
rv = self.dispatch_request()
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 902, in dispatch_request
return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
File "E:\tp2-fask-taches\app.py", line 18, in index
return render_template("taches.html", taches=taches)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\templating.py", line 150, in render_template
template = app.jinja_env.get_or_select_template(template_name_or_list)
File "E:\tp2-fask-taches\.venv\lib\site-packages\jinja2\environment.py", line 1087, in get_or_select_template
return self.get_template(template_name_or_list, parent, globals)
File "E:\tp2-fask-taches\.venv\lib\site-packages\jinja2\environment.py", line 1016, in get_template
return self._load_template(name, globals)
File "E:\tp2-fask-taches\.venv\lib\site-packages\jinja2\environment.py", line 975, in _load_template
template = self.loader.load(self, name, self.make_globals(globals))
File "E:\tp2-fask-taches\.venv\lib\site-packages\jinja2\loaders.py", line 126, in load
source, filename, uptodate = self.get_source(environment, name)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\templating.py", line 66, in get_source
return self._get_source_fast(environment, template)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\templating.py", line 100, in _get_source_fast
raise TemplateNotFound(template)


V - Mission 5 — Ajouter une tâche 

1. Ajouter une tâche. Sur la page qui s'affiche, appuyer sur F5. Observe : que demande le navigateur ?
Combien de fois la tâche apparaît-elle ?

-> ca affiche le formulaire et quand on remplis, ca rajoute une nouvelle tache

Accueil
Tâches
Mes taches (Total : [{'ID': 1, 'TITRE': 'RÉVISER LES DÉCORATEURS', 'PRIORITE': 'HAUTE', 'TERMINEE': FALSE}, {'ID': 2, 'TITRE': 'INSTALLER FLASK', 'PRIORITE': 'NORMALE', 'TERMINEE': TRUE}, {'ID': 3, 'TITRE': 'LIRE LA DOC JINJA2', 'PRIORITE': 'BASSE', 'TERMINEE': FALSE}, {'ID': 4, 'TITRE': 'GGGDGSD', 'PRIORITE': 'BASSE', 'TERMINEE': FALSE}])
1 ) RÉVISER LES DÉCORATEURS
2 ) INSTALLER FLASK
3 ) LIRE LA DOC JINJA2
4 ) GGGDGSD


2. Ouvrir F12, onglet Réseau, et ajouter une tâche. Observe : quelle méthode, quelle URL ?

Méthode : POST

URL : /taches/ajouter


3. Remplacer la dernière ligne du bloc POST par return redirect(url_for("index")). Refaire les
essais 1 et 2. Observe : combien de requêtes, avec quels codes ?

* pour la methode 1 : 

Mes taches (Total : [{'ID': 1, 'TITRE': 'RÉVISER LES DÉCORATEURS', 'PRIORITE': 'HAUTE', 'TERMINEE': FALSE}, {'ID': 2, 'TITRE': 'INSTALLER FLASK', 'PRIORITE': 'NORMALE', 'TERMINEE': TRUE}, {'ID': 3, 'TITRE': 'LIRE LA DOC JINJA2', 'PRIORITE': 'BASSE', 'TERMINEE': FALSE}, {'ID': 4, 'TITRE': 'BLA BLA BLA', 'PRIORITE': 'HAUTE', 'TERMINEE': FALSE}])
1 ) RÉVISER LES DÉCORATEURS
2 ) INSTALLER FLASK
3 ) LIRE LA DOC JINJA2
4 ) BLA BLA BLA

127.0.0.1 - - [23/Oct/2026 16:02:25] "GET /taches/ajouter?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 -
 * Detected change in 'E:\\tp2-fask-taches\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 956-468-667
127.0.0.1 - - [23/Oct/2026 16:03:25] "POST /taches/ajouter HTTP/1.1" 302 -
127.0.0.1 - - [23/Oct/2026 16:03:26] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [23/Oct/2026 16:03:26] "GET /static/style.css HTTP/1.1" 304 -

* methode 2 :

Méthode : GET

URL : /


4. Envoyer un titre vide. Observe. Ajouter ensuite une validation : titre non vide, 80 caractères au plus,
priorité parmi les trois valeurs ; sinon, réafficher le formulaire.

-> envoie un message pour remplir le champ vide et n'envoie rien grace a "required" mais sans required, cela envoie vide 


5. Remplacer temporairement request.form.get("titre", "") par request.form["titr"], avec
une faute volontaire. Observe le code d'erreur, puis corriger.

l'erreur :

BadRequestKeyError
werkzeug.exceptions.BadRequestKeyError: 400 Bad Request: The browser (or proxy) sent a request that this server could not understand.
KeyError: 'titr'

Traceback (most recent call last)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1536, in __call__
return self.wsgi_app(environ, start_response)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1514, in wsgi_app
response = self.handle_exception(e)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 1511, in wsgi_app
response = self.full_dispatch_request()
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 919, in full_dispatch_request
rv = self.handle_user_exception(e)
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 917, in full_dispatch_request
rv = self.dispatch_request()
File "E:\tp2-fask-taches\.venv\lib\site-packages\flask\app.py", line 902, in dispatch_request
return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
File "E:\tp2-fask-taches\app.py", line 37, in ajouter
titre = request.form["titr"].strip()
File "E:\tp2-fask-taches\.venv\lib\site-packages\werkzeug\datastructures\structures.py", line 238, in __getitem__
raise exceptions.BadRequestKeyError(key)


* fixation :

titre = request.form["titre"].strip() # on ajoute le "e" qui manque


6. Retirer method="post" du formulaire et l'envoyer. Observe l'adresse dans la barre du navigateur.
Remettre ensuite method="post". 

http://127.0.0.1:5000/taches/ajouter?titre=python&priorite=normale 


7. Remettre le lien « Ajouter » dans le menu de base.html.

on peut acceser a ajouter sans mettre /taches/ajouter dans la barre navigation




VI - Mission 6 — Messages et mémoire


1. Juste avant la redirection de la mission 5, ajouter flash("Tâche ajoutée"), sans définir de clé
secrète. Ajouter une tâche. Observe l'erreur et lis le message en entier.

RuntimeError
RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.






Bonus :

Ajouter une route /api/taches qui renvoie la liste des tâches. Observe : quel format reçoit le
navigateur ? Chercher la réponse dans Quickstart › About Responses.

obseration : http://127.0.0.1:5000/api/taches


[
  {
    "id": 1,
    "priorite": "haute",
    "terminee": false,
    "titre": "R\u00e9viser les d\u00e9corateurs"
  },
  {
    "id": 2,
    "priorite": "normale",
    "terminee": true,
    "titre": "Installer Flask"
  },
  {
    "id": 3,
    "priorite": "basse",
    "terminee": false,
    "titre": "Lire la doc Jinja2"
  }
]

* Format reçu par le navigateur : Le navigateur reçoit du JSON

* Explication (selon Quickstart › About Responses) : Puisque la fonction de vue renvoie une liste Python, Flask applique automatiquement sa règle de conversion en appelant jsonify() pour produire un objet de réponse avec le type MIME approprié (application/json), au lieu d'un simple texte HTML.
