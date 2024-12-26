# -*- coding: utf-8 -*-
"""Task09.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wSsfLw93fdOAyRIoez_BDWFz0nCjdAUV

**Task 09: Data linking**
"""

# !pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials/"

from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage+"rdf/data03.rdf", format="xml")
g2.parse(github_storage+"rdf/data04.rdf", format="xml")

"""Busca individuos en los dos grafos y enlázalos mediante la propiedad OWL:sameAs, inserta estas coincidencias en g3. Consideramos dos individuos iguales si tienen el mismo apodo y nombre de familia. Ten en cuenta que las URI no tienen por qué ser iguales para un mismo individuo en los dos grafos.

Listamos individuos en g1
"""

from rdflib.plugins.sparql import prepareQuery
q1 = prepareQuery('''
  SELECT ?individual WHERE {
    ?individual rdf:type ?class .
  }
''')

for r in g1.query(q1):
  print(r.individual)

"""Si ignoramos los resultados que definen relaciones, tenemos 4 individuos que probablemente serán elementos de la clase Person."""

ns1 = Namespace("http://data.three.org#")
q2 = prepareQuery('''
  SELECT ?individual WHERE {
    ?individual rdf:type :Person .
  }
''',
    initNs = {"": ns1})
print("\n")
for r in g1.query(q2):
  print(r.individual)

"""Hacemos lo mismo en g2: primero listamos todos los individuos."""
print("\n")
for r in g2.query(q1):
  print(r.individual)

"""Y ahora sólo las que sean de tipo Person."""
print("\n")
for r in g2.query(q2):
  print(r.individual)

"""No nos devuelve nada con la query usada en g1, así que probablemente Person tenga una namespace distinta en g2."""

ns2 = Namespace("http://data.four.org#")
q3 = prepareQuery('''
  SELECT ?individual WHERE {
    ?individual rdf:type :Person .
  }
''',
  initNs = {"": ns2})
print("\n")
for r in g2.query(q3):
  print(r.individual)

"""Vamos a ver que campos tiene cada elemento Person de g2."""

vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
q4 = prepareQuery('''
  SELECT ?person ?fn ?given ?family WHERE {
    ?person rdf:type :Person .
    ?person vcard:FN ?fn .
    ?person vcard:Given ?given .
    ?person vcard:Family ?family .
  }
''',
    initNs = {"vcard": vcard, "": ns2})
print("\n")
for r in g2.query(q4):
  print(f"{r.person}, {r.fn}, {r.given}, {r.family}")

"""Ahora, como sabemos a quien corresponde cada elemento de Person de g2, contruimos el grafo g3 y asociamos cada elemento de g2 con su equivalente en g1 usando la propiedad OWL:sameAs."""

from rdflib.namespace import RDF, RDFS
OWL = Namespace("http://www.w3.org/2002/07/owl#")

# Añadimos los namespaces a g3
g3.namespace_manager.bind("ns1", ns1)
g3.namespace_manager.bind("ns2", ns2)
g3.namespace_manager.bind("rdfs", RDFS)
g3.namespace_manager.bind("OWL", OWL)
g3.namespace_manager.bind("vcard-rdf", vcard)

# Añadimos las clases de Person de cada grafo
g3.add((ns1.Person, RDF.type, RDFS.Class))
g3.add((ns2.Person, RDF.type, RDFS.Class))

# Añadimos las personas de g1
for s, p, o in g1.triples((None, RDF.type, ns1.Person)):
  g3.add((s, p, o))

# Añadimos las personas de g2
for s, p, o in g2.triples((None, RDF.type, ns2.Person)):
  g3.add((s, p, o))

# Enlazamos los elementos equivalentes en g3
g3.add((ns1.Person, OWL.sameAs, ns2.Person))
g3.add((ns1.SaraJones, OWL.sameAs, ns2["0001"])) # Poniendo ns2.0001 no funciona. Consultando la documentación de rdflib vi que una forma alternativa de construir URIs es ns2["0001"]
g3.add((ns1.JohnSmith, OWL.sameAs, ns2["0002"]))
g3.add((ns1.HarryPotter, OWL.sameAs, ns2["0003"]))
g3.add((ns1.JohnDoe, OWL.sameAs, ns2["0005"]))

# Vemos el resultado
print("\n")
print(g3.serialize(format="ttl"))