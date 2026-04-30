def progress_snapshot(state):
    s=state['summary']
    return {'ts': state['last_updated_utc'], 'knowledge_files': s['knowledge_files'], 'manuscript_files': s['manuscript_files'], 'open_questions_sections': s['open_questions_sections']}
