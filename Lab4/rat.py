#
# CS2400 Introduction to AI
# rat.py
#
# Spring, 2020
#
# Author: Ryan Burleson
#
# Stub class for Lab 2 
# This class creates a Rat agent to be used to explore a Dungeon
# 
# Note: Instance variables with a single preceeding underscore are intended 
# to be protected, so setters and getters are included to enable this convention.
#
# Note: The -> notation in the function definition line is a type hint.  This 
# will make identifying the appropriate return type easier, but they are not 
# enforced by Python.  
#

from dungeon import Dungeon, Room, Direction
from typing import *


class Rat:
    """Represents a Rat agent in a dungeon. It enables navigation of the 
        dungeon space through searching.

    Attributes:
        dungeon (Dungeon): identifier for the dungeon to be explored
        start_location (Room): identifier for current location of the rat
    """
    def __init__(self, dungeon: Dungeon, start_location: Room):
        """ This constructor stores the references when the Rat is 
        initialized. """
        self._dungeon = dungeon
        self.start_location = start_location
        self._echo_rooms_searched = False
        self._astar_visited_nodes = []

    @property
    def dungeon(self) -> Dungeon:
        """ This function returns a reference to the dungeon.  """
        return self._dungeon

    def set_echo_rooms_searched(self) -> None:
        """ The _echo_rooms_searched variable is used as a flag for whether
        the rat should display rooms as they are visited. """
        self._echo_rooms_searched = True

    def path_to(self, target_location: Room) -> List[Room]:
        """ This function finds and returns a list of rooms from 
        start_location to target_location.  The list will include
        both the start and destination, and if there isn't a path
        the list will be empty. This function uses depth first search. """
        path = []
        self._dfs_search(self.start_location, target_location, path, set(), -1)
        return reversed(path)

    def directions_to(self, target_location: Room) -> List[str]:
        """ This function returns a list of the names of the rooms from the
        start_location to the target_location. """
        return self._directions(self.path_to(target_location))

    def _dfs_search(self, current: Room, target_location: Room, path: List[Room], table: set, max_depth: int) -> bool:
        """ Recursively searches rooms until it finds the target room. """

        # Using a Python Set to check if a room
        # has already been visited.
        if current in table:
            return False
        else:
            table.add(current)

        # Echo visiting message
        if self._echo_rooms_searched:
            print("Visiting:", current.name)

        if current == target_location:
            # Base case
            path.append(current)
            return True
        elif max_depth < 0 or max_depth > 0:
            for neighbor in current.neighbors():
                if self._dfs_search(neighbor, target_location, path, table, max_depth - 1):
                    path.append(current)
                    return True
        return False

    def bfs_directions_to(self, target_location: Room) -> List[str]:
        """ Return the list of rooms names from the rat's current location to
        the target location. Uses breadth-first search."""
        return self._directions(self.bfs_path_to(target_location))

    def bfs_path_to(self, target_location: Room) -> List[Room]:
        """ Returns the list of rooms from the start location to the
        target location, using breadth-first search to find the path."""
        return self._bfs_search(self.start_location, target_location)

    class _bfs_node:
        def __init__(self, room, previous):
            self.room = room
            self.previous = previous
    

    def _bfs_search(self, start_location: Room, target_location: Room) -> List[Room]:
        """ Breadth first search it finds the target room. """

        queue = []
        table = set()
        n = self._bfs_node(start_location, None)

        while n.room != target_location:
            if n.room not in table:
                table.add(n.room)
                if self._echo_rooms_searched:
                    print("Visiting:", n.room.name)
                for i in range(len(n.room.neighbors())):
                    neighbor = n.room.neighbors()[i]
                    queue.append(self._bfs_node(neighbor, n))
            if len(queue) > 0:
                n = queue.pop(0)
            else:
                return []

        path = []
        while n != None:
            path.append(n.room)
            n = n.previous

        return reversed(path)

    def id_directions_to(self, target_location: Room) -> List[str]:   
        """ Return the list of rooms names from the rat's current location to   
        the target location. Uses iterative deepening.""" 
        return self._directions(self.id_path_to(target_location)) 

    def id_path_to(self, target_location: Room) -> List[Room]:
        """ Returns the list of rooms from the start location to the   
        target location, using iterative deepening."""
        path = []
        i = 1
        while i < 100 and not self._dfs_search(self.start_location, target_location, path, set(), i):
            i += 1

        return reversed(path) 

    def _directions(self, path: List[Room]) -> List[str]:
        """ Converts the list of Rooms to a list of names."""
        return list(map(lambda room : room.name, path))


    def astar_direction_to(self, target_location: Room) -> List[str]:
        #todo

    def astar_path_to(self, target_location: Room) -> List[Room]:
        #todo

    def rooms_visited_by_last_search(self) -> List[str]:
        #todo
