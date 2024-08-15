all: $(addprefix images/, \
	ptb_clocks.jpg \
	sundial.jpg \
	first_caesium_clock.jpg \
	harrison_h4.png \
	quadrant.jpg \
  xkcd_iso.png \
  xkcd_time_interval.png \
	waterclock.jpg \
	vlba_st_croyx.jpg \
	timezones.svg \
	)

ifeq (, $(shell, command -v magick))
MAGICK=magick
else
MAGICK=convert
endif

all: $(addprefix build/, \
	dut1.svg \
  standards_venn.svg \
  )

images/ptb_clocks.jpg: | images
	curl -fsSL -o $@ https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/D0841_092.jpg/2560px-D0841_092.jpg 

images/first_caesium_clock.jpg: | images
	curl -fsSL -o $@ https://upload.wikimedia.org/wikipedia/commons/5/55/Atomic_Clock-Louis_Essen.jpg

images/sundial.jpg: | images
	curl -fsSL -o $@ https://upload.wikimedia.org/wikipedia/commons/a/aa/Ancient-egyptian-sundial.jpg

images/harrison_h4.png: | images
	curl -fsSL https://collections.rmg.co.uk/media/450/748/f7024_009.jpg | \
		$(MAGICK) jpg:- -fuzz 5% -transparent white $@

images/quadrant.jpg: | images
	curl -fsSL -o $@ https://collections.rmg.co.uk/media/548/35/l2157_001.jpg

images/xkcd_iso.png: | images
	curl -fsSL https://imgs.xkcd.com/comics/iso_8601_2x.png | \
		$(MAGICK) png:- -channel RGB -negate -transparent black -trim $@

images/xkcd_time_interval.png: | images
	curl -fsSL https://imgs.xkcd.com/comics/datetime_2x.png | \
		$(MAGICK) png:- -channel RGB -negate -transparent black -trim $@

images/vlba_st_croyx.jpg: | images
	curl -fsSL -o $@ https://upload.wikimedia.org/wikipedia/commons/e/e2/VLBA_St_Croix-04.jpg 

images/waterclock.jpg: | images
	curl -fsSL -o $@ https://upload.wikimedia.org/wikipedia/commons/f/ff/AGMA_Clepsydre.jpg

images/timezones.svg: | images
	curl -fsSL -o $@ https://upload.wikimedia.org/wikipedia/commons/e/ec/World_Time_Zones_Map.svg

build/%.svg: plots/plot_%.py | build 
	python $<

images:
	mkdir -p $@

build:
	mkdir -p $@

clean:
	rm -rf build

.PHONY: all clean
