#!/usr/bin/python3
"""Interview prep"""


def canUnlockAll(boxes):
    """ Unlock boxes method """
    len_boxes = len(boxes)
    keys = set()
    opened = []
    index = 0

    while index < len_boxes:
        temp = index
        opened.append(index)
        keys.update(boxes[index])
        for key in keys:
            if key != 0 and key < len_boxes and key not in opened:
                index = key
                break
        if temp == index:
            break

    for index in range(len_boxes):
        if index not in opened and index != 0:
            return False
    return True
