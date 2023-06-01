import astroquery
import astropy
import pyvo
import time

def reference_finder(obj):
    '''
    This is a function that queries the simbad catalogue with a user specified search term, and returns research papers that reference the search term.
    
    Parameters: 
    obj(str): The object that needs to be queried
    
    Returns:
    biblioQuery(astropy.table): A table that contains the papers that the queried object was referenced in. 
    '''
    
    tapSimbad = pyvo.dal.TAPService("http://simbad.u-strasbg.fr:80/simbad/sim-tap")
    adql_query = f"""
    SELECT BIBCode, Journal, Title, "year", Volume,
           Page || '-' || Last_Page AS "Pages", DOI 
    FROM ref JOIN has_ref ON oidbibref = oidbib 
             JOIN ident ON has_ref.oidref = ident.oidref 
    WHERE id = '{obj}'
    ORDER BY "year" DESC;"""
    t0 = time.time()
    biblioQuery = tapSimbad.search(adql_query).to_table()
    print(f"Query completed in {time.time()-t0} seconds.")
    return biblioQuery
