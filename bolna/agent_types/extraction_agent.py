from .base_agent import BaseAgent


class ExtractionContextualAgent(BaseAgent):
    def __init__(self, llm, prompt=None, log_dir_name=None):
        super().__init__(log_dir_name)
        self.brain = llm
        self.current_messages = 0
        self.is_inference_on = False
        self.has_intro_been_sent = False

    async def generate(self, history, stream=True, synthesize=False):
        self.logger.info("extracting json from the previous conversation data")
        json_data = await self.brain.generate(history, stream=False, synthesize=False, request_json=True)
        return json_data
