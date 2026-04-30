import argparse
from .load_agents import load_agents
from .deterministic_review_agent import run_master_continuity, run_character_voice
from .linter_proposal_agent import run_linter_proposal
p=argparse.ArgumentParser(); p.add_argument('--agent-id'); a=p.parse_args()
for ag in load_agents():
 if not ag.get('enabled',True): continue
 if a.agent_id and ag['id']!=a.agent_id: continue
 if ag['id']=='master_continuity': run_master_continuity()
 elif ag['id']=='character_voice': run_character_voice()
 elif ag['id']=='linter_proposal_agent': run_linter_proposal()
