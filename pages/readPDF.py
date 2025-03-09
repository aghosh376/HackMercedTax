from pypdf import PdfReader
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import json
from PyPDFForm import PdfWrapper
from google.genai import Client
import config

API_KEY = config.api 
client = Client(api_key=API_KEY)


reader = PdfReader("TaxForms/W-2_Tax_Form_2024.pdf")
page = reader.pages[0]

st.write(page.extract_text())
if '1545-0008' in page.extract_text():
    st.write("W-2 form found")
    
pdf_viewer("TaxForms/2024_Form_1040.pdf")



preview_stream = PdfWrapper("TaxForms/2024_Form_1040.pdf").preview

with open("output.pdf", "wb+") as output:
    output.write(preview_stream)
    pdf_viewer("output.pdf")

pdf_form_schema = PdfWrapper("TaxForms/2024_Form_1040.pdf").schema

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

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_information_with_llm(text, field_structure):
    # Creating a prompt to extract the data in the required structure
    prompt = f"Extract information from the following text and map it to the provided field structure. Fields: {field_structure}\n\nText:\n{text}"

    try:
        # Calling the Gemini API to generate the content
        response = client.models.generate_text(
            model="gemini-2.0-flash",  # You can change the model name if necessary
            prompt=prompt,
            temperature=0.7,
            max_output_tokens=1500
        )
        st.write("Raw Response from Gemini API:", response)
        # Extracting the generated text from the response
        return 

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Function to parse the extracted data and fill it into the dictionary
def fill_fields(pdf_path, field_structure):
    text = extract_text_from_pdf(pdf_path)
    filled_data = extract_information_with_llm(text, field_structure)
    
    return filled_data

