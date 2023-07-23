# Python 🐍 base64 encoder/decoder CLI tool

### I made this tool to learn how to use the args parsing in python. If you think I could add some features, feel free to open an issue or a pull request !

## Usage 📖
```bash
python3 b64.py [-h] [-e] [-d] [string]
```

Encode a string:
```bash
$ python3 b64.py -e "Hello World"
SGVsbG8gV29ybGQ=
```

Decode a string:
```bash
$ python3 b64.py -d SGVsbG8gV29ybGQ=
Hello World
```

Get some help:
```bash
$ python3 b64.py -h
```

## Made with ❤️ by [babou](https://github.com/Babou-Dev)
