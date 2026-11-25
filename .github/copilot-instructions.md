# Copilot code review instructions
When reviewing Python code:
- Flag hard-coded secrets, SQL built by string concatenation, and subprocess shell=True.
- Flag missing None / empty-input handling and unclosed resources.
- Classify each finding as critical, high, medium or low.
- Suggest a concrete fix for every finding.
