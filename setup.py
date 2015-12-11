# coding=utf-8
'''
Created on 22/01/2014

#Author: Adastra.
#twitter: @jdaanial

Tortazo.py

Tortazo es software libre, puedes editarlo/modificarlo, mejorarlo, traducirlo o distribuirlo
bajo los terminos indicados por la licencia GNU (GNU General Public License) en su version 2..

Tortazo es distribuido con la esperanza de que sea util, sin embargo no se brinda una garantia
ni siquiera una garantia de COMERCIALIZACION O IDEONIDAD PARA NINGUN FIN. 
Para mas informacion favor de leer la licencia GNU.

Deberia de haber recibido una copia de la licencia GNU junto con Tortazo, si no fue asi
por favor escriba a la Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Tortazo",
    version = "1.1-es0.1",
    author = "Adastra",
    traductor="Masterapocalyptic"
    author_email = "debiadastra@gmail.com",
    description = ("Audit and Attack TOR Nodes"),
    license = "GPL",
    keywords = "stem tortazo tor",
    url = "http://packages.python.org/Tortazo",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Estado de Desarrollo :: 3 - Alpha",
        "Topic :: Auditoria y hacking",
        "License :: GNU/GPL v2",
    ],
)
