from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Pars Family</title>
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
        <h1>Pars Ailesi</h1>
        <img class="logo" src="https://raw.githubusercontent.com/kbgyazilim46/kbgyazilimsite/main/logo.png" alt="Logo" />
        <p>Sanala damga vuran bir aile.</p>
    </header>

    %%CONTENT%%
</body>
</html>
"""

@app.route("/")
def anasayfa():
    content = """
    <section id="hakkinda">
        <h2>Hakkımızda</h2>
        <p><strong>Selamün aleyküm.</strong> Ben namıdiğer <strong>Kimsebaşgöz</strong>.</p>
        <p>İsmim <strong>Ahmet Utku Can</strong>'dır.</p>
        <p>Aşağıdaki bilgiler iletişim içindir. Her türlü sanal işlem için ulaşabilirsiniz.</p>
    </section>

    <section id="iletisim">
        <h2>İletişim</h2>
        <p><strong>WhatsApp:</strong> <a href="https://wa.me/639092363984" target="_blank">+63 909 236 3984</a></p>
        <p><strong>E-posta:</strong> <a href="mailto:kimsebasgozedemez@mail.com">kimsebasgozedemez@mail.com</a></p>
        <a href="https://instagram.com/_kimsebasgoz_" class="btn" target="_blank">Instagram'da Ulaş</a>
    </section>

    <section id="pars-info">
        <h2>Pars Ailesi Hakkında</h2>
        <p><strong>Sanal alemde ismimiz duyulmuş olup bir grup (aile) olarak tag açmış kişileriz.</strong></p>
        <p><strong>Pars</strong> tagimizin baş kurucusu <strong>kimsebasgozedemez</strong>'dir.</p>
        <p><strong>Baş Leader:</strong> Leaxs Santo</p>
        <p><strong>Tagımıza gelmek için aşağıdaki hesaplara ulaşabilirsiniz:</p>
        <ul>
            <li>📸 <strong>Resmi Instagram:</strong> <a href="https://instagram.com/parsfamily.resmihesap" target="_blank">@parsfamily.resmihesap</a></li>
            <li>👑 <strong>Baş Kurucu:</strong> <a href="https://instagram.com/pars.bas.krc.kimsebasgoz" target="_blank">@pars.bas.krc.kimsebasgoz</a></li>
            <li>🛡️ <strong>Baş Leader:</strong> <a href="https://instagram.com/pars.leaxs" target="_blank">@pars.leaxs</a></li>
            <li>⚔️ <strong>1. Leader:</strong> <a href="https://instagram.com/pars.kroyy.nen" target="_blank">@pars.kroyy.nen</a></li>
        </ul>
    </section>
    """
    return HTML_TEMPLATE.replace("%%CONTENT%%", content)