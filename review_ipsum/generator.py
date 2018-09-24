import random

from .fixtures import SENTENCES


def create_review(number_of_sentences):
    """
    Create a generic containing (number_of_sentences) sentences.

    Args:
        number_of_sentences (int): The number of sentences desired.

    Returns:
        A paragraph of formatted sentences.
    """

    return " ".join(random.choice(SENTENCES) for _ in range(number_of_sentences))
