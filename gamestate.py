
# TODO: implement the __init__ class below by adding properties
# that meet the three requirements specified
rows, cols = 2, 3

class GameState:
    """
    Attributes
    ----------
    _board: list(list)
        Represent the board with a 2d array _board[x][y]
        where open spaces are 0 and closed spaces are 1
    
    _parity: bool
        Keep track of active player initiative (which
        player has control to move) where 0 indicates that
        player one has initiative and 1 indicates player 2
    
    _player_locations: list(tuple)
        Keep track of the current location of each player
        on the board where position is encoded by the
        board indices of their last move, e.g., [(0, 0), (1, 0)]
        means player 1 is at (0, 0) and player 2 is at (1, 0)
    TODO: Copy in your implementation from the previous quiz
    """
    def __init__(self):
        """The GameState class constructor performs required
        initializations when an instance is created. The class
        should:
        
        1) Keep track of which cells are open/closed
        2) Identify which player has initiative
        3) Record the current location of each player
        
        Parameters
        ----------
        self:
            instance methods automatically take "self" as an
            argument in python
        
        Returns
        -------
        None
        """
        # You can define attributes like this:
        # self.value = 73  # an arbitrary number
        # reassign it to a string (variable type is dynamic in Python)
        # self.value = "some string"
        # self.foo = []  # create an empty list
        #raise NotImplementedError
        self.board = [[0] * cols for r in range(rows)] #[0, for x in range(xlim) for y in range(ylim)]
        print([[0] * cols for r in range(rows)])
        self.board[-1][-1] = 1
        self._parity = 0
        self._player_locations = [None, None]

if __name__ == "__main__":
    # This code is only executed if "gameagent.py" is the run
    # as a script (i.e., it is not run if "gameagent.py" is
    # imported as a module)
    emptyState = GameState()  # create an instance of the object
