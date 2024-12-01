github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

#TASK 6.1
ns = Namespace("http://somewhere#")
g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)
  
#TASK 6.2
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for s, p, o in g:
  print(s,p,o)

#TASK 6.3
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/FN")

g.add((ns.Jane, VCARD.FN, Literal("Jane Smithers")))
g.add((ns.Jane, RDF.type, ns.Researcher))
for s, p, o in g:
  print(s,p,o)

#TASK 6.4
SCHEMA = Namespace("https://schema.org/")
g.add((ns.Jane, SCHEMA.EMAIL, Literal("janesmithers@example.com")))
g.add((ns.Jane, SCHEMA.givenName, Literal("Jane")))
g.add((ns.Jane, SCHEMA.name, Literal("Jane Smithers")))
g.add((ns.Jane, SCHEMA.familyName, Literal("Smithers")))
for s, p, o in g:
  print(s,p,o)

#TASK 6.5
EX = Namespace("https://example.org/")
g.add((EX.UPM, RDF.type, ns.University))
g.add((ns.JohnSmith, SCHEMA.worksFor, EX.UPM))
for s, p, o in g:
  print(s,p,o)

#TASK 6.6
from rdflib import FOAF
g.add((ns.JohnSmith, FOAF.knows, ns.Jane))
for s, p, o in g:
  print(s,p,o)