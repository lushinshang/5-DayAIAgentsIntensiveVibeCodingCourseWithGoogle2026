import sys
from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
from docling.document_converter import DocumentConverter, PdfFormatOption


def convert_document(pdf_path: Path) -> None:
    input_file = pdf_path.resolve()
    output_dir = input_file.parent
    base_name = input_file.stem

    image_dir = output_dir / f"{base_name}_images_raw"
    md_output = output_dir / f"{base_name}.md"

    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
    pipeline_options.images_scale = 5.0
    pipeline_options.generate_page_images = False
    pipeline_options.generate_picture_images = True

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    print(f"Converting {input_file.name} with docling at images_scale=5.0...")
    result = converter.convert(input_file)

    md_text = result.document.export_to_markdown()
    md_output.write_text(md_text, encoding="utf-8")
    print(f"Markdown saved to: {md_output}")

    image_dir.mkdir(parents=True, exist_ok=True)
    for old_file in image_dir.glob("*.png"):
        old_file.unlink()

    image_count = 0
    for index, picture in enumerate(result.document.pictures or []):
        if hasattr(picture, "image") and picture.image:
            image_filename = image_dir / f"picture_{index:02d}.png"
            picture.image.pil_image.save(image_filename, format="PNG", dpi=(600, 600))
            image_count += 1
            print(f"[{index:02d}] saved {image_filename.name}")

    print(f"Extracted {image_count} raw pictures to: {image_dir}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        pdf = Path(sys.argv[1])
    else:
        pdf = Path(__file__).resolve().parents[1] / "source" / "Agent Skills_Day_3.pdf"
    convert_document(pdf)
