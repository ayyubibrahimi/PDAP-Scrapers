import sys
import os
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from common import list_pdf_v3

# This script was generated by the setup gui
configs = {
    "webpage":"https://acworthpolice.org/departments/annual-report",
    "web_path":"/images/annualreport/",
    "domain_included":False,
    "domain":"https://acworthpolice.org",
    "sleep_time": 5,
    "non_important":['emergency', ' training', ' guidelines'],
    "debug": False,
    "csv_dir": "/csv/",
}

save_dir = "./data/annual_reports/"

list_pdf_v3(configs, save_dir)
