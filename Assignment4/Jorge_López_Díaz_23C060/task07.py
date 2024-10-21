# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fKyMYX8z1YNsP4nKhOChnVeuOQH8eO8S

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

query1 = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://somewhere#>
SELECT ?subClass
WHERE {
    ?subClass rdfs:subClassOf ns:LivingThing .
}
"""
results1 = g.query(query1)

for r in results1:
    print(r.subClass)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

query2 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://somewhere#>
SELECT ?individual
WHERE {
    {
        ?individual rdf:type ns:Person .
    }
    UNION
    {
        ?individual rdf:type ?subClass .
        ?subClass rdfs:subClassOf ns:Person .
    }
}
"""
results2 = g.query(query2)

for r in results2:
    print(r.individual)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

query3 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://somewhere#>
SELECT ?individual
WHERE {
  {
    ?individual rdf:type ns:Person .
  }
  UNION
  {
    ?individual rdf:type ns:Animal .
  }
}
"""
results3 = g.query(query3)
for r in results3:
  print(r.individual)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

from rdflib import FOAF
from rdflib import Namespace, Literal, RDF, Graph
ns = Namespace("http://somewhere#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
query4 = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX ns: <http://somewhere#>
SELECT ?peopleName
WHERE {
    ?person rdf:type ns:Person .
    ?person foaf:knows ns:Rocky .
    ?person vcard:FN ?peopleName .
}
"""
initNS = {"foaf":FOAF, "ns":ns, "vcard": vcard}

results4 = g.query(query4)
for r in results4:
  print(r.peopleName)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

query5 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://somewhere#>
PREFIX FOAF: <http://xmlns.com/foaf/0.1/>
PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0#>
SELECT ?animalName
WHERE {
    ?animal rdf:type ns:Animal .
    ?animal FOAF:knows ?anotherAnimal .
    ?anotherAnimal rdf:type ns:Animal .
    ?animal vcard:FN ?animalName .
    FILTER(?animal != ?anotherAnimal)
}
"""
results5 = g.query(query5)

for r in results5:
    print(r.animalName)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

query6 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ns: <http://somewhere#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0#>
SELECT ?livingThing ?age
WHERE {
    ?livingThing rdf:type ns:LivingThing .
    ?livingThing foaf:age ?age .
}
ORDER BY DESC(?age)
"""
initNS = {"foaf":FOAF, "ns":ns, "vcard": vcard}

results6 = g.query(query6)

for r in results6:
    print(f"{r.livingThing}: {r.age}")