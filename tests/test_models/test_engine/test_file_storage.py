#!/usr/bin/python3
"""Unittest Classe FileStorage"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    @classmethod
    def setUpClass(self):
        """setUpClass est une méthode spéciale dans unittest
        qui est appelée avant d'exécuter tous les tests de la classe.
        Ici, setUpClass est utilisée pour initialiser l'environnement de test
        avant d'exécuter les tests."""

        '''création d'une instance de la classe FileStorage
        stockée dans l'attribut de classe 'storage'.
        Ainsi 'storage' est une instance de 'FileStorage' utilisée dans les
        tests de cette classe pour effectuer des opérations de test sur
        l'objet FileStorage'''
        self.storage = FileStorage()

    def test_01_all(self):
        """Test case for 'all' method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_02_new(self):
        """Test case for 'new' method"""
        model = BaseModel()
        self.storage.new(model)
        key = model.__class__.__name__ + "." + model.id
        self.assertIn(key, self.storage.all())

    def test_03_save(self):
        """Test case for 'save' method"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """Test case for 'reload' method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = model.__class__.__name__ + "." + model.id
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
