#!/usr/bin/env python
"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

import unittest

def ReadFemResp():
    return nsfg.ReadFemResp()

def pregnum_value_counts(resp_df):
    return resp_df.pregnum.value_counts()

def cross_validate_with_preg(preg_df, resp_df):
    preg_map = nsfg.MakePregMap(preg_df)
    for preg_caseid, preg_idxs in preg_map.items():
        resp_pregnum = resp_df[resp_df.caseid==preg_caseid].pregnum.iloc[0]
        if resp_pregnum != len(preg_idxs):
            print(preg_caseid, preg_idxs[preg_caseid])
            return False
    return True


class TestNsfgData(unittest.TestCase):
    """
    Data for tests from http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=FEM&section=B&subSec=7820&srtLabel=604531
    """
    PREG_DF = nsfg.ReadFemPreg()
    RESP_DF = ReadFemResp()

    def test_total_number_of_response(self):
        self.assertEqual(len(RESP_DF), 7644)

    def test_pregnum_value_counts(self):
        pregnum_vc_series = pregnum_value_counts(TestNsfgData.RESP_DF)
        self.assertEqual(pregnum_vc_series[1], 1267)
        self.assertEqual(pregnum_vc_series[2], 1432)
        self.assertEqual(pregnum_vc_series[3], 1110)
        self.assertEqual(pregnum_vc_series[4], 611)
        self.assertEqual(pregnum_vc_series[5], 305)
        self.assertEqual(pregnum_vc_series[6], 150)

    def test_cross_validation(self):
        self.assertTrue(cross_validate_with_preg(
            TestNsfgData.PREG_DF,
            TestNsfgData.RESP_DF))

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    unittest.main()
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
