# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT

import pytest
import numpy as np

from pyoml.fuzzy.membership import TriMF, TrapMF


def test_trimf_set_abc_params():
    # Test getting/setting the parameters of the Triangular MF
    with pytest.raises(ValueError) as err:
        _ = TriMF(2, 1, 0)
    assert str(err.value) == 'The parameters must be specified such that'\
                             ' a <= b <= c.'

    # Ordered
    mf = TriMF(0, 1, 2)
    assert mf.get_params() == (0, 1, 2)


def test_trimf_set_non_numeric_abc_params():
    # Test setting a non numeric value for the MF params
    with pytest.raises(TypeError) as err:
        _ = TriMF('0', 1, 2)
    assert str(err.value) == 'All parameters must be numeric.'


def test_trimf_get_membership_degree():
    # Test the membership degrees computation for the Triangular MF
    mf = TriMF(0, 1, 2)
    assert mf.get_degree(-0.5) == 0
    assert mf.get_degree(0) == 0
    assert mf.get_degree(0.5) == 0.5
    assert mf.get_degree(1) == 1
    assert mf.get_degree(1.5) == 0.5
    assert mf.get_degree(2) == 0
    assert mf.get_degree(2.5) == 0


def test_trimf_get_membership_degree_np_array():
    # Test the membership degrees computation for the Trapezoidal MF
    mf = TriMF(0, 1, 2)
    ipt = np.array([-0.5, 0, 0.5, 1, 1.5, 2, 2.5])
    out = np.array([0, 0, 0.5, 1, 0.5, 0, 0])
    assert (mf.get_degree(ipt) == out).all()


def test_trapmf_set_abcd_params():
    # Test getting/setting the parameters of the Triangular MF
    with pytest.raises(ValueError) as err:
        _ = TrapMF(2, 1, 0, 1)
    assert str(err.value) == 'The parameters must be specified such that'\
                             ' a <= b <= c <= d.'

    # Ordered
    mf = TrapMF(0, 1, 2, 3)
    assert mf.get_params() == (0, 1, 2, 3)


def test_trapmf_set_non_numeric_abcd_params():
    # Test setting a non numeric value for the MF params
    with pytest.raises(TypeError) as err:
        _ = TrapMF('0', 1, 2, 3)
    assert str(err.value) == 'All parameters must be numeric.'


def test_trapmf_get_membership_degree():
    # Test the membership degrees computation for the Trapezoidal MF
    mf = TrapMF(0, 1, 2, 3)
    assert mf.get_degree(-0.5) == 0
    assert mf.get_degree(0) == 0
    assert mf.get_degree(0.5) == 0.5
    assert mf.get_degree(1) == 1
    assert mf.get_degree(1.5) == 1
    assert mf.get_degree(2) == 1
    assert mf.get_degree(2.5) == 0.5
    assert mf.get_degree(3) == 0
    assert mf.get_degree(3.5) == 0


def test_trapmf_get_membership_degree_np_array():
    # Test the membership degrees computation for the Trapezoidal MF
    mf = TrapMF(0, 1, 2, 3)
    ipt = np.array([-0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5])
    out = np.array([0, 0, 0.5, 1, 1, 1, 0.5, 0, 0])
    assert (mf.get_degree(ipt) == out).all()
