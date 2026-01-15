from abc import ABC, abstractmethod


class Client(ABC):
	def _read(self,file:Path)->str:
		with open(file, "rb") as f:
			content = base64.b64encode(f.read()).decode('utf-8')
		return content
	@abstractmethod
	def process(self, file: Path, **kwargs) -> list[dict] | dict:...
