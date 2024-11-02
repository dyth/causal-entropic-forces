# -------------------------------------------------------------------------------
#
#  Define classes for (uni/multi)-variate kernel density estimation.
#
#  Currently, only Gaussian kernels are implemented.
#
#  Written by: Robert Kern
#
#  Date: 2004-08-09
#
#  Modified: 2005-02-10 by Robert Kern.
#              Contributed to SciPy
#            2005-10-07 by Robert Kern.
#              Some fixes to match the new scipy_core
#
#  Copyright 2004-2005 by Enthought, Inc.
#
# -------------------------------------------------------------------------------

import numpy as np

from scipy import linalg
from scipy.stats._stats import gaussian_kernel_estimate


class gaussian_kde:
    def __init__(self, dataset):
        self.dataset = np.atleast_2d(np.asarray(dataset))
        if not self.dataset.size > 1:
            raise ValueError("`dataset` input should have multiple elements.")

        self.d, self.n = self.dataset.shape
        self.weights = np.ones(self.n) / self.n

        # This can be converted to a warning once gh-10205 is resolved
        if self.d > self.n:
            msg = ("Number of dimensions is greater than number of samples. "
                   "This results in a singular data np.covariance matrix, which "
                   "cannot be treated using the algorithms implemented in "
                   "`gaussian_kde`. Note that `gaussian_kde` interprets each "
                   "*column* of `dataset` to be a point; consider transposing "
                   "the input to `dataset`.")
            raise ValueError(msg)

        try:
            # this is scotts_factor
            neff = 1 / np.sum(self.weights ** 2)
            self.factor = np.power(neff, -1. / (self.d + 4))
            # Cache np.covariance and Cholesky decomp of np.covariance
            if not hasattr(self, '_data_cho_np.cov'):
                cov = np.cov(self.dataset, rowvar=1, bias=False, aweights=self.weights)
                self._data_covariance = np.atleast_2d(cov)
                self._data_cho_cov = linalg.cholesky(self._data_covariance, lower=True)

            self.covariance = self._data_covariance * self.factor ** 2
            self.cho_cov = (self._data_cho_cov * self.factor).astype(np.float64)
            self.log_det = 2 * np.log(np.diag(self.cho_cov * np.sqrt(2 * np.pi))).sum()
        except linalg.LinAlgError as e:
            msg = ("The data appears to lie in a lower-dimensional subspace "
                   "of the space in which it is expressed. This has resulted "
                   "in a singular data np.covariance matrix, which cannot be "
                   "treated using the algorithms implemented in "
                   "`gaussian_kde`. Consider performing principle component "
                   "analysis / dimensionality reduction and using "
                   "`gaussian_kde` with the transformed data.")
            raise linalg.LinAlgError(msg) from e

    def evaluate(self, points):
        points = np.atleast_2d(np.asarray(points))
        output_dtype, spec = _get_output_dtype(self.covariance, points)
        result = gaussian_kernel_estimate[spec](
            self.dataset.T, self.weights[:, None], points.T, self.cho_cov, output_dtype
        )

        return result[:, 0]


def _get_output_dtype(covariance, points):
    """
    Calculates the output dtype and the "spec" (=C type name).

    This was necessary in order to deal with the fused types in the Cython
    routine `gaussian_kernel_estimate`. See gh-10824 for details.
    """
    output_dtype = np.common_type(covariance, points)
    itemsize = np.dtype(output_dtype).itemsize
    if itemsize == 4:
        spec = 'float'
    elif itemsize == 8:
        spec = 'double'
    elif itemsize in (12, 16):
        spec = 'long double'
    else:
        raise ValueError(f"{output_dtype} has unexpected item size: {itemsize}")

    return output_dtype, spec