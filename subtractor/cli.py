#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Build subtracted images from zipping streams."""
import pathlib
import os
import sys

import subtractor.subtractor as diff

DEBUG_VAR = "SUBTRACTOR_DEBUG"
DEBUG = bool(os.getenv(DEBUG_VAR))

ABORT_VAR = "SUBTRACTOR_ABORT"
ABORT = bool(os.getenv(ABORT_VAR))

THRESHOLD_VAR = "SUBTRACTOR_THRESHOLD"
THRESHOLD = float(os.getenv(THRESHOLD_VAR, "0.01"))


# pylint: disable=expression-not-assigned
def main(argv=None, abort=None, debug=None, threshold=None):
    """Dispatch processing of the job.
    This is the strings only command line interface.
    For python API use interact with diff functions directly.
    """
    argv = sys.argv[1:] if argv is None else argv
    debug = debug if debug else DEBUG
    abort = abort if abort else ABORT
    threshold = threshold if threshold else THRESHOLD
    unique_trees = {arg: None for arg in argv}
    for tree_or_leaf in unique_trees:
        if not pathlib.Path(tree_or_leaf).is_file() and not pathlib.Path(tree_or_leaf).is_dir():
            print("ERROR: For now only existing paths accepted.")
            sys.exit(2)

    code, _ = diff.main(list(unique_trees.keys()), abort=abort, debug=debug, threshold=threshold)
    return code
