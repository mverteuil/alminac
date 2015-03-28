Contributing to Alminac

:+1: Firstly, thanks for reading this document. It's a good sign that you have
the right kind of attitude for a person who contributes to this project.

Thanks for your interest in improving Alminac. Here are some points to get you
started:

1. The main branch is `master`. The `master` branch is reserved for deployable
   code and nothing that isn't deployable belongs there.
2. Submit changes as pull requests. Please welcome and expect to make changes
   as a result of feedback to your pull requests. While your effort in making a
   contribution is wholly appreciated, it is important that this project maintain
   a certain level of quality to ensure that it doesn't become riddled with
   entropy.
3. The project is designed to run under the latest stable version of Python 2.7
   where code is written in python.
4. OS X and Linux are a priority over Windows, but Windows support is welcomed.
5. Any new feature is expected to come with unit tests compatible with the
   version of py.test indicated in the `master` branch's `dev-requirements.txt`.

This document also contains an opinionated style guide. Please make sure your
code follows these guidelines.  They will be enforced during pull review.

***

## Setup

1. Install [virtualenv](https://virtualenv.readthedocs.org/en/latest/) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html).

    ```
    $ pip install virtualenv virtualenvwrapper
    ```

2. Make a development virtualenv.

    ```
    $ mkvirtualenv alminac
    ```

4. Clone the repository.

    ```
    $ git clone https://github.com/mverteuil/almanac.git
    ```

5. Install dependencies, then install Almanac to the virtualenv.

    ```
    $ cd /path/to/almanac
    $ workon almanac
    (almanac-dev)$ pip install -r dev-requirements.txt
    (almanac-dev)$ pip install -e .
    ```

***

## Style

These are intended to be guidelines, not hard-and-fast requirements.

### PEP8

[PEP8](https://www.python.org/dev/peps/pep-0008/) is a strong guideline. Run your code through `flake8` to detect obvious problems.

Line-length is flexible, but try and keep it around 110 characters. Work around it using brackets and visual indentation.

### Seven Pillars

[The Seven Pillars of Pretty Code](http://www.perforce.com/resources/white-papers/seven-pillars-pretty-code)
    by Christopher Seiwald contains a good indication for what is expected of
    code that is submitted to this project.

### Imports

1. Group imports in three distinct sections:
    1. standard library dependencies
    2. remote dependencies (e.g., things in requirements.txt), 
    3. local dependencies.

2. Prefer module imports over importing individual objects from modules. This
   makes it immediately obvious where objects come from, and also simplifies
   refactoring.

    ```python
    # Bad
    from requests import get

    from alminac.module import UsefulClass

    # Good
    import requests

    from alminac import module
    ```

    Exceptions and cultural conventions are exceptions to this rule.

    ```python
    from StringIO import StringIO
    from datetime import datetime

    from alminac.module import AttemptFailure
    ```

2. Sort imports alphabetically the way Vi(m)/`sort` would (i.e., capitals
   first). If you are importing multiple objects from a module or package; only
   import one module per line. This makes transplanting code between modules much
   easier and reduces the opportunity for merge conflicts.

    ```python
    # Bad
    from alminac import AttemptFailure, UsefulClass, module

    # Good
    from alminac import AttemptFailure
    from alminac import UsefulClass
    from alminac import module
    ```

    `from` statements should follow `import` statements.

    ```python
    from alminac import AttemptFailure
    from alminac import UsefulClass
    from alminac import module
    import almanac
    ```

***

## Documentation

Documentation should follow any strict requirements declared by [PEP257](https://www.python.org/dev/peps/pep-0257/).
This document should be considered the final word on docstring convention, but
where no opinion exists here the matter is deferred to PEP257 guidelines.

 * One line summary docstrings should go on the same line as the delimiters (`"""`).
 * In multiline docstrings, delimiters (`"""`) go on their own lines, with a blank line preceding the final delimiter.
 * Docstrings should fit within 110 characters.
 * Document class construction in the class docstring, not the `__init__` docstring.
 * Do not include spurious documentation for things like `__str__` and `__unicode__`.
 * Do not include doctests, use py.test instead.

Document parameters with their types, return values, and checked exceptions using [Google notation](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html#Comments).

```python
class UsefulClass(object):
    """
    Provides a useful service.

    Args:
        required_word (str): A required word.
    
    """
    def __init__(self, required_word):
        ...
```
