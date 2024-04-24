from utils import string_to_cursor


s = "spark.sql(f\"\"\"\n\n\"\"\").createOrReplaceTempView(\"\")"
string_to_cursor(s)


