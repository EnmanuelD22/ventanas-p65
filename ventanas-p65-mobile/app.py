from flask import Flask, render_template, request, make_response

app = Flask(__name__)

def calcular_desglose(hueco, vias="2"):
    try:
        ancho_str, alto_str = hueco.lower().replace(',', '.').split('x')
        ancho = float(ancho_str.strip())
        alto  = float(alto_str.strip())

        laterales = alto - 0.12
        jambas    = laterales - 2

        if str(vias) == "3":
            cabezales = (ancho + 0.75) / 3
        else:
            cabezales = (ancho - 1) / 2

        rieles      = ancho - 1.38
        vidrio_ancho = cabezales - 2.62
        vidrio_alto  = alto - 5

        return {
            "hueco":     f"{ancho:.2f} x {alto:.2f}",
            "jambas":    f"{jambas:.2f}",
            "cabezales": f"{cabezales:.2f}",
            "laterales": f"{laterales:.2f}",
            "rieles":    f"{rieles:.2f}",
            "vidrios":   f"{vidrio_ancho:.2f} x {vidrio_alto:.2f}",
        }
    except (ValueError, AttributeError):
        return None


@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    huecos  = ""
    cliente = ""
    vias    = "2"

    if request.method == "POST":
        huecos  = request.form.get("huecos", "")
        cliente = request.form.get("cliente", "")
        vias    = request.form.get("vias", "2")

        for linea in huecos.strip().splitlines():
            r = calcular_desglose(linea, vias)
            if r:
                resultados.append(r)

    return render_template(
        "index.html",
        resultados=resultados,
        huecos=huecos,
        cliente=cliente,
        vias=vias,
    )


@app.route("/imprimir", methods=["POST"])
def imprimir():
    huecos  = request.form.get("huecos", "")
    cliente = request.form.get("cliente", "")
    vias    = request.form.get("vias", "2")
    resultados = []

    for linea in huecos.strip().splitlines():
        r = calcular_desglose(linea, vias)
        if r:
            resultados.append(r)

    html = render_template(
        "imprimir.html",
        resultados=resultados,
        cliente=cliente,
        vias=vias,
    )
    resp = make_response(html)
    resp.headers["Content-Type"] = "text/html"
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
