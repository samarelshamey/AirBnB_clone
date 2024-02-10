#!/usr/bin/python3
"""review unittest module"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """unittest for review class instantiation"""

    def test_with_None_kwargs(self):
        """test with no kwargs"""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_with_kwargs(self):
        """test with kwargs"""
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        review = Review(id="777", created_at=my_date_iso,
                        updated_at=my_date_iso)
        self.assertEqual(review.id, "777")
        self.assertEqual(review.created_at, my_date)
        self.assertEqual(review.updated_at, my_date)

    def test_str_(self):
        """test __str__"""
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        review = Review()
        review.id = "777777"
        review.created_at = review.updated_at = my_date
        review_str = review.__str__()
        self.assertIn("[Review] (777777)", review_str)
        self.assertIn("'id': '777777'", review_str)
        self.assertIn("'created_at': " + my_date_repr, review_str)
        self.assertIn("'updated_at': " + my_date_repr, review_str)

    def test_args_unused(self):
        """test args unused"""
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_two_reviews_unique_ids(self):
        """test two reviews id"""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_two_reviews_different_created_at(self):
        """test two reviews created at"""
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_two_reviews_different_updated_at(self):
        """test two reviews updated at"""
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_updated_at(self):
        """test updated at"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id(self):
        """test place id"""
        review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review))
        self.assertNotIn("place_id", review.__dict__)

    def test_user_id(self):
        """test user id"""
        review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review))
        self.assertNotIn("user_id", review.__dict__)

    def test_text(self):
        """test text"""
        review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review))
        self.assertNotIn("text", review.__dict__)

    def test_no_args(self):
        """test no args"""
        self.assertEqual(Review, type(Review()))

    def test_new_instance(self):
        """test new instance stored in object"""
        self.assertIn(Review(), models.storage.all().values())

    def test_id(self):
        """test id"""
        self.assertEqual(str, type(Review().id))

    def test_created_at(self):
        """test created at"""
        self.assertEqual(datetime, type(Review().created_at))


class TestReview_to_dict(unittest.TestCase):
    """unitest for review class to dict method"""

    def test__with_arg(self):
        """test to dict with arg"""
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)

    def test_output(self):
        """test output"""
        my_date = datetime.today()
        review = Review()
        review.id = "777777"
        review.created_at = review.updated_at = my_date
        to_dict = {
            'id': '777777',
            '__class__': 'Review',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """test contrast"""
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

    def test_contains_added_attributes(self):
        """test to dict contains added attrs"""
        review = Review()
        review.middle_name = "Johnson"
        review.my_number = 777
        self.assertEqual("Johnson", review.middle_name)
        self.assertIn("my_number", review.to_dict())

    def test_datetime_attrs_are_str(self):
        """test to dict datetime attrs are strs"""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(str, type(review_dict["id"]))
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def test_type(self):
        """test to dict type"""
        self.assertTrue(dict, type(Review().to_dict()))

    def test_contains_correct_keys(self):
        """test to dict contains correct keys"""
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())


class TestReview_save(unittest.TestCase):
    """unittest for review class save method"""

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
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_updates_file(self):
        """test save updates file"""
        review = Review()
        review.save()
        review_id = "Review." + review.id
        with open("file.json", "r") as f:
            self.assertIn(review_id, f.read())

    def test_one_save(self):
        """test oe save"""
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        self.assertLess(first_updated_at, review.updated_at)

    def test_two_saves(self):
        """test two saves"""
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        second_updated_at = review.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        review.save()
        self.assertLess(second_updated_at, review.updated_at)


if __name__ == "__main__":
    unittest.main()
