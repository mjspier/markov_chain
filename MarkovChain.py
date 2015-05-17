class MarkovChain:

    """
    initialize the Markov chain
    n_states: number of states
    n_order: order of the Markov chain [default =1]
    """
    def __init__(self, n_states, n_order=1):
        self.n_order = n_order
        self.np = __import__("numpy")
        self.it = __import__("itertools")
        if n_order == 1:
            self.A = range(n_states)
        else:
            self.A = list(self.it.product(range(n_states), repeat=n_order))
        nA = len(self.A)
        self.p = self.np.zeros((nA, nA))


    """
    compute Markov chain model
    with help of a state transition array
    """
    def fit(self, states, fill=0):
        if self.n_order == 1:
            # count transitions
            for i in xrange(0,len(states)-1):
                s1 = states[i]-1
                s2 = states[i+1]-1
                self.p[s1][s2] += 1
        else:
            words = [states[i:i+self.n_order] for i in xrange(0,len(states)-self.n_order+1)]
            # count transitions
            for i in xrange(0,len(words)-1):
                s1 = self.A.index(tuple(words[i]))
                s2 = self.A.index(tuple(words[i+1]))
                self.p[s1][s2] += 1
        # normalize each row
        for i in xrange(0, self.p.shape[0]):
            row = self.p[i]
            t = row.sum()
            if t <> 0:
                self.p[i] = row/t
        return self.score(states, fill)


    """
    score which is the product of all probabilities
    """
    def score(self, states, fill=0):
        p = self.p.copy()
        p[p == 0] = fill
        prod = 1
        if self.n_order == 1:
            # sum all transition probabilities
            for i in xrange(0,len(states)-1):
                s1 = states[i]-1
                s2 = states[i+1]-1
                prod *= p[s1][s2]
            return prod
        else:
            words = [states[i:i+self.n_order] for i in xrange(0,len(states)-self.n_order+1)]
            # count transitions
            for i in xrange(0,len(words)-1):
                s1 = self.A.index(tuple(words[i]))
                s2 = self.A.index(tuple(words[i+1]))
                prod *= p[s1][s2]
            return prod

    """
    alternative score, log likelihood
    """
    def ll(self, states, fill=0):
        p = self.p.copy()
        p[p == 0] = fill
        ll = 0
        if self.n_order == 1:
            for i in xrange(0,len(states)-1):
                s1 = states[i]-1
                s2 = states[i+1]-1
                ll += self.np.log(p[s1][s2])
            return ll
        else:
            words = [states[i:i+self.n_order] for i in xrange(0,len(states)-self.n_order+1)]
            for i in xrange(0,len(words)-1):
                s1 = self.A.index(tuple(words[i]))
                s2 = self.A.index(tuple(words[i+1]))
                ll += self.np.log(p[s1][s2])
            return ll
