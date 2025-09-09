'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # We have a dictionary that we want to check if our users are indeed friends or not.
    
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Create a list.
    from_follows = social_graph.get (from_member, {}) .get ('following', []) # LtoR, if the user exists in that dictionary, get their following.
    to_follows = social_graph.get (to_member, {}) .get ('following', [])   
    # Is y and x in the list?
    does_from_follow = to_member in from_follows
    does_to_follow = from_member in to_follows
    # Conditionals
    if does_from_follow and does_to_follow:
        return 'friends'
    elif does_from_follow:
        return 'follower'
    elif does_to_follow:
        return 'followed by'
    else:
        return 'no relationship'

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # A straight line across a grid is a winner.
    # To check for a win, you need to examine all possible winning lines: three rows, three columns, and two diagonals.
    # The board is always a square (nxn)
    n = len (board) # Output of len (board1): 3
    # Rows
    for row in range (n):
        first = board [row][0] # Fixed row, varying column from 0
        if first and all (board [row][col] == first for col in range(n)): # 'and' ensures if no value, will not return
            return first
    # Note: Process of this for loop
    # Pick row. 
    # Use its first cell as symbol to check.
    # 'and' conditional if both are valid
    # all (board [row][col] == first for col in range(n)) to check *every* column in that row equals defined first.
    # loop for each row
    # if both true, return first symbol.

    # Column
    for col in range (n):
        first = board [0][col] # Fixed column, varying row from 0
        if first and all (board [row][col] == first for row in range(n)):
            return first
    # Pick column.
    # Use its first cell as symbol to check.
    # 'and' conditional if both are valid
    # all (board [row][col] == first for row in range(n)) to check every row in that column equals defined first.
    # loop for each column
    # if both true, return first symbol.

    #TR to BL
    first = board [0][n-1] # Both varying from 0
    if first and all(board[d][n-1-d] == first for d in range (n)):
        return first
    # BL as symbol to check.
    # Start Row 1, Last Column.
    # Decrease by pattern of n-1-d

    #TL to BR
    first = board [0][0] # Both varying from 0
    if first and all(board[d][d] == first for d in range (n)):
        return first
    # TL as symbol to check.
    # Both go up by 1. L to R, T to B.

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # cyclical route_map
    # dictionary use
    # first_stop as departure
    # second_stop as where to arrive
    # given tuples (an immutable order of elements, *important for routes)
    # should return time in minutes it will take to travel
    # logic of code: if i get to one stop, where is my next stop? 
    new_map = {} 
    for (start, end), leg_time in route_map.items(): # seperates key from value | .items gives each key and value.
        minutes = leg_time ['travel_time_mins'] # from 'travel_time_mins': 10 to only int 10

        new_map [start] = (end, minutes) # new dictionary by adding key, value (tuple) pair

    if first_stop == second_stop: # if one full loop case
        total_mins = 0 
        current_stop = first_stop

        for _ in range (len(next_map)): # len returns number of key-value pairs unlike a string
            next_stop, leg_time = new_map [current_stop] # unpack tuple value from current stop into next_stop, and leg_data
            total_mins = total_mins + leg_time
            current_stop = next_stop # advance to next stop until loop

            if current_stop == first_stop:
                return total_minutes

    total_mins = 0
    current_stop = first_stop

    for _ in range (len(new_map)): # loop until hit next stop
        next_stop, leg_time = new_map [current_stop] # unpack tuple value from current stop into next_stop, and leg_data
        total_mins = total_mins + leg_time # add time took for each iteration

        if next_stop == second_stop:
            return total_mins # advance to next stop until hit
        current_stop = next_stop
