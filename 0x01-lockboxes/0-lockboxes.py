#!/usr/bin/python3
"""Solves the lock boxes puzzle"""

def get_next_open_box(open_boxes):
    """Gets the next opened box with keys
    Args:
        open_boxes (dict): Dictionary of opened boxes
    Returns:
        list: List of keys in the next opened box, or None if no opened boxes
    """
    for box in open_boxes.values():
        if box['status'] == 'opened':
            box['status'] = 'checked'
            return box['keys']
    return None

def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked
    Args:
        boxes (list): List of boxes with keys
    Returns:
        bool: True if all boxes can be unlocked, False otherwise
    """
    if not boxes or boxes == [[]]:
        return True

    open_boxes = {0: {'status': 'opened', 'keys': boxes[0]}}
    while True:
        keys = get_next_open_box(open_boxes)
        if keys:
            for key in keys:
                if key not in open_boxes:
                    if key < len(boxes):
                        open_boxes[key] = {'status': 'opened', 'keys': boxes[key]}
        elif any(box['status'] == 'opened' for box in open_boxes.values()):
            continue
        else:
            return len(open_boxes) == len(boxes)

def main():
    """Main entry point"""
    canUnlockAll([[]])

if __name__ == '__main__':
    main()

