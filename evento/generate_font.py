import os

# Percorso della cartella dei font
font_folder = "static/fonts"
output_css_file = "static/css/fonts.css"

# Crea la stringa CSS con tutte le regole @font-face
font_face_rules = ""

for font_file in os.listdir(font_folder):
    if font_file.endswith(".otf"):  # Puoi aggiungere più formati qui, se necessario
        font_name = os.path.splitext(font_file)[0]
        font_face_rules += f"""
        @font-face {{
            font-family: '{font_name}';
            src: url('{{% static "fonts/{font_file}" %}}') format('opentype');
            font-weight: normal;
            font-style: normal;
        }}
        """

# Salva il contenuto in un file CSS
with open(output_css_file, "w") as f:
    f.write(font_face_rules)

print(f"CSS file generated at {output_css_file}")
