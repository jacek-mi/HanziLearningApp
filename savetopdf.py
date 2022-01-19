from fpdf import FPDF

def saveLearningResults(state):
    if state.listOfLearnedCharacters:
        from fpdf import FPDF

        pdf = FPDF()
        pdf.add_page()

        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 14)
        pdf.write(10,"Learning Results\n")
        text = ""
        for key in state.listOfLearnedCharacters:
            text = text + key + '\n'

        for txt in text.split('\n'):
            pdf.write(8, txt)
            pdf.ln(8)



        pdf.output("result.pdf", 'F')