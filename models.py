from  My_Garden.index.py import db 
from flask_login import UserMixin
from   My_Garden.index.py import login

#### MODELO DE USUARIO ####
class cliente (UserMixin, db.Model):
    def __init__(self) -> None:
        super().__init__()
        
        