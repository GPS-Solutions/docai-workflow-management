# Project name
PROJECT_NAME = "claims-processing-dev"

# Attributes not required from specialized parser raw json
NOT_REQUIRED_ATTRIBUTES_FROM_SPECIALIZED_PARSER_RESPONSE = ["textStyles",
                                                            "textChanges",
                                                            "revisions",
                                                            "pages.image"]

# GCS temp folder to store async form parser output
GCS_OP_URI = "gs://async_form_parser"
FORM_PARSER_OP_TEMP_FOLDER = "temp"

"""
This is Document and state mapping dict Default entities sections have entities
that are coming from parser Derived section have information of entities which
are not extracted from parser and need to extract them by using pattern.
Create state wise mapping if it form parser, and one doc type mapping if it is
a specialized parser.
"""

MAPPING_DICT = {
  "unemployment_form_arizona": {
    "default_entities": {
      "Social Security Number:": ["Social Security Number"],
      "Date:": ["Date"],
      "Primary Phone: ": ["Employee Primary Phone"],
      "First Name": ["Employee First Name"],
      "Last Name": ["Employee Last Name"],
      "Mailing Address (No., Street, Apt., P.O. Box) ": [
        "Employee Mailing Address (No., Street, Apt., P.O.Box)"],
      "E-MAIL Address (Optional but Encouraged) ": [
        "Employee E-MAIL Address (Optional but Encouraged)"],
      "Gender": ["Employee Gender"],
      "Race": ["Employee Race"],
      "Ethnicity": ["Employee Ethnicity"],
      "Language": ["Employee Language"],
      "Mailing Address (No., Street, Apt., P.O. Box, City)": [
        "Employer Mailing Address (No., Street, Apt., P.O.Box, City)"],
      "Date": ["Date"],
      "City": ["Employee Residence City", "Employee City"],
      "State": ["Employee State", "Employee Residence State"],
      "State": ["Employer State"],
      "Employer's Phone No.": ["Employer's Phone No."],
      "Claimant's Signature": ["Claimant's Signature"],
      "Company's Name ": ["Company's Name"],
      "ZIP": ["Employee Residence ZIP", "Employee ZIP", "Employer ZIP"],
      "Month": ["Employee DOB Month", "Month (Last Day of Work)"],
      "Day": ["Employee DOB Day", "Day (Last Day of Work)"],
      "Year": ["Employee DOB Year", "Year (Last Day of Work)"]
    }
  },

  "unemployment_form_california": {
    "default_entities": {
      "Name of issuing State/entity": ["Name of issuing Stata/entity"],
      "Driver License Number": ["Driver License Number"],
      "Race": ["Employee Race"],
      "Ethnicity": ["Employee Ethnicity"],
      "Language": ["Employee Language"],
      "22. Employer name": ["Longest Employer name"],
      "Months": ["Months worked for longest employer"]
    },
    "derived_entities":
      {
        "What is your birth date?": {
          "rule": "What is your birth date\?\n\d\.(.*?)\((mm/dd/yyyy)"},
        "What is your gender?": {
          "rule": "What is your gender\?\n\d\.(.*?)\n\d"},
        "Expiration Date (EXP)": {
          "rule": "\sAlien Registration Number \(A#\)\n3\)\s(\d{4}-\d{2}-\d{2})\n"}}
  },

  "unemployment_form_arkansas": {
    "default_entities": {
      "TODAY'S DATE": ["TODAY'S DATE"],
      "SOCIAL SECURITY NUMBER": ["SOCIAL SECURITY NUMBER"],
      "EFFECTIVE DATE: (Local Office Only)": [
        "EFFECTIVE DATE: (Local Office Only)"],
      "FIRST NAME": ["EMPLOYEE FIRST NAME"],
      "MIDDLE INITIAL": ["EMPLOYEE MIDDLE INITIAL"],
      "LAST NAME": ["EMPLOYEE LAST NAME"],
      "Mailing Address": ["EMPLOYEE Mailing Address"],
      "State of Residence": ["Employee State of Residence"],
      "County of Residence": ["Employee County of Residence"],
      "DATE OF BIRTH": ["EMPLOYEE DATE OF BIRTH"],
      "EMPLOYER NAME": ["EMPLOYER NAME"],
      "STREET NAME": ["EMPLOYER STREET NAME"],
      "COUNTY": ["EMPLOYER COUNTY"],
      "EMPLOYER PHONE": ["EMPLOYER PHONE"],
      "FIRST DATE WORKED AT YOUR LAST JOB": [
        "FIRST DATE WORKED AT YOUR LAST JOB"],
      "DATE LAST WORK ENDED": ["DATE LAST WORK ENDED"],
      "What kind of work did you do on your last job": [
        "What kind of work did you do on your last job?"],
      "Date": ["Date"],
      "Signature": ["Signature"],
      "E-Mail Address": ["Employee E-Mail Address"]
    }
  },

  "unemployment_form_illinois": {
    "default_entities": {
      "Claimant ID": ["Claimant ID"],
      "SSN": ["SSN"],
      "First Name": ["Employee First Name"],
      "MI": ["Employee MI"],
      "Last Name": ["Employee Last Name"],
      "Date of Birth: (mm/dd/yyyy)": ["Date of Birth: (mm/dd/yyyy)"],
      "E-Mail Address": ["Employee E-Mail Address"],
      "Driver's License Number": ["Driving Licence Number"],
      "Primary Telephone": ["Employee Mailing Primary Telephone"],
      "Employer Name": ["Employer Name"],
      "Expiration Date": ["Expiration Date"],
      "Document Type": ["Document Type"],
      "Gender": ["Employee Gender"],
      "Ethnicity": ["Employee Ethinicity"],
      "Company Phone": ["Company Phone"],
      "For this period of employment, what date did you start": [
        "For this period of employment, what date did you start?"],
      "Last date worked": ["Last date worked"],
      "CLAIMANT SIGNATURE": ["CLAIMANT SIGNATURE"],
      "DATE": ["DATE"]
    }
  },

  "claims_form_arizona": {
    "default_entities": {
      "Social Security Number": ["Social Security Number"],
      "Name": ["Employee Name"],
      "Week Ending Date": ["Week Ending Date"],
      "What were your gross earnings before deductions?": [
        "What were your gross earnings before deductions?"],
      "What was your last day of work?": ["What was your last day of work?"],
      "Claimant's Signature": ["Claimant's Signature "]
    },
    "table_entities":
    {
      # 1. get header info from user and search that table
      # 2. name of entity row and col no
      # 3. map OCR to Col A
      # range of page_num or table_num starts from 0 to n-1
      # 'page_num': 0,
      # 'table_num': 0,
      # proper header name to be provided so that it does not match
      #  with other table
      # headers.
      # value of row and col should not be greater than the range of rows
      # and cols in the table
      "header": ["Date", "Name of Employer/Company/ Union and Address (City, State and Zip Code)",
								 "Website URL or Name of person contacted",
								 "Method (In person, Internet, mail)",
								 "Type of work sought", "Action taken on the date of contact"],
      "entity_extraction": [{"col": 0, "row_no": 1},
                            {"col": 1, "row_no": 2},
                            {"col": 2, "row_no": 3},
                            {"col": 3, "row_no": 4},
                            {"col": 4, "row_no": 1},
                            {"col": 3, "row_no": 1},
                            {"col": 2, "row_no": 2},
                            {"col": 0, "row_no": 4},
                          ],

      "max_rows": 3, # -1 for all rows
      # if 1 all columns will de extracted
      # if -1 check for specific columns
      "all_columns": -1,
      # if -1 uses column name
      "use_column_index": -1,
      # to use this feature make the colum
      "column_index": [0, 1, 3]
  },

  "claim_form_arkansas": {
        "default_entities": {
            "SIGNATURE": ["signature"],
            "NAME ": ["name"],
            "SSN": ["ssn"],
            "street_or_box_no": ["employer_address","mailing address"],
            "CITY": ["mailing_city","employer_city"],
            "STATE": ["mailing_state","employer_state"],
            "ZIP CODE": ["employer_zip","mailing_zip"],
            "LAST DAY WORKED ": ["work_end_date"],
            "PHONE NO": ["phone_no"],
            "DATE BEGAN WORK ": ["work_start_date"],
            "EMPLOYER'S NAME AND ADDRESS" :["employee_info"]

            }
    },

   "utility_bill":{
        "default_entities":{
                        "receiver_name" : ["name"],
                        "supplier_address": ["address"],
                        "due_date": ["due_date"],
                        "invoice_date": ["invoice_date"],
                        "supplier_account_number": ["account_no"],
                        }



   },

  "driver_license": {
    "default_entities": {
      "Document Id": ["DLN"],
      "Expiration Date": ["EXP"],
      "Date Of Birth": ["DOB"],
      "Family Name": ["LN"],
      "Given Names": ["FN"],
      "Issue Date": ["ISS"],
      "Address": ["Address"],
    },
    "derived_entities": {"SEX": {"rule": "SEX.*?(?<!\w)(F|M)(?!\w)"}}
  },

  "pay_stub": {
    "default_entities": {
      "employee_address": ["EMPLOYER ADDRESS"],
      "employee_name": ["EMPLOYEE NAME"],
      "end_date": ["PAY PERIOD(TO)"],
      "gross_earnings_ytd": ["YTD Gross"],
      "pay_date": ["PAY DATE"],
      "ssn": ["SSN"],
      "start_date": ["PAY PERIOD(FROM)"]

    },
    "derived_entities":
      {"EMPLOYER NAME": {"rule": "([a-zA-Z ]*)\d*.*"},
       "RATE": {"rule": "Regular\n(.*?)\n"},
       "HOURS": {"rule": "Regular\n.*?\n(.*?)\n"}}
  }
}
