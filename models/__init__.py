#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage

#importing FileStorage class from file_storage.py
storage = FileStorage()
storage.reload()
