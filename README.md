# lackeyhasher

Reimplementation of [Lackey's file hashing routine in C][lackey-forum-1] as a python module.

## Pipenv

Add it to your `Pipfile`:

* `pipenv install -e path/to/lackeyhasher`

## Build

Ensure you have a platform-correct compiler installed and referenced in `PATH`. 
Then, run `setup.py` in your virtual environment.

* `python setup.py build_ext -i`

## Resources

* [making-your-c-library-callable-from-python][1]
* [Documentation][2]


[lackey-forum-1]: http://www.lackeyccg.com/forum/index.php?topic=808.msg6056#msg6056
[1]: https://stavshamir.github.io/python/making-your-c-library-callable-from-python-by-wrapping-it-with-cython/
[2]: https://cython.readthedocs.io/en/latest/src/userguide/external_C_code.html
