#!/usr/bin/python3
"""Module for TestHBNBCommand class."""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import os.path


class TestHBNBCommand(unittest.TestCase):
    """Test the console file."""

    def tearDown(self):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_unkown_command(self):
        """Test commands that do not exist."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("something")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: something")

    def test_emptyline(self):
        """Tests emptyline in the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        out = ""
        self.assertEqual(out, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
        out = ""
        self.assertEqual(out, f.getvalue())

    def test_Base_model(self):
        """Test Basemodel with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel " + str(id) + " name Manga")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Manga" in f.getvalue().strip())

    def test_user(self):
        """Test User with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id) + " name Manga")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Manga" in f.getvalue().strip())

    def test_state(self):
        """Test State with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State " + str(id) + " name Manga")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Manga" in f.getvalue().strip())

    def test_city(self):
        """Test City with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update City " + str(id) + " name Manga")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Manga" in f.getvalue().strip())

    def test_amenity(self):
        """Test Amenity with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Amenity " + str(id) + " name Manga")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Manga" in f.getvalue().strip())

    def test_place(self):
        """Test Place with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Place " + str(id) + " name Manga")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Manga" in f.getvalue().strip())

    def test_review(self):
        """Test Review with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Review " + str(id) + " name Manga")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Manga" in f.getvalue().strip())

    def test_create(self):
        """Test create command with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Animal")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User name="David"')
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

    def test_destroy(self):
        """Test destroy command with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Manga")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel " + str(id))
            self.assertEqual(f.getvalue().strip(), "")

    def test_all(self):
        """Test all command with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertTrue("[User]" in f.getvalue().strip())
            self.assertTrue("[State]" in f.getvalue().strip())
            self.assertTrue("[City]" in f.getvalue().strip())
            self.assertTrue("[Amenity]" in f.getvalue().strip())
            self.assertTrue("[Place]" in f.getvalue().strip())
            self.assertTrue("[Review]" in f.getvalue().strip())
            self.assertTrue("created_at" in f.getvalue().strip())
            self.assertTrue("updated_at" in f.getvalue().strip())
            self.assertTrue("id" in f.getvalue().strip())

    def test_update(self):
        """Test update command with the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Brent")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User Manga")
            self.assertEqual(f.getvalue().strip(),
                             "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id))
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id) + " name Manga")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Manga" in f.getvalue().strip())
