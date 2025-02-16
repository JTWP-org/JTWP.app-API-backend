#!/bin/bash

# Ask if the user wants to generate a new primary API key (for a new curl set)
read -p "Do you want to generate a new primary API key? (y/n) " update_primary

if [ "$update_primary" = "y" ] || [ "$update_primary" = "Y" ]; then
    # Generate a new primary API key (32 hex characters)
    API_KEY=$(openssl rand -hex 16)
    echo "Generated primary API Key: $API_KEY"

    # Update or create the .env file with the new key
    ENV_FILE=".env"
    if [ -f "$ENV_FILE" ]; then
        # Replace existing API_KEY line with new key
        sed -i.bak "s/^API_KEY=.*/API_KEY=$API_KEY/" "$ENV_FILE"
    else
        echo "API_KEY=$API_KEY" > "$ENV_FILE"
    fi
    echo ".env file updated with new primary API key."

    # Create a hidden Markdown file with the curl commands containing the new API key
    DEFAULT_MD="docs/default_curl.md"
    HIDDEN_MD="docs/.built_curls.md"
    if [ -f "$DEFAULT_MD" ]; then
        cp "$DEFAULT_MD" "$HIDDEN_MD"
        sed -i.bak "s/API_KEY_HERE/$API_KEY/g" "$HIDDEN_MD"
        echo "Hidden Markdown file $HIDDEN_MD created with the new primary API key."
    else
        echo "Warning: Default Markdown file $DEFAULT_MD not found."
    fi
fi

# Ask if the user wants to generate a secondary API key for a second party
read -p "Do you want to generate a new secondary API key? (y/n) " secondary_choice

if [ "$secondary_choice" = "y" ] || [ "$secondary_choice" = "Y" ]; then
    # Generate a new secondary API key
    SECONDARY_KEY=$(openssl rand -hex 16)
    echo "Generated secondary API Key: $SECONDARY_KEY"

    # Append the new secondary API key to a secondary key file
    SECONDARY_FILE="secondary_keys.txt"
    echo "$SECONDARY_KEY" >> "$SECONDARY_FILE"
    echo "Secondary API key appended to $SECONDARY_FILE."
fi

echo "Setup complete."