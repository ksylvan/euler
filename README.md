# Project Euler

Project Euler is a series of challenging mathematical/computer programming problems
that will require more than just mathematical insights to solve. Although mathematics will help you arrive
at elegant and efficient methods, the use of a computer and programming skills will be required to solve the
problems.

See <https://projecteuler.net>

## This Repository

This repository is for the solutions of the Project Euler problems.

Conventions for the code: All python code uses doctest and is structured into small understandable methods.

The answers to all the Euler problems can be seen by:

```bash
make answers
```

This default target assumes convention that the output to summarize the answer starts with the
string "@ " at the beginning of the line.

```bash
make measurements
```

This target runs the tests and reports timing measurements of the methods/functions that
were run to determine the solution.

```bash
make tests
```

This target simply runs all the tests in every file, showing only the pass/fail lines from doctest.

```bash
make verbose
```

The `verbose` target runs all the python modules, with no filtering.
