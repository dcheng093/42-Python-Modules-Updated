import sys
import importlib
REQUIRED_PACKAGES = ["pandas", "numpy", "requests", "matplotlib"]

DISPLAY_MESSAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    missing = []
    for package in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown version")
            if package in DISPLAY_MESSAGES:
                message = DISPLAY_MESSAGES[package]
                print(f"[OK] {package} ({version}) - {message}")
        except ImportError:
            print(f"[MISSING] {package}")
            missing.append(package)
    if missing:
        print("\nSome dependencies are missing.")
        print("Install using pip:")
        print("  pip install -r requirements.txt\n")
        print("Or using Poetry:")
        print("  poetry install")
        sys.exit(1)


def run_analysis():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=["Signal"])
    print("Generating visualization...")
    plt.figure()
    plt.plot(df["Signal"])
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Index")
    plt.ylabel("Signal Value")
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    check_dependencies()
    run_analysis()
