# -*- coding: utf-8 -*-
"""Genera 6 slides 1080x1080 con layout limpio y auto-ajuste (NAUFest 2026)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080
PAD = 84
FOOT_H = 74
BG = (17, 24, 39)
CARD = (31, 41, 55)
ACCENT = (56, 189, 248)
ACCENT2 = (16, 185, 129)
TEXT = (243, 244, 246)
MUTED = (156, 163, 175)
FD = "C:/Windows/Fonts/"
HEAD = FD + "segoeuib.ttf"
BOLD = FD + "segoeuib.ttf"
REG = FD + "segoeui.ttf"


def fnt(path, size):
    try:
        return ImageFont.truetype(path, max(16, int(size)))
    except Exception:
        return ImageFont.load_default()


def wrap(d, text, f, max_w):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textbbox((0, 0), t, font=f)[2] <= max_w:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out or [""]


def measure(d, bullets, f_body, max_w):
    """Devuelve (lineas, altura) dibujando en modo 'calculo'."""
    total_lines = 0
    for b in bullets:
        total_lines += len(wrap(d, b, f_body, max_w))
    h = total_lines * LINE_H + len(bullets) * 26 + 60
    return total_lines, h


def render(idx, kicker, title, bullets, title_sz, body_sz, foot):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 14], fill=ACCENT)

    maxw = W - 2 * PAD
    y = 96

    # kicker
    d.text((PAD, y), kicker.upper(), font=fnt(BOLD, 28), fill=ACCENT)
    y += 52

    # titulo envuelto
    f_t = fnt(HEAD, title_sz)
    tl = wrap(d, title, f_t, maxw)
    while len(tl) > 3 and title_sz > 44:
        title_sz -= 4
        f_t = fnt(HEAD, title_sz)
        tl = wrap(d, title, f_t, maxw)
    for ln in tl:
        d.text((PAD, y), ln, font=f_t, fill=TEXT)
        y += int(title_sz * 1.22)
    y += 16

    d.rectangle([PAD, y, PAD + 130, y + 6], fill=ACCENT2)
    y += 48

    # tarjeta con auto-ajuste
    avail = H - FOOT_H - y - 24
    f_b = fnt(REG, body_sz)
    while True:
        lines = [ln for b in bullets for ln in wrap(d, b, f_b, maxw - 84)]
        need = len(lines) * int(body_sz * 1.45) + len(bullets) * 24 + 56
        if need <= avail or body_sz <= 26:
            break
        body_sz -= 2
        f_b = fnt(REG, body_sz)

    lh = int(body_sz * 1.45)
    card_h = min(need, avail)
    d.rounded_rectangle([PAD, y, W - PAD, y + card_h], radius=24, fill=CARD)

    cy = y + 28
    for b in bullets:
        for i, ln in enumerate(wrap(d, b, f_b, maxw - 84)):
            d.ellipse([PAD + 30, cy + 14, PAD + 44, cy + 28], fill=ACCENT)
            d.text((PAD + 70, cy), ln, font=f_b, fill=TEXT)
            cy += lh
        cy += 24

    # pie
    f_f = fnt(REG, 27)
    d.rectangle([0, H - FOOT_H, W, H], fill=(12, 17, 28))
    d.text((PAD, H - 52), foot, font=f_f, fill=MUTED)
    num = "%d/6" % idx
    tw = d.textbbox((0, 0), num, font=f_f)[2]
    d.text((W - PAD - tw, H - 52), num, font=f_f, fill=ACCENT)

    # validacion de desborde
    ok_y = (y + card_h) <= (H - FOOT_H - 10)
    print("slide%d  body=%d  card_end=%d  limit=%d  %s"
          % (idx, body_sz, y + card_h, H - FOOT_H - 10, "OK" if ok_y else "OVERFLOW"))

    out = "C:/Users/val/Desktop/proyectospersonales/naufest-kitia/carrusel_img/slide%d.png" % idx
    img.save(out, "PNG")


LINE_H = 56

SLIDES = [
    (1, "NAUFest 2026", "KitIA",
     ["Diagnóstico de errores en circuitos",
      "Para docentes sin conectividad",
      "Herbert Steven Galeano Flores · Guatemala",
      "#AIforImpact2026"], 74, 34),
    (2, "El problema", "Un kit de robótica que no se puede explicar",
     ["Don José es maestro multigrado en Alta Verapaz: atiende 6 grados a la vez.",
      "Le entregaron un kit de robótica, pero no sabe por qué el circuito no enciende.",
      "Solo 9.1% de escuelas de primaria tienen internet · 24% sin electricidad.",
      "Fuente: UNESCO SDG4, UNICEF/Giga 2026"], 54, 30),
    (3, "Por qué la IA", "Los modelos de visión fallan en el diagnóstico eléctrico",
     ["EEE-Bench (CVPR 2025): ignoran la imagen y empeoran con más contexto.",
      "CircuitSense: percepción >85% vs. derivación simbólica <19%.",
      "KitIA usa reglas deterministas + IA para explicar.",
      "Traduce lo técnico a lenguaje didáctico en español."], 50, 30),
    (4, "La solución", "Reglas eléctricas + explicación didáctica",
     ["1. Detecta el error con un motor determinista.",
      "2. Traduce el fallo a pasos cortos con IA.",
      "3. Explica en menos de 30 segundos.",
      "4. Funciona sin internet.",
      "5. Pensado para escuelas rurales multigrado."], 54, 30),
    (5, "Rol de la IA", "Traducir lo técnico a lo enseñable",
     ["TAREA: traducir el fallo técnico a instrucciones paso a paso.",
      "INFORMACIÓN: tipo de fallo y componente afectado.",
      "RESULTADO: explicación causal + acción concreta.",
      "REVISIÓN: docente, validado por reglas (no adivinado).",
      "VALOR: convierte conocimiento técnico en enseñable."], 50, 30),
    (6, "Demostración", "MVP funcionando con 3 casos reales",
     ["LED en polaridad inversa.",
      "Resistencia muy baja (>20 mA en el pin Arduino).",
      "Falta de tierra común (GND).",
      "Explicación en español, clara y accionable.",
      "Sin internet · enfoque en equidad educativa."], 54, 30),
]

if __name__ == "__main__":
    import os
    os.makedirs("C:/Users/val/Desktop/proyectospersonales/naufest-kitia/carrusel_img", exist_ok=True)
    for s in SLIDES:
        render(*s, foot="KitIA - #AIforImpact2026")
    print("Listo: 6 slides")
