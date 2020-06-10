# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:47:26 2020

@author: Marco Katz
"""

class Puzzle:
    
    def __init__(self,state,size=3):
        
        if len(state) != size**2:
            raise Exception("invalid length of state")
        self.state = state
        self.size = size
        self.blank_row = self.state.index("0") // self.size
        self.blank_col = self.state.index("0") % self.size
        self.state_list = list(self.state)
       

    def display(self,text):
        print(text)
        for i in range(0,self.size):
            row =""
            j = i*self.size
            for k in range(j,(j+self.size)):
                row += self.state[k]+" "
            print(row)
#        print("\n")

    def move_up(self):
        if self.blank_row == 0:
            return None
#            return Puzzle(self.state)
        else:
            self.new_state_list = list(self.state)
            zero_position = self.blank_row * self.size + self.blank_col
            dislodged_position = (self.blank_row - 1) * self.size + self.blank_col
            dislodged = self.new_state_list[dislodged_position]
            self.new_state_list[dislodged_position]="0"
            self.new_state_list[zero_position]=dislodged
            self.new_state = ''.join(str(e) for e in self.new_state_list)
            return Puzzle(self.new_state)

    def move_down(self):
        if self.blank_row == self.size-1:
            return None
#            return Puzzle(self.state)
        else:
            self.new_state_list = list(self.state)
            zero_position = self.blank_row * self.size + self.blank_col
            dislodged_position = (self.blank_row + 1) * self.size + self.blank_col
            dislodged = self.new_state_list[dislodged_position]
            self.new_state_list[dislodged_position]="0"
            self.new_state_list[zero_position]=dislodged
            self.new_state = ''.join(str(e) for e in self.new_state_list)
            return Puzzle(self.new_state)


    def move_right(self):
        if self.blank_col == self.size-1:
            return None
#            return Puzzle(self.state)
        else:
            self.new_state_list = list(self.state)
            zero_position = self.blank_row * self.size + self.blank_col
            dislodged_position = (self.blank_row) * self.size + (self.blank_col + 1)
            dislodged = self.new_state_list[dislodged_position]
            self.new_state_list[dislodged_position]="0"
            self.new_state_list[zero_position]=dislodged
            self.new_state = ''.join(str(e) for e in self.new_state_list)
            return Puzzle(self.new_state)

    def move_left(self):
        if self.blank_col == 0:
            return None
#            return Puzzle(self.state)
        else:
            self.new_state_list = list(self.state)
            zero_position = self.blank_row * self.size + self.blank_col
            dislodged_position = (self.blank_row) * self.size + (self.blank_col - 1)
            dislodged = self.new_state_list[dislodged_position]
            self.new_state_list[dislodged_position]="0"
            self.new_state_list[zero_position]=dislodged
            self.new_state = ''.join(str(e) for e in self.new_state_list)
            return Puzzle(self.new_state)
    
    def find_value(self,goal):
        value = 0
        for i in range(0,self.size):
            state_index = self.state_list.index(i)
            goal_index = goal.state_index.index(i)
            value += abs(state_index - goal_index)
        return value
    

    def seek_for_neighbors(self,search_order = "UDLR"):
        standard_path = {"U": "Up","D": "Down","L": "Left","R": "Right"}
        neighbors = []
        path = [] 
        for i,direction in enumerate(search_order):
            if direction == "U":
                nb = self.move_up()
            elif direction == "D":
                nb = self.move_down()
            elif direction == "L":
                nb = self.move_left()
            elif direction == "R":
                nb = self.move_right()
            else:
                nb = None
            if nb != None:
                neighbors.append(nb)
                path.append(standard_path[direction])
        return neighbors, path

    def seek_for_neighbor_states(self,search_order = "UDLR"):
        standard_path = {"U": "Up","D": "Down","L": "Left","R": "Right"}
        neighbors = []
        path = [] 
        for i,direction in enumerate(search_order):
            if direction == "U":
                nb = self.move_up()
            elif direction == "D":
                nb = self.move_down()
            elif direction == "L":
                nb = self.move_left()
            elif direction == "R":
                nb = self.move_right()
            else:
                nb = None
            if nb != None:
                neighbors.append(nb.state)
                path.append(standard_path[direction])
        return neighbors, path


class FastQ:
    
    def __init__(self,type):
        self.type=type 
        if self.type == "queue":
             self.q = deque()
        elif self.type =="stack":
             self.q = []
        elif self.type =="heap":
             self.q = []
        else:
             raise Exception("Invalid FastQ")
        self.set = set()

    def qadd(self,state,value):
#note that value is irrelevant if not heap
        if self.type == "queue" or self.type == "stack":
            self.q.append(state)
        elif self.type =="heap":
            heapq.heappush(self.q,(value,state))
        else:
            raise Exception("Invalid FastQ")        
        self.set.add(state)
        
    def qdrop(self):
        if self.type == "queue":
            state=self.q.popleft()
        elif self.type =="stack":
            state=self.q.pop()
        elif self.type == "heap":
            value, state = heapq.heappop(self.q)
        else:
            raise Exception("Invalid FastQ")        
        self.set.remove(state)
        return state
        
    def qlen(self):
        return len(self.q)
        
    def qsearch(self,value):
        if value in self.set:
            return True
        else:
            return False

    def qreplace(self,source_state,target_value):
        result = []
        for (value, state) in self.q:
            if state == source_state:
                heapq.heappush(result,(target_value,state))
            else:
                heapq.heappush(result,(value,state))
        return result


    def qprint(self,text,double=False):
        print("{} {} {}".format(text,self.type,self.q))
        if double:
            print ("{} Set {}".format(text,self.set))
"""
        if self.type == "queue":
            print("{} Queue {}".format(text,self.q))
        elif self.type == "stack":
            print("{} Stack {}".format(text,self.q))
        else:
             raise Exception("Invalid FastQ")        
