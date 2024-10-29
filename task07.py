# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ih9tmVWFfDf7xZfta0EMgLs4iFmjmhp-

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

from rdflib.plugins.sparql import prepareQuery

ns = Namespace("http://somewhere#")

q1 = prepareQuery('''
  SELECT ?subclass WHERE {
    ?subclass rdfs:subClassOf ns:LivingThing .
  }
  ''', initNs={"rdfs": RDFS, "ns": ns})

for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

q2 = prepareQuery('''
  SELECT ?individual WHERE {
    {?individual rdf:type ns:Person .}
    UNION
    {?subclass rdfs:subClassOf ns:Person .
    ?individual rdf:type ?subclass }
  }
  ''', initNs={"rdf": RDF, "rdfs": RDFS, "ns": ns})

for r in g.query(q2):
  print(r)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

q3 = prepareQuery('''
  SELECT ?individual WHERE {
    {?individual rdf:type ns:Person .}
    UNION
    {?individual rdf:type ns:Animal .}
  }
  ''', initNs={"rdf": RDF, "ns": ns})

for r in g.query(q3):
    print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

from rdflib.namespace import FOAF

q4 = prepareQuery('''
  SELECT ?person WHERE {
    ?person rdf:type ns:Person .
    ?person foaf:knows ns:RockySmith .
  }
  ''', initNs={"foaf": FOAF, "ns": ns})

for r in g.query(q4):
    print(r)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

q5 = prepareQuery('''
  SELECT ?animal WHERE {
    ?animal rdf:type ns:Animal .
    ?otherAnimal rdf:type ns:Animal .
    ?animal foaf:knows ?otherAnimal .
  }
  ''', initNs={"foaf": FOAF, "rdf": RDF, "ns": ns})

for r in g.query(q5):
    print(r)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

q6 = prepareQuery('''
  SELECT ?livingThing ?age WHERE {
    {?livingThing rdf:type ns:Person .
    ?livingThing foaf:age ?age .}
    UNION
    {?livingThing rdf:type ns:Animal .
    ?livingThing foaf:age ?age .}
  }
  ORDER BY DESC(?age)
  ''', initNs={"foaf":FOAF, "rdf": RDF, "rdfs": RDFS, "ns": ns})

for r in g.query(q6):
  print(r)