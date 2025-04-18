from ssml.core import SsmlBuilder

if __name__ == "__main__":
    ssml = (
        SsmlBuilder()
        .text("Welcome to SSML Builder!")
        .break_time(time="500ms")
        .say_as("2025", interpret_as="digits")
        .build()
    )
    print(ssml)