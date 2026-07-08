from os import PathLike

from davidkhala.utils.http_request import Request as RawRequest
from davidkhala.utils.http_request.on_response import file
from testcontainers.core.container import DockerContainer
from testcontainers.core.wait_strategies import HealthcheckWaitStrategy


class Image(DockerContainer):
    PORT = 3000

    def __init__(
            self, image: str = "ghcr.io/data-privacy-stack/presidio-image-redactor", **kwargs
    ):
        super().__init__(image=image, **kwargs)
        self.with_exposed_ports(self.PORT)
        self.waiting_for(HealthcheckWaitStrategy())

    @property
    def exposed_port(self) -> int:
        return self.get_exposed_port(self.PORT)


class Request(RawRequest):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

    def image_redact(self, *, source: PathLike, data: dict | None = None, target: PathLike):
        """
        curl -XPOST "http://localhost:3000/redact" -H "content-type: multipart/form-data" -F "image=@ocr_test.png" -F "data=\"{'color_fill':'255'}\"" > out.png
        """
        url = f"{self.base_url}/redact"

        self.on_response = file
        if not data:
            data = {}
        with open(source, "rb") as f:
            resp: bytes = self.request(url, method="POST", files={"image": (f.name, f)}, data={"data": str(data)})

        with open(target, "wb") as out:
            out.write(resp)
