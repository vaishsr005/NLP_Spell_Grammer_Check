from textblob import TextBlob
from language_tool_python import LanguageTool

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = LanguageTool('en-US')

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        matches = self.grammar_check.check(text)

        found_mistakes = []
        for mistake in matches:

            error_details = {
                'ruleId': mistake.ruleId,
                'message': mistake.message,
                'incorrect_word': text[mistake.offset:mistake.offset + mistake.errorLength],
                'suggestions': mistake.replacements
            }
            found_mistakes.append(error_details)
            #found_mistakes.append(mistake.ruleId)

        found_mistakes_count = len(found_mistakes)
        return found_mistakes, found_mistakes_count
    
