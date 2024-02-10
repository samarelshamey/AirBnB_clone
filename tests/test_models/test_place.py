#!/usr/bin/python3
"""Place class unittest module"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """unittest for place class instantiation"""

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
        """test no arguments"""
        self.assertEqual(Place, type(Place()))

    def test_new_instance(self):
        """test new instance stored in object"""
        self.assertIn(Place(), models.storage.all().values())

    def test_id(self):
        """test id """
        self.assertEqual(str, type(Place().id))

    def test_created_at(self):
        """test created at"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at(self):
        """test updated at"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_name(self):
        """test name"""
        my_place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(my_place))
        self.assertNotIn("name", my_place.__dict__)

    def test_city_id(self):
        """test city id"""
        my_place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(my_place))
        self.assertNotIn("city_id", my_place.__dict__)

    def test_user_id(self):
        """test user id"""
        my_place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(my_place))
        self.assertNotIn("user_id", my_place.__dict__)

    def test_max_guest(self):
        """test max guest"""
        my_place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(my_place))
        self.assertNotIn("max_guest", my_place.__dict__)

    def test_number_bathrooms(self):
        """test number of bathroms atrr"""
        my_place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(my_place))
        self.assertNotIn("number_bathrooms", my_place.__dict__)

    def test_number_rooms(self):
        """test number of rooms"""
        my_place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(my_place))
        self.assertNotIn("number_rooms", my_place.__dict__)

    def test_description(self):
        """test description"""
        my_place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(my_place))
        self.assertNotIn("desctiption", my_place.__dict__)

    def test_amenity_ids(self):
        """test amenity ids"""
        my_place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(my_place))
        self.assertNotIn("amenity_ids", my_place.__dict__)

    def test_longitude(self):
        """test longitude"""
        my_place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(my_place))
        self.assertNotIn("longitude", my_place.__dict__)

    def test_latitude(self):
        """test latitude"""
        my_place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(my_place))
        self.assertNotIn("latitude", my_place.__dict__)

    def test_price_by_night(self):
        """test price by night"""
        my_place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(my_place))
        self.assertNotIn("price_by_night", my_place.__dict__)

    def test_two_places_unique_ids(self):
        """test two places ids"""
        my_place1 = Place()
        my_place2 = Place()
        self.assertNotEqual(my_place1.id, my_place2.id)

    def test_two_places_different_created_at(self):
        """test two places created at"""
        my_place1 = Place()
        sleep(0.05)
        my_place2 = Place()
        self.assertLess(my_place1.created_at, my_place2.created_at)

    def test_two_places_different_updated_at(self):
        """test two places updated at"""
        my_place1 = Place()
        sleep(0.05)
        my_place2 = Place()
        self.assertLess(my_place1.updated_at, my_place2.updated_at)

    def test_str_(self):
        """test __str__"""
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        my_place = Place()
        my_place.id = "777777"
        my_place.created_at = my_place.updated_at = my_date
        my_place_str = my_place.__str__()
        self.assertIn("[Place] (777777)", my_place_str)
        self.assertIn("'id': '777777'", my_place_str)
        self.assertIn("'created_at': " + my_date_repr, my_place_str)
        self.assertIn("'updated_at': " + my_date_repr, my_place_str)

    def test_with_None_kwargs(self):
        """test instantiation with no kwargs"""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_args_unused(self):
        """test args"""
        my_place = Place(None)
        self.assertNotIn(None, my_place.__dict__.values())

    def test_with_kwargs(self):
        """test instantiation with kwargs"""
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        my_place = Place(id="777", created_at=my_date_iso,
                         updated_at=my_date_iso)
        self.assertEqual(my_place.id, "777")
        self.assertEqual(my_place.created_at, my_date)
        self.assertEqual(my_place.updated_at, my_date)


class TestPlace_to_dict(unittest.TestCase):
    """unittest for place class to dict method"""

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
        self.assertTrue(dict, type(Place().to_dict()))

    def test_contains_correct_keys(self):
        """test to dict contain correct keys"""
        my_place = Place()
        self.assertIn("id", my_place.to_dict())
        self.assertIn("created_at", my_place.to_dict())
        self.assertIn("updated_at", my_place.to_dict())
        self.assertIn("__class__", my_place.to_dict())

    def test_contains_added_attrs(self):
        """test to dict contain added attr"""
        my_place = Place()
        my_place.middle_name = "Johnson"
        my_place.my_number = 777
        self.assertEqual("Johnson", my_place.middle_name)
        self.assertIn("my_number", my_place.to_dict())

    def test_datetime_attrs(self):
        """test to dict datetime attrs are str"""
        my_place = Place()
        my_place_dict = my_place.to_dict()
        self.assertEqual(str, type(my_place_dict["id"]))
        self.assertEqual(str, type(my_place_dict["created_at"]))
        self.assertEqual(str, type(my_place_dict["updated_at"]))

    def test_output(self):
        """test to dict output"""
        my_date = datetime.today()
        my_place = Place()
        my_place.id = "777777"
        my_place.created_at = my_place.updated_at = my_date
        to_dict = {
            'id': '777777',
            '__class__': 'Place',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(my_place.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """test contrast"""
        my_place = Place()
        self.assertNotEqual(my_place.to_dict(), my_place.__dict__)

    def test_with_arg(self):
        """test to dict with arg"""
        my_place = Place()
        with self.assertRaises(TypeError):
            my_place.to_dict(None)


class TestPlace_save(unittest.TestCase):
    """place class save method unittest"""

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
        my_place = Place()
        sleep(0.05)
        first_updated_at = my_place.updated_at
        my_place.save()
        self.assertLess(first_updated_at, my_place.updated_at)

    def test_two_saves(self):
        """test two saves"""
        my_place = Place()
        sleep(0.05)
        first_updated_at = my_place.updated_at
        my_place.save()
        second_updated_at = my_place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_place.save()
        self.assertLess(second_updated_at, my_place.updated_at)

    def test_updates_file(self):
        """test save updates file"""
        my_place = Place()
        my_place.save()
        my_place_id = "Place." + my_place.id
        with open("file.json", "r") as f:
            self.assertIn(my_place_id, f.read())

    def test_with_arg(self):
        """test save with arg"""
        my_place = Place()
        with self.assertRaises(TypeError):
            my_place.save(None)


if __name__ == "__main__":
    unittest.main()
