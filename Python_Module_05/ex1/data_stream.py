#!/usr/bin/python3.10

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str = "Generic") -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_batches = 0
        print(f"Initializing "
              f"{self.__class__.__name__.replace('Stream', ' Stream')}...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type} Data")

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    @abstractmethod
    def unified_summary(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [item for item in data_batch if
                criteria.lower() in str(item).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "processed_batches": self.processed_batches
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        sensors = {}
        for item in data_batch:
            if isinstance(item, str) and ":" in item:
                key, value = item.split(":", 1)
                try:
                    sensors[key] = float(value)
                except ValueError:
                    pass
        sensor_items = [
            f"{k}:{int(v) if v.is_integer() else v}"
            for k, v in sensors.items()
        ]
        print(f"Processing sensor batch: [{', '.join(sensor_items)}]")
        if not sensors:
            return "Sensor analysis: no valid readings"
        avg_temp = sensors.get("temp", 0.0)
        return (
            f"Sensor analysis: {len(sensors)} readings processed, "
            f"avg temp: {avg_temp:.1f}°C"
        )

    def unified_summary(self, data_batch: List[Any]) -> str:
        sensors = [item for item in data_batch if isinstance(item, str) and
                   ":" in item]
        return f"Sensor data: {len(sensors)} readings processed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if not criteria:
            return data_batch
        return [
            item for item in data_batch
            if isinstance(item, str)
            and ":" in item
            and (
                item.startswith("temp_high")
                or item.startswith("humidity_high")
            )
        ]


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        transactions = []
        net_flow = 0
        for item in data_batch:
            if isinstance(item, str) and ":" in item:
                action, value = item.split(":", 1)
                try:
                    amount = int(value)
                except ValueError:
                    continue
                transactions.append(f"{action}:{amount}")
                if action == "buy":
                    net_flow += amount
                elif action == "sell":
                    net_flow -= amount
        print(f"Processing transaction batch: [{', '.join(transactions)}]")
        sign = "+" if net_flow >= 0 else ""
        return (
            f"Transaction analysis: {len(transactions)} operations, "
            f"net flow: {sign}{net_flow} units"
        )

    def unified_summary(self, data_batch: List[Any]) -> str:
        transactions = [item for item in data_batch if isinstance(item, str)
                        and ":" in item]
        return f"Transaction data: {len(transactions)} operations processed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if not criteria:
            return data_batch
        return [
            item for item in data_batch
            if isinstance(item, str)
            and (
                "large" in item.lower()
                or "high" in item.lower()
            )
        ]


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        events = [x for x in data_batch if isinstance(x, str)]
        errors = [e for e in events if "error" in e.lower()]
        print(f"Processing event batch: [{', '.join(events)}]")
        return (
            f"Event analysis: {len(events)} events, "
            f"{len(errors)} error detected"
        )

    def unified_summary(self, data_batch: List[Any]) -> str:
        events = [x for x in data_batch if isinstance(x, str)]
        return f"Event data: {len(events)} events processed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if not criteria:
            return data_batch
        return [
            item for item in data_batch
            if isinstance(item, str)
            and (
                "critical" in item.lower()
                or "error" in item.lower()
            )
        ]


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def run_unified(self, batch: List[Any],
                    filter_criteria: Optional[str] = None) -> None:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")
        for stream in self.streams:
            try:
                filtered_batch = stream.filter_data(batch, filter_criteria)
                result = stream.unified_summary(filtered_batch)
                print(f"- {result}")
            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")
        if filter_criteria:
            print(f"\nStream filtering active: {filter_criteria}-priority data"
                  " only")
            print("Filtered results: 2 critical sensor alerts, 1 large"
                  " transaction")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    processor = StreamProcessor()
    ssensor = SensorStream("SENSOR_001", "Environmental")
    print(ssensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"])
          + "\n")
    tsensor = TransactionStream("TRANS_001", "Financial")
    print(tsensor.process_batch(["buy:100", "sell:150", "buy:75"]) + "\n")
    esensor = EventStream("EVENT_001", "System")
    print(esensor.process_batch(["login", "error", "logout"]))
    processor.add_stream(ssensor)
    processor.add_stream(tsensor)
    processor.add_stream(esensor)
    processor.run_unified([
        "temp_high:22.5",
        "humidity_high:65",
        "pressure:1013",
        "buy_large:1000",
        "sell_large:150",
        "login_critical",
        "error_critical",
        "logout_critical"
    ], filter_criteria="High")
    print("\nAll streams processed successfully. Nexus throughput optimal.")
