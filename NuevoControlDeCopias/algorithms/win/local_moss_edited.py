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

def select_parser_factory(lang):
    import pygments.lexers
    if lang is None:
        return Parser
    else:
        return partial(Parser, lexer=pygments.lexers.get_lexer_by_name(lang))

def local_moss(args):
    """
    parser_factory = select_parser_factory(None)
    fingerprinter = Winnower(parser_factory, window, kgrams)
    filter = Filter(10)
    moss = MossEngine(fingerprinter, filter)
    softwares = Software.list_from_globs(paths)
    reference = None
    moss.build_index(softwares, reference)
    count_sim = moss.query(Ranking.as_query(CountSimilarity()))
    jaccard_sim = moss.query(Ranking.as_query(JaccardSimilarity()))
    tf_idf_sim = moss.query(Ranking.as_query(TfIdfSimilarity()))
    args = parser.parse_args()
    """

    parser_factory = select_parser_factory(args["language"])

    fingerprinter = Winnower(parser_factory, args["window_size"], args["kgram_len"])
    filter = Filter(args["collision_threshold"])

    moss = MossEngine(fingerprinter, filter)

    softwares = Software.list_from_globs(args["paths"])

    reference = None

    moss.build_index(softwares, reference)

    count_sim = moss.query(Ranking.as_query(CountSimilarity()))
    jaccard_sim = moss.query(Ranking.as_query(JaccardSimilarity()))
    tf_idf_sim = moss.query(Ranking.as_query(TfIdfSimilarity()))

    for _ in jaccard_sim:
        return round(_[0] * 100, 2)
    return 0