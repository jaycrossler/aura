from .chapter_generator import generate_chapter

def run_item(item):
    if item.get('kind')=='chapter_draft': return generate_chapter(item)
    return None
