# بسم الله الرحمن الرحيم

from array import Array2D

class Matrix :
    def __init__( self, num_rows, num_cols ):                
        self._the_grid = Array2D( num_rows, num_cols )
        self._the_grid.clear( 0 )                              
        
    def num_rows( self ):
        return self._the_grid.num_rows()
        
    def num_cols( self ):
        return self._the_grid.num_cols()

    def __getitem__( self, ndx_tuple ):
        return self._the_grid[ ndx_tuple[0], ndx_tuple[1] ]

    def __setitem__( self, ndx_tuple, scalar ):
        self._theGrid[ ndx_tuple[0], ndx_tuple[1] ] = scalar

    def scaleBy( self, scalar ):        
        for r in range( self.num_rows() ) :
            for c in range( self.num_cols() ) :
                self[r, c] *= scalar

    def __add__( self, rhsMatrix ): 
        assert rhsMatrix.num_rows() == self.num_rows() and \
            rhsMatrix.num_cols() == self.num_cols(), \
        "Matrix sizes not compatible for the add operation."     
        
        newMatrix = Matrix( self.numRows(), self.numCols() )      
        
        for r in range( self.numRows() ) :
            for c in range( self.num_cols() ) :
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]
        return newMatrix         
