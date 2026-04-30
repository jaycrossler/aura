from .rules.prose import sentence_length,repeated_words,paragraph_length
from .rules.fiction import dialogue_speaker_tags
from .rules.continuity import missing_frontmatter,broken_cross_references
from .rules.interactive import html_safety
from .rules.audio import dialogue_attribution
RULES={
 'prose.sentence_length': sentence_length.run,
 'prose.repeated_words': repeated_words.run,
 'prose.paragraph_length': paragraph_length.run,
 'fiction.dialogue_speaker_tags': dialogue_speaker_tags.run,
 'continuity.missing_frontmatter': missing_frontmatter.run,
 'continuity.broken_cross_references': broken_cross_references.run,
 'interactive.html_safety': html_safety.run,
 'audio.dialogue_attribution': dialogue_attribution.run,
}
