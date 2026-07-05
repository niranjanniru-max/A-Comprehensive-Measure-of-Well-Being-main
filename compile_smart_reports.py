import os
import base64
import re
import markdown
from playwright.sync_api import sync_playwright

# ─── CONFIGURATION ───
LOCAL_IMAGE_PATH = "photo_2026-07-05_17-11-36.jpg"
IGNORE_FOLDERS = {".git", "venv", "__pycache__", "static", "templates", "models", "dataset"}

DYNAMIC_PROJECT_META = {
    "Date": "4 July 2026",
    "Team_ID": "XXXXXX",
    "Project_Name": "A Comprehensive Measure of Well Being"
}

def determine_phase_marks(folder_name):
    folder_lower = folder_name.lower()
    # Explicitly check for documentation (7) and demonstration (8) phases to assign 1 Mark
    if "7." in folder_lower or "8." in folder_lower or "documentation" in folder_lower or "demonstration" in folder_lower: 
        return "1 Mark"
    if "brainstorming" in folder_lower or "1." in folder_lower: return "2 Marks"
    if "requirement" in folder_lower or "2." in folder_lower: return "3 Marks"
    if "design" in folder_lower or "architecture" in folder_lower: return "4 Marks"
    if "implementation" in folder_lower or "code" in folder_lower: return "5 Marks"
    return "3 Marks"

def convert_image_to_base64(img_path):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Missing banner image asset: '{img_path}'")
    with open(img_path, "rb") as img_file:
        return f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"

def sanitize_and_clean_markdown(raw_text):
    """Restores text box grids, escapes erratic table markings, and converts Mermaid blocks."""
    cleaned = re.sub(re.compile(r"Page \d+ of \d+", re.IGNORECASE), "", raw_text)
    
    def mermaid_replcer(match):
        diagram_code = match.group(1).strip()
        return f'\n<div class="mermaid">\n{diagram_code}\n</div>\n'
    
    cleaned = re.sub(r'```mermaid\s*([\s\S]*?)\s*```', mermaid_replcer, cleaned)

    lines = cleaned.splitlines()
    rebuilt_lines = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|") and len(stripped) > 2:
            if "SAYS" in stripped or "THINKS" in stripped or "DOES" in stripped or "FEELS" in stripped:
                rebuilt_lines.append(stripped)
            else:
                rebuilt_lines.append(line)
        else:
            rebuilt_lines.append(line)

    return "\n".join(rebuilt_lines)

