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
        .table-container {{
            margin-top: 20px;
            margin-left: 10px;
            width: 98%;
        }}
        .headers-doc{{
            margin-top: 50px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 10px;
        }}
        th, td {{
            border: 1px solid black;
            padding: 8px;
            text-align: left;
            vertical-align: top; /* Alineación vertical */
            line-height: 1.4; /* Ajuste del espaciado vertical */
        }}
        th {{
            background-color: black;
            color: white;
            text-align: center;
        }}
        hr {{
            margin-top: 50px;
            border: none;
            border-top: 2px solid black;
            width: 100%;
        }}
        .total-left{{
             text-align: right;
        }}
         .grand-total {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}

        .grand-total table {{
            width: 100%;
            border-collapse: collapse;
        }}

        .grand-total th,
        .grand-total td {{
            border: 1px solid black;
            padding: 8px;
            text-align: right;
        }}

        .grand-total th:nth-child(1),
        .grand-total td:nth-child(1) {{
            width: 200px; /* Ancho fijo para el primer columna (Total mandatory items y Total smart display kits) */
        }}

        .grand-total th:nth-child(2),
        .grand-total td:nth-child(2) {{
            width: 150px; /* Ancho fijo para el segunda columna ($ 1,404.0) */
        }}

        .grand-total th:nth-child(3),
        .grand-total td:nth-child(3) {{
            width: 150px; /* Ancho fijo para el tercera columna (Grand Total y $ 4,072.31) */
        }}

        .grand-total th {{
            background-color: black;
            color: white;
            text-align: left;
        }}
        .feauture-total {{
             font-size: 20px;
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
    </header>
    <div class="table-container">
        <h2 class="headers-doc">Mandatory items: </h2>
        <table>
            <tr>
                <th>Item</th>
                <th>Cost</th>
            </tr>
            <tr>
                <td>Video processor + 4G card</td>
                <td class="total-left">$ 377.99</td>
            </tr>
            <tr>
                <td>Freight + import taxes</td>
                <td class="total-left">$ 487.20</td>
            </tr>
            <tr>
                <td>Installation</td>
                <td class="total-left">$ 931.02</td>
            </tr>
            <tr>
                <td>CMS annual fee</td>
                <td class="total-left">$ 152.10</td>
            </tr>
            <tr>
                <td>NOC + cell data annual fee</td>
                <td class="total-left">$ 152.10</td>
            </tr>
            <tr>
                <td><strong>Total</strong></td>
                <td class="total-left"><strong>$ 2,668.31</strong></td>
            </tr>
            <tr>
                <td><strong>Mandatory items: 1</strong></td>
                <td class="total-left"><strong>$ 2,668.31</strong></td>
            </tr>
        </table>
    </div>
    <hr>
    <h2 class="headers-doc">Smart Display Kit: </h2>
    <hr>
    <div class="table-container">
        <h3 class="">Option 1: </h3>
        <table>
            <tr>
                <th>Quantity</th>
                <th>Type</th>
                <th>Size</th>
                <th>Price per item</th>
                <th> Total price per item</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Header</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Header</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Shelf</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Shelf</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Shelf</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Shelf</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Shelf</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Shelf</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td><strong>Smart Display</strong></td>
                <td class="total-left" colspan="4"><strong>5</strong></td>
            </tr>
            <tr>
                <td><strong>Headers Total</strong></td>
                <td class="total-left" colspan="4"><strong>$15,000</strong></td>
            </tr>
            <tr>
                <td><strong>Shelfs Total</strong></td>
                <td class="total-left" colspan="4"><strong>$15,000</strong></td>
            </tr>
            <tr>
                <td><strong>Total Option 1</strong></td>
                <td class="total-left" colspan="4"><strong>$30,000</strong></td>
            </tr>
        </table>

        <h3 class="">Option 2: </h3>
        <table>
            <tr>
                <th>Quantity</th>
                <th>Type</th>
                <th>Size</th>
                <th>Price per item</th>
                <th> Total price per item</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Header</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Header</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Shelf</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Shelf</td>
                <td>Pitch 2</td>
                <td>$ 848.90</td>
                <td class="total-left">$ 848.90</td>
            </tr>
            <tr>
                <td><strong>Smart Display</strong></td>
                <td class="total-left" colspan="4"><strong>5</strong></td>
            </tr>
            <tr>
                <td><strong>Headers Total</strong></td>
                <td class="total-left" colspan="4"><strong>$15,000</strong></td>
            </tr>
            <tr>
                <td><strong>Shelfs Total</strong></td>
                <td class="total-left" colspan="4"><strong>$15,000</strong></td>
            </tr>
            <tr>
                <td><strong>Total Option 2</strong></td>
                <td class="total-left" colspan="4"><strong>$30,000</strong></td>
            </tr>
        </table>
        <hr>
        <br>
            <div class="grand-total">
                <table>
                    <tr>
                        <th class="feauture-total">Total mandatory items:</th>
                        <td class="feauture-total"><strong>$ 1,404.0</strong></td>
                    </tr>
                </table>
            </div>
            <div class="grand-total">
                <table>
                    <tr>
                        <th class="feauture-total">Total smart display kits:</th>
                        <td class="feauture-total"><strong>$ 1,404.0</strong></td>
                    </tr>
                </table>
            </div>
            <div class="grand-total">
                <table>
                    <tr>
                        <th class="feauture-total">Grand Total:</th>
                        <td class="feauture-total"><strong>$ 4,072.31</strong></td>
                    </tr>
                </table>
            </div>
        <hr>
    </div>
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
