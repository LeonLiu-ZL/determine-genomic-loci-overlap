import sys


class InvalidChrError(Exception):
    """
    Raised when the chr parameters of ChrCoordinate class are not valid
    
    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message='Error: chr was not found. An example of chr: "chr1".'):
        self.message = message
        super().__init__(self.message)


class ChrCoordinate(object):
    """
    Define chromose coordinate objects.

    Attributes:
        chr -- chromosome,
        start -- locus start position
        stop -- locus stop positon
    """


    def __init__(self, chr: str, start: int, stop: int):
        if not isinstance(chr, str):
            raise InvalidChrError
        if not chr.startswith('chr'):
            raise InvalidChrError
        if not isinstance(start, int) or not isinstance(stop, int):
            sys.stderr.write("Error: start or stop position was not found\n")
            raise TypeError
        self.chr = chr
        self.start = start
        self.stop = stop


    def find_overlap(self, coordinate):
        '''
        This function determines if the locus overlaps with another locus.

        Parameters:
            coordinate (ChrCoordinate): An ChrCoordinate object
        
        Returns:
            overlap(dict): An dictionary containing whether the two loci are overlapped and the overlapping informaiton.
        '''


        if not isinstance(coordinate, ChrCoordinate):
            sys.stderr.write("The coordinate of the second locus was not found")
            raise TypeError

        overlap = {'overlap': False, 'overlap starts at': None,
                   'overlap ends at': None, 'overlap width': None}
        # Determine if the two loci are on the same chromosome.
        if self.chr != coordinate.chr:
            pass
        # If they are on the same chromosome, determine if they are overlapped, ignoring the strand direction.
        else:
            overlap_start = max(self.start, coordinate.start)
            overlap_end = min(self.stop, coordinate.stop)
            # If they are overlapped, determine the overlapped region.
            if overlap_start <= overlap_end:
                overlap['overlap'] = True
                overlap['overlap starts at'] = self.chr + ":" + str(overlap_start)
                overlap['overlap ends at'] = self.chr + ":" + str(overlap_end)
                overlap['overlap width'] = overlap_end - overlap_start + 1

        return overlap


coordinate_1 = ChrCoordinate('chr3', 800, 5000)
coordinate_2 = ChrCoordinate('chr3', 100, 900)

print(coordinate_1.find_overlap(coordinate_2))