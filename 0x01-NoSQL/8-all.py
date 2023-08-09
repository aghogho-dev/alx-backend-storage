#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """List all function"""
    docs = mongo_collection.find()
    return docs if docs else []
