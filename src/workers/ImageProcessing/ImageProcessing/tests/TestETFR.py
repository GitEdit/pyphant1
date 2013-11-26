# -*- coding: utf-8 -*-

# Copyright (c) 2006-2007, Rectorate of the University of Freiburg
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of the Freiburg Materials Research Center,
#   University of Freiburg nor the names of its contributors may be used to
#   endorse or promote products derived from this software without specific
#   prior written permission.
#
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

u"""Provides unittest classes for EdgeTouchingFeatureRemover worker
"""


import unittest
import numpy


class EDFRTestCase(unittest.TestCase):
    def testETFR(self):
        from ImageProcessing.EdgeTouchingFeatureRemover \
             import EdgeTouchingFeatureRemover
        from pyphant.core.DataContainer import FieldContainer
        from pyphant.quantities import Quantity
        from ImageProcessing import BACKGROUND_COLOR, FEATURE_COLOR
        data = numpy.ones((10, 10), dtype='uint8') * BACKGROUND_COLOR
        data[5:10,3:8] = FEATURE_COLOR
        data[1:4,3:8] = FEATURE_COLOR
        image = FieldContainer(data)
        for dim in image.dimensions:
            dim.unit = Quantity('2 mum')
        image.seal()
        etfr = EdgeTouchingFeatureRemover()
        result = etfr.fillFeatures(image)
        self.assertEqual(result.dimensions, image.dimensions)
        expected = numpy.ones((10, 10), dtype='uint8') * BACKGROUND_COLOR
        expected[1:4,3:8] = FEATURE_COLOR
        self.assertTrue((expected == result.data).all())


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        unittest.main()
    else:
        suite = unittest.TestLoader().loadTestsFromTestCase(
            eval(sys.argv[1:][0]))
        unittest.TextTestRunner().run(suite)