PDFFLAGS = -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress \
           -dCompressPages=true -dUseFlateCompression=true  \
           -dEmbedAllFonts=true -dSubsetFonts=true -dMaxSubsetPct=100


all:	book.tex
	pdflatex book
	makeindex book.idx
	pdflatex book
	mv book.pdf thinkbayes.pdf
	evince thinkbayes.pdf

HEVEABUILDLOG=build.log

hevea:
	sed 's/\(figs\/[^.]*\).\(pdf\|png\)/\1.eps/' book.tex > thinkbayes.tex
	rm -rf html
	mkdir html
	hevea macros.hva -O -e latexonly htmlonly thinkbayes 2>&1 | tee ${HEVEABUILDLOG}
# the following greps are a kludge to prevent imagen from seeing
# the definitions in latexonly, and to avoid headers on the images
	grep -v latexonly thinkbayes.image.tex > a; mv a thinkbayes.image.tex
	sed s/\\\\usepackage{fancyhdr}// < thinkbayes.image.tex > a; mv a thinkbayes.image.tex
	imagen -png thinkbayes
	hacha thinkbayes.html
	cp up.png next.png back.png html
	cp custom.css thinkbayes.css
	mv index.html thinkbayes.css thinkbayes*.html thinkbayes*.png *motif.gif html

DEST = /home/downey/public_html/greent/thinkbayes

distrib:
	rm -rf dist
	mkdir dist
	rsync -a thinkbayes.pdf html dist
	rsync -a dist/* $(DEST)
	chmod -R o+r $(DEST)/*
	cd $(DEST)/..; sh back

plastex:
	# Before running plastex, we need the current directory in PYTHONPATH
	# export PYTHONPATH=$PYTHONPATH:.
	rm -rf /home/downey/thinkbayes/trunk/book/.svn
	plastex --renderer=DocBook --theme=book --image-resolution=300 --filename=book.xml book.tex
	rm -rf /home/downey/thinkbayes/trunk/book/.svn

xxe:
	xmlcopyeditor ~/ThinkBayes/book/book/book.xml &

lint:
	xmllint -noout book/book.xml

OREILLY = atlas

oreilly:
	rsync -a book/ $(OREILLY)
	rsync -a figs/* $(OREILLY)/figs/
	cd $(OREILLY); git add .
	cd $(OREILLY); git commit -m "Automated check in."
	cd $(OREILLY); git push

clean:
	rm -f *~ *.aux *.log *.dvi *.idx *.ilg *.ind *.toc



