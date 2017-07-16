# Using Patching For Faster Odoo Tests
Example Odoo module to show off how to patch Odoo registries (http://colinwren.is/patching-out-registries-in-odoo-tests.html)

## Test Times
Run One:
 - test_demo:  Ran 2 tests in 0.025s
 - test_mock:  Ran 2 tests in 0.002s
 - test_setup: Ran 2 tests in 0.354s
 
Run Two:
 - test_demo:  Ran 2 tests in 0.033s
 - test_mock:  Ran 2 tests in 0.001s
 - test_setup: Ran 2 tests in 0.359s
 
Run Three:
 - test_demo:  Ran 2 tests in 0.034s
 - test_mock:  Ran 2 tests in 0.002s
 - test_setup: Ran 2 tests in 0.354s
 
Averages:
 - test_demo:  0.030s
 - test_mock:  0.002s
 - test_setup: 0.355s
