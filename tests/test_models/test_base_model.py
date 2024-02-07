#!/usr/bin/python3
"""Unittests for base module"""
import datetime
from unittest import TestCase
from models.base_model import BaseModel


class BaseModelTest(TestCase):
    """Unittests for BaseModel class"""

    def setUp(self):
        """Set up code for BaseModel tests"""
        self.obj1 = BaseModel()
	self.obj2 = BaseModel()
	self.invalid_obj = {"created_at": "invalid", "updated_at": "invalid"}

    def test_base_id(self):
        """Test id attribute""" 
	self.assertIsInstance(self.obj1.id, str)
	self.assertIsInstance(self.obj2.id, str)
	self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_base_created_at(self):
        """Test created_at attribute"""
        try:
            datetime.fromisoformat(obj1.created_at)
            self.assertTrue(True)  #Assertion passes if conversion is successful
        except ValueError:
            self.fail("created_at attribute is invalid isoformat")

        with self.AssertRaises(ValueError):
            datetime.fromisoformat(invalid_obj["created_at"])

    def test_base_updated_at(self):
        """Test updated_at attribute"""
        try:
            datetime.fromisoformat(obj1.updated_at)
            self.assertTrue(True)  #Assertion passes if conversion is successful
         except ValueError:
             self.fail("updated_at attribute is invalid isoformat")

         with self.AssertRaises(ValueError):
             datetime.fromisoformat(invalid_obj["updated_at"])

     def test_base_str(self):
         """Test __str__ method"""
         _dict = obj2.__dict__
	 str1 = "[BaseModel] ({}) {}".format(obj2.id, _dict)
	 str2 = str(obj2)
	 self.assertEqual(str1, str2)

     def test_base_save(self):
         """Test save method"""
         first_updated = obj1.updated_at
	 obj1.save()
	 second_updated = obj1.updated_at
	 self.assertNotEqual(first_updated, second_updated)

     def test_base_to_dict(self):
         """Test to_dict method"""
        my_dict = obj2.to_dict()
        self.assertIsInstance(my_dict, dict)
        for key, value in my_dict.items():
            flag = 0
            if my_dict['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict.items():
            if key == "created_at":
                self.assertIsInstance(value, str)
            if key == "updated_at":
                self.assertIsInstance(value, str)
