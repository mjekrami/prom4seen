from .range import Range
from prometheus_api_client import PrometheusConnect

class Prometheus:
    def __init__(self, url: str, ssl: bool = False) -> None:
        self.prom_client = PrometheusConnect(url,disable_ssl=ssl)
        if not self.prom_client.check_prometheus_connection():
            raise ConnectionError(f"Could not connect to prometheus {url}")

    def cpu_usage(self, range: Range):
        metric = self.prom_client.custom_query_range(
        query = f"100 - (avg(rate(node_cpu_seconds_total{range.step})) * 100)",
        **range
        )
        
        return metric

    def memory_usage(self):
        pass
    
    def disk_usage(self):
        pass
