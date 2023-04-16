#!/usr/bin/env python3
"""
Insert a document in Python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserts a document into a collection
    """
    # data returned is stored and id is returned
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
    # i also noticed returning data itself after using 
    # simple .insert instead of .insert_one, returns the id
    # this means that .insert returns an object id.
