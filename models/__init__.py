#!/usr/bin/python3
"""Initialization code for models package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
