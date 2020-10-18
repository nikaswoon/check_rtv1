import ctypes
import os
import unittest
import pytest
import subprocess
from decimal import Decimal
from test_data import *


def test_double(send, expect):
    data = [f"sphere\t{send} 0.0 0.0\n"]

    with open(PATH_SCENE, 'w') as file:
        file.writelines(data)
    text = str(subprocess.check_output([PATH_RTV1, PATH_SCENE]), 'utf-8')
    first_string = text.split('\n')[1]
    assert first_string == f'sphere [{expect}, 0.00, 0.00] 1.00 (0 0 0) -1.00', f"""
                                                    double error:
                                                    send: {send}
                                                    got: {first_string}
                                                    exp: sphere [{expect}, 0.00, 0.00] 1.00 (0 0 0) -1.00"""


def test_empty_figure():
    with open(PATH_SCENE, 'r') as file:
        data = file.readlines()

    data[0] = f"sphere\n"

    with open(PATH_SCENE, 'w') as file:
        file.writelines(data)
    try:
        subprocess.check_output([PATH_RTV1, PATH_SCENE], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        assert str(e.output,
                   'utf-8') == "SCENE ERROR: There is no figures in configuration file! What did you expect, nah??\n"


def test_double_camera():
    data = [f"sphere\t0 0 0\n", f"camera\t0 0 0\n", f"camera\t0 0 0\n"]

    with open(PATH_SCENE, 'w') as file:
        file.writelines(data)
    try:
        subprocess.check_output([PATH_RTV1, PATH_SCENE], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        assert str(e.output,
                   'utf-8') == "SCENE ERROR: In configuration file should be only 1 camera! not less not more!\n"


def test_not_full_data(data):
    f = open(PATH_SCENE, 'r+')
    f.truncate()

    with open(PATH_SCENE, 'w') as file:
        file.writelines(data)
    try:
        output = subprocess.check_output([PATH_RTV1, PATH_SCENE], stderr=subprocess.STDOUT)
        assert 'bus' not in str(output, 'utf-8'), output
        assert 'seg' not in str(output, 'utf-8'), output
        assert 'free' not in str(output, 'utf-8'), output
        assert 'malloc' not in str(output, 'utf-8'), output
        assert 'alloc' not in str(output, 'utf-8'), output
        assert 'memory' not in str(output, 'utf-8'), output
    except subprocess.CalledProcessError as e:
        assert 'bus' not in str(e.output, 'utf-8'), e.output
        assert 'seg' not in str(e.output, 'utf-8'), e.output
        assert 'free' not in str(e.output, 'utf-8'), e.output
        assert 'malloc' not in str(e.output, 'utf-8'), e.output
        assert 'alloc' not in str(e.output, 'utf-8'), e.output
        assert 'memory' not in str(e.output, 'utf-8'), e.output
        assert 'sphere' not in str(e.output, 'utf-8'), e.output


# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for test in TEST_DATA_DOUBLES:
        test_double(test, Decimal(TEST_DATA_DOUBLES[test]).quantize(Decimal('1.00')))
    test_empty_figure()
    test_double_camera()
    for section in [TEST_NOT_FULL_SPHERE, TEST_NOT_FULL_CYLINDER, TEST_NOT_FULL_CONE, TEST_NOT_FULL_PLANE,
                    TEST_NOT_FULL_CAMERA, TEST_NOT_FULL_LIGHT]:
        for items in section:
            test_not_full_data(items)
