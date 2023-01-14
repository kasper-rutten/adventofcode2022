class RPS:
    """Contains methods to play Rock, Paper, Scissors
    """

    def __init__(self, matchups):
        self.matchups = matchups
        self.score = 0
        for matchup in matchups:
            self.score += self.compute_score(matchup)
        self.score2 = 0
        for matchup in matchups:
            self.score2 += self.compute_score2(matchup)

    def compute_score(self, matchup):
        """Computes score of one matchup based on standard RPS rules
            Rock, Paper, Scissors are encoded as A, B, C for player 1
            and X, Y, Z for player 2 respectively.
            Player 2 gets 1, 2, 3 bonus points
            for playing Rock, Paper, Scissors respectively
        """
        player_1 = matchup.split(' ')[0]
        player_2 = matchup.split(' ')[1]
        score = 0
        if player_2 == 'X':
            score += 1
            if player_1 == 'C':
                score += 6
            if player_1 == 'A':
                score += 3
        if player_2 == 'Y':
            score += 2
            if player_1 == 'A':
                score += 6
            if player_1 == 'B':
                score += 3
        if player_2 == 'Z':
            score += 3
            if player_1 == 'B':
                score += 6
            if player_1 == 'C':
                score += 3
        return score

    def compute_score2(self, matchup):
        """For part 2, meaning of X, Y, Z changes.
        X now encodes win, Y = draw and Z = loss
        """
        player_1 = matchup.split(' ')[0]
        player_2 = matchup.split(' ')[1]
        score = 0
        if player_2 == 'X':
            if player_1 == 'A': # other guy plays rock, we play scissors
                score += 3
            if player_1 == 'B': # other guy plays paper, we play rock
                score += 1
            if player_1 == 'C': # other guy plays scissors, we play paper
                score += 2
        
        if player_2 == 'Y':
            score += 3
            if player_1 == 'A': # we play same
                score += 1
            if player_1 == 'B':
                score += 2
            if player_1 == 'C':
                score += 3
        if player_2 == 'Z':
            score += 6
            if player_1 == 'A': # other guy plays rock, we play paper
                score += 2
            if player_1 == 'B': # other guy plays paper, we play scissors
                score += 3
            if player_1 == 'C': # other guy plays scissors, we play rock
                score += 1
        return score



with open("input.txt", "r") as input:
    matchups = input.readlines()
    matchups = [x.strip('\n') for x in matchups]
    game = RPS(matchups)
    print(game.score)
    print(game.score2)