all: $(addprefix images/, \
	ptb_clocks.jpg \
	sundial.jpg \
	xkcd_iso.png \
	)

all: build/dut1.svg
all: build/standards_venn.svg


images/ptb_clocks.jpg: images
	curl -fsSL -o $@ https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/D0841_092.jpg/2560px-D0841_092.jpg 

images/sundial.jpg: images
	curl -fsSL -o $@ https://upload.wikimedia.org/wikipedia/commons/a/aa/Ancient-egyptian-sundial.jpg

images/xkcd_iso.png: images
	curl -fsSL -o  $@ https://imgs.xkcd.com/comics/iso_8601_2x.png


build/%.svg: plots/plot_%.py | build 
	python $<



images:
	mkdir -p $@

build:
	mkdir -p $@

clean:
	rm -rf build

.PHONY: all clean
