#!/usr/bin/env python3
"""
Insert a document in Python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserts a document into a collection
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
