ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}

class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=None, votes=0, influence=0): #initial value for winning_statesvotes/influence = 0
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name = name              #get the name, votes from user's argument;
        self.votes = votes
        self.winning_states = []       #winning_states begin with an empty list; stays empty if winning_states=None;
        if winning_states is not None:  #if winning_states does not begin with None, run 'win_state' method
            for state in winning_states:
                self.win_state(state)

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        s = ''     #start with empty string box
        for state in self.winning_states:
            s += state + ' '             #gives a space in between each state in the 'winning_states' list;
        return self.name + ' wins ' + s     #return at the end, not print!

    def win_state(self, state):
        """Adds a state to winning_states and updates votes.
        state: a string of state abbreviation
        """
        self.winning_states.append(state)            #append winning states to 'winning_states' list;
        self.votes += ELECTORS.get(state)            #update the votes for winning_states from ELECTORS dict;

    def __gt__(self, other):
        """ Overloads > operator """
        if self.votes == other.votes:          #compare influence if vote is the same for each candidate;
            return self.influence > other.influence
        else:
            return self.votes > other.votes

def main():
    trump = Candidate('Donald Trump', influence = 10)
    clinton = Candidate('Hillary Clinton', winning_states=['CA'], influence = 80)
    print(trump)
    print(trump.votes)
    print(clinton)
    print(clinton.votes)
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)
    print(clinton > trump)

if __name__ == '__main__':
    main()