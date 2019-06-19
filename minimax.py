# TODO: Implement the my_moves() function
# TODO: Change the value returned when the depth cutoff is
#       reached to call and return the score from my_moves()

# Use the player_id when you call "my_moves()"
# DO NOT MODIFY THE PLAYER ID
player_id = 0

def my_moves(gameState):
    # TODO: Finish this function!
    # HINT: the global player_id variable is accessible inside
    #       this function scope
    #raise NotImplementedError
    loc = gameState._player_locations[player_id]
    return len(gameState.liberties(loc))
    
def minimax_decision(gameState, depth):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    # TODO: Finish this function!
    #pass
    #return arg max a belongs to actions(s) Min-Value(result(state,a))
    max_score = float("-inf")
    max_move = None
    for a in gameState.actions():
        v = min_value(gameState.result(a), depth - 1)
        if v > max_score:
            max_score = v
            max_move = a
    return max_move

def max_value(gameState, depth):
    """ Return the game state utility if the game is over,
    otherwise return the maximum value over all legal successors
    
    # HINT: Assume that the utility is ALWAYS calculated for
            player 1, NOT for the "active" player
    """
    # TODO: finish this function!
    #pass
#    if terminalTest(state) then return utility(state)
#    v = -inf
#    for each a in actions(state) do:
#        v = max(v,min_value(result(state,a)))
#    return v
    if gameState.terminal_test():
        return gameState.utility(0)
    
    if depth <= 0:  #Check if the depth limit is reached
        return my_moves(gameState)
    
    v = float("-inf")
    for a in gameState.actions():
        v = max(v,min_value(gameState.result(a), depth - 1))
    return v

def min_value(gameState, depth):
    """ Return the game state utility if the game is over,
    otherwise return the minimum value over all legal successors
    
    # HINT: Assume that the utility is ALWAYS calculated for
            player 1, NOT for the "active" player
    """
    # TODO: finish this function!
    #pass
#    if terminalTest(state) then return utility(state)
#    v = inf
#    for each a in actions(state) do:
#            v = min(v,max_value(results(state,a)))
#    return v
    if gameState.terminal_test():
        return gameState.utility(0)
    
    if depth <= 0:  #Check if the depth limit is reached
        return my_moves(gameState)
    
    v = float("inf")
    for a in gameState.actions():
            v = min(v,max_value(gameState.result(a), depth - 1))
    return v
