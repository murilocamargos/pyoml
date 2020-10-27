# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT
from typing import Union, Tuple

NumericType = Union[int, float]

__all__ = [
    'TriMF',
]

class MF:
    """General membership function.

    Parameters
    ----------
    params : tuple of ints or floats
        A tuple with all the MF parameters.
    """
    def __init__(self, params: Tuple[NumericType]):
        self._check_num_type(params)
    
    def _check_num_type(self, params: Tuple[NumericType]) -> None:
        """Check if the each param in `params` is numeric [int, float].
        
        Parameters
        ----------
        params : tuple of ints or floats
            A tuple with all the MF parameters.
        """
        for p in params:
            if type(p) not in [int, float]:
                raise TypeError('All parameters must be numeric.')
    
    def get_params(self) -> Tuple[NumericType]:
        """Get the MF parameters."""
        raise NotImplementedError('The `get_params` method must be implemented')
    
    def get_degree(self, x: NumericType) -> NumericType:
        """Get the membership degree of a float value `x` for
        the MF.
        """
        raise NotImplementedError('The `get_degree` method must be implemented')


class TrapMF(MF):
    """Trapezoidal membership function.

    Parameters
    ----------
    a : float
        First parameter to control the trapzoidal shape.

    b : float
        Second parameter to control the trapzoidal shape.

    c : float
        Third parameter to control the trapzoidal shape.
    
    d : float
        Fourth parameter to control the trapzoidal shape.

    Attributes
    ----------
    a_ : float
        Trapezoidal shape lower bound.

    b_ : float
        Trapezoidal shape first mid point.

    c_ : float
        Trapezoidal shape second mid point.
    
    d_ : float
        Trapezoidal shape upper bound.
    
    Examples
    --------
    >>> from pyoml.fuzzy.membership import TrapMF
    >>> mf = TrapMF(0,1,2,3)
    """
    def __init__(self, a: NumericType, b: NumericType, c: NumericType,\
        d: NumericType):
        super().__init__((a, b, c, d))

        if not a <= b <= c <= d:
            raise ValueError('The parameters must be specified such that a <= b <= c <= d.')
        
        self.a_ = a
        self.b_ = b
        self.c_ = c
        self.d_ = d


class TriMF(MF):
    """Triangular membership function.

    Parameters
    ----------
    a : float
        First parameter to control the triangular shape.

    b : float
        Second parameter to control the triangular shape.

    c : float
        Third parameter to control the triangular shape.

    Attributes
    ----------
    a_ : float
        Triangular shape lower bound.

    b_ : float
        Triangular shape mid point.

    c_ : float
        Triangular shape upper bound.
    
    Examples
    --------
    >>> from pyoml.fuzzy.membership import TriMF
    >>> mf = TriMF(0,1,2)
    """
    def __init__(self, a: NumericType, b: NumericType, c: NumericType):
        super().__init__((a, b, c))

        if not a <= b <= c:
            raise ValueError('The parameters must be specified such that a <= b <= c.')
        
        self.a_ = a
        self.b_ = b
        self.c_ = c

    def get_params(self) -> Tuple[NumericType]:
        """Get the triangular form's parameters.

        Returns
        -------
        params : tuple(float, float, float)
            Ordered triangular three parameters (a,b,c).
        """
        params = (self.a_, self.b_, self.c_)
        return params
    
    def get_degree(self, x: NumericType) -> NumericType:
        """Get the membership degree of a float value `x` for
        the triangular MF.

        Parameters
        ----------
        x : float
            Input data for which the membership degree will be
            computed.
        
        Returns
        -------
        degree : float 
            The membership degree for the input `x`. The value
            is in [0, 1].
        """
        degree = max(min((x - self.a_)/(self.b_ - self.a_),\
            (self.c_ - x)/(self.c_ - self.b_)), 0)
        return degree