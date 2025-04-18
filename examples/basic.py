from ssml.core import SsmlBuilder

if __name__ == "__main__":
    # Example text to test various SSML elements
    ssml = (
        SsmlBuilder()
        .text("Welcome to SSML Builder!")
        .break_time(time="700ms")
        .text("This library supports emphasis,")
        .say_as("2025-04-18", interpret_as="date", format="yyyy-MM-dd")
        .break_time(strength="strong")
        .text("enumeration of numbers like")
        .say_as("1, 2, 3", interpret_as="digits")
        .text("and subtle prosody adjustments.")
        # You can add more elements: Emphasis, Prosody, Audio, etc.
        .build()
    )
    print(ssml)
