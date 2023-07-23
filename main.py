from base64 import b64encode, b64decode
import sys

main_arg = sys.argv[1]
string = "".join(sys.argv[2:])


def output_to_string(output):
    output = output.decode("utf-8")
    output.replace("'", "")
    output.replace("b", "")
    print(output)


if main_arg == "-h":
    print(
        "Usage: python3 main.py [option] [string]"
        "\n\nOptions:\n-e\tEncode string\n-d\tDecode string\n-h\tShow this help message"
    )
else:
    match main_arg:
        case "-e":
            output_to_string(b64encode(string.encode("utf-8")))

        case "-d":
            output_to_string(b64decode(string.encode("utf-8")))