field_structure = {
    "f1_01[0]":{
    "type":"string"
    },
    "f1_02[0]":{
    "type":"string"
    },
    "f1_03[0]":{
    "type":"string",
    "maxLength":2
    },
    "f1_04[0]":{
    "type":"string"
    },
    "f1_05[0]":{
    "type":"string"
    },
    "f1_06[0]":{
    "type":"string",
    "maxLength":9
    },
    "f1_07[0]":{
    "type":"string"
    },
    "f1_08[0]":{
    "type":"string"
    },
    "f1_09[0]":{
    "type":"string",
    "maxLength":9
    },
    "f1_10[0]":{
    "type":"string"
    },
    "f1_11[0]":{
    "type":"string"
    },
    "f1_12[0]":{
    "type":"string"
    },
    "f1_13[0]":{
    "type":"string"
    },
    "f1_14[0]":{
    "type":"string"
    },
    "f1_15[0]":{
    "type":"string"
    },
    "f1_16[0]":{
    "type":"string"
    },
    "f1_17[0]":{
    "type":"string"
    },
    "c1_1[0]":{
    "type":"boolean"
    },
    "c1_2[0]":{
    "type":"boolean"
    },
    "c1_3[0]":{
    "type":"boolean"
    },
    "c1_3[1]":{
    "type":"boolean"
    },
    "c1_3[2]":{
    "type":"boolean"
    },
    "f1_18[0]":{
    "type":"string"
    },
    "c1_4[0]":{
    "type":"boolean"
    },
    "f1_19[0]":{
    "type":"string"
    },
    "c1_5[0]":{
    "type":"boolean"
    },
    "c1_5[1]":{
    "type":"boolean"
    },
    "c1_6[0]":{
    "type":"boolean"
    },
    "c1_7[0]":{
    "type":"boolean"
    },
    "c1_8[0]":{
    "type":"boolean"
    },
    "c1_9[0]":{
    "type":"boolean"
    },
    "c1_10[0]":{
    "type":"boolean"
    },
    "c1_11[0]":{
    "type":"boolean"
    },
    "c1_12[0]":{
    "type":"boolean"
    },
    "c1_13[0]":{
    "type":"boolean"
    },
    "f1_20[0]":{
    "type":"string"
    },
    "f1_21[0]":{
    "type":"string",
    "maxLength":9
    },
    "f1_22[0]":{
    "type":"string"
    },
    "c1_14[0]":{
    "type":"boolean"
    },
    "c1_15[0]":{
    "type":"boolean"
    },
    "f1_23[0]":{
    "type":"string"
    },
    "f1_24[0]":{
    "type":"string",
    "maxLength":9
    },
    "f1_25[0]":{
    "type":"string"
    },
    "c1_16[0]":{
    "type":"boolean"
    },
    "c1_17[0]":{
    "type":"boolean"
    },
    "f1_26[0]":{
    "type":"string"
    },
    "f1_27[0]":{
    "type":"string",
    "maxLength":9
    },
    "f1_28[0]":{
    "type":"string"
    },
    "c1_18[0]":{
    "type":"boolean"
    },
    "c1_19[0]":{
    "type":"boolean"
    },
    "f1_29[0]":{
    "type":"string"
    },
    "f1_30[0]":{
    "type":"string",
    "maxLength":9
    },
    "f1_31[0]":{
    "type":"string"
    },
    "c1_20[0]":{
    "type":"boolean"
    },
    "c1_21[0]":{
    "type":"boolean"
    },
    "f1_32[0]":{
    "type":"string"
    },
    "f1_33[0]":{
    "type":"string"
    },
    "f1_34[0]":{
    "type":"string"
    },
    "f1_35[0]":{
    "type":"string"
    },
    "f1_36[0]":{
    "type":"string"
    },
    "f1_37[0]":{
    "type":"string"
    },
    "f1_38[0]":{
    "type":"string"
    },
    "f1_39[0]":{
    "type":"string"
    },
    "f1_40[0]":{
    "type":"string"
    },
    "f1_41[0]":{
    "type":"string"
    },
    "f1_42[0]":{
    "type":"string"
    },
    "f1_43[0]":{
    "type":"string"
    },
    "f1_44[0]":{
    "type":"string"
    },
    "f1_45[0]":{
    "type":"string"
    },
    "f1_46[0]":{
    "type":"string"
    },
    "f1_47[0]":{
    "type":"string"
    },
    "f1_48[0]":{
    "type":"string"
    },
    "f1_49[0]":{
    "type":"string"
    },
    "f1_50[0]":{
    "type":"string"
    },
    "f1_51[0]":{
    "type":"string"
    },
    "c1_22[0]":{
    "type":"boolean"
    },
    "c1_23[0]":{
    "type":"boolean"
    },
    "f1_52[0]":{
    "type":"string"
    },
    "f1_53[0]":{
    "type":"string"
    },
    "f1_54[0]":{
    "type":"string"
    },
    "f1_55[0]":{
    "type":"string"
    },
    "f1_56[0]":{
    "type":"string"
    },
    "f1_57[0]":{
    "type":"string"
    },
    "f1_58[0]":{
    "type":"string"
    },
    "f1_59[0]":{
    "type":"string"
    },
    "f1_60[0]":{
    "type":"string"
    },
    "c2_1[0]":{
    "type":"boolean"
    },
    "c2_2[0]":{
    "type":"boolean"
    },
    "c2_3[0]":{
    "type":"boolean"
    },
    "f2_01[0]":{
    "type":"string"
    },
    "f2_02[0]":{
    "type":"string"
    },
    "f2_03[0]":{
    "type":"string"
    },
    "f2_04[0]":{
    "type":"string"
    },
    "f2_05[0]":{
    "type":"string"
    },
    "f2_06[0]":{
    "type":"string"
    },
    "f2_07[0]":{
    "type":"string"
    },
    "f2_08[0]":{
    "type":"string"
    },
    "f2_09[0]":{
    "type":"string"
    },
    "f2_10[0]":{
    "type":"string"
    },
    "f2_11[0]":{
    "type":"string"
    },
    "f2_12[0]":{
    "type":"string"
    },
    "f2_13[0]":{
    "type":"string"
    },
    "f2_14[0]":{
    "type":"string"
    },
    "f2_15[0]":{
    "type":"string"
    },
    "f2_16[0]":{
    "type":"string"
    },
    "f2_17[0]":{
    "type":"string"
    },
    "f2_18[0]":{
    "type":"string"
    },
    "f2_19[0]":{
    "type":"string"
    },
    "f2_20[0]":{
    "type":"string"
    },
    "f2_21[0]":{
    "type":"string"
    },
    "f2_22[0]":{
    "type":"string"
    },
    "f2_23[0]":{
    "type":"string"
    },
    "c2_4[0]":{
    "type":"boolean"
    },
    "f2_24[0]":{
    "type":"string"
    },
    "f2_25[0]":{
    "type":"string",
    "maxLength":9
    },
    "c2_5[0]":{
    "type":"boolean"
    },
    "c2_5[1]":{
    "type":"boolean"
    },
    "f2_26[0]":{
    "type":"string",
    "maxLength":17
    },
    "f2_27[0]":{
    "type":"string"
    },
    "f2_28[0]":{
    "type":"string"
    },
    "f2_29[0]":{
    "type":"string"
    },
    "c2_6[0]":{
    "type":"boolean"
    },
    "c2_6[1]":{
    "type":"boolean"
    },
    "f2_30[0]":{
    "type":"string"
    },
    "f2_31[0]":{
    "type":"string"
    },
    "f2_32[0]":{
    "type":"string",
    "maxLength":5
    },
    "f2_33[0]":{
    "type":"string"
    },
    "f2_34[0]":{
    "type":"string",
    "maxLength":6
    },
    "f2_35[0]":{
    "type":"string"
    },
    "f2_36[0]":{
    "type":"string",
    "maxLength":6
    },
    "f2_37[0]":{
    "type":"string"
    },
    "f2_38[0]":{
    "type":"string"
    },
    "f2_39[0]":{
    "type":"string"
    },
    "f2_40[0]":{
    "type":"string",
    "maxLength":11
    },
    "c2_7[0]":{
    "type":"boolean"
    },
    "f2_41[0]":{
    "type":"string"
    },
    "f2_42[0]":{
    "type":"string"
    },
    "f2_43[0]":{
    "type":"string"
    },
    "f2_44[0]":{
    "type":"string",
    "maxLength":10
    }
}

uploaded_file = st.file_uploader("Upload Your W2", type=["pdf"])
if uploaded_file is not None:
    filled_data = fill_fields(uploaded_file, field_structure)

    st.write(filled_data)
    filled = fill_pdf("TaxForms/2024_Form_1040.pdf", filled_data)

    with open("outputs/filled.pdf", "wb+") as output:
        output.write(filled.read())
        pdf_viewer("outputs/filled.pdf")