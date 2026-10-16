# test_draftwarehouse.py
"""
Tests for DraftWarehouse module.
"""

import unittest
from draftwarehouse import DraftWarehouse

class TestDraftWarehouse(unittest.TestCase):
    """Test cases for DraftWarehouse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftWarehouse()
        self.assertIsInstance(instance, DraftWarehouse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftWarehouse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
