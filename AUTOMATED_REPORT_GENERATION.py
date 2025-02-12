import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def read_data(file_path):
    """Reads data from a CSV file."""
    return pd.read_csv(file_path)

def analyze_data(df):
    """Performs analysis on the dataset."""
    summary = df.describe()
    dept_avg = df.groupby('Department')[['Salary', 'Performance Score']].mean().round(2)
    top_performers = df.nlargest(5, 'Performance Score')
    return summary, dept_avg, top_performers

def generate_pdf_report(file_path, summary, dept_avg, top_performers):
    """Generates a PDF report with analysis results."""
    pdf_file = "report.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("Data Analysis Report", styles['Title']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Summary Statistics:", styles['Heading2']))
    
    data_summary = [summary.columns.to_list()] + summary.round(2).values.tolist()
    table_summary = Table(data_summary)
    table_summary.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table_summary)
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph("Department-wise Average Salary & Performance Score:", styles['Heading2']))
    dept_data = [dept_avg.columns.to_list()] + dept_avg.values.tolist()
    table_dept = Table(dept_data)
    table_dept.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table_dept)
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph("Top 5 Performers:", styles['Heading2']))
    top_perf_data = [top_performers.columns.to_list()] + top_performers.values.tolist()
    table_top_perf = Table(top_perf_data)
    table_top_perf.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table_top_perf)
    
    doc.build(elements)
    print(f"Report generated: {pdf_file}")

if __name__ == "__main__":
    file_path = "data.csv"  # Update with the actual file path
    df = read_data(file_path)
    summary, dept_avg, top_performers = analyze_data(df)
    generate_pdf_report(file_path, summary, dept_avg, top_performers)
