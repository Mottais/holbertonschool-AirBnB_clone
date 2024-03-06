#!/usr/bin/python3
"""Definition of User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Create an instance of user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    ''' Je ne comprends pas pourquoi ces attributs
    sont de Classe publique. Ils ne servent à rien.
    ci-dessous, une version qui me semble plus judicieuse
    def __init__(self, *args, **kwargs):
        """Initialize user"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
    '''
