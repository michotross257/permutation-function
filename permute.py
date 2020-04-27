from typing import Sequence


def permute(seq):
    """
    Permute a sequence.

    Args:
        seq(Typing.sequence): a sequence to be permuted

    Returns:
        generator: generator that can be iterated through to return permutations
    """
    msg = "Arg 'seq' must be a sequence. See docs for typing.Sequence"
    assert isinstance(seq, Sequence), msg
    if len(seq) == 2:
        for i in [(seq[0], seq[1]), (seq[1], seq[0])]:
            yield i
    else:
        for index in range(len(seq)):
            if index == 0:
                for i in permute(seq[1:]):
                    yield (seq[index],) + i
            else:
                for i in permute(seq[0:index] + seq[index+1:]):
                    yield (seq[index],) + i
