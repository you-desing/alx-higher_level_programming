# test_base.py
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_assigned_when_provided(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_id_incremented_when_not_provided(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_private_nb_objects_attribute(self):
        obj = Base()
        self.assertTrue(hasattr(obj, '_Base__nb_objects'))

    def test_nb_objects_incremented_correctly(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(Base._Base__nb_objects, 2)


if __name__ == '__main__':
    unittest.main()
