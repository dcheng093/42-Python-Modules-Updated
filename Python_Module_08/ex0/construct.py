import sys
import os


def main():
    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    python_executable = sys.executable
    if in_venv:
        venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)
        site_packages = os.path.join(
            venv_path,
            "lib",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
            "site-packages"
        )
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\n"
              "the global system.")
        print(f"\nPackage installation path:\n{site_packages}")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate   # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
