#!/usr/bin/env python3
"""Learn Python, Now"""


def schools_by_topic(mongo_collection,topic):
    """Find school function"""
    return mongo_collection.find({'topics': topic})
