#!/usr/bin/python3
"""state unittest module"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """unittest for state instantiation"""

    def test_with_kwargs(self):
        """test instantiation with kwargs"""
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        state = State(id="345", created_at=my_date_iso,
                      updated_at=my_date_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, my_date)
        self.assertEqual(state.updated_at, my_date)

    def test_with_None_kwargs(self):
        """test instantiation with no kwargs"""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_two_states_updated_at(self):
        """test two states updated at"""
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_str_(self):
        """test __str__"""
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        state = State()
        state.id = "777777"
        state.created_at = state.updated_at = my_date
        state_str = state.__str__()
        self.assertIn("[State] (777777)", state_str)
        self.assertIn("'id': '777777'", state_str)
        self.assertIn("'created_at': " + my_date_repr, state_str)
        self.assertIn("'updated_at': " + my_date_repr, state_str)

    def test_args_unused(self):
        """test args unused"""
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_updated_at(self):
        """test updated at"""
        self.assertEqual(datetime, type(State().updated_at))

    def test_name(self):
        """test name"""
        state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_two_states_unique_ids(self):
        """test two states id"""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_two_states_different_created_at(self):
        """test tw state created at"""
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_no_args(self):
        """test no args"""
        self.assertEqual(State, type(State()))

    def test_new_instance(self):
        """test new instance stored in object"""
        self.assertIn(State(), models.storage.all().values())

    def test_id(self):
        """test id """
        self.assertEqual(str, type(State().id))

    def test_created_at(self):
        """test created at"""
        self.assertEqual(datetime, type(State().created_at))


class TestState_to_dict(unittest.TestCase):
    """unittest for to dict method"""

    def test_contrast_to_dict_dunder_dict(self):
        """test contrast"""
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_with_arg(self):
        """test to dict with arg"""
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)

    def test_output(self):
        """test to dict output"""
        my_date = datetime.today()
        state = State()
        state.id = "777777"
        state.created_at = state.updated_at = my_date
        tdict = {
            'id': '777777',
            '__class__': 'State',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), tdict)

    def test_contains_added_attributes(self):
        """test to dict contains added attrs"""
        state = State()
        state.middle_name = "Johnson"
        state.my_number = 777
        self.assertEqual("Johnson", state.middle_name)
        self.assertIn("my_number", state.to_dict())

    def test_datetime_attributes_are_strs(self):
        """test to dict datetime attr are strs"""
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(str, type(state_dict["id"]))
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))

    def test_type(self):
        """test to dict type"""
        self.assertTrue(dict, type(State().to_dict()))

    def test_contains_correct_keys(self):
        """test to dict contains correct keys"""
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())


class TestState_save(unittest.TestCase):
    """unittest for save method"""

    @classmethod
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

    def test_with_arg(self):
        """test save with args"""
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_updates_file(self):
        """test save updates file"""
        state = State()
        state.save()
        state_id = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())

    def test_one_save(self):
        """test one save"""
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)

    def test_two_saves(self):
        """test two saves"""
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        second_updated_at = state.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        state.save()
        self.assertLess(second_updated_at, state.updated_at)


if __name__ == "__main__":
    unittest.main()
