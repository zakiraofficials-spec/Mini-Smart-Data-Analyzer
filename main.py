import os
import numpy as np
from dotenv import load_dotenv

# Load settings from the local .env file, if it exists.
load_dotenv()


def analyze_numbers(raw_numbers):
    """Validate comma-separated input and calculate useful statistics."""
    if not raw_numbers:
        raise ValueError("Please enter at least 10 numbers, separated by commas.")

    parts = raw_numbers.split(",")

    if len(parts) < 10:
        raise ValueError("Please enter at least 10 numbers.")

    try:
        numbers = [float(part.strip()) for part in parts]
    except ValueError:
        raise ValueError("Every value must be a valid number. Separate numbers with commas.")

    if not all(np.isfinite(numbers)):
        raise ValueError("Please enter normal finite numbers only (no NaN or infinity).")

    data = np.array(numbers, dtype=float)
    mean_value = float(np.mean(data))
    median_value = float(np.median(data))
    above_mean = data[data > mean_value]

    return {
        "count": int(data.size),
        "mean": mean_value,
        "median": median_value,
        "maximum": float(np.max(data)),
        "minimum": float(np.min(data)),
        "sum": float(np.sum(data)),
        "sorted_values": [float(value) for value in np.sort(data)],
        "above_mean": [float(value) for value in above_mean],
    }


def get_ai_analysis(results):
    """Ask Groq to explain the statistics. Return a friendly message on failure."""
    api_key = os.getenv("GROQ_API_KEY", "").strip()

    if not api_key or api_key == "your_groq_api_key_here":
        return (
            "AI analysis is not available yet because GROQ_API_KEY is missing. "
            "Add your key to the local .env file and restart the application. "
            "Your numerical results above were still calculated successfully."
        )

    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        summary = (
            f"Number count: {results['count']}\n"
            f"Mean: {results['mean']}\n"
            f"Median: {results['median']}\n"
            f"Maximum: {results['maximum']}\n"
            f"Minimum: {results['minimum']}\n"
            f"Sum: {results['sum']}\n"
            f"Values above mean: {results['above_mean']}\n"
        )

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a friendly data tutor. Explain numerical statistics "
                        "in simple English suitable for a Class 9 student. Explain "
                        "what the mean and median suggest, mention the range from "
                        "minimum to maximum, and describe values above the mean. "
                        "Use short paragraphs and do not invent facts."
                    ),
                },
                {"role": "user", "content": "Explain these results:\n" + summary},
            ],
            temperature=0.4,
            max_tokens=500,
        )
        return response.choices[0].message.content.strip() or "The AI returned an empty response."
    except Exception as exc:
        # The detailed exception is useful in the terminal, not on the public page.
        print(f"Groq API error: {exc}")
        return (
            "The numbers were analyzed successfully, but the AI explanation could not "
            "be loaded. Check your API key, internet connection, model access, and "
            "Groq account, then try again."
        )


if __name__ == "__main__":
    # Quick calculation test: run with `python main.py`.
    sample = "12, 15, 18, 20, 22, 25, 28, 30, 32, 40"
    print("Sample analysis:")
    print(analyze_numbers(sample))
