# Copyright (c) 2001, 2002, 2003 Python Software Foundation
# Copyright (c) 2004-2008 Paramjit Oberoi <param.cs.wisc.edu>
# Copyright (c) 2007 Tim Lauridsen <tla@rasmil.dk>
# All Rights Reserved.  See LICENSE-PSF & LICENSE for details.

from reconfigure.parsers.iniparse.ini import INIConfig, change_comment_syntax
from reconfigure.parsers.iniparse.config import BasicConfig, ConfigNamespace
from reconfigure.parsers.iniparse.compat import RawConfigParser, ConfigParser, SafeConfigParser
from reconfigure.parsers.iniparse.utils import tidy

try:
  from ConfigParser import DuplicateSectionError,    \
                    NoSectionError, NoOptionError,   \
                    InterpolationMissingOptionError, \
                    InterpolationDepthError,         \
                    InterpolationSyntaxError,        \
                    DEFAULTSECT, MAX_INTERPOLATION_DEPTH
except ImportError:
  from configparser import DuplicateSectionError,    \
                    NoSectionError, NoOptionError,   \
                    InterpolationMissingOptionError, \
                    InterpolationDepthError,         \
                    InterpolationSyntaxError,        \
                    DEFAULTSECT, MAX_INTERPOLATION_DEPTH

__all__ = [
    'BasicConfig', 'ConfigNamespace',
    'INIConfig', 'tidy', 'change_comment_syntax',
    'RawConfigParser', 'ConfigParser', 'SafeConfigParser',
    'DuplicateSectionError', 'NoSectionError', 'NoOptionError',
    'InterpolationMissingOptionError', 'InterpolationDepthError',
    'InterpolationSyntaxError', 'DEFAULTSECT', 'MAX_INTERPOLATION_DEPTH',
]