#!/usr/bin/env python3
"""All students sorted by average score"""


def top_students(mongo_collection):
    """All students sorted by average score"""
    return mongo_collection.aggregate([
        {"$project": {"name": "$name",
                      "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
