import os
import pytest
from app import llm_pipeline, file_preprocessing, displayPDF  # Replace 'my_streamlit_app' with your script name

# Define test cases

# Test case 1: Test llm_pipeline function
def test_llm_pipeline():
    # Create a sample PDF file path for testing
    sample_pdf_path = "sample.pdf"
    
    # Call the llm_pipeline function and capture the summary
    summary = llm_pipeline(sample_pdf_path)
    
    # Assert that the summary is not empty
    assert summary.strip() != ""

# Test case 2: Test file_preprocessing function
def test_file_preprocessing():
    # Create a sample PDF file path for testing
    sample_pdf_path = "QUANTUM NEXUS - storyline.pdf"
    
    # Call the file_preprocessing function and capture the result
    result = file_preprocessing(sample_pdf_path)
    
    # Assert that the result is not empty
    assert result.strip() != ""

# Test case 3: Test displayPDF function
def test_displayPDF():
    # Create a sample PDF file path for testing
    sample_pdf_path = "sample.pdf"
    
    # Call the displayPDF function
    display = displayPDF(sample_pdf_path)
    
    # Assert that the display is not empty
    assert display.strip() != ""

# Test case 4: Test the main function
def test_main():
    # Mock file_uploader and run the main function with a sample PDF file
    with pytest.raises(SystemExit):
        os.environ['STREAMLIT_TEST'] = 'true'
        from streamlit.testing import test_cmd_line
        test_cmd_line.main("my_streamlit_app.py", "--upload-file", "sample.pdf", "--", "Summarize")

# This allows you to run pytest from the command line
if name == "main":
    pytest.main([os.path.basename(file)])
