import sys
import re

models = sys.stdin.read()

models = re.sub(
    "(.*class Meta:)",
    r"""    @classmethod
    def _check_fields(cls, **kwargs):
        return []

\1""",
    models,
)

print(models)
