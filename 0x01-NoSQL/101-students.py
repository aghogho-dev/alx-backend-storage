#!/usr/bin/env python3
"""Aggregration"""


def top_students(mongo_collection):
    """Top student"""
    return mongo_collection.aggregrate(
            [{'$project': {'name': '$name', 'averageScore': {'$avg': '$topics.score'}},
                {'$sort': {'averageScore': - 1}}
            ])
