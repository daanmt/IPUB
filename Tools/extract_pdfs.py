import pdfplumber
import PyPDF2
import sys
import os

def extract_pdf(path, out_path):
    """Extrai texto de um PDF usando pdfplumber (fallback para PyPDF2)."""
    lines = []
    print(f"Processando: {path}")
    
    try:
        # Tentativa primária com pdfplumber (melhor para layouts complexos)
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text(x_tolerance=2, y_tolerance=3)
                if text and text.strip():
                    lines.append(f"\n# --- PAGINA {i+1} ---\n")
                    lines.append(text)
    except Exception as e:
        print(f"Erro com pdfplumber em {path}: {e}. Tentando PyPDF2...")
        try:
            # Fallback para PyPDF2
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for i, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text:
                        lines.append(f"\n# --- PAGINA {i+1} (PyPDF2) ---\n")
                        lines.append(text)
        except Exception as e2:
            print(f"Falha total ao processar {path}: {e2}")
            return False

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Salvo em: {out_path}")
    return True

if __name__ == "__main__":
    # Exemplo de uso para Preventiva (conforme solicitado no contexto atual)
    base_dir = r'c:\Users\daanm\IPUB\Temas\Preventiva'
    files = [
        ('Medidas_de_Saúde_Coletiva_-_Parte_II.pdf', 'preventiva_parte_2.txt'),
        ('Medidas_de_Saúde_Coletiva_-_Parte_III.pdf', 'preventiva_parte_3.txt')
    ]
    
    output_dir = r'c:\Users\daanm\IPUB\Extracted'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for pdf_name, txt_name in files:
        full_pdf_path = os.path.join(base_dir, pdf_name)
        full_txt_path = os.path.join(output_dir, txt_name)
        if os.path.exists(full_pdf_path):
            extract_pdf(full_pdf_path, full_txt_path)
        else:
            print(f"Arquivo não encontrado: {full_pdf_path}")

