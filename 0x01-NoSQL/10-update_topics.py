#!/usr/bin/env python3
"""Update many"""


def update_topics(mongo_collection, name, topics):
    """Update topics function"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
