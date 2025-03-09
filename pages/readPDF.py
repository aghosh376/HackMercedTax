from pypdf import PdfReader
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import json
from PyPDFForm import PdfWrapper


reader = PdfReader("TaxForms/W-2_Tax_Form_2024.pdf")
page = reader.pages[0]

st.write(page.extract_text())
if '1545-0008' in page.extract_text():
    st.write("W-2 form found")
    
pdf_viewer("TaxForms/ScheduleCEng.pdf")



preview_stream = PdfWrapper("TaxForms/ScheduleCEng.pdf").preview

with open("output.pdf", "wb+") as output:
    output.write(preview_stream)
    pdf_viewer("output.pdf")

pdf_form_schema = PdfWrapper("TaxForms/ScheduleCEng.pdf").schema

st.json(json.dumps(pdf_form_schema, indent=4, sort_keys=False))

#filled = PdfWrapper("TaxForms/ScheduleCEng.pdf").fill(
#    {
#        "f1_1[0]": "sample_string_1",
#        "f1_2[0]": "abcdefghijk",   # maxLength is 11
#        "f1_3[0]": "sample_string_2",
#        "f1_4[0]": "abcdef",         # maxLength is 6
#        "f1_5[0]": "sample_string_3",
#        "f1_6[0]": "abcdefghi",      # maxLength is 9
#        "f1_7[0]": "sample_string_4",
#        "f1_8[0]": "sample_string_5",
#        "c1_1[0]": True,
#        "c1_1[1]": False,
#        "c1_1[2]": True,   
#    },
#)
def fill_pdf(pdf, data):
    """
    Fills a PDF form with the provided data.

    Args:
        pdf (str): A string representing the file path to the PDF file that will be filled.
                   The file path should point to a valid existing PDF file.
        data (dict): A dictionary where the keys represent the form field names and the values
                     represent the corresponding values to be filled in the PDF.

    
    Example:
        pdf_file = "path/to/pdf.pdf"
        data_dict = {"name": "John Doe", "age": "30"}
        filled_pdf = fill_pdf(pdf_file, data_dict)
    """
    return PdfWrapper(pdf).fill(data,)
test_values = {
    "f1_1[0]": "value1",
    "f1_2[0]": "test_123456",
    "f1_3[0]": "value3",
    "f1_4[0]": "abc123",
    "f1_5[0]": "value5",
    "f1_6[0]": "test_12345",
    "f1_7[0]": "value7",
    "f1_8[0]": "value8",
    "c1_1[0]": True,
    "c1_1[1]": False,
    "c1_1[2]": True,
    "f1_9[0]": "value9",
    "c1_2[0]": False,
    "c1_2[1]": True,
    "c1_3[0]": False,
    "c1_4[0]": True,
    "c1_4[1]": False,
    "c1_5[0]": True,
    "c1_5[1]": False,
    "c1_6[0]": True,
    "f1_10[0]": "value10",
    "f1_11[0]": "value11",
    "f1_12[0]": "value12",
    "f1_13[0]": "value13",
    "f1_14[0]": "value14",
    "f1_15[0]": "value15",
    "f1_16[0]": "value16",
    "f1_17[0]": "value17",
    "f1_18[0]": "value18",
    "f1_19[0]": "value19",
    "f1_20[0]": "value20",
    "f1_21[0]": "value21",
    "f1_22[0]": "value22",
    "f1_23[0]": "value23",
    "f1_24[0]": "value24",
    "f1_25[0]": "value25",
    "f1_26[0]": "value26",
    "f1_27[0]": "value27",
    "f1_28[0]": "value28",
    "f1_29[0]": "value29",
    "f1_30[0]": "value30",
    "f1_31[0]": "value31",
    "f1_32[0]": "value32",
    "f1_33[0]": "value33",
    "f1_34[0]": "value34",
    "f1_35[0]": "value35",
    "f1_36[0]": "value36",
    "f1_37[0]": "value37",
    "f1_38[0]": "value38",
    "f1_39[0]": "value39",
    "f1_40[0]": "value40",
    "f1_41[0]": "value41",
    "f1_42[0]": "value42",
    "f1_43[0]": "value43",
    "f1_44[0]": "value44",
    "f1_45[0]": "value45",
    "f1_46[0]": "value46",
    "c1_7[0]": True,
    "c1_7[1]": False,
    "c2_1[0]": True,
    "c2_2[0]": False,
    "c2_3[0]": True,
    "c2_4[0]": False,
    "c2_4[1]": True,
    "f2_1[0]": "value47",
    "f2_2[0]": "value48",
    "f2_3[0]": "value49",
    "f2_4[0]": "value50",
    "f2_5[0]": "value51",
    "f2_6[0]": "value52",
    "f2_7[0]": "value53",
    "f2_8[0]": "value54",
    "f2_9[0]": "01",
    "f2_10[0]": "02",
    "f2_11[0]": "1234",
    "f2_12[0]": "value55",
    "f2_13[0]": "value56",
    "f2_14[0]": "value57",
    "c2_5[0]": True,
    "c2_5[1]": False,
    "c2_6[0]": True,
    "c2_6[1]": False,
    "c2_7[0]": True,
    "c2_7[1]": False,
    "c2_8[0]": True,
    "c2_8[1]": False,
    "f2_15[0]": "value58",
    "f2_16[0]": "value59",
    "f2_17[0]": "value60",
    "f2_18[0]": "value61",
    "f2_19[0]": "value62",
    "f2_20[0]": "value63",
    "f2_21[0]": "value64",
    "f2_22[0]": "value65",
    "f2_23[0]": "value66",
    "f2_24[0]": "value67",
    "f2_25[0]": "value68",
    "f2_26[0]": "value69",
    "f2_27[0]": "value70",
    "f2_28[0]": "value71",
    "f2_29[0]": "value72",
    "f2_30[0]": "value73",
    "f2_31[0]": "value74",
    "f2_32[0]": "value75",
    "f2_33[0]": "value76"
}

filled = fill_pdf("TaxForms/ScheduleCEng.pdf", test_values)

with open("outputs/filled.pdf", "wb+") as output:
    output.write(filled.read())
    pdf_viewer("outputs/filled.pdf")


