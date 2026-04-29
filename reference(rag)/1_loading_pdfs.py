import os, json, glob
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader

load_dotenv()

PDF_FOLDER = os.getenv("PDF_FOLDER", "pdfs")
DATASET_FOLDER = os.getenv("DATASET_STORAGE_FOLDER", "datasets")
OUTPUT_FILE = os.path.join(DATASET_FOLDER, "data.txt")

os.makedirs(PDF_FOLDER, exist_ok=True)
os.makedirs(DATASET_FOLDER, exist_ok=True)

def run_loader():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    files = (
        glob.glob(f"{PDF_FOLDER}/*.pdf") +
        glob.glob(f"{PDF_FOLDER}/*.txt") +
        glob.glob(f"{PDF_FOLDER}/*.docx")
    )

    if not files:
        raise RuntimeError("No files found")

    count = 0

    for path in files:
        if path.endswith(".txt"):
            text = open(path, encoding="utf-8", errors="ignore").read()
            if text.count(" ") < 20:
                continue
            records = [{"source": path, "text": text}]

        elif path.endswith(".docx"):
            text = Docx2txtLoader(path).load()[0].page_content
            if text.count(" ") < 20:
                continue
            records = [{"source": path, "text": text}]

        else:
            records = []
            for d in PyPDFLoader(path).load():
                if d.page_content.count(" ") < 20:
                    continue
                records.append({
                    "source": path,
                    "page": d.metadata.get("page"),
                    "text": d.page_content
                })

        for r in records:
            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
            count += 1

    print(f"✅ Loaded {count} text blocks")

if __name__ == "__main__":
    run_loader()
