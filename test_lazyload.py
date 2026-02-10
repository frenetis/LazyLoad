# test_lazyload.py
"""
Tests for LazyLoad module.
"""

import unittest
from lazyload import LazyLoad

class TestLazyLoad(unittest.TestCase):
    """Test cases for LazyLoad class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LazyLoad()
        self.assertIsInstance(instance, LazyLoad)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LazyLoad()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
