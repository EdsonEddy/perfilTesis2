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

import argparse


def select_parser_factory(lang):
    import pygments.lexers
    if lang is None:
        return Parser
    else:
        return partial(Parser, lexer=pygments.lexers.get_lexer_by_name(lang))

def local_moss(args1):
    
    args = args1
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

    """
    if verbose:
        print("Building index and matching graph...", file=sys.stderr)
    """
    moss.build_index(softwares, reference)
    """
    if verbose:
        print("Querying...", file=sys.stderr)
    """
    #moss.query(metadata_query)
    #moss.query(SoftwareList())
    #moss.query(CorpusStat())

    count_sim = moss.query(Ranking.as_query(CountSimilarity()))
    jaccard_sim = moss.query(Ranking.as_query(JaccardSimilarity()))
    tf_idf_sim = moss.query(Ranking.as_query(TfIdfSimilarity()))

    """
    with tf_idf_sim.top(args.top):

        moss.query(MostSimilar(tf_idf_sim, jaccard_sim, count_sim))

        if args.output_size == "medium":
            moss.query(MatchingLocations(tf_idf_sim))
        elif args.output_size == "long":
            moss.query(MatchingSnippets(tf_idf_sim, pre_lines=args.pre_lines,
                                     post_lines=args.post_lines))
    """
    """
    if verbose:
        print()
        print("="*80)
        print("To re-run the code, use (from {})"
              "".format(os.path.realpath(os.getcwd())))
        print(" ".join(sys.argv))
        # TODO shorten the paths stuff

    """

    for _ in jaccard_sim:
        return round(_[0] * 100, 2)
    return 0