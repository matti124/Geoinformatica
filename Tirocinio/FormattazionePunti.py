import json

# Percorso al file GeoJSON originale (non formattato)
input_file = 'punti_no2_geojson.geojson'

# Percorso al file GeoJSON formattato (output)
output_file = 'punti_no2_formattato.geojson'

# Leggi il file GeoJSON
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Riscrivi il file con indentazione per renderlo leggibile
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'File GeoJSON formattato salvato come {output_file}')
