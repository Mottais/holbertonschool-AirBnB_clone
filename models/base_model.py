#!/usr/bin/python3
"""
Module de la classe BaseModel
(attributs et fonctions communs à toutes les classes (tables de données)).

"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Classe 'BaseModel'.

    Attributs communs à toutes les classes:
        id (str): identifiant unique pourchaque instance.
        created_at (datetime): Date et heure de création.
        updated_at (datetime): Date et heure de modification.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise les attributs communs à toutes les classes:
        """
        self.created_at = self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    try:
                        value = datetime.fromisoformat(value)
                    except ValueError:
                        pass
                self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Retourne une chaine representant l'instance.
        [nom de la classe] (id) {dictionnaire des attributs de l'instance}

        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        Modifie l'attribute 'updated_at' avec date et heure actuelles.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Crée un dictionnaire contenant tous les attributs de l'instance.
        Ajoute l'attribut '__class__'
        Formate 'created_at' et 'updated_at' au format ISO
        Retourne le dictionnaire.

        """
        # créer une copie du dictionnaire __dict__ de l'instance.
        obj_dict = self.__dict__.copy()

        # Ajoute l'attribut '__class__' avec le nom de la classe.
        obj_dict['__class__'] = self.__class__.__name__

        # Formate 'created_at' au format ISO
        obj_dict['created_at'] = self.created_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')

        # Formate 'updated_at' au format ISO (via la méthode 'isoformat')
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
