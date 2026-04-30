from pathlib import Path
from .deterministic_review_agent import write_proposal

def run_linter_proposal():
 body='# Linter Proposal Ideas\n\n- Add acronym consistency rule for hard sci-fi terms.\n- Add timeline date contradiction checker.\n'
 write_proposal(Path('proposals/linters/linter_proposals.md'),'linter_proposal_agent',body,['generated/lint/lint-summary.json'])
