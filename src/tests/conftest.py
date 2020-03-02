"""Shared fixtures for pytest"""

import pytest

from example_py_project.example_module import Example_class

@pytest.fixture
def example_class(tmpdir):
    """provides empty resource for testing"""
    return Example_class(tmpdir)
