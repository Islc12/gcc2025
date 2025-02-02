#!/usr/bin/env python3


def unicode_to_readable(unicode_string):
    try:
        # Decode Unicode escapes into human-readable text
        readable_string = unicode_string.encode().decode('unicode_escape')
        return readable_string
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string with Unicode escapes (e.g., '\\u0041\\u0042\\u0043'): ")
    print("Human-readable text:", unicode_to_readable(input_string))

