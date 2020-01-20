from typing import TextIO
from io import StringIO

def process_file(reader: TextIO) -> int:
    """ Read and process reader, which must start with a time_series header. Return the largest value after the header.
    There may be multiple pieces of data on each line.
    
    >>> infile = StringIO('Example\\n 20. 3.\\n')
    >>> process_file(infile)
    20
    >>> infile = StringIO('Example\\n 20. 3.\\n 100. 17. 15.\\n')
    >>> process_file(infile)
    100
    """
    #Read the description line
    line = reader.readline()
    
    #Find the first non-comment line
    line = reader.readline()
    while line.startswith('#'):
      line = reader.readline()
      
      
