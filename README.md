# roulette-martingale-simulator

Roulette martingale simulator is an educational GUI app that emulates roulette gambling using martingale betting system.
Simulator is configurable - user can specify starting cash, betting stake and desired result (i.e. how much money will satisfy player to leave the casino). 
Simulator can be configured to repead the simulation chosen number of times, then aggregate stats are presented.
Once configured, app simulates roulette games until player either achieves his/her target or go broke.
Decision algorithm is as follows: 
- after winning a round player bets again with his chosen base stake
- after losing a round player doubles down (increases stake 2x)
