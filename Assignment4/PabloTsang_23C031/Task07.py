# %% [markdown]
# **Task 07: Querying RDF(s)**

# %%
!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

# %% [markdown]
# First let's read the RDF file

# %%
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

# %% [markdown]
# **TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**

# %%
# TO DO
# Visualize the results

ns = Namespace("http://somewhere#")

q1 = prepareQuery("""
SELECT ?subclass WHERE {
  ?subclass rdfs:subClassOf ns:LivingThing
}""",
     initNs={"ns": ns, "rdfs": RDFS})

for r in g.query(q1):
  print(r)


# %% [markdown]
# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# %%
# TO DO
q2 = prepareQuery("""
SELECT ?individuals WHERE{
  ?individuals a ns:Person
}""", initNs={"ns": ns})

for r in g.query(q2):
  print(r)

# Visualize the results

# %% [markdown]
# **TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**
# 

# %%
# TO DO
q3 = prepareQuery("""
SELECT ?animal WHERE{
  {?animal a ns:Animal} UNION {?animal a ns:Person}
}""", initNs={"ns":ns})

for r in g.query(q3):
  print(r)

# Visualize the results

# %% [markdown]
# **TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**

# %%
# TO DO
foaf = Namespace("http://xmlns.com/foaf/0.1/")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
ns = Namespace("http://somewhere#")

q4 = prepareQuery("""
SELECT ?name WHERE {
  ?person a ns:Person .
  ?person foaf:knows ns:RockySmith .
  ?person vcard:FN ?name .
}
""", initNs={"ns": ns, "foaf": foaf, "vcard": vcard})

for i in g.query(q4):
    print(i.name)
# Visualize the results

# %% [markdown]
# **Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**

# %%
# TO DO
q5 = prepareQuery("""
SELECT ?name WHERE{
  ?animal a ns:Animal .
  ?animal2 a ns:Animal .
  ?animal foaf:knows ?animal2 .
  ?animal vcard:Given ?name
  FILTER(?animal != ?animal2)
}""", initNs={"ns":ns, "foaf":foaf, "vcard":vcard})

for i in g.query(q5):
  print(i.name)
# Visualize the results

# %% [markdown]
# **Task 7.6: List the age of all living things in descending order (in SPARQL only)**

# %%
# TO DO
q6 = prepareQuery("""
SELECT ?age WHERE{
  ?subclass rdfs:subClassOf ns:LivingThing .
  ?individual a ?subclass .
  ?individual foaf:age ?age .
}""", initNs = {"foaf":foaf, "rdfs":RDFS, "ns":ns})

edades = g.query(q6)
edades_int = []
for i in edades:
  edades_int.append(int(i.age))

edades_int.sort(reverse=True)
print(edades_int)

# Visualize the results


