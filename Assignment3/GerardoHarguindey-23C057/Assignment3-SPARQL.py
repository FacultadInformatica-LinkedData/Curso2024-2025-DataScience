# 1. Get all the properties that can be applied to instances of the Politician class (<http://dbpedia.org/ontology/Politician> or its equivalent in Wikidata)

"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT DISTINCT ?property
WHERE {
  ?politician a <http://dbpedia.org/ontology/Politician> .
  ?politician ?property ?value .
}

"""

# 2. Get all the properties, except for rdf:type, that are applied to instances of the Politician class

"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT DISTINCT ?property
WHERE {
  ?politician a <http://dbpedia.org/ontology/Politician> .
  ?politician ?property ?value .
  FILTER(?property != rdf:type)
}

"""

# 3. Which different values exist for the properties, except for rdf:type, of the instances of the Politician class?

"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT DISTINCT ?property ?value
WHERE {
  ?politician a <http://dbpedia.org/ontology/Politician> .
  ?politician ?property ?value .
  FILTER(?property != rdf:type)
}


"""

# 4. For each of these properties, except for rdf:type, which different values do they take in those instances?

"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT ?property ?value
WHERE {
  ?politician a <http://dbpedia.org/ontology/Politician> .
  ?politician ?property ?value .
  FILTER(?property != rdf:type)
}
ORDER BY ?property

"""

# 5. For each of the properties, except for rdf:type, how many distinct values do they take?

"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT ?property (COUNT(DISTINCT ?value) AS ?distinctValueCount)
WHERE {
  ?politician a <http://dbpedia.org/ontology/Politician> .
  ?politician ?property ?value .
  FILTER(?property != rdf:type)
}
GROUP BY ?property
ORDER BY DESC(?distinctValueCount)
"""