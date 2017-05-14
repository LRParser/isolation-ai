# Research Review

This is a summary of the paper "Deep Blue" by the IBM Watson Team. 

## Goals and Techniques Introduced

The paper begins by giving background on the CMU-based DeepThought system, which could evaluate 500,000-700,000 chess positions per second in the late-1980s. It describes the effort to evolve this system to "Deep Blue I" and then "Deep Blue II", the latter of which eventually beat Chess Grandmaster Gary Kasparov in a six-game match.

Deep Blue I introduced a number of additional features for scoring, such as "bishops of opposite color", which was not (due to memory limitations) available in DeepThought. Although Deep Blue I beat a number of chess grandmasters, the approx. 6,000 features it evaluated in its scoring function were thought to be insufficient, and a reason for its initial 2-4 loss to Kasparov in 1996. This was increased to 8,000 evaluated features in Deep Blue II, which further due to hardware improvements "increased the per chip search speed to 2-2.5 million positions per second".

The authors note that most of the work in Deep Blue II was spent "designing, testing, and tuning the new evaluation function".

## Summary of Paper's Results

The paper notes that search strategy and evaluation function refinement were critical to the victory of Deep Blue II. Techniques used included: 
> quiescence search, iterative deepening, transposition tables...and NegaScout

Additionally important were hardware improvements. The authors credit hardware as a major factor, referencing:
> Massively parallel search...with over 500 processors available to participate in the game tree search.

Further a large amount of chess domain knowledge appears to be embedded in the features chosen for the evaluation function. The authors specifically reference:
> computing values for chess concepts such as square control,
pins, X-rays, king safety, pawn structure, passed pawns, ray control, outposts, pawn majority, rook on the 7th, blockade, restraint, color complex, trapped pieces, development

Domain knowledge was further embedded in Deep Blue II via the inclusion of known good opening moves:
> The book consisted of about 4000 positions, 19 and every position had been checked by Deep Blue in overnight runs.

The authors concluded by noting that each of the above factors (adverserial search techniques, hardware improvements, and reference move databases) played a role in the victory of Deep Blue II over Kasparov in 1997:

>The success of Deep Blue in the 1997 match was not the result of any one factor. The
large searching capability, non-uniform search, and complex evaluation function were all
critical. However other factors also played a role, e.g., endgame databases, the extended
book, and evaluation function tuning.