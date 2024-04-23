import sys
from utils import string_to_cursor, press_enter

s = "spark.sql(f\"\"\""
string_to_cursor(s)

press_enter()

s = "\"\"\")"
string_to_cursor(s)


