.PHONY: answers measurements tests verbose

LIB=primes.py testing.py
SRCS=$(LIB) $(shell echo p[0-9][0-9][0-9].py)

answers:
	@for f in $(SRCS); do echo "-- $$f --"; python3 $$f | grep '^@' | sed 's/^@ //'; done

measurements:
	@for f in $(SRCS); do echo "-- $$f --"; TIMING=1 python3 $$f | grep -v '^@' ; done

tests:
	@for f in $(SRCS); do echo "-- $$f --"; TESTING=1 python3 $$f | grep 'pass\|fail'; done

verbose:
	@for f in $(SRCS); do echo "-- $$f --"; TESTING=1 TIMING=1 python3 $$f; done
