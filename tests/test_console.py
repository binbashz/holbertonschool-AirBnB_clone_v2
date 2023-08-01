#!/usr/bin/python3
import unittest
from console import HBNBCommand
from models import storage
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.user import User
from io import StringIO
from unittest.mock import patch


class TestCreateCommand(unittest.TestCase):
    """Test for the 'create' command in the console"""
    def setUp(self):
        self.console = HBNBCommand()
        storage.reload()

    def tearDown(self):
        del self.console

    def test_create_state(self):
        """Test create command for State"""
        self.console.onecmd("create State name=\"California\"")
        california_id = self.console.stdout.strip()
        self.assertIsInstance(california_id, str)

        # Check if the created State object is stored in the FileStorage
        state = storage.all()["State." + california_id]
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "California")

    def test_create_place(self):
        """Test create command for Place"""
        command = "create Place city_id=\"0001\" user_id=\"0001\" " \
                  "name=\"My_little_house\
                  \" number_rooms=4 number_bathrooms=2 " \
                  "max_guest=10 price_by_night=300 latitude=37.773972 " \
                  "longitude=-122.431297"
        self.console.onecmd(command)
        place_id = self.console.stdout.strip()
        self.assertIsInstance(place_id, str)

        # Check if the created Place object is stored in the FileStorage
        place = storage.all()["Place." + place_id]
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "0001")
        self.assertEqual(place.user_id, "0001")
        self.assertEqual(place.name, "My little house")
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 300)
        self.assertEqual(place.latitude, 37.773972)
        self.assertEqual(place.longitude, -122.431297)


if __name__ == '__main__':
    unittest.main()
