"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkbayes
import thinkplot

from math import exp

"""This file contains a solution to an exercise from Think Bayes,
by Allen B. Downey

I got the idea from Tom Campbell-Ricketts author of the Maximum
Entropy blog at 

http://maximum-entropy-blog.blogspot.com

And he got the idea from E.T. Jaynes, author of the classic
_Probability Theory: The Logic of Science_.

Here's the version from Think Bayes:

Radioactive decay is well modeled by a Poisson process; the
probability that an atom decays is the same at any point in time.

Suppose that a radioactive source emits particles toward a Geiger
counter at an average rate of $r$ particles per second, but the
counter only registers a fraction, $f$, of the particles that hit it.
If $f$ is 10\% and the counter registers 15 particles in a one second
interval, what is the posterior distribution of $n$, the actual number
of particles that hit the counter, and $p$, the average rate particles
are emitted?

"""

FORMATS = ['pdf', 'eps', 'png']

class Emitter(thinkbayes.Suite):
    """Represents hypotheses about r."""

    def __init__(self, rs, f=0.1):
        """Initializes the Suite.

        rs: sequence of hypothetical emission rates
        f: fraction of particles registered
        """
        detectors = [Detector(r, f) for r in rs]
        thinkbayes.Suite.__init__(self, detectors)

    def Update(self, data):
        """Updates the Suite based on data.

        data: number of particles counted
        """
        thinkbayes.Suite.Update(self, data)
        
        for detector in self.Values():
            detector.Update()

    def Likelihood(self, data, hypo):
        """Likelihood of the data given the hypothesis.

        Args:
            data: number of particles counted
            hypo: emission rate, r

        Returns:
            probability density of the data under the hypothesis
        """
        detector = hypo
        like = detector.SuiteLikelihood(data)
        return like

    def DistOfR(self, name=''):
        """Returns the PMF of r."""
        items = [(detector.r, prob) for detector, prob in self.Items()]
        return thinkbayes.MakePmfFromItems(items, name=name)

    def DistOfN(self, name=''):
        """Returns the PMF of n."""        
        return thinkbayes.MakeMixture(self, name=name)


class Emitter2(thinkbayes.Suite):
    """Represents hypotheses about r."""

    def __init__(self, rs, f=0.1):
        """Initializes the Suite.

        rs: sequence of hypothetical emission rates
        f: fraction of particles registered
        """
        detectors = [Detector(r, f) for r in rs]
        thinkbayes.Suite.__init__(self, detectors)

    def Likelihood(self, data, hypo):
        """Likelihood of the data given the hypothesis.

        Args:
            data: number of counted per unit time
            hypo: emission rate, r

        Returns:
            probability density of the data under the hypothesis
        """
        return hypo.Update(data)

    def DistOfR(self, name=''):
        """Returns the PMF of r."""
        items = [(detector.r, prob) for detector, prob in self.Items()]
        return thinkbayes.MakePmfFromItems(items, name=name)

    def DistOfN(self, name=''):
        """Returns the PMF of n."""        
        return thinkbayes.MakeMixture(self, name=name)


class Detector(thinkbayes.Suite):
    """Represents hypotheses about n."""

    def __init__(self, r, f, high=500, step=5):
        """Initializes the suite.

        r: known emission rate, r
        f: fraction of particles registered
        high: maximum number of particles, n
        step: step size between hypothetical values of n
        """
        pmf = thinkbayes.MakePoissonPmf(r, high, step=step)
        thinkbayes.Suite.__init__(self, pmf, name=r)
        self.r = r
        self.f = f

    def Likelihood(self, data, hypo):
        """Likelihood of the data given the hypothesis.

        data: number of particles counted
        hypo: number of particles hitting the counter, n
        """
        k = data
        n = hypo
        p = self.f

        return thinkbayes.EvalBinomialPmf(k, n, p)

    def SuiteLikelihood(self, data):
        """Adds up the total probability of the data under the suite.

        data: number of particles counted
        """
        total = 0
        for hypo, prob in self.Items():
            like = self.Likelihood(data, hypo)
            total += prob * like
        return total
        

def main():
    k = 15
    f = 0.1

    # plot Detector suites for a range of hypothetical r
    thinkplot.PrePlot(num=3)
    for r in [100, 250, 400]:
        suite = Detector(r, f, step=1)
        suite.Update(k)
        thinkplot.Pmf(suite)
        print suite.MaximumLikelihood()

    thinkplot.Save(root='jaynes1',
                   xlabel='Number of particles (n)',
                   ylabel='PMF',
                   formats=FORMATS)

    # plot the posterior distributions of r and n
    hypos = range(1, 501, 5)
    suite = Emitter2(hypos, f=f)
    suite.Update(k)

    thinkplot.PrePlot(num=2)
    post_r = suite.DistOfR(name='posterior r')
    post_n = suite.DistOfN(name='posterior n')

    thinkplot.Pmf(post_r)
    thinkplot.Pmf(post_n)

    thinkplot.Save(root='jaynes2',
                   xlabel='Emission rate',
                   ylabel='PMF',
                   formats=FORMATS)


if __name__ == '__main__':
    main()
