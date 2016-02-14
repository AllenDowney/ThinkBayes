ThinkBayes
==========

This material was adapted from Alan Downey's Think Bayes 
Github repository by Roger Labbe. 

Mostly I took his code and tex file and converted them into
a series of Jupyter notebooks. This was sometimes problamatic.
Alan uses a lot of Python classes, and his exposition splits
the code across multiple paragraphs. This does not cleanly 
work in notebooks. Furthermore, most of his code is in .py 
files. 

I made this work as best I could, but sometimes there were
authorial decisions that I do not feel comfortable making. 
The code just doesn't run in those spots. 

He generates many graphs, but does not supply the source code.
Maybe the code is in the /code subdirectory? In a few places 
I took the liberty of supplying the Python, but in many places
I did not. Maybe somebody else will feel like doing that; 
I don't really have time right now. Pull requests accepted!

There are several places in the text where it was not clear
to me where he got his datasets. Rather than making something
up, I just let the code cells fail to execute. I hope Alan
will help me rectify these situations. If not, and there is
enough interest, we can make some decisions and get the cells
working.


I put his code in a /code subdirectory. I did not fix the references
in the book, which specify going to his home page to get the code.

I did alter most of the code to work with Python 3. Mainly by using

    from __future__ import print_function
    
but in a few places I had to fix things like removing `xrange` or
`iterkeys()`. I only did just enough work to get it working.


His original README is:

https://github.com/AllenDowney/ThinkBayes

Code repository for Think Bayes: Bayesian Statistics Made Simple
by Allen B. Downey

Available from Green Tea Press at http://thinkbayes.com.

Published by O'Reilly Media, October 2013.

