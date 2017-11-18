#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""run-tests.py
Runs through all test cases for run-command

Dependencies:
    pytest: to run tests
    zlib: to compress/decompress test cases
            - test code is highly compressible, and runs infrequently

Todo:
    * Setup test files loader
    * Halt output at failed case, logging passes before it
    * Colorize output
    * Put inside of run-command as option --run-tests
    * Write article on TDD & pyTest
    * Make test files compressed at end of tests (fail or pass)
    * Make test files open a compressed gzip file
"""
import pytest

# start script execution at end of file for forward declaration of functions
if __name__ == '__main__':
    # TODO: refactor for more pythonic way of handling tests
    #       - find way to make run-command managable single while including test
    import sys
    path.insert(0, '../..')
    import run-command
    print_usage(argv)
