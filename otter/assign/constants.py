"""
Constants (global variables) for Otter Assign
"""

import re

from jinja2 import Template

NB_VERSION = 4
BLOCK_QUOTE = "```"
COMMENT_PREFIX = "#"
TEST_HEADERS = ["TEST", "HIDDEN TEST"]
ALLOWED_NAME = re.compile(r'[A-Za-z][A-Za-z0-9_]*')
NB_VERSION = 4

TEST_REGEX = r"(##\s*(hidden\s*)?test\s*##|#\s*(hidden\s*)?test)"
OTTR_TEST_NAME_REGEX = r'''(?:testthat::)?test_that\(['"]([A-Za-z0-9_]+)['"],'''
MD_SOLUTION_REGEX = r"(<strong>|\*{2})solution:?(<\/strong>|\*{2})"
SEED_REGEX = r"##\s*seed\s*##"

OTTR_TEST_FILE_TEMPLATE = Template("""\
library(testthat)

test_metadata = "
{{ metadata }}
"
{% for test in tests %}
{{ test.body }}
{% endfor %}""")
