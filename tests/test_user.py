#!/usr/bin/python3
"""User class module"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """unit test for user class"""

    def test_no_args(self):
        """test no arguments"""
        self.assertEqual(User, type(User()))

    def test_created_at(Self):
        """test created at attr"""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at(self):
        """test updated at attr"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_new_instance(self):
        """test new instance"""
        self.assertIn(User(), models.storage.all().values())

    def test_id(self):
        """test id"""
        self.assertEqual(str, type(User().id))

    def test_email(Self):
        """test email"""
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """test password"""
        self.assertEqual(str, type(User.password))

    def test_firstname(Self):
        """test first name"""
        self.assertEqual(str, type(User.first_name))

    def test_lastname(Self):
        """test last name"""
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        """test two users id"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_created_at(self):
        """test two users different created at"""
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_users_updated_at(self):
        """test two users different updated at"""
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_unused_args(self):
        """test unused arguments"""
        user1 = User(None)
        self.assertNotIn(None, user1.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        """test instan with no kwargs"""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_kwargs(self):
        """test instan with kwargs"""
        date = datetime.today()
        date_iso = date.isoformat()
        user1 = User(id="777", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(user1.id, "777")
        self.assertEqual(user1.created_at, date)
        self.assertEqual(user1.updated_at, date)

    def test_str_(self):
        """test __str__"""
        date = datetime.today()
        date_repr = repr(date)
        user1 = User()
        user1.id = "777777"
        user1.created_at = user1.updated_at = date
        user1_str = user1.__str__()
        self.assertIn("[User] (777777)", user1_str)
        self.assertIn("'id': '777777'", user1_str)
        self.assertIn("'created_at': " + date_repr, user1_str)
        self.assertIn("'updated_at': " + date_repr, user1_str)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method"""

    @classmethod
    def setUp(self):
        """setup"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save(self):
        """test one save"""
        usr = User()
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        self.assertLess(first_updated_at, usr.updated_at)

    def test_saves(self):
        """test two saves"""
        usr = User()
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        second_updated_at = usr.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        usr.save()
        self.assertLess(second_updated_at, usr.updated_at)

    def test_updates_file(self):
        """test save updates file"""
        usr = User()
        usr.save()
        usr_id = "User." + usr.id
        with open("file.json", "r") as f:
            self.assertIn(usr_id, f.read())

    def test_with_arg(self):
        """test save with args"""
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method"""

    def test_to_dict_type(self):
        """test to_dict"""
        self.assertTrue(dict, type(User().to_dict()))

    def test_added_attr(self):
        """test to_dict with added attr"""
        usr = User()
        usr.middle_name = "Holberton"
        usr.my_number = 98
        self.assertEqual("Holberton", usr.middle_name)
        self.assertIn("my_number", usr.to_dict())

    def test_correct_keys(self):
        """test to_dict contains correct keys"""
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def test_datetime_attributes_are_strs(self):
        """test to_dict datetime attr"""
        usr = User()
        usr_dict = usr.to_dict()
        self.assertEqual(str, type(usr_dict["id"]))
        self.assertEqual(str, type(usr_dict["created_at"]))
        self.assertEqual(str, type(usr_dict["updated_at"]))

    def test_contrast_to_dict(self):
        """test contrast to dict """
        usr = User()
        self.assertNotEqual(usr.to_dict(), usr.__dict__)

    def test_output(self):
        """test output"""
        date = datetime.today()
        usr = User()
        usr.id = "777777"
        usr.created_at = usr.updated_at = date
        tdict = {
            'id': '777777',
            '__class__': 'User',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(usr.to_dict(), tdict)

    def test_with_arg(self):
        """test to dict with args"""
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)


if __name__ == "__main__":
    unittest.main()
