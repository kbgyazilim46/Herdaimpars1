from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Hayalet Family</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f7f7f7;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        header {
            background-color: #000;
            color: white;
            padding: 20px;
            text-align: center;
        }
        img.logo {
            width: 100px;
            border-radius: 10px;
        }
        .btn {
            display: inline-block;
            background-color: #E1306C;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: background-color 0.3s ease;
            margin-top: 10px;
        }
        .btn:hover {
            background-color: #c2265c;
        }
        section {
            margin-bottom: 40px;
        }
        ul {
            list-style: none;
            padding-left: 0;
        }
        li {
            margin: 6px 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Hayalet Ailesi</h1>
        <img class="logo" src="https://raw.githubusercontent.com/kbgyazilim46/Herdaimpars1/main/background.jpg" alt="Logo" />
        <p>Sanala damga vuran bir aile.</p>
    </header>

    %%CONTENT%%
</body>
</html>
"""

@app.route("/")
def anasayfa():
    content = """
    <section id="hayalet-info">
        <h2>Hayalet Ailesi Hakkında</h2>
        <p><strong>Sanal alemde ismimiz duyulmuş olup bir grup (aile) olarak tag açmış kişileriz.</strong></p>
        <p><strong>Hayalet</strong> tagimizin baş kurucusu <strong>kimsebasgozedemez</strong>'dir.</p>
        <p><strong>Baş Leaderi:</strong> Leaxs Santo</p>
        <p><strong>Tagımıza gelmek için aşağıdaki hesaplara ulaşabilirsiniz:</p>
        <ul>
            <li>📸 <strong>Resmi Instagram:</strong> <a href="https://instagram.com/hayaletfamily.resmihesap" target="_blank">@hayaletfamily.resmihesap</a></li>
            <li>👑 <strong>Baş Kurucu:</strong> <a href="https://instagram.com/_hayalet.bas.krc.kimsebasgoz_" target="_blank">@_hayalet.bas.krc.kimsebasgoz_</a></li>
            <li>🛡️ <strong>Baş Leader:</strong> <a href="https://instagram.com/hayalet.leaxs" target="_blank">@hayalet.leaxs</a></li>
            <li>⚔️ <strong>1. Leader:</strong> <a href="https://instagram.com/hayalet.versace" target="_blank">@hayalet.versace</a></li>
        </ul>
    </section>
    """
    return HTML_TEMPLATE.replace("%%CONTENT%%", content)