def build_html_document(md_text, phase_title, max_marks, base64_banner):
    cleaned_md = sanitize_and_clean_markdown(md_text)
    markdown_html = markdown.markdown(cleaned_md, extensions=['tables', 'fenced_code'])
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
        <script>
            mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
        </script>
        <style>
            @page {{
                margin: 0px;
            }}
            body {{
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                color: #2d3748;
                line-height: 1.75;
                font-size: 14.5px;
                margin: 0px;
                padding: 0px;
                background-color: #ffffff;
                -webkit-font-smoothing: antialiased;
            }}
            .banner-container {{
                width: 100%;
                margin: 0;
                padding: 0;
            }}
            .banner-container img {{
                width: 100%;
                display: block;
                height: auto;
            }}
            .content-wrapper {{
                padding: 45px 55px;
            }}
            .phase-title {{
                text-align: center;
                font-size: 26px;
                font-weight: 700;
                color: #1a365d;
                margin-top: 10px;
                margin-bottom: 30px;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            .meta-table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 40px;
                font-size: 14px;
                background-color: #f8fafc;
                border-radius: 8px;
                overflow: hidden;
                border-style: hidden;
                box-shadow: 0 0 0 1px #e2e8f0;
            }}
            .meta-table td {{
                border: 1px solid #e2e8f0;
                padding: 14px 18px;
                color: #4a5568;
            }}
            .meta-table tr td:first-child {{
                width: 30%;
                font-weight: 600;
                color: #2d3748;
                background-color: #edf2f7;
            }}
            .report-content {{
                margin-top: 30px;
            }}
            
            /* Enhanced Paragraph and List Typographic Structure */
            .report-content p {{
                margin-bottom: 20px;
                color: #2d3748;
                text-align: justify;
            }}
            .report-content table {{
                width: 100%;
                border-collapse: collapse;
                margin: 30px 0;
                font-size: 14px;
                background-color: #ffffff;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
                border-radius: 6px;
                overflow: hidden;
            }}
            .report-content th, .report-content td {{
                border: 1px solid #e2e8f0;
                padding: 14px 16px;
                text-align: left;
                vertical-align: top;
            }}
            .report-content th {{
                background-color: #ebf8ff;
                color: #2b6cb0;
                font-weight: 600;
                border-bottom: 2px solid #bee3f8;
                text-transform: uppercase;
                font-size: 12px;
                letter-spacing: 0.5px;
            }}
            .report-content tr:nth-child(even) {{
                background-color: #f8fafc;
            }}
            
            .report-content ul, .report-content ol {{
                padding-left: 24px;
                margin-bottom: 24px;
            }}
            .report-content li {{
                margin-bottom: 10px;
                color: #2d3748;
            }}
            
            h1, h2, h3 {{ 
                color: #1a365d; 
                margin-top: 40px; 
                margin-bottom: 18px;
                font-weight: 700;
                letter-spacing: -0.3px;
            }}
            h1 {{ font-size: 24px; }}
            h2 {{
                font-size: 20px;
                border-bottom: 2px solid #e2e8f0;
                padding-bottom: 8px;
                margin-top: 45px;
            }}
            h3 {{ font-size: 17px; }}
            
            /* Clean structural callout for diagram graphics */
            .mermaid {{
                display: flex;
                justify-content: center;
                margin: 35px 0;
                background: #f8fafc;
                padding: 24px;
                border-radius: 8px;
                border: 1px solid #e2e8f0;
                box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.02);
            }}
        </style>
    </head>
    <body>
        <div class="banner-container">
            <img src="{base64_banner}" />
        </div>
        
        <div class="content-wrapper">
            <div class="phase-title">{phase_title}</div>
            
            <table class="meta-table">
                <tr><td>Date</td><td>{DYNAMIC_PROJECT_META['Date']}</td></tr>
                <tr><td>Team ID</td><td>{DYNAMIC_PROJECT_META['Team_ID']}</td></tr>
                <tr><td>Project Name</td><td>{DYNAMIC_PROJECT_META['Project_Name']}</td></tr>
                <tr><td>Maximum Marks</td><td>{max_marks}</td></tr>
            </table>
            
            <div class="report-content">
                {markdown_html}
            </div>
        </div>
    </body>
    </html>
    """

def process_pipeline():
    print("⏳ Initiating Structural Document Pipeline Update...")
    img_uri = convert_image_to_base64(LOCAL_IMAGE_PATH)
    processed_count = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]
            current_folder_name = os.path.basename(root)
            
            for file in files:
                if file.endswith(".md"):
                    md_path = os.path.join(root, file)
                    pdf_filename = file.rsplit(".", 1)[0] + ".pdf"
                    pdf_path = os.path.join(root, pdf_filename)
                    
                    phase_clean_title = current_folder_name.replace("_", " ").replace("-", " ")
                    calculated_marks = determine_phase_marks(current_folder_name)
                    
                    with open(md_path, "r", encoding="utf-8") as f:
                        raw_md_text = f.read()
                        
                    html_document = build_html_document(raw_md_text, phase_clean_title, calculated_marks, img_uri)
                    
                    page.set_content(html_document)
                    
                    try:
                        page.wait_for_selector(".mermaid svg", timeout=3000)
                    except:
                        pass 
                    
                    page.pdf(
                        path=pdf_path,
                        format="A4",
                        display_header_footer=False,
                        margin={"top": "0px", "bottom": "40px", "left": "0px", "right": "0px"}
                    )
                    
                    os.remove(md_path)
                    processed_count += 1
                    print(f"   🎉 Pristine Layout Generated: '{pdf_path}'")

        browser.close()
    print(f"\n✅ Pipeline complete! Processed {processed_count} files beautifully.")

if __name__ == "__main__":
    try:
        process_pipeline()
    except Exception as err:
        print(f"❌ Execution stopped: {str(err)}")