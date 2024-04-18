# Week 5 report

Time spent this week: 3h

Managed to find the problem with the minimax algorithm and fix it. Still not entirely sure why this was the problem, but changein != to is not fixed the issue. Also did some small fixes to the check_for_winner function and the player choose_move funtion. I also added a check for ties.

I added some initial evaluation in the score funtion. The minimax algorithm will now look around the move and see if there are its own pieces, empty spots, or enemy pieces, and score the postion based on those. 

I have also added a basic alpha-beta pruning to the minimax algorithm.