"""


def bfs_search(initial,goal_test,max_test,debug=False):

    start_time=time.time()
    if debug:
        max_trial = 10
    else:
        max_trial = max_test
    
    initial.display("bfs_search: Initial")
    goal_test.display("Goal")
    print("\n")


    search_frontier = FastQ("queue")
    search_frontier.qadd(initial.state,0)
    search_explored = FastQ("stack")

    path_to_goal =[]
    bfs_result = {"success": False, "visited": [], "nodes": 0, "cost": 0, "duplicates": 0, "breadth": 0, "search_time": 50000.0}

    max_breadth = 0
    count_duplicates = 0
    puzzle_count = 0
    node_opened_count = 0

    
    while not search_frontier.qlen() == 0 and puzzle_count < max_trial:
        
        puzzle_state = search_frontier.qdrop()
        puzzle_current = Puzzle(puzzle_state)
        if debug:
            puzzle_current.display("Current")
            print("Current state {}".format(puzzle_state))
        search_explored.qadd(puzzle_state,0)

        
        puzzle_count += 1
        if debug and puzzle_count % 1000 == 0:
            print(puzzle_count)
            
        if puzzle_state == goal_test.state:
            puzzle_current.display("Solution")
            bfs_result["success"] = True
            bfs_result["visited"] = puzzle_count
            bfs_result["nodes"] = node_opened_count
            bfs_result["cost"] = len(path_to_goal)
            bfs_result["duplicates"] = count_duplicates
            bfs_result["breadth"] = max_breadth
            bfs_result["search_time"] = time.time()-start_time
            return bfs_result

        else:
            duplicates=[]
            neighbor_states, path = puzzle_current.seek_for_neighbor_states()
            node_opened_count +=1
            if len(neighbor_states) > max_breadth:
                max_breadth = len(neighbor_states)
            if debug:
                search_frontier.qprint("Tested Frontier",True)
                search_explored.qprint("Tested Explored",True)
                print("Neighbor states {}".format(neighbor_states))
            for i, neighbor_state in enumerate(neighbor_states):
                if not search_frontier.qsearch(neighbor_state):
                    if not search_explored.qsearch(neighbor_state):
                        path_to_goal.append(path[i])
                        search_frontier.qadd(neighbor_state,0)
                    else:
                        count_duplicates += 1
                        duplicates.append(neighbor_state)
                else:
                    count_duplicates += 1
                    duplicates.append(neighbor_state)

            if debug:
                print("Duplicates {} ".format(duplicates))           
                print("\n")


    search_frontier.qprint("Final search frontier",True)
    bfs_result["success"] = False
    bfs_result["visited"] = puzzle_count
    bfs_result["nodes"] = node_opened_count
    bfs_result["cost"] = len(path_to_goal)
    bfs_result["duplicates"] = count_duplicates
    bfs_result["breadth"] = max_breadth
    bfs_result["search_time"] = time.time()-start_time
    return bfs_result


def dfs_search(initial,goal_test,max_test,debug=False):

    start_time=time.time()
    if debug:
        max_trial = 10
    else:
        max_trial = max_test

    initial.display("dfs_search: Initial")
    goal_test.display("Goal")
    print("\n")


    search_frontier = FastQ("stack")
    search_frontier.qadd(initial.state,0)
    search_explored = FastQ("stack")

    path_to_goal =[]
    dfs_result = {"success": False, "visited": [], "nodes": 0, "cost": 0, "duplicates": 0, "breadth": 0, "search_time": 50000.0}

    max_breadth = 0
    count_duplicates = 0
    puzzle_count = 0
    node_opened_count = 0

    
    while not search_frontier.qlen() == 0 and puzzle_count < max_trial:
        
        puzzle_state = search_frontier.qdrop()
        puzzle_current = Puzzle(puzzle_state)
        if debug:
            puzzle_current.display("Current")
            print("Current state {}".format(puzzle_state))
        search_explored.qadd(puzzle_state,0)

        
        puzzle_count += 1
        if debug and puzzle_count % 1000 == 0:
            print(puzzle_count)
            
        if puzzle_state == goal_test.state:
            puzzle_current.display("Solution")
            dfs_result["success"] = True
            dfs_result["visited"] = puzzle_count
            dfs_result["nodes"] = node_opened_count
            dfs_result["cost"] = len(path_to_goal)
            dfs_result["duplicates"] = count_duplicates
            dfs_result["breadth"] = max_breadth
            dfs_result["search_time"] = time.time()-start_time
            return dfs_result

        else:
            duplicates=[]
            neighbor_states, path = puzzle_current.seek_for_neighbor_states("RLDU")
            node_opened_count +=1
            if len(neighbor_states) > max_breadth:
                max_breadth = len(neighbor_states)
            if debug:
                search_frontier.qprint("Tested Frontier",True)
                search_explored.qprint("Tested Explored",True)
                print("Neighbor states {}".format(neighbor_states))
            for i, neighbor_state in enumerate(neighbor_states):
                if not search_frontier.qsearch(neighbor_state):
                    if not search_explored.qsearch(neighbor_state):
                        path_to_goal.append(path[i])
                        search_frontier.qadd(neighbor_state,0)
                    else:
                        count_duplicates += 1
                        duplicates.append(neighbor_state)
                else:
                    count_duplicates += 1
                    duplicates.append(neighbor_state)

            if debug:
                print("Duplicates {} ".format(duplicates))           
                print("\n")


    if debug:
        search_frontier.qprint("Final search frontier",True)
    dfs_result["success"] = False
    dfs_result["visited"] = puzzle_count
    dfs_result["nodes"] = node_opened_count
    dfs_result["cost"] = len(path_to_goal)
    dfs_result["duplicates"] = count_duplicates
    dfs_result["breadth"] = max_breadth
    dfs_result["search_time"] = time.time()-start_time
    return dfs_result

def astar_search(initial,goal_test,max_test,debug=False):

    start_time=time.time()
    if debug:
        max_trial = 10
    else:
        max_trial = max_test

    initial.display("astar_search: Initial")
    goal_test.display("Goal")
    print("\n")


    search_frontier = FastQ("heap")
    search_frontier.qadd(initial.state,initial.findvalue(goal_test))
    search_explored = FastQ("stack")

    path_to_goal =[]
    astar_result = {"success": False, "visited": [], "nodes": 0, "cost": 0, "duplicates": 0, "breadth": 0, "search_time": 50000.0}

    max_breadth = 0
    count_duplicates = 0
    puzzle_count = 0
    node_opened_count = 0

    
    while not search_frontier.qlen() == 0 and puzzle_count < max_trial:
        
        puzzle_state = search_frontier.qdrop()
        puzzle_current = Puzzle(puzzle_state)
        if debug:
            puzzle_current.display("Current")
            print("Current state {}".format(puzzle_state))
        search_explored.qadd(puzzle_state,0)

        
        puzzle_count += 1
        if debug and puzzle_count % 1000 == 0:
            print(puzzle_count)
            
        if puzzle_state == goal_test.state:
            puzzle_current.display("Solution")
            astar_result["success"] = True
            astar_result["visited"] = puzzle_count
            astar_result["nodes"] = node_opened_count
            astar_result["cost"] = len(path_to_goal)
            astar_result["duplicates"] = count_duplicates
            astar_result["breadth"] = max_breadth
            astar_result["search_time"] = time.time()-start_time
            return astar_result

        else:
            duplicates=[]
            neighbor_states, path = puzzle_current.seek_for_neighbor_states("UDLR")
            node_opened_count +=1
            if len(neighbor_states) > max_breadth:
                max_breadth = len(neighbor_states)
            if debug:
                search_frontier.qprint("Tested Frontier",True)
                search_explored.qprint("Tested Explored",True)
                print("Neighbor states {}".format(neighbor_states))
            for i, neighbor_state in enumerate(neighbor_states):
                neighbor=Puzzle(neighbor_state)
                neighbor_value=neighbor.findvalue(goal_test)
                if not search_frontier.qsearch(neighbor_state):
                    if not search_explored.qsearch(neighbor_state):
                        path_to_goal.append(path[i])
                        search_frontier.qadd(neighbor_state,neighbor_value)
                    else:
                        count_duplicates += 1
                        duplicates.append(neighbor_state)
                else:
                    count_duplicates += 1
                    duplicates.append(neighbor_state)
                    search_frontier.qreplace(neighbor_state,neighbor_value)

            if debug:
                print("Duplicates {} ".format(duplicates))           
                print("\n")


    if debug:
        search_frontier.qprint("Final search frontier",True)
    astar_result["success"] = False
    astar_result["visited"] = puzzle_count
    astar_result["nodes"] = node_opened_count
    astar_result["cost"] = len(path_to_goal)
    astar_result["duplicates"] = count_duplicates
    astar_result["breadth"] = max_breadth
    astar_result["search_time"] = time.time()-start_time
    return astar_result

from collections import deque
import time
import heapq

max_trials = 200000


def display_search_results(search_name,search_result):
    sr = search_result
    print("{} search with search time {}".format(search_name,sr["search_time"]))
    if sr["success"]:
        print("I found the answer after {} steps, {} nodes opened, {} moves, {} duplicates dropped, breadth is {}".format(sr["visited"],sr["nodes"],sr["cost"],sr["duplicates"],sr["breadth"]))
    else:
        print("I failed to find the answer despite {} steps, {} nodes opened, {} moves, {} duplicates dropped,  breadth is {}".format(sr["visited"],sr["nodes"],sr["cost"],sr["duplicates"],sr["breadth"]))
    print("\n============================================================================== \n")



start = Puzzle("125468037")
goal = Puzzle("012345678")

bfs_out = bfs_search(start,goal,max_trials,False)
display_search_results("bfs",bfs_out)


dfs_out = dfs_search(start,goal,max_trials,False)
display_search_results("dfs",dfs_out)

#astar_out = astar_search(start,goal,max_trials,True)
#display_search_results("astar",astar_out)