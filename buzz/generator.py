import random

buzz = ('continious testing', 'continious integration', 
        'continious deployment', 'continious impovement', 'devops')
adjectives = ('complete', 'modern', 'sel-service', 'integrated', 'end-to-end')
adverbs = ('ramarkably', 'enormously', 'substantially', 'significantly',
           'seriously')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')

def sample(l: list, n : int = 1) -> str:
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz() -> str:
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
        sample(verbs), buzz_terms[1]])
    return phrase.title()

if __name__ == '__main__':
    print(generate_buzz())
