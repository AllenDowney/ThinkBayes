>>> G=BayesNet()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'BayesNet' is not defined
>>> G=BayesNet()
>>> ebunch=[('a', 'b', '+'), ('a', 'c', '+'), ('b', 'c', '-')]
>>> add_edges_from(G, ebunch)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'add_edges_from' is not defined
>>> G.add_edges_from(ebunch)
>>> G.Items()
[((0, 1, 1), 0.0), ((1, 1, 0), 0.125), ((1, 0, 0), 0.0625), ((0, 0, 1), 0.25), ((1, 0, 1), 0.1875), ((0, 0, 0), 0.25), ((0, 1, 0), 0.0), ((1, 1, 1), 0.125)]
>>> 0.5**3
0.125
>>> f=lambda x, a, b: 1.0/(b-a)
>>> f(0.5, 0, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() takes exactly 1 argument (3 given)
>>> f=lambda x, a, b: 1.0/(b-a)
>>> f(0.5, 0, 1)
1.0
>>> pmf=Pmf()
>>> [pmf.Set(x, f(x, 0, 1)) for x in numpy.linspace(0, 1, 100)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'linespace' is not defined
>>> [pmf.Set(x, f(x, 0, 1)) for x in numpy.linspace(0, 1, 100)]
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> pmf.Items()[:10]
sorted(pmf.Items()[:10])
[(0.0, 1.0), (1.0, 1.0), (0.29292929292929293, 1.0), (0.6262626262626263, 1.0), (0.23232323232323235, 1.0), (0.58585858585858586, 1.0), (0.80808080808080818, 1.0), (0.17171717171717174, 1.0), (0.8787878787878789, 1.0), (0.27272727272727276, 1.0)]
>>> sorted(pmf.Items())
[(0.0, 1.0), (0.17171717171717174, 1.0), (0.23232323232323235, 1.0), (0.27272727272727276, 1.0), (0.29292929292929293, 1.0), (0.58585858585858586, 1.0), (0.6262626262626263, 1.0), (0.80808080808080818, 1.0), (0.8787878787878789, 1.0), (1.0, 1.0)]
>>> sorted(pmf.Items())
[(0.0, 1.0), (0.010101010101010102, 1.0), (0.020202020202020204, 1.0), (0.030303030303030304, 1.0), (0.040404040404040407, 1.0), (0.050505050505050511, 1.0), (0.060606060606060608, 1.0), (0.070707070707070718, 1.0), (0.080808080808080815, 1.0), (0.090909090909090912, 1.0), (0.10101010101010102, 1.0), (0.11111111111111112, 1.0), (0.12121212121212122, 1.0), (0.13131313131313133, 1.0), (0.14141414141414144, 1.0), (0.15151515151515152, 1.0), (0.16161616161616163, 1.0), (0.17171717171717174, 1.0), (0.18181818181818182, 1.0), (0.19191919191919193, 1.0), (0.20202020202020204, 1.0), (0.21212121212121213, 1.0), (0.22222222222222224, 1.0), (0.23232323232323235, 1.0), (0.24242424242424243, 1.0), (0.25252525252525254, 1.0), (0.26262626262626265, 1.0), (0.27272727272727276, 1.0), (0.28282828282828287, 1.0), (0.29292929292929293, 1.0), (0.30303030303030304, 1.0), (0.31313131313131315, 1.0), (0.32323232323232326, 1.0), (0.33333333333333337, 1.0), (0.34343434343434348, 1.0), (0.35353535353535359, 1.0), (0.36363636363636365, 1.0), (0.37373737373737376, 1.0), (0.38383838383838387, 1.0), (0.39393939393939398, 1.0), (0.40404040404040409, 1.0), (0.4141414141414142, 1.0), (0.42424242424242425, 1.0), (0.43434343434343436, 1.0), (0.44444444444444448, 1.0), (0.45454545454545459, 1.0), (0.4646464646464647, 1.0), (0.47474747474747481, 1.0), (0.48484848484848486, 1.0), (0.49494949494949497, 1.0), (0.50505050505050508, 1.0), (0.51515151515151525, 1.0), (0.5252525252525253, 1.0), (0.53535353535353536, 1.0), (0.54545454545454553, 1.0), (0.55555555555555558, 1.0), (0.56565656565656575, 1.0), (0.5757575757575758, 1.0), (0.58585858585858586, 1.0), (0.59595959595959602, 1.0), (0.60606060606060608, 1.0), (0.61616161616161624, 1.0), (0.6262626262626263, 1.0), (0.63636363636363646, 1.0), (0.64646464646464652, 1.0), (0.65656565656565657, 1.0), (0.66666666666666674, 1.0), (0.6767676767676768, 1.0), (0.68686868686868696, 1.0), (0.69696969696969702, 1.0), (0.70707070707070718, 1.0), (0.71717171717171724, 1.0), (0.72727272727272729, 1.0), (0.73737373737373746, 1.0), (0.74747474747474751, 1.0), (0.75757575757575768, 1.0), (0.76767676767676774, 1.0), (0.77777777777777779, 1.0), (0.78787878787878796, 1.0), (0.79797979797979801, 1.0), (0.80808080808080818, 1.0), (0.81818181818181823, 1.0), (0.8282828282828284, 1.0), (0.83838383838383845, 1.0), (0.84848484848484851, 1.0), (0.85858585858585867, 1.0), (0.86868686868686873, 1.0), (0.8787878787878789, 1.0), (0.88888888888888895, 1.0), (0.89898989898989912, 1.0), (0.90909090909090917, 1.0), (0.91919191919191923, 1.0), (0.92929292929292939, 1.0), (0.93939393939393945, 1.0), (0.94949494949494961, 1.0), (0.95959595959595967, 1.0), (0.96969696969696972, 1.0), (0.97979797979797989, 1.0), (0.98989898989898994, 1.0), (1.0, 1.0)]
>>> G.nodes()
[0, 1, 2]
>>> G.Conditional(2, 0, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Conditional() takes at least 4 arguments (3 given)
>>> G.Conditional(2, 0, 1).Items()
<__main__.Pmf object at 0x2e090d0>
>>> G.Conditional(2, 0, 0).Items()
[(0, 0.375), (1, 0.625)]
>>> G.Conditional(2, 1, 0).Items()
[(0, 0.5), (1, 0.5)]
>>> G.Conditional(2, 1, 1).Items()
[(0, 0.41666666666666663), (1, 0.5833333333333333)]
>>> G.Conditional(2, 1, 1).Items()
[(0, 0.5), (1, 0.5)]
>>> Percentile(G, 6)
(1, 1, 0)
>>> Percentile(G, 7)
(1, 1, 0)
>>> Percentile(G, 8)
(1, 1, 0)
>>> Percentile(G, 9)
(1, 1, 0)
>>> Percentile(G, 10)
(1, 1, 0)
>>> Percentile(G, 11)
(1, 1, 0)
>>> Percentile(G, 12)
(1, 1, 0)
>>> Percentile(G, 13)
(1, 1, 0)
>>> Percentile(G, 13)
(1, 0, 0)
>>> G.P((1, 1, 0))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'BayesNet' object has no attribute 'Probability'
>>> G.Prob((1, 1, 0))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'BayesNet' object has no attribute 'P'
>>> G.Prob((1, 0, 0))
0.125
>>> G.Prob((0, 0, 0))
0.0625
>>> G.Prob((0, 1, 0))
0.25
>>> G.Prob((1, 1, 0))
0.0
>>> G.Prob((1, 1, 1))
0.125
>>> G.Prob((1, 0, 1))
0.125
>>> G.Prob((1, 0, 1))
0.1875
>>> gaus=lambda x: EvalGaussianPdf(x, 0, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'GausianPdf' is not defined
>>> gaus=lambda x: EvalGaussianPdf(x, 0, 1)
>>> gaus(1)
0.00013383022576488537
>>> gaus(1.96)
0.24197072451914337
>>> gaus(-1.96)
0.058440944333451476
>>> gaus(-1.96)
0.058440944333451476
>>> type(gaus)
<type 'function'>
>>> xs=numpy.linspace(-2, 2, 0.5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: integer argument expected, got float
>>> xs=numpy.linspace(-2, 2, 20)
>>> xs
array([], dtype=float64)
>>> xs=numpy.linspace(-2, 2, 20)
>>> zip(*list(xs), [gaus(x) for x in xs])
array([-2.        , -1.78947368, -1.57894737, -1.36842105, -1.15789474,
       -0.94736842, -0.73684211, -0.52631579, -0.31578947, -0.10526316,
        0.10526316,  0.31578947,  0.52631579,  0.73684211,  0.94736842,
        1.15789474,  1.36842105,  1.57894737,  1.78947368,  2.        ])
>>> zip(*xs, gauss)
  File "<stdin>", line 1
SyntaxError: only named arguments may follow *expression
>>> xs=list(xs)
>>> gauss=[gaus(x) for x in xs]
>>> zip(*xs, gauss)
  File "<stdin>", line 1
SyntaxError: only named arguments may follow *expression
>>> from pylab import *
>>> plot(xs, gauss)
[<matplotlib.lines.Line2D object at 0x3b5b4d0>]
>>> pylab.show()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pylab' is not defined
>>> show()
>>> show()
>>> plot(xs, gauss)
[<matplotlib.lines.Line2D object at 0x3df9e10>]
>>> show()
>>> gaus(5)
0.00013383022576488537
>>> gaus(0)
1.4867195147342979e-06
>>> gaus(1)
0.3989422804014327
>>> gaus(1)
0.24197072451914337
>>> pmf=MakeUniformPmf(0, 1, 100)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/tmp/py28474dFK", line 775, in MakeUniformPmf
  File "/tmp/py28474dFK", line 414, in Normalize
TypeError: unsupported operand type(s) for /: 'float' and 'dictionary-valueiterator'
>>> pmf=MakeUniformPmf(0, 1, 100)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/tmp/py28474dFK", line 775, in MakeUniformPmf
  File "/tmp/py28474dFK", line 414, in Normalize
TypeError: unsupported operand type(s) for /: 'float' and 'dictionary-valueiterator'
>>> pmf.d[0]
1.0
>>> pmf.Normalize()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/tmp/py28474dFK", line 414, in Normalize
TypeError: unsupported operand type(s) for /: 'float' and 'dictionary-valueiterator'
>>> pmf.Total()
<dictionary-valueiterator object at 0x3debd08>
>>> sum(x for x in pmf.d.itervalues())
<dictionary-valueiterator object at 0x3debcb0>
>>> sum(x for x in pmf.d.itervalues())
100.0
>>> pmf=MakeUniformPmf(0, 1, 100)
>>> pmf.d[1]
0.01
>>> pmf.d[0.1]
0.01
>>> pmf.d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0.1
>>> pmf.Items()
{0.0: 0.01, 1.0: 0.01, 0.29292929292929293: 0.01, 0.6262626262626263: 0.01, 0.23232323232323235: 0.01, 0.58585858585858586: 0.01, 0.80808080808080818: 0.01, 0.17171717171717174: 0.01, 0.8787878787878789: 0.01, 0.27272727272727276: 0.01, 0.96969696969696972: 0.01, 0.85858585858585867: 0.01, 0.28282828282828287: 0.01, 0.50505050505050508: 0.01, 0.61616161616161624: 0.01, 0.78787878787878796: 0.01, 0.95959595959595967: 0.01, 0.75757575757575768: 0.01, 0.54545454545454553: 0.01, 0.68686868686868696: 0.01, 0.71717171717171724: 0.01, 0.090909090909090912: 0.01, 0.44444444444444448: 0.01, 0.010101010101010102: 0.01, 0.060606060606060608: 0.01, 0.81818181818181823: 0.01, 0.40404040404040409: 0.01, 0.49494949494949497: 0.01, 0.4646464646464647: 0.01, 0.5757575757575758: 0.01, 0.37373737373737376: 0.01, 0.11111111111111112: 0.01, 0.91919191919191923: 0.01, 0.92929292929292939: 0.01, 0.25252525252525254: 0.01, 0.42424242424242425: 0.01, 0.51515151515151525: 0.01, 0.6767676767676768: 0.01, 0.56565656565656575: 0.01, 0.050505050505050511: 0.01, 0.84848484848484851: 0.01, 0.76767676767676774: 0.01, 0.30303030303030304: 0.01, 0.32323232323232326: 0.01, 0.77777777777777779: 0.01, 0.72727272727272729: 0.01, 0.15151515151515152: 0.01, 0.47474747474747481: 0.01, 0.53535353535353536: 0.01, 0.34343434343434348: 0.01, 0.70707070707070718: 0.01, 0.16161616161616163: 0.01, 0.18181818181818182: 0.01, 0.63636363636363646: 0.01, 0.60606060606060608: 0.01, 0.10101010101010102: 0.01, 0.070707070707070718: 0.01, 0.88888888888888895: 0.01, 0.97979797979797989: 0.01, 0.020202020202020204: 0.01, 0.14141414141414144: 0.01, 0.5252525252525253: 0.01, 0.19191919191919193: 0.01, 0.21212121212121213: 0.01, 0.73737373737373746: 0.01, 0.45454545454545459: 0.01, 0.66666666666666674: 0.01, 0.83838383838383845: 0.01, 0.12121212121212122: 0.01, 0.080808080808080815: 0.01, 0.59595959595959602: 0.01, 0.38383838383838387: 0.01, 0.98989898989898994: 0.01, 0.26262626262626265: 0.01, 0.93939393939393945: 0.01, 0.13131313131313133: 0.01, 0.94949494949494961: 0.01, 0.030303030303030304: 0.01, 0.69696969696969702: 0.01, 0.43434343434343436: 0.01, 0.90909090909090917: 0.01, 0.040404040404040407: 0.01, 0.31313131313131315: 0.01, 0.86868686868686873: 0.01, 0.79797979797979801: 0.01, 0.4141414141414142: 0.01, 0.48484848484848486: 0.01, 0.55555555555555558: 0.01, 0.64646464646464652: 0.01, 0.39393939393939398: 0.01, 0.36363636363636365: 0.01, 0.89898989898989912: 0.01, 0.74747474747474751: 0.01, 0.20202020202020204: 0.01, 0.65656565656565657: 0.01, 0.35353535353535359: 0.01, 0.24242424242424243: 0.01, 0.8282828282828284: 0.01, 0.22222222222222224: 0.01, 0.33333333333333337: 0.01}
>>> pmf.Items()
[(0.0, 0.01), (1.0, 0.01), (0.29292929292929293, 0.01), (0.6262626262626263, 0.01), (0.23232323232323235, 0.01), (0.58585858585858586, 0.01), (0.80808080808080818, 0.01), (0.17171717171717174, 0.01), (0.8787878787878789, 0.01), (0.27272727272727276, 0.01), (0.96969696969696972, 0.01), (0.85858585858585867, 0.01), (0.28282828282828287, 0.01), (0.50505050505050508, 0.01), (0.61616161616161624, 0.01), (0.78787878787878796, 0.01), (0.95959595959595967, 0.01), (0.75757575757575768, 0.01), (0.54545454545454553, 0.01), (0.68686868686868696, 0.01), (0.71717171717171724, 0.01), (0.090909090909090912, 0.01), (0.44444444444444448, 0.01), (0.010101010101010102, 0.01), (0.060606060606060608, 0.01), (0.81818181818181823, 0.01), (0.40404040404040409, 0.01), (0.49494949494949497, 0.01), (0.4646464646464647, 0.01), (0.5757575757575758, 0.01), (0.37373737373737376, 0.01), (0.11111111111111112, 0.01), (0.91919191919191923, 0.01), (0.92929292929292939, 0.01), (0.25252525252525254, 0.01), (0.42424242424242425, 0.01), (0.51515151515151525, 0.01), (0.6767676767676768, 0.01), (0.56565656565656575, 0.01), (0.050505050505050511, 0.01), (0.84848484848484851, 0.01), (0.76767676767676774, 0.01), (0.30303030303030304, 0.01), (0.32323232323232326, 0.01), (0.77777777777777779, 0.01), (0.72727272727272729, 0.01), (0.15151515151515152, 0.01), (0.47474747474747481, 0.01), (0.53535353535353536, 0.01), (0.34343434343434348, 0.01), (0.70707070707070718, 0.01), (0.16161616161616163, 0.01), (0.18181818181818182, 0.01), (0.63636363636363646, 0.01), (0.60606060606060608, 0.01), (0.10101010101010102, 0.01), (0.070707070707070718, 0.01), (0.88888888888888895, 0.01), (0.97979797979797989, 0.01), (0.020202020202020204, 0.01), (0.14141414141414144, 0.01), (0.5252525252525253, 0.01), (0.19191919191919193, 0.01), (0.21212121212121213, 0.01), (0.73737373737373746, 0.01), (0.45454545454545459, 0.01), (0.66666666666666674, 0.01), (0.83838383838383845, 0.01), (0.12121212121212122, 0.01), (0.080808080808080815, 0.01), (0.59595959595959602, 0.01), (0.38383838383838387, 0.01), (0.98989898989898994, 0.01), (0.26262626262626265, 0.01), (0.93939393939393945, 0.01), (0.13131313131313133, 0.01), (0.94949494949494961, 0.01), (0.030303030303030304, 0.01), (0.69696969696969702, 0.01), (0.43434343434343436, 0.01), (0.90909090909090917, 0.01), (0.040404040404040407, 0.01), (0.31313131313131315, 0.01), (0.86868686868686873, 0.01), (0.79797979797979801, 0.01), (0.4141414141414142, 0.01), (0.48484848484848486, 0.01), (0.55555555555555558, 0.01), (0.64646464646464652, 0.01), (0.39393939393939398, 0.01), (0.36363636363636365, 0.01), (0.89898989898989912, 0.01), (0.74747474747474751, 0.01), (0.20202020202020204, 0.01), (0.65656565656565657, 0.01), (0.35353535353535359, 0.01), (0.24242424242424243, 0.01), (0.8282828282828284, 0.01), (0.22222222222222224, 0.01), (0.33333333333333337, 0.01)]
>>> integrant=lambda x : x*(1/1) if abs(1-x) <=1 else 0
>>> integrant(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'integrat' is not defined
>>> integrant(1)
0
>>> integrant(0.5)
1
>>> integrant(0.3)
0.5
>>> integrant(0.3)
0.3
>>> from scipy.integrate import quad
>>> quad(integrand, 0, 1, x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'integrand' is not defined
>>> quad(integrand, 0, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'integrand' is not defined
>>> quad(integrant, 0, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'integrand' is not defined
>>> quad(integrant, 0, 1)
(0.5, 5.551115123125783e-15)
>>> EvalPoissonPmf(5, 3)
0.03608940886309672
>>> EvalPoissonPmf(5, 5)
0.10081881344492448
>>> EvalPoissonPmf(5, 7)
0.1754673697678507
>>> EvalPoissonPmf(5, 10)
0.12771666829228961
>>> EvalPoissonPmf(20, 10)
0.03783327480207071
>>> EvalPoissonPmf(20, 10)
0.0018660813139987594
>>> math.log(math.exp(2))
7.38905609893065
>>> math.log(math.exp(2))
2.0
>>> 1.5%1
0.5
>>> 1.5%1
0.5
>>> effect_pdf=lambda p: 1 if p>=0 and p<=1 else 0
>>> effect_pdf(1.5)
1
>>> effect_pdf(.6)
0
>>> effect_pdf(.6)
1
>>> gamma(5)
4.492160846229
>>> from scipy.stats import beta
>>> beta(5, 6, 3)
<scipy.stats.distributions.rv_frozen object at 0x7f7a92702090>
>>> numargs = beta.numargs
>>> numargs
2
>>> rv=beta(2, 2)
<scipy.stats.distributions.rv_frozen object at 0x7f7a92702090>
>>> rv=beta(2, 4)
>>> x = np.linspace(0, np.minimum(rv.dist.b, 3))
>>> type(np)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'typ' is not defined
>>> type(np)
<type 'module'>
>>> rv.dist.b
<scipy.stats.distributions.beta_gen object at 0x284cc90>
>>> rv.dist.b
1.0
>>> h = plt.plot(x, rv.pdf(x))
>>> plt.show()
>>> rv=beta(4, 2)
>>> h = plt.plot(x, rv.pdf(x))
>>> plt.show()
>>> rv=beta(2, 2)
>>> h = plt.plot(x, rv.pdf(x))
>>> plt.show()
>>> rv=beta(4, 2)
>>> h = plt.plot(x, rv.pdf(x))
>>> plt.show()
>>> rv=beta(2, 2)
>>> h = plt.plot(x, rv.pdf(x))
>>> plt.show()
>>> beta(4, 2)(0.5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'rv_frozen' object has no attribute '__getitem__'
>>> beta(4, 2).pdf(0.5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'rv_frozen' object is not callable
>>> beta(4, 2).pdf(0.6)
1.25
>>> beta(4, 2).pdf(0.02)
1.7279999999999998
>>> beta(2, 2).pdf(0.02)
0.00015680000000000002
>>> beta(2, 2).pdf(0.5)
0.1176
>>> beta(2, 2).pdf(0.6)
1.5
>>> beta(2, 2).pdf(0.7)
1.4399999999999999
>>> beta(2, 2).pdf(0.3)
1.2600000000000002
>>> beta(2, 2).pdf(0.3)
1.26
>>> f =beta(2, 2).pdf
>>> type(f)
<type 'instancemethod'>
>>> f(0.5)
1.5
>>> f=lambda x: beta(2, 2).pdf(x)
>>> type(f)
<type 'function'>
>>> f(0.7)
1.5
>>> f(0.1)
1.2600000000000002
>>> f(0.5)
0.54000000000000015
>>> f(0.5)
1.5
>>> max(f(x) for x in linspace(0, 1, 1000))
1.4998469543924089
>>> max(f(x) for x in linspace(0, 1, 1000000))
1.4999984969954943
>>> max(f(x) for x in linspace(0, 1, 100000))

  C-c C-z  C-c C-cTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <genexpr>
  File "<stdin>", line 1, in <lambda>
  File "/usr/lib/python2.7/dist-packages/scipy/stats/distributions.py", line 447, in pdf
    return self.dist.pdf(x, *self.args, **self.kwds)
  File "/usr/lib/python2.7/dist-packages/scipy/stats/distributions.py", line 1295, in pdf
    goodargs = argsreduce(cond, *((x,)+args+(scale,)))
  File "/usr/lib/python2.7/dist-packages/scipy/stats/distributions.py", line 635, in argsreduce
    expand_arr = (cond==cond)
KeyboardInterrupt
>>> max(f(x) for x in linspace(0, 1, 1000))
  C-c C-cTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <genexpr>
  File "<stdin>", line 1, in <lambda>
  File "/usr/lib/python2.7/dist-packages/scipy/stats/distributions.py", line 447, in pdf
    return self.dist.pdf(x, *self.args, **self.kwds)
  File "/usr/lib/python2.7/dist-packages/scipy/stats/distributions.py", line 1295, in pdf
    goodargs = argsreduce(cond, *((x,)+args+(scale,)))
  File "/usr/lib/python2.7/dist-packages/scipy/stats/distributions.py", line 636, in argsreduce
    return [extract(cond, arr1 * expand_arr) for arr1 in newargs]
KeyboardInterrupt
>>> min(f(x) for x in linspace(0, 1, 1000))
1.4999984969954943
>>> min(f(x) for x in linspace(0, 1, 1000))
0.0
>>> rv=beta(2, 2)
>>> h = plt.plot(x, rv.pdf(x))
>>> plt.show()
>>> def integrand(x):
... 	return f(x)*x
...
>>> integrant(0.7)
0.5
>>> integrant(0.7)
0.7
>>> f(0.7)*(0.7)
1.2600000000000002
>>> f(0.7)*(0.7)
0.88200000000000012
>>> integrand = lambda x: beta(2, 2).pdf(x)*x
... 	integrand = lambda x: beta(2, 2).pdf(x)*x
>>> integrant(0.7)
0.7
>>> integrand = lambda x: beta(2, 2).pdf(x)*x
>>> integrant(0.7)
0.7
>>> beta(2, 2).pdf(0.7)*0.7
1.2600000000000002
>>> f=lambda x: beta(2, 2).pdf(0.7)*0.7
0.88200000000000012
>>> f=lambda x: beta(2, 2).pdf(x)*x
>>> f(0.6)
0.88200000000000012
>>> quad(f, 0, 1)
(0.8820000000000001, 9.792167077193883e-15)
>>> f(0.6)
0.88200000000000012
>>> f=lambda x, a, b: beta(a, b).pdf(x)*x
>>> f(0.5)
0.86399999999999999
>>> f(0.7)
0.88200000000000012
>>> f(0.5)
0.75
>>> quad(f, 0, 1)
(0.5, 5.551115123125783e-15)
>>> f=lambda x, a, b: beta(a, b).pdf(x)*x
>>> f(2, 2, 0.6)
0.0
>>> f(0.6, 2, 2)
0.0
>>> f(0.5, 2, 2)
0.86399999999999999
>>> f(0.5, 2, 2)
0.75
>>> def f(x):
... 	alpha=2
... 	beta=2
... 	return beta(alpha, beta).pdf(x)*x
...
>>> f(0.6)
<function <lambda> at 0x3dd86e0>
>>> def f(x):
... 	alpha=2
... 	beta=2
... 	return beta(alpha, beta).pdf(x)*x
...
>>> beta(2, 2).pdf(0.6)
<scipy.stats.distributions.rv_frozen object at 0x2dfef90>
>>> f=lambda x : beta(2, 2).pdf(x)
1.4399999999999999
>>> f=lambda x : beta(a, b).pdf(x)
>>> f(0.6)
1.4399999999999999
>>> f=lambda x, a, b : beta(a, b).pdf(x)
>>> f(0.5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
NameError: global name 'a' is not defined
>>> f=lambda x, a, b : beta(a, b).pdf(x)
>>> f(0.6, 2, 2)
1.4399999999999999
>>> g = lambda x : f(x, 2, 2)
>>> g(0.6)
1.4399999999999999
>>> H=BayesNet()
1.5
>>> H=BayesNet()
1.44
>>> H=BayesNet()
1.26
>>> H=BayesNet()
1.26
>>> H=BayesNet()
1.26
>>> H=BayesNet()
1.44
>>> H=BayesNet()
1.5
>>> G.dep_vars
[0]
>>> G.dep_vars
[1, 2]
>>> G.nodes()
[0, 1, 2]
>>> g(0.6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() takes exactly 3 arguments (1 given)
>>> g(0.6)
1.4399999999999999
>>> pr= lambda x : 0.6*0.6*0.5*(1.0-x)*g(x)
>>> 0.6*0.6*0.5*quad(lambda x: (1.0-x)*g(x), 0, 1)
(0.09, 9.992007221626409e-16)
>>> 0.6*0.6*0.5*quad(lambda x: (1.0-x)*g(x), 0, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
>>> 0.6*0.6*0.5*quad(lambda x: (1.0-x)*g(x), 0, 1)[0]
(0.5, 5.551115123125783e-15)
>>> 0.6*0.6*0.5*quad(lambda x, y: (1.0-x)*g(x)*(1.0-y)*g(y), 0, 1)[0]
0.09
>>> 0.6*0.6*0.5*quad(lambda x, y: ((1.0-x)*g(x)*(1.0-y)*g(y)), 0, 1, 0, 1)[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/scipy/integrate/quadpack.py", line 247, in quad
    retval = _quad(func,a,b,args,full_output,epsabs,epsrel,limit,points)
  File "/usr/lib/python2.7/dist-packages/scipy/integrate/quadpack.py", line 312, in _quad
    return _quadpack._qagse(func,a,b,args,full_output,epsabs,epsrel,limit)
TypeError: <lambda>() takes exactly 2 arguments (1 given)
>>> 0.6*0.6*0.5*quad(lambda x, y: ((1.0-x)*g(x)*(1.0-y)*g(y)), 0, 0, 1, 1)[0]
0.0
>>> quad(lambda x, y: ((1.0-x)*g(x)*(1.0-y)*g(y)), 0, 0, 1, 1)[0]
0.0
>>> quad(lambda x, y: ((1.0-x)*g(x)*(1.0-y)*g(y)), 0, 0, 1, 1)
0.0
>>> quad(lambda x, y: ((1.0-x)*g(x)*(1.0-y)*g(y)), 0, 1)
(0.0, 0.0, {'rlist': array([  0.00000000e+000,   3.41409005e-316,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         4.74303020e-322,   7.90505033e-323]), 'last': 1, 'elist': array([  0.00000000e+000,   3.25981904e-316,   9.30819677e-321,
         2.97079545e-313,   0.00000000e+000,   0.00000000e+000,
         4.24400727e-314,   0.00000000e+000,   0.00000000e+000,
         1.06099946e-313,   0.00000000e+000,   0.00000000e+000,
         4.24400815e-314,   0.00000000e+000,   0.00000000e+000,
         1.26480805e-321,   0.00000000e+000,   0.00000000e+000,
         2.92835433e-312,   3.07441795e-316,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         3.45845952e-323,   2.10077583e-312]), 'iord': array([        1,     32634,  68611280,         0,  63285808,         0,
               6,         0,       809,         9,         1,         0,
              12,        13,       808,        15,        16,         0,
              18,        19,       811,        21,        22,         0,
              24,        25,       811,        27,        28,         0,
              30,        31,  51739168,        33,        34,         0,
              36,        37,         0,        39,        40,        41,
              42, 733389503,        44,        45,   8696288,         0,
             208,         0], dtype=int32), 'alist': array([  0.00000000e+000,   3.16768964e-316,   0.00000000e+000,
         1.30294992e-319,   0.00000000e+000,   8.87835966e-321,
         2.12201148e-314,   0.00000000e+000,   0.00000000e+000,
         8.60069476e-320,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         8.48798317e-314,   8.48798317e-314]), 'blist': array([  0.00000000e+000,   3.16918843e-316,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         8.48798317e-314,   8.48798317e-314]), 'neval': 21})
>>> quad(quad(lambda x, y: ((1.0-x)*g(x)*(1.0-y)*g(y)), 0, 1), 0, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/scipy/integrate/quadpack.py", line 247, in quad
    retval = _quad(func,a,b,args,full_output,epsabs,epsrel,limit,points)
  File "/usr/lib/python2.7/dist-packages/scipy/integrate/quadpack.py", line 312, in _quad
    return _quadpack._qagse(func,a,b,args,full_output,epsabs,epsrel,limit)
TypeError: <lambda>() takes exactly 2 arguments (1 given)
>>> quad(lambda x, y: ((1.0-x)*g(x)*(1.0-y)*g(y)), 0, 1, args(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/scipy/integrate/quadpack.py", line 247, in quad
    retval = _quad(func,a,b,args,full_output,epsabs,epsrel,limit,points)
  File "/usr/lib/python2.7/dist-packages/scipy/integrate/quadpack.py", line 312, in _quad
    return _quadpack._qagse(func,a,b,args,full_output,epsabs,epsrel,limit)
TypeError: <lambda>() takes exactly 2 arguments (1 given)
>>> quad(lambda x, y: ((1.0-x)*g(x)*(1.0-y)*g(y)), 0, 1, args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'args' is not defined
>>> f=lambda x, y: ((1.0-x)*g(x)*(1.0-y)*g(y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> f=lambda x y: ((1.0-x)*g(x)*(1.0-y)*g(y))
>>> f(0.6, 0.6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
  File "<stdin>", line 1, in <lambda>
TypeError: <lambda>() takes exactly 2 arguments (3 given)
>>> f=lambda (x,y): ((1.0-x)*g(x)*(1.0-y)*g(y))
  File "<stdin>", line 1
    f=lambda x y: ((1.0-x)*g(x)*(1.0-y)*g(y))
               ^
SyntaxError: invalid syntax
>>> f=lambda (x, y): ((1.0-x)*g(x)*(1.0-y)*g(y))
>>> f((0.6, 0.6))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() takes exactly 1 argument (2 given)
>>> f((0.6, 0.6))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
  File "<stdin>", line 1, in <lambda>
TypeError: <lambda>() takes exactly 1 argument (3 given)
>>> h=lambda (x, y): ((1.0-x)*g(x)*(1.0-y)*g(y))
>>> g(0.6)*g(0.7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
TypeError: <lambda>() takes exactly 1 argument (3 given)
>>> g(0.6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
TypeError: <lambda>() takes exactly 1 argument (3 given)
>>> g = lambda x : f(x, 2, 2)
>>> g(0.6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
TypeError: <lambda>() takes exactly 1 argument (3 given)
>>> f(0.6, 2, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() takes exactly 1 argument (3 given)
>>> f=lambda x, a, b : beta(a, b).pdf(x)
>>> g = lambda x : f(x, 2, 2)
>>> g(0.6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
TypeError: <lambda>() takes exactly 1 argument (3 given)
>>> f=lambda x, a, b : beta(a, b).pdf(x)
>>> g = lambda x : f(x, 2, 2)
>>> g(0.6)
1.4399999999999999
>>> h=lambda (x, y): ((1.0-x)*g(x)*(1.0-y)*g(y))
>>> h((0.6, 0.2))
0.33177599999999996
>>> h((0.6, 0.2))
0.44236800000000009
>>> quad(lambda x, y: ((1.0-x)*g(x)*(1.0-y)*g(y)), 0, 1, args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> quad(lambda y: y*g(y), 0, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> quad(lambda x, y: x*g(y), 0, 1)
(0.5, 5.551115123125783e-15)
>>> quad(lambda x, y: x*g(y), 0, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/scipy/integrate/quadpack.py", line 247, in quad
    retval = _quad(func,a,b,args,full_output,epsabs,epsrel,limit,points)
  File "/usr/lib/python2.7/dist-packages/scipy/integrate/quadpack.py", line 312, in _quad
    return _quadpack._qagse(func,a,b,args,full_output,epsabs,epsrel,limit)
TypeError: <lambda>() takes exactly 2 arguments (1 given)
>>> quad(lambda x, y: x*g(y), 0, 1, args=(x, y))
<function <lambda> at 0x433b7d0>
>>> quad(lambda x, y: x*g(y), 0, 1, args=(y, x))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> tplquad(lambda x, y: x*g(y), 0, 1, args=(y, x))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> tplquad(lambda x, y: x*g(y), 0, 1, args=(y, x))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tplquad' is not defined
>>> from scipy.integrate import tplquad
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name tplquad
>>> from scipy.integrate import tplquad
>>> tplquad(lambda x, y: x*g(y), 0, 1, args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> tplquad(lambda x, y: x*g(y), 0, 1, 0, 1, args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> tplquad(lambda x, y: x*g(y), 0, 1, 0, 1, args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> 6
>>> tplquad(g(y)*x**2, 0,1,0, 1 args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> tplquad(g(y)*x**2, 0,1,0, 1, args=(x, y))
  File "<stdin>", line 1
    tplquad(g(y)*x**2, 0,1,0, 1 args=(x, y))
                                   ^
SyntaxError: invalid syntax
>>> tplquad(x**2+y**2, 0,1,0, 1, args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> tplquad(lambda x, y: x**2+y**2, 0,1,0, 1, args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> tplquad(lambda x, y: d(x, y), 0,1,0, 1, args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> d=labda x, y: x**2+y**2
  File "<stdin>", line 1
    labda x, y: x**2+y**2
          ^
SyntaxError: invalid syntax
>>> d=lambda x, y: x**2+y**2
  File "<stdin>", line 1
    d=labda x, y: x**2+y**2
            ^
SyntaxError: invalid syntax
>>> d=lambda x, y: x**2+y**2
>>> tplquad(d(x, y), 0,1,0, 1, args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> tplquad(d(x, y), 0,1,0, 1, args=(x, y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> d(2, 3)
13
>>> 2**2 + 3**2
13
>>> 