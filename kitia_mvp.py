# KitIA - MVP mínimo para demostrar la propuesta
# 3 casos concretos que cualquier docente se encuentra

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ERRORES = {
    "led_polaridad_inversa": {
        "titulo": "LED en polaridad inversa",
        "situacion": "Conectaste el LED pero NO enciende.",
        "explicacion": "El LED tiene polaridad: el ánodo (pata larga) va al lado positivo y el cátodo (pata corta) al negativo. En este caso están invertidos.",
        "accion": "Invierte el LED: coloca su pata larga hacia la resistencia y la pata corta hacia tierra (GND).",
        "tiempo": "15 segundos"
    },
    "corriente_excesiva": {
        "titulo": "Resistencia muy baja",
        "situacion": "El LED parpadea raro, se calienta o temes dañar el Arduino.",
        "explicacion": "Con una resistencia muy pequeña pasa demasiada corriente por el pin del Arduino (máximo 20 mA). Eso puede dañarlo con el tiempo.",
        "accion": "Cambia la resistencia por una de 330 Ω (o entre 220 Ω y 330 Ω). Es más segura para el Arduino.",
        "tiempo": "20 segundos"
    },
    "sin_gnd_comun": {
        "titulo": "Falta tierra común (GND)",
        "situacion": "Conectaste un sensor pero no lee nada o da valores erráticos.",
        "explicacion": "El Arduino y el sensor necesitan compartir la misma tierra (GND). Sin ella, no tienen una referencia común para comunicarse.",
        "accion": "Conecta el cable GND del sensor directamente al GND del Arduino.",
        "tiempo": "10 segundos"
    }
}

def mostrar_circuitar():
    print("=" * 60)
    print("  KitIA - Asistente para diagnosticar circuitos")
    print("  Pensado para docentes sin formación técnica")
    print("=" * 60)
    print()
    
    for clave, error in ERRORES.items():
        print(f"► {error['titulo']}")
        print(f"  ¿Qué pasa? {error['situacion']}")
        print(f"  ¿Por qué?  {error['explicacion']}")
        print(f"  ¿Qué hacer? {error['accion']}")
        print(f"  Tiempo estimado: {error['tiempo']}")
        print()
        print("-" * 60)
        print()

if __name__ == "__main__":
    mostrar_circuitar()
    print("KitIA: Traduce errores técnicos a pasos simples en español.")
    print("Funciona sin internet. Pensado para escuelas rurales.")
