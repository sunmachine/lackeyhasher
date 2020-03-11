from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


hashmodule_extensions = [
    Extension(
        name="lackeyhash",
        sources=["pylackeyhash.pyx", "src/lackeyhash.c"],
        library_dirs=["src"],
        include_dirs=["src"],
    )
]

setup(
    name="lackeyhash",
    version="0.1.0",
    description="Custom hash function used by LackeyCCG.",
    long_description="Custom hash function written by Trevor over at LackeyCCG. This is a simple reimplementation in C and packaged as a python module.",
    author="Dan Peavey",
    author_email="danpeavey@gmail.com",
    url="https://github.com/sunmachine/duelworks-lackey/master/build/hashmodule/",
    ext_modules=cythonize(hashmodule_extensions, language_level="3"),
)
