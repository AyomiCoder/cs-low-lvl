# implement disk scheduling algorithms

from collections import deque
from enum import Enum
from typing import List, Tuple

class Direction(Enum):
    LEFT = 0
    RIGHT = 1

def fcfs(sequence: List[int], head: int) -> Tuple[int, List[int]]:
    total_head_movement = 0
    movement_sequence = []
    current_head = head

    for track in sequence:
        total_head_movement += abs(current_head - track)
        movement_sequence.append(track)
        current_head = track

    return total_head_movement, movement_sequence

def sstf(sequence: List[int], head: int) -> Tuple[int, List[int]]:
    total_head_movement = 0
    movement_sequence = []
    current_head = head
    sequence = deque(sorted(sequence, key=lambda x: abs(x - current_head)))

    while sequence:
        track = sequence.popleft()
        total_head_movement += abs(current_head - track)
        movement_sequence.append(track)
        current_head = track

    return total_head_movement, movement_sequence

def scan(sequence: List[int], head: int, direction: Direction) -> Tuple[int, List[int]]:
    total_head_movement = 0
    movement_sequence = []
    current_head = head
    sequence = sorted(sequence)

    if direction == Direction.LEFT:
        left_sequence = [track for track in sequence if track < head]
        right_sequence = [track for track in sequence if track >= head]
    else:
        left_sequence = [track for track in sequence if track <= head]
        right_sequence = [track for track in sequence if track > head]

    left_sequence.reverse()
    sequence = left_sequence + right_sequence

    for track in sequence:
        total_head_movement += abs(current_head - track)
        movement_sequence.append(track)
        current_head = track

    return total_head_movement, movement_sequence

def cscan(sequence: List[int], head: int, direction: Direction) -> Tuple[int, List[int]]:
    total_head_movement = 0
    movement_sequence = []
    current_head = head
    sequence = sorted(sequence)

    if direction == Direction.LEFT:
        left_sequence = [track for track in sequence if track < head]
        right_sequence = [track for track in sequence if track >= head]
    else:
        left_sequence = [track for track in sequence if track <= head]
        right_sequence = [track for track in sequence if track > head]

    left_sequence.reverse()
    sequence = left_sequence + right_sequence

    for track in sequence:
        total_head_movement += abs(current_head - track)
        movement_sequence.append(track)
        current_head = track

    return total_head_movement, movement_sequence

def look(sequence: List[int], head: int, direction: Direction) -> Tuple[int, List[int]]:
    total_head_movement = 0
    movement_sequence = []
    current_head = head
    sequence = sorted(sequence)

    if direction == Direction.LEFT:
        left_sequence = [track for track in sequence if track < head]
        right_sequence = [track for track in sequence if track > head]
    else:
        left_sequence = [track for track in sequence if track <= head]
        right_sequence = [track for track in sequence if track >= head]

    left_sequence.reverse()
    sequence = left_sequence + right_sequence

    for track in sequence:
        total_head_movement += abs(current_head - track)
        movement_sequence.append(track)
        current_head = track

    return total_head_movement, movement_sequence