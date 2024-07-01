import pandas as pd
import re
import os

def clean_text(text):
    # Mengganti kata "iteung" dengan "gays"
    text = text.replace("iteung", "gays")
    # Menghapus karakter yang tidak diinginkan (contoh: simbol, angka, dll.)
    text = re.sub(r'[^A-Za-z\s\n]', '', text)
    # Menghapus spasi berlebih
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_csv(input_file, output_file):
    try:
        # Periksa apakah file input ada
        if not os.path.isfile(input_file):
            print(f"File {input_file} tidak ditemukan.")
            return
        
        # Baca file CSV
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        data = []
        for line in lines:
            # Pisahkan question dan answer
            parts = line.strip().split('|')
            if len(parts) == 2:
                question, answer = parts
                data.append(f"{clean_text(question)}|{clean_text(answer)}")
            else:
                print(f"Format salah pada baris: {line.strip()}")
        
        # Simpan ke dataframe
        df = pd.DataFrame(data, columns=['question_answer'])
        
        # Simpan kembali ke file CSV
        df.to_csv(output_file, index=False, header=False)
        print(f"Proses preprocessing selesai. Hasil disimpan di {output_file}.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
input_file = 'dataset_clean.csv'
output_file = 'dataset_clean2.csv'
preprocess_csv(input_file, output_file)
