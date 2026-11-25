# Bugbot review rules
- Treat hard-coded secrets, SQL string concatenation and shell=True as blocking bugs.
- Flag division by zero, None dereference and unclosed resources.
- Prefer minimal fixes that keep public function signatures unchanged.
