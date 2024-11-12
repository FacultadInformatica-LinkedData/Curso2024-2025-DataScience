#%% md
# **Task 08: Completing missing data**
#%%
!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"
#%%
from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

#%% md
# Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas.
#%%
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import FOAF, RDF, RDFS


VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
ns = Namespace("http://data.org#")

query = prepareQuery('''
    SELECT ?person ?givenName ?familyName ?email WHERE {
        {?person rdf:type ?PersonClass} UNION
        {?person vcard:EMAIL ?email} UNION
        {?person vcard:Given ?givenName} UNION
        {?person vcard:Family ?familyName} 
    }
''', initNs={"vcard": VCARD, "rdf": RDF})

for i in g1.query(query, initBindings={"?PersonClass": ns.Person}):
    print(i)
    

for i in g2.query(query, initBindings={"?PersonClass": ns.Person}):
    if i.email:
        g1.add((i.person, VCARD.EMAIL, i.email))
    if i.givenName:
        g1.add((i.person, VCARD.Given, i.givenName))
    if i.familyName:
        g1.add((i.person, VCARD.Family, i.familyName))
    
    

    

#%%
