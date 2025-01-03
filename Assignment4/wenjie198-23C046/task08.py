# -*- coding: utf-8 -*-
"""Task08.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16njVdWnXn2F1X2BNXrvQyFTdQCNRx3Jq

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

from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF

ns = Namespace("http://data.org#")

# Elementos de la clase persona de data01.rdf
q1 = prepareQuery("""
  SELECT ?persona
  WHERE {
    ?persona rdf:type :Person
  }
""",
                  initNs={"rdf": RDF, "":ns})

for r in g1.query(q1):
  print(r)

vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

print("Given Name:")
for s, p, o in g1.triples((None, vcard.Given, None)):
  print(s, o)

print("\nFamily Name:")
for s, p, o in g1.triples((None, vcard.Family, None)):
  print(s, o)

print("\nEmail:")
for s, p, o in g1.triples((None, vcard.EMAIL, None)):
  print(s, o)

# Conseguir datos de g2

lista_given = []
for s, p, o in g2.triples((None, vcard.Given, None)):
  lista_given.append((s, p, o))

lista_family = []
for s, p, o in g2.triples((None, vcard.Family, None)):
  lista_family.append((s, p, o))

lista_email = []
for s, p, o in g2.triples((None, vcard.EMAIL, None)):
  lista_email.append((s, p, o))

# Incorporo lista_given
for tripleta in lista_given:
  g1.add(tripleta)

# Incorporo lista_family
for tripleta in lista_family:
  g1.add(tripleta)
# Incorpor lista_email
for tripleta in lista_email:
  g1.add(tripleta)

print(g1.serialize(format="ttl"))

print(g2.serialize(format="ttl"))