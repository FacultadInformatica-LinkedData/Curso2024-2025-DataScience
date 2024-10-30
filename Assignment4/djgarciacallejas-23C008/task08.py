# -*- coding: utf-8 -*-
"""Task08.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s3WXdq1ySxpHqh_xW2FTy3ZpkVKvs4xU

**Task 08: Completing missing data**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

"""Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas."""

for s,p,o in g1:
  print(s,p,o)

for s,p,o in g2:
  print(s,p,o)

"""Primero buscamos las personas con las que trabajaremos"""

from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
RDF=Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
ns=Namespace("http://data.org#")
q1=prepareQuery('''
 SELECT ?person WHERE{
  ?person rdf:type ns:Person
 }

''',
initNs={"rdf":RDF, "ns":ns}

)
for o in g1.query(q1):
  print(o)

"""Buscamos los atributos que les falta a cada uno"""

vcard=Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
q2=prepareQuery('''
 SELECT ?person ?givenname ?email ?familyname ?fullname WHERE{
  ?person rdf:type ns:Person
  OPTIONAL{ ?person vcard:Given ?givenname}
  OPTIONAL{ ?person vcard:EMAIL ?email}
  OPTIONAL{ ?person vcard:FN ?fullname}

 }

''',
initNs={"rdf":RDF, "ns":ns, "vcard":vcard}

)
for o in g1.query(q2):
  print(o)

"""Una vez sabemos lo que le falta, obtenemos la informacion del segundo grafo y lo vamos añadiento respectivamente"""

q3=prepareQuery('''
 SELECT  ?person ?givenname ?email ?familyname ?fullname WHERE {
  ?person rdf:type ns:Person.
  ?person vcard:Given ?givenname.
  ?person vcard:EMAIL ?email.
  OPTIONAL{ ?person vcard:Family ?familyname}
  OPTIONAL{ ?person vcard:FN ?fullname}

  }

  ''',
  initNs={"rdf":RDF, "ns":ns, "vcard":vcard}

  )
for o in g2.query(q3):
  print(o)

"""Rellenamos cada campo de cada persona"""

nombre=Literal("Sara")
apellido=Literal("Jones")
email=Literal("sara.jones@data.org")
g1.add((ns.SaraJones ,vcard.Given, nombre))
g1.add((ns.SaraJones ,vcard.EMAIL, email ))
g1.add((ns.SaraJones ,vcard.Family, apellido))

apellido_1=Literal("Smith")
g1.add((ns.JohnSmith, vcard.Family, apellido))

email_1 = Literal("hpotter@hogwarts.org")
g1.add((ns.HarryPotter, vcard.EMAIL,email_1))

nombre_1 = Literal("John")
g1.add((ns.JohnDoe, vcard.Given,nombre_1))

"""Comprobamos que este todo bien"""

for s,p,o in g1:
  print(s,p,o)