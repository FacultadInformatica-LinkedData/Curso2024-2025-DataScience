#%% md
# **Task 07: Querying RDF(s)**
#%%
!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"
#%% md
# First let's read the RDF file
#%%
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")
#%% md
# **TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**
#%%
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS, XSD, FOAF

ns = Namespace("http://somewhere#")

q1 = prepareQuery('''
    SELECT ?subclass WHERE {
        ?subclass rdfs:subClassOf ?LivingThing .
    }
''', initNs={'rdfs': RDFS})

# Visualize the results

for r in g.query(q1, initBindings={"?LivingThing": ns.LivingThing}):
 print(r.subclass)
#%% md
# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 
#%%

q2 = prepareQuery('''
    SELECT ?individual ?relation WHERE {
        ?individual ?relation ?person.
    }
''')
# Visualize the results
for r in g.query(q2, initBindings={"?person": ns.Person}):
    print(r.individual)
#%% md
# **TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**
# 
#%%
q3 = prepareQuery('''
  SELECT ?individual WHERE {
     {?individual rdf:type ?person.} UNION 
     {?individual rdf:type ?animal}
  }
 ''')

# Visualize the results
for r in g.query(q3, initBindings={"?person": ns.Person, "?animal": ns.Animal}):
    print(r.individual)
#%% md
# **TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**
#%%
q4 = prepareQuery('''
 SELECT ?person WHERE {
  ?person foaf:knows ?rocky.
  ?person rdf:type ?personClass
 }
''', initNs={"foaf": FOAF, "rdf": RDF})
# Visualize the results
for r in g.query(q4, initBindings={"?rocky": ns.RockySmith, "?personClass": ns.Person}):
    print(r.person)
    
#%% md
# **Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**
#%%
q5 = prepareQuery('''
    SELECT ?animal WHERE {
        ?animal foaf:knows ?anotherAnimal.
        ?animal rdf:type ?animalClass.
        ?anotherAnimal rdf:type ?animalClass.
    }
''', initNs={"rdf": RDF, "foaf": FOAF})
# Visualize the results
for r in g.query(q5, initBindings={"?animalClass": ns.Animal}):
    print(r.animal)
#%% md
# **Task 7.6: List the age of all living things in descending order (in SPARQL only)**
#%%
q6 = prepareQuery('''
    SELECT ?thing ?age WHERE {
        ?subclass rdfs:subClassOf ?LivingThing.
        ?thing rdf:type ?subclass.
        ?thing foaf:age ?age
    }
''', initNs={"rdfs": RDFS, "foaf": FOAF, "rdf": RDF})

# Visualize the results
for r in g.query(q6, initBindings={"?LivingThing": ns.LivingThing}):
    print(r.thing, r.age)