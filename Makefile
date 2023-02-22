.PHONY: answers measurements tests verbose

LIB=primes.py testing.py
SRCS=$(LIB) p001.py p002.py p003.py p004.py p005.py p006.py p007.py p008.py \
	p009.py p010.py p011.py p012.py p013.py p014.py p015.py p016.py \
	p017.py p018.py p019.py p020.py p021.py p022.py p023.py p024.py \
	p025.py p026.py p027.py p028.py p029.py p030.py p031.py p032.py p033.py \
	p034.py p035.py p036.py p037.py p038.py p039.py p040.py p041.py p042.py \
	p043.py p044.py p045.py p046.py p047.py p048.py p049.py p050.py p051.py \
	p052.py p053.py

answers:
	@for f in $(SRCS); do echo "-- $$f --"; python3 $$f | grep '^@' | sed 's/^@ //'; done

measurements:
	@for f in $(SRCS); do echo "-- $$f --"; TIMING=1 python3 $$f | grep -v '^@' ; done

tests:
	@for f in $(SRCS); do echo "-- $$f --"; TESTING=1 python3 $$f | grep 'pass\|fail'; done

verbose:
	@for f in $(SRCS); do echo "-- $$f --"; TESTING=1 TIMING=1 python3 $$f; done
