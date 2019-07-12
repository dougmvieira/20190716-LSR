all: 20190716-LSR.html

20190716/optimal_quotes.html: optimal_options_market_making.py
	mkdir -p 20190716
	python3 optimal_options_market_making.py

20190716-LSR.html: LSR.md References.bib 20190716/optimal_quotes.html
	pandoc -s -c scrollable.css -t revealjs -V theme=white -V revealjs-url=. --mathjax --toc --toc-depth=1 -o 20190716-LSR.html --bibliography References.bib LSR.md
