# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RzVZVqryxJsXumpJoSvMu2_XgdR2qqRj

**Task 07: Querying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")

q1 = prepareQuery('''
  SELECT ?Subject WHERE {
    ?Subject rdfs:subClassOf ns:LivingThing.
  }
  ''',
  initNs = { "rdfs": RDFS, "ns" : ns}
)
# Visualize the results

for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
q2 = prepareQuery('''
  SELECT DISTINCT ?Subject WHERE {
    ?Class rdfs:subClassOf* ns:Person .
    ?Subject rdf:type ?Class .
    }
  ''',
  initNs = { "rdfs": RDFS, "rdf": RDF, "ns" : ns}
)
# Visualize the results

for r in g.query(q2):
  print(r)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

# TO DO
q3 = prepareQuery('''
  SELECT ?individual WHERE {
    ?subclass rdfs:subClassOf ns:LivingThing.
    ?individual rdf:type ?subclass .
    }
  ''',
  initNs = { "rdfs": RDFS, "rdf": RDF, "ns" : ns}
)
# Visualize the results

for r in g.query(q3):
  print(r)

""":**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

# TO DO
from rdflib import FOAF

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")

q4 = prepareQuery('''
  SELECT ?name WHERE {
    ?Friend foaf:knows ns:RockySmith .
    ?Friend vcard:FN ?name
  }
  ''',
  initNs={"ns": ns, "vcard": VCARD, "foaf": FOAF}
)
# Visualize the results

for r in g.query(q4):
    print(r.name)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

# TO DO
q5 = prepareQuery('''
  SELECT ?name WHERE {
    ?class rdfs:subClassOf* ns:Animal .
    ?Animal rdf:type ?class .
    ?Animal2 rdf:type ?class .
    ?Animal foaf:knows ?Animal2 .
    ?Animal vcard:Given ?name
  }
  ''',
  initNs={"ns": ns, "vcard": VCARD, "foaf": FOAF}
)
# Visualize the results

for r in g.query(q5):
  print(r.name)
# Visualize the results

""":**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

# TO DO
q6 = prepareQuery('''
  SELECT ?age WHERE {
    ?class rdfs:subClassOf* ns:LivingThing .
    ?alive rdf:type ?class .
    ?alive foaf:age ?age
  }
  ORDER BY DESC(?age)
  ''',
  initNs={"ns": ns, "vcard": VCARD, "foaf": FOAF}
)
# Visualize the results

for r in g.query(q6):
  print(r.age)
# Visualize the results