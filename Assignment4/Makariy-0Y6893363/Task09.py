#%% md
# **Task 09: Data linking**
#%%
!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials/"
#%%
from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage+"rdf/data03.rdf", format="xml")
g2.parse(github_storage+"rdf/data04.rdf", format="xml")
#%% md
# Busca individuos en los dos grafos y enlázalos mediante la propiedad OWL:sameAs, inserta estas coincidencias en g3. Consideramos dos individuos iguales si tienen el mismo apodo y nombre de familia. Ten en cuenta que las URI no tienen por qué ser iguales para un mismo individuo en los dos grafos.
#%%
from rdflib.plugins.sparql import prepareQuery

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
OWL = Namespace("http://www.w3.org/TR/owl2-rdf-based-semantics/#")

query = prepareQuery('''
    SELECT ?person ?nickname ?familyName WHERE {
        ?person vcard:FN ?nickname.
        ?person vcard:Family ?familyName.
    }
''', initNs={"vcard": VCARD})

people_g1 = {}
for r in g1.query(query):
    people_g1[(r.nickname, r.familyName)] = r.person
    
people_g2 = {}
for r in g2.query(query):
    people_g2[(r.nickname, r.familyName)] = r.person 
    
    
for key in people_g1:
    if key in people_g2:
        g3.add((people_g1[key], OWL.sameAs, people_g2[key]))
        
        
for i in g3:
    print(i)
    