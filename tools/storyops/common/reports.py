def markdown_table(headers, rows):
    out = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---']*len(headers)) + ' |']
    out += ['| ' + ' | '.join(map(str,r)) + ' |' for r in rows]
    return '\n'.join(out)
