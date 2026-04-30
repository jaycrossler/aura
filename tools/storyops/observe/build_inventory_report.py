from tools.storyops.common.reports import markdown_table

def build_inventory(docs):
    rows=[(d['path'].as_posix(), d['words'], 'yes' if d['frontmatter'] else 'no') for d in docs]
    return '# Knowledge Inventory\n\n' + markdown_table(['File','Words','Frontmatter'], rows)
