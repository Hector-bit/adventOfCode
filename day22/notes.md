day22:
    partOne:
        pretty easy
    partTwo:
        wtf, the rules they added was just confusing,
        other than that it is still the same thing
        New rules:
            Before either player deals a card, if there was a previous round in
            this game that had exactly the same cards in the same order in the 
            same players' decks, the game instantly ends in a win for player 1.

            Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.

            If both players have at least as many cards remaining in their deck as
            the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat

            Otherwise, at least one player must not have enough cards left in 
            their deck to recurse; the wiwnner of the round is the player with
            the higher-value card.
        I hate that I did almost the same thing here as
        in the solution i found on github
        the main difference was what I returned vs what
        the solution returned.