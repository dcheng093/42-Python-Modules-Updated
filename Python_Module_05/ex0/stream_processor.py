#!/usr/bin/python3.10

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def __init__(self):
        pass

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list)
            and all(isinstance(x, (int, float)) for x in data)
        )

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")
        count = len(data)
        total = sum(data)
        avg = total / count if count else 0
        return f"Processed {count} numeric values, sum={total}, avg={avg}"

    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):
    def __init__(self):
        pass

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")
        char_count = len(data)
        word_count = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"

    def format_output(self, result: str) -> str:
        return result


class LogProcessor(DataProcessor):
    def __init__(self):
        pass

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return any(data.startswith(level) for level in ("ERROR:", "INFO:",
                                                        "WARNING:"))

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log entry")
        level, message = data.split(":", 1)
        message = message.strip()
        return f"{level} level detected: {message}"

    def format_output(self, result: str) -> str:
        if result.startswith("ERROR"):
            return f"[ALERT] {result}"
        elif result.startswith("INFO"):
            return f"[INFO] {result}"
        else:
            return f"[WARNING] {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    print("Initializing Numeric Processor...")
    print(f"Processing data: {numeric_data}")
    print("Validation: Numeric data verified")
    output = numeric_processor.format_output(
        numeric_processor.process(numeric_data))
    print(f"Output: {output}\n")
    print("Initializing Text Processor...")
    print(f'Processing data: "{text_data}"')
    print("Validation: Text data verified")
    output = text_processor.format_output(text_processor.process(text_data))
    print(f"Output: {output}\n")
    print("Initializing Log Processor...")
    print(f'Processing data: "{log_data}"')
    print("Validation: Log entry verified")
    output = log_processor.format_output(log_processor.process(log_data))
    print(f"Output: {output}\n")
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    data_samples = [
        [1, 2, 3],
        "Twelve Chars",
        "INFO: System ready"
    ]
    for i, (processor, data) in enumerate(zip(processors, data_samples),
                                          start=1):
        result = processor.process(data)
        output = processor.format_output(result)
        print(f"Result {i}: {output}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
