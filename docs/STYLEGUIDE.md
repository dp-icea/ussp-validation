# BR-UTM Python Style Guide

This document describes Python practices or styles that should generally be used
when adding or modifying Python code in BR-UTM repositories.

## [Black](https://black.readthedocs.io/en/stable/)

Black automatically formats Python code and can be invoked with `make format`.
Its style choices take precedence over all other recommendations here to
maintain the ability to always be confident of not introducing invalid
formatting using `make format`.

## Type annotations

The following should almost always have type annotations according to
[PEP 484](https://peps.python.org/pep-0484/):

* Arguments in function or method declarations
* Return values of functions or methods
  * Exception: when it is obvious the function or method has no return value,
      the correct return type of `None` may be omitted (though annotating
      non-returning functions or methods with `-> None` is still encouraged)
* Class member variables
* Complex or confusing local variables within a function
  ([PEP 526](https://peps.python.org/pep-0526/))

The type `Any` should usually be avoided if a more specific type is known.

## Function documentation

When the purpose or behavior of a function or method, its input parameters, or
its result is not reasonably obvious from its name and
[typing](#type-annotations), it should at least be:

1. given a docstring explaining at least the components (input parameters,
   return value, behavior of function) that are not obvious, or
2. annotated as private or internal with a single leading underscore in its
   name.

Docstrings should be via [PEP 257](https://peps.python.org/pep-0257/).
[Google format](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)
is encouraged.
