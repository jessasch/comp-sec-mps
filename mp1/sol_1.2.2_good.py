#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           y���T8��� A0�.�������1��;���h��)�;F�߇t���v_m��#��ls3+lh��r{�[����aZ�N����_�mA�O�i'��X�k1��
>.��Y����ro�\�C"""
from hashlib import sha256
if sha256(blob).hexdigest() == 'baffada0eecf4ed18dd6bf5d4475519a8054c9e7a5c020fdda6049de74a9fbf9':
    print "I come in peace."
else:
    print "Prepare to be destroyed!"
