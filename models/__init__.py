#!/usr/bin/python3
<<<<<<< HEAD
from models.engine.file_storage import FileStorage


storage = FileStorage()
=======
"""Initialization code for models package"""
from models.engine import file_storage


storage = file_storage.FileStorage()
>>>>>>> master
storage.reload()
