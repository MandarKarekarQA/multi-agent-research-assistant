class CostTracker:
    def __init__(self, model_name: str, model_mode: str):
        self.model_name = model_name
        self.model_mode = model_mode

    def get_metrics(self, agent_count: int, execution_time_seconds: float) -> dict:
        api_cost = 0.0

        if self.model_mode == "OpenAI Cloud":
            api_cost = "Estimated low cost - controlled by OpenAI budget limit"

        return {
            "model_name": self.model_name,
            "model_mode": self.model_mode,
            "agent_count": agent_count,
            "api_cost": api_cost,
            "execution_time_seconds": execution_time_seconds,
        }