from fpdf import FPDF  
  
def create_pdf(input_string, output_file):  
    pdf = FPDF()  
  
    # Add a page  
    pdf.add_page()  
  
    # Set font  
    pdf.set_font("Arial", size = 15)  
  
    # Add a cell  
    pdf.cell(200, 10, txt = input_string, ln = True, align = 'C')  
  
    # Save the pdf with name .pdf  
    pdf.output(output_file)  
  
# Usage:  
create_pdf("Hello World", "test.pdf")  
