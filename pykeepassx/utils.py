import collections


def partition(pred, iterables):
    trues = list()
    falses = list()

    for i in iterables:
        if pred(i):
            trues.append(i)
        else:
            falses.append(i)

    return trues, falses


def flatten(l):
    for e in l:
        if isinstance(e, basestring):
            for ce in e:
                yield ce
        elif isinstance(e, collections.Iterable):
            for ce in flatten(e):
                yield ce
        else:
            yield e


def print_group_tree(group, level=0):
    print("{indent}***[{title}]***".format(indent=" " * level, title=group.title))
    for e in group.entries:
        print("{indent}-{title}".format(indent=" " * (level + 2), title=e.title))
    for g in group.children:
        print_group_tree(g, level + 4)