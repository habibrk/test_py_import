from pkg.tests.test_foo import test_Foo
from pkg.tests.test_qux import test_qux

if __name__ == '__main__':

	print(test_Foo)

	test_Foo()

	print(test_qux)

	test_qux()