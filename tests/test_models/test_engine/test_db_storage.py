#!/usr/bin/python3
"""Test for DBStorage class"""

import os
import unittest
import models
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.engine.db_storage import DBStorage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'only DBStorage')
class testDBStorage(unittest.TestCase):
    """Testing for DBStorage class"""

    def test_user(self):
        '''
        Test user class with database
        '''
        user = User(email="suaro@suaro.com", password="password")
        user.save()
        for key, obj in models.storage.all('User').items():
            if obj.id == user.id:
                self.assertTrue(obj.password, "password")
                self.assertTrue(obj.email, "suaro@suaro.com")
            else:
                continue

    def test_state(self):
        """Test state class with database"""
        state = State(name="Illinois")
        state.save()
        for key, obj in models.storage.all('State').items():
            if obj.id == state.id:
                self.assertTrue(obj.name, "Illinois")
            else:
                continue

    def test_city(self):
        """Test city class with database"""
        state = State(name="California")
        city = City(name="Los Angeles", state_id=state.id)
        state.save()
        city.save()
        for key, obj in models.storage.all('City').items():
            if obj.id == city.id:
                self.assertTrue(obj.name, "Los Angeles")
                self.assertTrue(obj.state_id, state.id)
            else:
                continue

    def test_place(self):
        """Test place class with database"""
        state = State(name="Washington")
        city = City(name="Seattle", state_id=state.id)
        user = User(email="@holberton", password="pwd")
        place = Place(city_id=city.id, user_id=user.id, name="House",
                      number_rooms=2, number_bathrooms=1, max_guest=2,
                      price_by_night=50)
        state.save()
        city.save()
        user.save()
        place.save()
        for key, obj in models.storage.all('Place').items():
            if obj.id == place.id:
                self.assertTrue(obj.city_id, city.id)
                self.assertTrue(obj.user_id, user.id)
                self.assertTrue(obj.name, "House")
                self.assertTrue(obj.number_rooms, 2)
                self.assertTrue(obj.number_bathrooms, 1)
                self.assertTrue(obj.max_guest, 2)
                self.assertTrue(obj.price_by_night, 50)
                self.assertTrue(obj.description is None)
            else:
                continue

    def test_amenity(self):
        """Test amenity class with database"""
        amenity = Amenity(name="Wifi")
        amenity.save()
        for key, obj in models.storage.all('Amenity').items():
            if obj.id == amenity.id:
                self.assertTrue(obj.name, "Wifi")
            else:
                continue

    def test_all(self):
        """Test all function"""
        user1 = User(email="email1", password="password1")
        user2 = User(email="email2", password="password2")
        user3 = User(email="email3", password="password3")

        user1.save()
        user2.save()
        user3.save()
        obj_dict = models.storage.all('User')
        self.assertTrue(len(obj_dict), 3)

    def test_delete(self):
        """Test delete function"""
        state = State(name="New York")
        state.save()
        models.storage.delete(state)
        models.storage.save()
        all_stored = models.storage.all()
        self.assertRaises(KeyError, all_stored.__getitem__, "State." + state.id)

    def teardown(self):
        self.session.close()
        self.session.rollback()

if __name__ == '__main__':
    unittest.main()
