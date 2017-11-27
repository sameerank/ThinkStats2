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

def pregnum_value_counts():
    resp = ReadFemResp()
    return resp.pregnum.value_counts()

def cross_validate_with_preg(preg_df, resp_df):
    preg_map = nsfg.MakePregMap(preg_df)
    for preg_caseid, preg_idxs in preg_map.items():
        resp_pregnum = resp_df[resp_df.caseid==preg_caseid].pregnum.iloc[0]
        if resp_pregnum != len(preg_idxs):
            print(preg_caseid, preg_idxs[preg_caseid])
            return False
    return True


class TestNsfgData(unittest.TestCase):
    def setUp(self):
        self.preg = nsfg.ReadFemPreg()
        self.resp = ReadFemResp()

    def test_cross_validation(self):
        self.assertTrue(cross_validate_with_preg(self.preg, self.resp))

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    unittest.main()
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
