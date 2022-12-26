# roulette-martingale-simulator

Roulette martingale simulator is an educational GUI app that emulates roulette gambling using martingale betting system.
Simulator is configurable - user can specify starting cash, betting stake and desired result (i.e. how much money will satisfy player to leave the casino). 
Simulator can be configured to repeat the simulation chosen number of times, then aggregate stats are presented.
Once configured, app simulates roulette games until player either achieves his/her target or go broke.
Decision algorithm is as follows: 
- after winning a round player bets again with his chosen base stake
- after losing a round player doubles down (increases stake 2x)


SPOILER-ALERT: In the long run casino always wins, however if you follow this strategy with a lot of starting cash, lets say 1 mln USD, and will be happy to exit with a small win, like 1k USD, you have ~99.9% chance of winning, or put another way - one in thousand chance of losing. However, if you try to repeat it until you walk away with another million (like many 'smart' gamblers), you could as well save yourself time and just bet it all on your lucky color, because probabilities are exactly the same: ~51.35% chance that casino wins and ~48.65% chance that you win.
