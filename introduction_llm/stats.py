import random


def token_count(dataset, tokenizer_callables, feature: str, num_samples: int) -> dict:

    num_samples = min(num_samples, len(dataset))
    sample_indices = random.sample(range(len(dataset)), k=num_samples)

    return {
        n: [len(tokenizer_callable(sample[feature])) for sample in dataset.select(sample_indices)]
        for n, tokenizer_callable in tokenizer_callables.items()
    }
