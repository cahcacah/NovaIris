# test_novairis.py
"""
Tests for NovaIris module.
"""

import unittest
from novairis import NovaIris

class TestNovaIris(unittest.TestCase):
    """Test cases for NovaIris class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaIris()
        self.assertIsInstance(instance, NovaIris)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaIris()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
