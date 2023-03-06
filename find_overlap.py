class InvalidInputError(Exception):
    """Raised when the loci inputs are not valid
    
    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message='Error: The locus inputs are not found. An example of the locus inputs: "chr1:1-100".'):
        self.message = message
        super().__init__(self.message)


def find_overlap(locus_x: str, locus_y: str):
    '''
    This function determines if two genomic loci are overlapped or not.

    Parameters: 
        locus_x (str) -- the first locus. Example: "chr1:100-200"
        locus_y (str) -- the second locus to compare. Example: "chr1:150-200"
    Returns:
        True or False
    '''

    # Parse the inputs of loci.
    locus_x_coord = locus_x.split(":")
    locus_y_coord = locus_y.split(":")
    # If the coordniates don't contain chromosome and position information, raise InvalidInputError. 
    if len(locus_x_coord) != 2 or len(locus_y_coord) != 2:
        raise InvalidInputError
    else:
        # Obtain chromosome infomation
        locus_x_chr = locus_x_coord[0].rstrip()
        locus_y_chr = locus_y_coord[0].rstrip()
        # Determine if the chromosome informaiton is in good format.
        if not locus_x_chr.startswith("chr") or not locus_y_chr.startswith("chr"):
            raise InvalidInputError
        
    # If the coordinates don't contain start and stop position information, raise InvalidInputError. 
    if len(locus_x_coord[1].split('-')) != 2 or len(locus_x_coord[1].split('-')) !=2:
        raise InvalidInputError
    else:
        # Obtain position information
        # Remove spaces on both ends in case the format are from different sources.
        # If considering the strands, the start and stop coordinates need to be sorted.
        locus_x_start = int(locus_x_coord[1].split('-')[0].rstrip().lstrip())
        locus_y_start = int(locus_y_coord[1].split('-')[0].rstrip().lstrip())
        locus_x_stop = int(locus_x_coord[1].split('-')[1].rstrip().lstrip())
        locus_y_stop = int(locus_y_coord[1].split('-')[1].rstrip().lstrip())

    # Determine if the two loci are on the same chromosome.
    if locus_x_chr != locus_y_chr:
        return False
    # If they are on the same chromosome, determine if they are overlapped.
    else:
        overlap_start = max(locus_x_start, locus_y_start)
        overlap_end = min(locus_x_stop, locus_y_stop)
        # The strands of the loci are ignored.
        if overlap_start <= overlap_end:
            return True
        else:
            return False


print(find_overlap("chr2:400 - 600", "chr2 : 200-500"))