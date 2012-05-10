class Player:
    """This is the base class for your AI.  To get started:
        1) Derive this class.  See stock.py for examples.
        2) Implement callback functions below; you must re-implement the
           ones that raise exceptions. 
         
        All player data passed to your AI is done as a data-structure, for
        example to list other players:

            for p in players:
                if p.index != self.index:
                    print p.name
        
        See the SimplePlayer in stock.py for more examples. 
    """

    def reveal(self, players, spies):
        """If you're a spy, this function will be called to list the spies,
        including others and yourself.
        @param players  List of all players in the game.
        @param spies    List of players that are spies."""
        pass

    def select(self, players, count):
        """Pick a sub-group of players to go on the next mission.
        @return list    The players selected."""
        raise NotImplemented

    def vote(self, team, leader, tries):
        """Given a selected team, decide whether the mission should proceed.
        @param team      List of players with index and .
        @param leader    Single player that chose this team.
        @param tries     Number of attemps for this vote.
        @return bool     Answer Yes/No.""" 
        raise NotImplemented

    def onVoteComplete(self, players, votes, team):
        """Callback once the whole team has voted.
        @param players      List of all the players in the game.
        @param votes        Boolean votes for each player (ordered).
        @param team         The team that was chosen for this vote."""
        pass

    def sabotage(self):
        """Decide what to do on the mission once it has been approved.
        @return bool        Yes to shoot down a mission."""
        raise NotImplemented

    def onMissionComplete(self, team, sabotaged):
        """Callback once the players have been chosen.
        @param selected     List of players that participated in the mission.
        @param sabotaged    Integer how many times the mission was sabotaged."""
        pass

    def __init__(self, name, index, spy):
        """Constructor called before a game starts.
        @param name     The public name of your bot.
        @param index    Your own index in the player list.
        @param spy      Are you supposed to play as a spy?"""
        self.name = name
        self.index = index
        self.spy = spy

    def __repr__(self):
        """Built-in function to support pretty-printing."""
        type = {True: "SPY", False: "RESISTANCE"}
        return "<%s #%i %s>" % (self.name, self.index, type[self.spy])

