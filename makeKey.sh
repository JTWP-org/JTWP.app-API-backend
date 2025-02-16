#!/bin/bash

# Generate a 32-byte random string and encode it in hexadecimal
API_KEY=$(openssl rand -hex 16)

# Output only the generated API key
echo $API_KEY
