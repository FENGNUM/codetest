# GraphQL Query

This project contains a Python script to query a GraphQL endpoint and transform the response data. Follow the steps below to set up and run the script locally.

## Prerequisites

- Python 3.6 or higher
- Homebrew (optional, for installing Python on macOS)

### Install Python and run the script

If you don't have Python installed, you can install it using Homebrew on macOS or on Windows you need to download python and add it to your PATH environment. For Unix you can use apt-get or other commands

```sh
brew install python

cd /path/to/your/project
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

pthon main.py

```

Expected output:

```json
{
  "average_swap_size_usd": "0.00",
  "pools": [
    {
      "token": "0xde104342b32bca03ec995f999181f7cf1ffc04d7",
      "current_price": "0"
    },
    {
      "token": "0x6437fdc89ced41941b97a9f1f8992d88718c81c5",
      "current_price": "0"
    },
    {
      "token": "0x22b9fa698b68bba071b513959794e9a47d19214c",
      "current_price": "0"
    }
  ]
}
