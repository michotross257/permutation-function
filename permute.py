def permute(seq):
    '''Permute an iterable. Returns a generator.'''
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
