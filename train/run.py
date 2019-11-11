import pandas as pd
import json
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint = "http://localhost:17200/repositories/data"

query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX db: <http://localhost/rdf/ontology/>
    PREFIX dbo: <http://um-cds/ontologies/databaseontology/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    select * where { 
        ?row rdf:type db:Clinical1.
        ?row dbo:has_column [
            rdf:type db:Clinical1.Age;
            dbo:has_value ?age;
        ];
        dbo:has_column [
            rdf:type db:Clinical1.Sex;
            dbo:has_value ?sex;
        ].
    }
"""

def get_sparql_dataframe(service, query):
    """
    Helper function to convert SPARQL results into a Pandas data frame.
    """
    sparql = SPARQLWrapper(service)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query()

    processed_results = json.load(result.response)
    cols = processed_results['head']['vars']

    out = []
    for row in processed_results['results']['bindings']:
        item = []
        for c in cols:
            item.append(row.get(c, {}).get('value'))
        out.append(item)

    return pd.DataFrame(out, columns=cols)

df = get_sparql_dataframe(endpoint, query)
print(df.describe())