#!/usr/bin/env python3
"""
 returns a list of all documents
 in a collection using pymongo
"""
import pymongo


def list_all(mongo_collection):
    """
    function to list all doc in a collection
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    all_posts = [post for post in documents]
    return all_posts
