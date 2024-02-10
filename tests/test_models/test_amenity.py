#!/usr/bin/python3
"""unittest for amenity module"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """test amenity class"""

    def setUp(self):
        """setup"""
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_no_args(self):
        """test no arguments instanciation"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance(self):
        """test new instance stored in object"""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id(self):
        """test id"""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at(self):
        """test created at"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at(self):
        """test updated at"""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name(self):
        """test name is a public attr"""
        amenity1 = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenity1.__dict__)

    def test_two_unique_ids(self):
        """test two amenties with unique ids"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_two_different_created_at(self):
        """test two amenities created at"""
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_two_different_updated_at(self):
        """test two amenities updated at"""
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_str_(self):
        """test __str__"""
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        amenity1 = Amenity()
        amenity1.id = "777777"
        amenity1.created_at = amenity1.updated_at = my_date
        amenity_str = amenity1.__str__()
        self.assertIn("[Amenity] (777777)", amenity_str)
        self.assertIn("'id': '777777'", amenity_str)
        self.assertIn("'created_at': " + my_date_repr, amenity_str)
        self.assertIn("'updated_at': " + my_date_repr, amenity_str)

    def test_args_unused(self):
        """test args unused"""
        amenity1 = Amenity(None)
        self.assertNotIn(None, amenity1.__dict__.values())

    def test_with_kwargs(self):
        """test instantiation with kwargs"""
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        amenity1 = Amenity(id="777", created_at=my_date_iso,
                           updated_at=my_date_iso)
        self.assertEqual(amenity1.id, "777")
        self.assertEqual(amenity1.created_at, my_date)
        self.assertEqual(amenity1.updated_at, my_date)

    def test_with_None_kwargs(self):
        """test instantiation with no kwargs"""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for to_dict method of the Amenity class"""

    def setUp(self):
        """setup"""
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_type(self):
        """test to dict type"""
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_contains_correct_keys(self):
        """test to dict contain correct keys"""
        amenity1 = Amenity()
        self.assertIn("id", amenity1.to_dict())
        self.assertIn("created_at", amenity1.to_dict())
        self.assertIn("updated_at", amenity1.to_dict())
        self.assertIn("__class__", amenity1.to_dict())

    def test_contains_added_attrs(self):
        """test to dict contain added attr"""
        amenity1 = Amenity()
        amenity1.middle_name = "Johnson"
        amenity1.my_number = 777
        self.assertEqual("Johnson", amenity1.middle_name)
        self.assertIn("my_number", amenity1.to_dict())

    def test_datetime_attr(self):
        """test to dict datetime attrs are str"""
        amenity1 = Amenity()
        amenity_dict = amenity1.to_dict()
        self.assertEqual(str, type(amenity_dict["id"]))
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_output(self):
        """test output"""
        my_date = datetime.today()
        amenity1 = Amenity()
        amenity1.id = "777777"
        amenity1.created_at = amenity1.updated_at = my_date
        to_dict = {
            'id': '777777',
            '__class__': 'Amenity',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(amenity1.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """test contrast"""
        amenity1 = Amenity()
        self.assertNotEqual(amenity1.to_dict(), amenity1.__dict__)

    def test_with_arg(self):
        """test to dict with arg"""
        amenity1 = Amenity()
        with self.assertRaises(TypeError):
            amenity1.to_dict(None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for save method of the Amenity class"""

    def setUp(self):
        """setup"""
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_one_save(self):
        """test one save"""
        amenity1 = Amenity()
        sleep(0.05)
        first_updated_at = amenity1.updated_at
        amenity1.save()
        self.assertLess(first_updated_at, amenity1.updated_at)

    def test_two_saves(self):
        """test two saves"""
        amenity1 = Amenity()
        sleep(0.05)
        first_updated_at = amenity1.updated_at
        amenity1.save()
        second_updated_at = amenity1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity1.save()
        self.assertLess(second_updated_at, amenity1.updated_at)

    def test_with_arg(self):
        """test save with args"""
        amenity1 = Amenity()
        with self.assertRaises(TypeError):
            amenity1.save(None)

    def test_updates_file(self):
        """test save updates file"""
        amenity1 = Amenity()
        amenity1.save()
        amenity_id = "Amenity." + amenity1.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


if __name__ == "__main__":
    unittest.main()
