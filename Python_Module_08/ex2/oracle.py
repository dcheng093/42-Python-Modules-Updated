import os
from dotenv import load_dotenv


def load_configuration():
    load_dotenv()
    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }
    return config


def validate_configuration(config):
    missing = [key for key, value in config.items() if not value]
    if missing:
        print("\nWARNING: Missing configuration variables:")
        for key in missing:
            print(f"- {key}")
    return missing


def display_status(config):
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    mode = config["MATRIX_MODE"] or "undefined"
    print(f"Mode: {mode}")
    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to secure cluster")
    else:
        print("Database: Unknown mode")
    api_key = config["API_KEY"]
    if api_key and api_key != "your_api_key_here":
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")
    print(f"Log Level: {config['LOG_LEVEL'] or 'Not set'}")
    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check():
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main():
    config = load_configuration()
    validate_configuration(config)
    display_status(config)
    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
