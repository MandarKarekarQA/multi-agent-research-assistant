import time


class CostTracker:
    """
    Simple cost tracker for the local AI pipeline.
    Since we are using Ollama locally, API cost is £0.
    """

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.model_name = "mistral"
        self.model_mode = "Local - Ollama"
        self.agent_count = 4
        self.api_cost_gbp = 0.00

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def get_metrics(self) -> dict:
        execution_time = 0

        if self.start_time and self.end_time:
            execution_time = round(self.end_time - self.start_time, 2)

        return {
            "model_name": self.model_name,
            "model_mode": self.model_mode,
            "agent_count": self.agent_count,
            "api_cost_gbp": self.api_cost_gbp,
            "execution_time_seconds": execution_time
        }