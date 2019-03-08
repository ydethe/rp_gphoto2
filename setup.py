from setuptools import setup, find_packages, Extension

#============================================================
#TUTO
#http://sametmax.com/creer-un-setup-py-et-mettre-sa-bibliotheque-python-en-ligne-sur-pypi/
#
#============================================================

# notez qu'on import la lib
# donc assurez-vous que l'importe n'a pas d'effet de bord
import rp_gphoto2

# extension = Extension("imu_driver", ["RPFirmware/lsm9ds0_yann.cpp", "RPFirmware/imu_driver_wrap.cpp"])
extension = Extension( "rp_gphoto2",
    sources = ["rp_gphoto2/rp_gphoto2.c", "rp_gphoto2/config.c", "rp_gphoto2/focus.c", "rp_gphoto2/context.c", "rp_gphoto2/rp_gphoto2.i"],
    swig_opts=["-py3"],
    libraries=["gphoto2"],
    library_dirs=["/usr/local/lib"],
	 )

# Ceci n'est qu'un appel de fonction. Mais il est trèèèèèèèèèèès long
# et il comporte beaucoup de paramètres
setup(

   # le nom de votre bibliothèque, tel qu'il apparaitre sur pypi
   name='rp_gphoto2',

   # la version du code
   version=rp_gphoto2.__version__,

	ext_modules=[extension],

   # Liste les packages à insérer dans la distribution
   # plutôt que de le faire à la main, on utilise la foncton
   # find_packages() de setuptools qui va cherche tous les packages
   # python recursivement dans le dossier courant.
   # C'est pour cette raison que l'on a tout mis dans un seul dossier:
   # on peut ainsi utiliser cette fonction facilement
   packages=find_packages(),

   # votre pti nom
   author="Y. BLAUDIN DE THE",

   # Votre email, sachant qu'il sera publique visible, avec tous les risques
   # que ça implique.
   author_email="ydethe@gmail.com",

   # Une description courte
   description="Library to simulate closed-loop controlled systems",

   # Une description longue, sera affichée pour présenter la lib
   # Généralement on dump le README ici
   long_description=open('README.md').read(),

   # Vous pouvez rajouter une liste de dépendances pour votre lib
   # et même préciser une version. A l'installation, Python essayera de
   # les télécharger et les installer.
   #
   # Ex: ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"]
   #
   # Dans notre cas on en a pas besoin, donc je le commente, mais je le
   # laisse pour que vous sachiez que ça existe car c'est très utile.
   install_requires=[
        ],

   # Active la prise en compte du fichier MANIFEST.in
   include_package_data=True,

   # Une url qui pointe vers la page officielle de votre lib
   url='',

   # Il est d'usage de mettre quelques metadata à propos de sa lib
   # Pour que les robots puissent facilement la classer.
   # La liste des marqueurs autorisées est longue:
   # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
   #
   # Il n'y a pas vraiment de règle pour le contenu. Chacun fait un peu
   # comme il le sent. Il y en a qui ne mettent rien.
   classifiers=[
       "Programming Language :: Python",
       "Development Status :: 1 - Planning",
       "License :: OSI Approved",
       "Natural Language :: French",
       "Operating System :: OS Independent",
       "Programming Language :: Python :: 3.5",
   ],


   test_suite='nose.collector',
   tests_require=['nose'],

   # Il y a encore une chiée de paramètres possibles, mais avec ça vous
   # couvrez 90% des besoins

)
