import pandas as pd
import numpy as np
from datetime import datetime


class ProjectReportGenerator:

    @staticmethod
    def generate_full_report(
        df: pd.DataFrame,
        output_path="reports/Customer_Analytics_Project_Report.pdf"
    ):

        from reportlab.platypus import (
            SimpleDocTemplate, Paragraph, Spacer,
            ListFlowable, ListItem, Preformatted
        )
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import inch

        doc = SimpleDocTemplate(output_path, pagesize=A4)
        elements = []
        styles = getSampleStyleSheet()

        title = styles["Heading1"]
        section = styles["Heading2"]
        normal = styles["Normal"]
        code = styles["Code"]

        elements.append(Paragraph("CUSTOMER ANALYTICS PROJECT REPORT", title))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph(f"Generated On: {datetime.now()}", normal))
        elements.append(Spacer(1, 0.4 * inch))

        elements.append(Paragraph("1. DATASET OVERVIEW", section))
        elements.append(Spacer(1, 0.2 * inch))
        elements.append(Paragraph(f"Total Rows: {df.shape[0]}", normal))
        elements.append(Paragraph(f"Total Columns: {df.shape[1]}", normal))
        elements.append(Spacer(1, 0.3 * inch))

        elements.append(Paragraph("2. BASIC STATISTICS", section))
        elements.append(Spacer(1, 0.2 * inch))
        elements.append(Preformatted(df.describe().to_string(), code))
        elements.append(Spacer(1, 0.3 * inch))

        elements.append(Paragraph("3. KEY INSIGHTS", section))
        elements.append(Spacer(1, 0.2 * inch))

        insights = [
            "Majority of customers fall between 30–50 years of age.",
            "Income distribution is positively skewed.",
            "Slightly more male customers than female customers.",
            "Moderate negative relationship between Income and Spending Score.",
            "Strong positive correlation between Age and Years Employed."
        ]

        elements.append(
            ListFlowable(
                [ListItem(Paragraph(i, normal)) for i in insights],
                bulletType="bullet"
            )
        )

        doc.build(elements)

        print("PDF report successfully generated.")