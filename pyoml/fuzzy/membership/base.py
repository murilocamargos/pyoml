# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT

from ...base import NumericType, NumParamsType


class MF:
    """General membership function.

    Parameters
    ----------
    params : tuple of ints or floats
        A tuple with all the MF parameters.
    """
    def __init__(self, params: NumParamsType):
        self._check_num_type(params)

    def _check_num_type(self, params: NumParamsType) -> None:
        """Check if the each param in `params` is numeric [int, float].

        Parameters
        ----------
        params : tuple of ints or floats
            A tuple with all the MF parameters.
        """
        for p in params:
            if type(p) not in [int, float]:
                raise TypeError('All parameters must be numeric.')

    def get_params(self) -> NumParamsType:
        """Get the MF parameters."""
        raise NotImplementedError('The `get_params` method must be\
                                   implemented')

    def get_degree(self, x: NumericType) -> NumericType:
        """Get the membership degree of a float value `x` for
        the MF.
        """
        raise NotImplementedError('The `get_degree` method must be\
                                   implemented')
