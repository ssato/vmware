"""setup.py
"""
import glob
import os
import subprocess

import setuptools.command.install
import setuptools


_CURDIR = os.path.abspath(os.path.dirname(__file__))

_MAN_SECT = "7"  # TBD
_MAN_EXT = "." + _MAN_SECT

_DOC_SRCS = glob.glob(os.path.join(_CURDIR, "docs/*.rst"))
_MAN_DATA = [
    ("/usr/share/man/man{}".format(_MAN_SECT), 
     tuple(rst.replace(".rst", _MAN_EXT) for rst in _DOC_SRCS))
]


class install(setuptools.command.install.install):
    """custom build_py class
    """

    def run(self):
        """override do_build_py method to pre-process man sources.
        """
        for rst in _DOC_SRCS:
            mout = rst.replace(".rst", _MAN_EXT)
            subprocess.check_call(["rst2man", rst, mout])

        super(install, self).run()


setuptools.setup(data_files=_MAN_DATA,
                 cmdclass=dict(install=install, ))
