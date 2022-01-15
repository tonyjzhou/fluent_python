import doctest
import sys

from fluent_python.abc.tombola import Tombola

TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'


def test(cls, verbose=False):
    res = doctest.testfile(
        TEST_FILE,
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE,
    )

    tag = "FAIL" if res.failed else "OK"

    print(TEST_MSG.format(cls.__name__, res, tag))


def main(argv):
    verbose = "-v" in argv
    real_subclasses = Tombola.__subclasses__()
    # virtual_subclasses = list(Tombola._abc_registry)

    for cls in real_subclasses:
        test(cls, verbose)


if __name__ == "__main__":
    main(sys.argv)
