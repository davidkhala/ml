from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.document import ConversionResult
from docling.datamodel.extraction import ExtractionResult, ExtractionTemplateType
from docling.document_converter import DocumentConverter, FormatOption
from docling.document_extractor import DocumentExtractor, ExtractionFormatOption

from davidkhala.ml.ocr import Client


class Converter(Client):
    def __init__(self, format_options: dict[InputFormat, FormatOption] | None = None):
        self._ = DocumentConverter(
            format_options=format_options
        )

    def process(self, source: Path | str, **kwargs) -> ConversionResult:
        return self._.convert(source, **kwargs)


class Extractor(Client):
    """
    Beta preview
    """
    def __init__(self):
        self._ = DocumentExtractor(
            allowed_formats=[InputFormat.IMAGE, InputFormat.PDF]
            # known issue, you have to set allowed_formats, otherwise RuntimeError: No default extraction backend configured for InputFormat.DOCX
        )

    def process(self, source: Path | str, **kwargs) -> ExtractionResult:
        schema: ExtractionTemplateType = kwargs["schema"]
        return self._.extract(source, template=schema)
