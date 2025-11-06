# instagram-followers-insight
Ce projet permet de savoir qui ne te suit pas en retour sur ton compte Instagram sans application tierce, en local. On utilise simplement l’export officiel des données fourni par Instagram (donc 100 % sûr et conforme au RGPD) 

---

## Principe

1. Tu demandes à Instagram une copie de tes données (tes abonnés et abonnements)
2. Tu places ces fichiers dans le dossier du projet  
3. Tu lances un script Python ('follow.py')
4. Le programme affiche :
   - combien de personnes tu suis
   - combien te suivent
   - qui ne te suit pas en retour

---

## Ce qu’il te faut

- Un ordinateur avec Python3 installé
  (Si t'es pas sûr tape `python --version` dans ton terminal)
  Dans le cas ou il n'est pas installé, il existe de nombreuses vidéos qui expliquent comment procéder à l'installation
- Ton export de données Instagram (au format JSON).
---

## Étape 1 : Télécharger tes données Instagram

1. Va sur  [https://www.instagram.com/download/request/](https://www.instagram.com/download/request/)
2. Connecte-toi à ton compte
3. Choisis :
   - De télécharger en local
   - Format : JSON
   - Données à inclure : uniquement *Abonnés et abonnements*
   - Depuis la date de création de ton compte
4. Si t'as choisi mail, Instagram t’enverra un lien de téléchargement (ça peut prendre quelques minutes)
5. Télécharge le fichier `.zip` et décompresse-le.

T'obtiendras un dossier qui ressemble à ceci :
connections/
└── followers_and_following/
├── followers.json // ou followers_1.json
├── following.json

Dans le cas ou le fichier se nomme **followers.json**, renomme-le **followers_1.json**


---

## Étape 2 : Mettre le script dans le dossier

Télécharge le fichier python présent sur le git, et met-le dans le dossier instagram que tu viens de télécharger, au même niveau que les autres fichiers.


---

## Étape 3 : Lancer le script

Ouvre un terminal dans le dossier (clic-droit, ouvrir terminal), tape :
```
python follow.py
```
Le programme va :

lire les deux fichiers (followers_1.json et following.json), comparer les listes, afficher le résultat à l’écran et créer un fichier texte not_following_back.txt avec la liste complète

Exemple de résultat

Tu suis 245 comptes.
Tu as 230 abonnés.
15 ne te suivent pas en retour :

- pseudo1
- pseudo2
- pseudo3
...
Et dans ton dossier, tu trouveras :

not_following_back.txt

 ## Sécurité & respect de la vie privée
Le script fonctionne uniquement avec des fichiers locaux (rien n’est envoyé sur Internet), aucun mot de passe Instagram n’est requis...

Tu peux supprimer le dossier de données après usage.
Petite note, certains pseudos apparaîtront alors qu'ils ne sont plus présent sur instagram, n'y prête pas attention... Certaines données extraites datent d'il y a longtemps, je ne sais 
pas comment Instagram gère son extraction de données, mais à part ça c'est fonctionnel (et efficace)

---
## Note auteur

Réalisé pour aider des amis qui avaient besoin de connaître ces informations, j'ai choisi de procéder ainsi pour avoir cette liste de non-follower, il existe sûrement d'autres manières (pas toutes légales)!
N’hésite pas à le forker, l’améliorer ou proposer des idées !
