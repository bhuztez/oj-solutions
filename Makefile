RSTS=$(wildcard *.rst */*.rst */*/*.rst)
HTMLS=$(RSTS:%.rst=%.html)

all: $(HTMLS)

%.html: %.rst
	python2 render.py --traceback --link-stylesheet --no-xml-declaration --math-output=mathjax "$<" "$@"

clean:
	rm -f $(HTMLS)
