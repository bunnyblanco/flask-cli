from __future__ import absolute_import
import os
import re
import sys
import types
import warnings
from gettext import gettext as _
from collections import OrderedDict
import argparse
from .cli import prompt, prompt_pass, prompt_bool, prompt_choices

__all__ = ["prompt", "prompt_pass", "prompt_bool", "prompt_choices"]

safe_actions = (argparse._StoreAction,
                argparse._StoreConstAction,
                argparse._StoreTrueAction,
                argparse._StoreFalseAction,
                argparse._AppendAction,
                argparse._AppendConstAction,
                argparse._CountAction)


try:
    import argcomplete
    ARGCOMPLETE_IMPORTED = True
except ImportError:
    ARGCOMPLETE_IMPORTED = False

def add_help(parser, help_args): 
    if not help_args:
        return
    parser.add_argument(*help_args,
                        action='help', default=argparse.SUPPRESS, help=_('show this help message and exit'))

