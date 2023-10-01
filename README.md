# ChessAi Introduction
K16 (Kyro 16) is a chess engine that uses a range of algorithms and evaluation functions to determine which move is best, and this will run at a main depth of 3. The depth increase depending on the number of pieces on the board.

# Backstory

- Some time in January 2023 | chess.com blew up in my school, Year 12. I thought I was good until I started playing it with random people online and in my school, and yes, there is much more to it than meets the eye. Hey, stockfish is pretty powerful, and I like python, I wonder how they do it...
- Days later | Hmm... the minimax algorithm is pretty cool, I'll give it a go... with number arrays.
- Sunday, ‎12 ‎February ‎2023 | First minimax demonstration, I think it went well! I zone out every time I see x amount of nodes processed on my screen.
- Monday, ‎27 ‎February ‎2023 | So I made the minimax faster somehow by only using numbers, I just did some brute force testing and its good.
- Tuesday, ‎28 ‎February ‎2023 | Okay so... I'm kind of getting sick of this minimax business with just numbers, I just realised there is a simpler method and that I've been thinking to hard to see it... and since I have only been using numbers, I have been splitting them into pairs (a non-full depth search) so its faster but not the desired output. Time to cry myself to sleep and start again...
- Wednesday, 29 February 2023 | Installed the chess module, feeling good! How does this work exactly... Ok I think I know the basics now, time for some chess.
- ‎Wednesday, ‎1 March | Chess sucks, I'm bored of it now, I have programmed too much I need a break, I just went on a rage after putting the code in the wrong order and making it self-checkmate playing the worst moves possible.
- Sunday, ‎12 ‎March ‎2023 | Created first revamp of my previous code, time to improve some functions and do stuff, I named it a.py since past me thought its a smart idea to track progress than looking at code history. I included some evaluation like piece square tables that I slapped onto my file form [https://www.chessprogramming.org/Main_Page](https://www.chessprogramming.org/Main_Page) wiki.
- Saturday, ‎25 ‎March ‎2023 | Update: Actually, I made b, c, d, e, f, g, and h.py, all look similar, my programming folder looks extra ugly now and with only minor improvements, all versions still suck, all I did was have multipliers for evaluations and change their values. Oh and alpha beta pruning was such a big breakthrough I was so happy but has since been forgotten about many versions later.
- Thursday, ‎30 ‎March ‎2023 | Final.py was never meant to be, I have since learned there is never a stop to improvement perfection is either not real or temporary in designing. However I did find out transposition tables were pretty neat with the minimax function.
- i.py and many letters later I quit for a while, I had enough, my folder was a mess, I needed a break from chess as a whole, I started some other mini python projects for temporary distractions.

# Advantages

- Opening and endgame evaluations works better, forced checkmates are usually found
- K16 Engine can play as white or black
- Opening moves are intergrated, so computing values at the start is not needed (instant openings)

# Disadvantages

- K16 only evaluates what it considers 'best moves'
- Higher depth results in longer computing time.
- Midgame evaluations are usually more complicated, and accuracy may decrease

# Additions

- Engine types: K16_1 is slower but includes more evaluations, making it (?) more accurate, K16_2 is faster (higher depth) at the cost of (?) lower accuracy

# Things I need to add
- Increase the values of piece mappings so it can decide if taking is really the best option and not doing an improving / repositional move
- calculate a supposed infinite number of takes until there is no takes left, then record the material value and add it on

# Unfamiliar with SAN Notation?
- Check out this link: https://support.chess.com/article/409-what-do-the-numbers-and-letters-like-knight-c-3-mean
