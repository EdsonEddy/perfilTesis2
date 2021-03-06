#!/usr/bin/env python
import os
from functools import partial

import sys

from locmoss import MossEngine, Parser, Winnower
from locmoss.moss import Filter
from locmoss.query import MatchingLocations
from locmoss.query import MetaData
from locmoss.query import SoftwareList, CorpusStat, MostSimilar, MatchingSnippets
from locmoss.query import Ranking, CountSimilarity, JaccardSimilarity, \
    TfIdfSimilarity
from locmoss.software import Software


__DESC__ = "Local MOSS (measure of software similarity). "  \
           "For ease of use, consider redirecting stdout to a file. " \
           "Report the most similar softwares from a bunch looking for " \
           "matching fingerprints. A fingerprint is a kgram, and subsets of " \
           "them are selected by min-hashing over a moving window of " \
           "consecutives kgrams. See `Schleimer, S., Wilkerson, D. S., " \
           "& Aiken, A. (2003, June). Winnowing: local algorithms for " \
           "document fingerprinting. In Proceedings of the 2003 ACM " \
           "SIGMOD international conference on Management of " \
           "data (pp. 76-85)` for more details"


def select_parser_factory(lang):
    import pygments.lexers
    if lang is None:
        return Parser
    else:
        return partial(Parser, lexer=pygments.lexers.get_lexer_by_name(lang))



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description=__DESC__)
    parser.add_argument("paths", nargs="*",
                        help="The paths to the software to analyze."
                             "Use path pattern for ease.") # TODO more details
    parser.add_argument("--reference", "-r", action="append",
                        help="Reference files. Files must be supplied one by one"
                             "by repeating the option."
                             "The fingerprints contained in "
                             "them will be ignored. Useful for plagiarism "
                             "detection where some code is intended to be "
                             "shared. ")
    parser.add_argument( "--language", "-l", default=None,
                         help="language of the software. If not supplied"
                              "will be guessed. See the `Short names` at "
                              "https://pygments.org/docs/lexers/")

    parser.add_argument("--window_size", "-w", default=15, type=int,
                        help="Size of the min-hashing window. The smaller,"
                             "the more fingerprints are selected. More robust "
                             "but much slower.")
    parser.add_argument("--kgram_len", "-k", default=5, type=int,
                        help="Size of the kgrams. Optimal size is "
                             "language-dependent. Longer kgrams will produce "
                             "less false-positive but will miss more "
                             "true-positives.")
    parser.add_argument("--collision_threshold", "-c", default=10, type=int,
                        help="In how many softwares a fingerprint must appear "
                             "before being discounted as too common.")
    parser.add_argument("--output_size", "-s", default="long",
                        choices=["short", "medium", "long"],
                        help="Size of the output to display")
    parser.add_argument("--top", "-t", default=15, type=int,
                        help="How many matches are reported.")
    parser.add_argument("--silent", action="store_true",
                        help="Shut up a few messages on stderr.")
    parser.add_argument("--pre_lines", default=5, type=int,
                        help="Number of lines before a fingerprint to display "
                             "when printing collisions. Ignored for "
                             "short output.")
    parser.add_argument("--post_lines", default=5, type=int,
                        help="Number of lines after a fingerprint to display "
                             "when printing collisions. Ignored for  "
                             "short output.")


    args = parser.parse_args()
    verbose = not args.silent

    metadata_query = MetaData(**{k: v for k, v in args.__dict__.items() if
                                 k != "paths"})

    parser_factory = select_parser_factory(args.language)

    fingerprinter = Winnower(parser_factory, args.window_size, args.kgram_len)
    filter = Filter(args.collision_threshold)

    moss = MossEngine(fingerprinter, filter)

    softwares = Software.list_from_globs(args.paths)

    reference = None
    if args.reference is not None and len(args.reference) > 0:
        reference = Software("Reference", args.reference)

    if verbose:
        print("Building index and matching graph...", file=sys.stderr)

    moss.build_index(softwares, reference)

    if verbose:
        print("Querying...", file=sys.stderr)
    moss.query(metadata_query)
    moss.query(SoftwareList())
    moss.query(CorpusStat())

    count_sim = moss.query(Ranking.as_query(CountSimilarity()))
    jaccard_sim = moss.query(Ranking.as_query(JaccardSimilarity()))
    tf_idf_sim = moss.query(Ranking.as_query(TfIdfSimilarity()))

    with tf_idf_sim.top(args.top):

        moss.query(MostSimilar(tf_idf_sim, jaccard_sim, count_sim))

        if args.output_size == "medium":
            moss.query(MatchingLocations(tf_idf_sim))
        elif args.output_size == "long":
            moss.query(MatchingSnippets(tf_idf_sim, pre_lines=args.pre_lines,
                                        post_lines=args.post_lines))

    if verbose:
        print()
        print("="*80)
        print("To re-run the code, use (from {})"
              "".format(os.path.realpath(os.getcwd())))
        print(" ".join(sys.argv))
        # TODO shorten the paths stuff

    print(args.paths)