import os
import pdfkit
import base64

# Ruta al ejecutable wkhtmltopdf en tu sistema
ruta_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=ruta_wkhtmltopdf)

# Ruta del directorio actual del script
ruta_script = os.path.dirname(os.path.abspath(__file__))
print("RUTA SCRIPT LF: ", ruta_script)

# Ruta de la imagen
ruta_imagen = os.path.join(ruta_script, 'media', 'black.jpg')

# Leer la imagen en formato base64
with open(ruta_imagen, 'rb') as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

# Contenido del HTML con la imagen en formato base64
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ejemplo PDF con imagen</title>
    <style>
        header {{
            text-align: center;
        }}
        img {{
            max-width: 500px;
        }}
        .info {{
            text-align: left;
            font-size: 20px;
            margin-top: 10px;
            margin-left: 10px;
        }}
    </style>
</head>
<body>
    <header>
        <img src="data:image/jpeg;base64,{img_base64}" alt="Logo"> <!-- Imagen incrustada en formato base64 -->
         <div class="info">
            <p><strong>POP ATELIER LLC</strong></p>
            <p><strong>Concept:</strong> Quotation</p>
            <p><strong>Date:</strong> 5/12/2023</p>
        </div>
        <h1>Generando un PDF con pdfkit</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin urna et pulvinar. Phasellus fringilla turpis a mi mollis malesuada. Morbi commodo est id dolor commodo, non hendrerit odio fermentum. Curabitur tincidunt justo nec aliquam finibus. Integer at ultrices mauris. Nunc vitae tincidunt odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae justo a leo aliquet auctor a in ligula. Nulla facilisi. Vivamus vestibulum fermentum elit at malesuada. Sed dapibus lacus non orci faucibus scelerisque.</p>
    </header>
    <p>Aquí puedes agregar más contenido para tu PDF.</p>
</body>
</html>
"""

# Guardar el contenido del HTML en un archivo
ruta_html = os.path.join(ruta_script, 'test.html')
with open(ruta_html, 'w', encoding='utf-8') as file:
    file.write(html_content)

# Generar un PDF desde el HTML y guardar en la ruta del script
ruta_salida_pdf = os.path.join(ruta_script, 'output_con_logo.pdf')

# Generar PDF desde el archivo HTML con la imagen incrustada
pdfkit.from_file(ruta_html, ruta_salida_pdf, configuration=config)
