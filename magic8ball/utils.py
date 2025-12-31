import hashlib

# Classic Magic 8-Ball responses
MAGIC8BALL_ANSWERS = [
    # Positive (10)
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",

    # Non-committal (5)
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",

    # Negative (5)
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]


def get_magic8ball_answer(question):
    """
    Generate a consistent answer for a given question using hash.

    Args:
        question (str): User's question

    Returns:
        str: Magic 8-ball answer

    Algorithm:
    1. Normalize question (lowercase, strip whitespace)
    2. Generate SHA256 hash
    3. Convert hash to integer
    4. Modulo by number of answers to get index
    5. Return answer at that index
    """
    # Normalize the question for consistency
    normalized_question = question.lower().strip()

    # Generate hash
    hash_object = hashlib.sha256(normalized_question.encode('utf-8'))
    hash_hex = hash_object.hexdigest()

    # Convert to integer and get index
    hash_int = int(hash_hex, 16)
    answer_index = hash_int % len(MAGIC8BALL_ANSWERS)

    return MAGIC8BALL_ANSWERS[answer_index]
