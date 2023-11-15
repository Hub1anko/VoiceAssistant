#!/usr/bin/env python3

import yaml
import sys

def get_user_input(prompt, default):
    user_input = input(f"{prompt} (default: {default}): ")
    return user_input if user_input.strip() != '' else default

def save_to_yaml(config):
    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)

def main():
    print("Welcome to the Installation Script")

    # Set default values
    default_url = "http://homeassistant.local"
    default_port = "8123"

    # Get user input for URL, port, and token
    url = get_user_input("Enter the URL address", default_url)
    port = get_user_input("Enter the port", default_port)
    token = input("Enter the token: (For access token go to home assistant -> profile -> Long-Lived Access Tokens): ")
    config = {
        'address': {
            'url': url,
            'port': port,
        },
        'token': token
    }
    
    save_to_yaml(config)
    print("\nInstallation parameters:")
    print(f"URL: {url}")
    print(f"Port: {port}")
    print(f"Token: {token}")

    # Here you can perform the installation steps using the provided parameters
    # For simplicity, let's just print a message indicating the installation is complete.
    print("\nInstallation complete!")

if __name__ == "__main__":
    main()


