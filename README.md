# pwHash

![Python](https://img.shields.io/badge/python-v3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Maintenance](https://img.shields.io/badge/maintained-yes-brightgreen)

Generate hashes from passwords in seconds!!

## Features

- Supports multiple hash functions: `md5`, `sha1`, `sha256`, `sha384`, `sha512`
- Command-line arguments for quick usage
- Interactive mode for step-by-step guidance
- Colorful output for better readability

## Usage

### Command-Line Arguments

You can specify the password and the hash function directly using command-line arguments.

```sh
python3 hasher.py -p <password> -f <hash_function>
```

**Example:**

```sh
python3 hasher.py -p mypassword -f sha256
```

### Interactive Mode

You can also run the script in interactive mode to be guided through the process.

```sh
python3 hasher.py -i
```

### Supported Hash Functions

- `md5`
- `sha1`
- `sha256`
- `sha384`
- `sha512`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/zanesense/hasher.git
    cd pwHash
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Requirements

- Python 3.7+
- `huepy` library

You can install the required library using pip:

```sh
pip install huepy
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

zaneee

Feel free to contribute to this project by submitting issues or pull requests. Any help is appreciated!
```
