from testcontainers.core.container import DockerContainer
from testcontainers.core.wait_strategies import HealthcheckWaitStrategy

PORT = 3000


class BaseContainer(DockerContainer):
    def __init__(self, image: str, **kwargs):
        super().__init__(image=image, **kwargs)
        self.with_exposed_ports(PORT)
        self.waiting_for(HealthcheckWaitStrategy())

    @property
    def exposed_port(self) -> int:
        return self.get_exposed_port(PORT)


class Image(BaseContainer):
    def __init__(self, image="ghcr.io/data-privacy-stack/presidio-image-redactor", **kwargs):
        super().__init__(image=image, **kwargs)


class Analyzer(BaseContainer):
    def __init__(self, image="ghcr.io/data-privacy-stack/presidio-analyzer", **kwargs):
        super().__init__(image=image, **kwargs)

class Anonymizer(BaseContainer):
    def __init__(self, image="ghcr.io/data-privacy-stack/presidio-anonymizer", **kwargs):
        super().__init__(image=image, **kwargs)