# python markov chain
Single and higher order Markov chain implementation in python

## Requirements

* python 2.7
* numpy


## Usage

```
n_states = 4
seq1 = [2,1,2,0,1,1,3,2,1,2,3,2,2,1]
seq2 = [2,3,0,0,1,1,0,2,1,0,3,2,2,1]
fill=0.0001

# single order markov chain

mc = MarkovChain.MarkovChain(n_states)
print 'score seq1',mc.fit(seq1, fill)
print 'score seq2',mc.score(seq2, fill)
print 'log likelihood seq1',mc.log(seq1, fill)
print 'log likelihood seq2',mc.log(seq2, fill)

# 3rd order markov chain
mc = MarkovChain.MarkovChain(n_states, 3)
print 'score seq1',mc.fit(seq1, fill)
print 'score seq2',mc.score(seq2, fill)
print 'log likelihood seq1',mc.log(seq1, fill)
print 'log likelihood seq2',mc.log(seq2, fill)
```
