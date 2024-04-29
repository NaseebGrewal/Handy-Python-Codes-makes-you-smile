"""
pip install pypdf2
"""
import PyPDF2


def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfWriter()

    for path in paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page])

    # Write out the merged PDF
    with open(output, "wb") as out:
        pdf_writer.write(out)


if __name__ == "__main__":
    # List of PDF files to merge
    pdfs = [
        "list_of_your_pdf_files.... with path, if in same director as code file, then use just name"
    ]

    # Output file name
    merge_pdfs(pdfs, "Define the name of your output file.pdf")
