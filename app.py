from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# ----------------------------
# Presets (com defaults t=0)
# ----------------------------
PRESETS = {
    "kiwi_hayward": {
        "label": "Kiwi (Hayward)",
        "Tref_C": 5.0, "Ea_J": 60000, "k_firm_ref": 0.06, "alpha_E": 1.8,
        "beta_RH": 1.2, "RH_ref": 90,
        "dureza_min": 3,
        "brix_min": 11, "brix_max": 17, "brix_g": 0.35,
        "dureza_0_default": 45, "brix_0_default": 11.0,
        "qual_firm_threshold": 8, "qual_brix_target": 15
    },
    "kiwi_baby": {
        "label": "Kiwi (Baby / Kiwi Berry)",
        "Tref_C": 4.0, "Ea_J": 58000, "k_firm_ref": 0.14, "alpha_E": 3.2,
        "beta_RH": 2.0, "RH_ref": 95,
        "dureza_min": 2,
        "brix_min": 13, "brix_max": 20, "brix_g": 0.50,
        "dureza_0_default": 28, "brix_0_default": 14.5,
        "qual_firm_threshold": 6, "qual_brix_target": 17
    },
    "maca_golden": {
        "label": "Maçã (Golden)",
        "Tref_C": 5.0, "Ea_J": 50000, "k_firm_ref": 0.025, "alpha_E": 0.8,
        "beta_RH": 0.8, "RH_ref": 90,
        "dureza_min": 12,
        "dureza_0_default": 72,
        "brix_min": 11.5, "brix_max": 15.5, "brix_g": 0.18,
        "brix_0_default": 12.0,
        "qual_firm_threshold": 35, "qual_brix_target": 13.5
    },
    "maca_reineta": {
        "label": "Maçã (Reineta)",
        "Tref_C": 5.0, "Ea_J": 52000, "k_firm_ref": 0.035, "alpha_E": 1.1,
        "beta_RH": 1.0, "RH_ref": 90,
        "dureza_min": 10,
        "dureza_0_default": 65,
        "brix_min": 11.0, "brix_max": 14.0, "brix_g": 0.16,
        "brix_0_default": 11.5,
        "qual_firm_threshold": 30, "qual_brix_target": 12.5
    },
    "maca_gala": {
        "label": "Maçã (Gala)",
        "Tref_C": 5.0, "Ea_J": 48000, "k_firm_ref": 0.040, "alpha_E": 1.3,
        "beta_RH": 0.9, "RH_ref": 90,
        "dureza_min": 9,
        "dureza_0_default": 60,
        "brix_min": 12.5, "brix_max": 17.0, "brix_g": 0.25,
        "brix_0_default": 13.0,
        "qual_firm_threshold": 28, "qual_brix_target": 14.5
    },
    "maca_fuji": {
        "label": "Maçã (Fuji)",
        "Tref_C": 5.0, "Ea_J": 47000, "k_firm_ref": 0.018, "alpha_E": 0.6,
        "beta_RH": 0.7, "RH_ref": 90,
        "dureza_min": 15,
        "dureza_0_default": 80,
        "brix_min": 13.0, "brix_max": 19.0, "brix_g": 0.15,
        "brix_0_default": 14.0,
        "qual_firm_threshold": 40, "qual_brix_target": 16.0
    },
    "laranja": {
        "label": "Laranja",
        "Tref_C": 5.0, "Ea_J": 42000, "k_firm_ref": 0.010, "alpha_E": 0.15,
        "beta_RH": 0.35, "RH_ref": 90,
        "dureza_min": 35,
        "brix_min": 10.5, "brix_max": 13.5, "brix_g": 0.10,
        "dureza_0_default": 55, "brix_0_default": 11.5,
        "qual_firm_threshold": 42, "qual_brix_target": 12.2
    },
    "banana": {
        "label": "Banana",
        "Tref_C": 14.0, "Ea_J": 65000, "k_firm_ref": 0.090, "alpha_E": 2.2,
        "beta_RH": 1.0, "RH_ref": 90,
        "dureza_min": 5,
        "brix_min": 12.0, "brix_max": 22.0, "brix_g": 0.45,
        "dureza_0_default": 80, "brix_0_default": 12.5,
        "qual_firm_threshold": 15, "qual_brix_target": 19
    },
    "mirtilo": {
        "label": "Mirtilo",
        "Tref_C": 2.0, "Ea_J": 52000, "k_firm_ref": 0.030, "alpha_E": 0.10,
        "beta_RH": 1.6, "RH_ref": 95,
        "dureza_min": 6,
        "brix_min": 10.0, "brix_max": 14.0, "brix_g": 0.20,
        "dureza_0_default": 30, "brix_0_default": 11.5,
        "qual_firm_threshold": 12, "qual_brix_target": 12.5
    },
    "framboesa": {
        "label": "Framboesa",
        "Tref_C": 2.0, "Ea_J": 56000, "k_firm_ref": 0.060, "alpha_E": 0.12,
        "beta_RH": 2.2, "RH_ref": 95,
        "dureza_min": 2.5,
        "brix_min": 7.0, "brix_max": 12.0, "brix_g": 0.22,
        "dureza_0_default": 18, "brix_0_default": 9.5,
        "qual_firm_threshold": 6, "qual_brix_target": 10.0
    },
    "pera": {
        "label": "Pera",
        "Tref_C": 2.0, "Ea_J": 54000, "k_firm_ref": 0.050, "alpha_E": 1.6,
        "beta_RH": 1.2, "RH_ref": 92,
        "dureza_min": 4,
        "brix_min": 10.5, "brix_max": 16.5, "brix_g": 0.28,
        "dureza_0_default": 55, "brix_0_default": 11.5,
        "qual_firm_threshold": 10, "qual_brix_target": 14.0
    },
    "ameixa": {
        "label": "Ameixa",
        "Tref_C": 2.0, "Ea_J": 52000, "k_firm_ref": 0.060, "alpha_E": 1.0,
        "beta_RH": 1.0, "RH_ref": 92,
        "dureza_min": 3,
        "brix_min": 11.0, "brix_max": 20.0, "brix_g": 0.30,
        "dureza_0_default": 40, "brix_0_default": 12.5,
        "qual_firm_threshold": 8, "qual_brix_target": 16.5
    },
    "pessego": {
        "label": "Pêssego",
        "Tref_C": 2.0, "Ea_J": 56000, "k_firm_ref": 0.080, "alpha_E": 1.4,
        "beta_RH": 1.1, "RH_ref": 92,
        "dureza_min": 2,
        "brix_min": 9.5, "brix_max": 18.0, "brix_g": 0.35,
        "dureza_0_default": 35, "brix_0_default": 11.0,
        "qual_firm_threshold": 6, "qual_brix_target": 15.0
    },
    "cereja": {
        "label": "Cereja",
        "Tref_C": 2.0, "Ea_J": 48000, "k_firm_ref": 0.045, "alpha_E": 0.05,
        "beta_RH": 1.6, "RH_ref": 95,
        "dureza_min": 4,
        "brix_min": 14.0, "brix_max": 20.0, "brix_g": 0.08,
        "dureza_0_default": 28, "brix_0_default": 16.0,
        "qual_firm_threshold": 10, "qual_brix_target": 18.0
    },
    "morango": {
        "label": "Morango",
        "Tref_C": 2.0, "Ea_J": 52000, "k_firm_ref": 0.120, "alpha_E": 0.05,
        "beta_RH": 2.4, "RH_ref": 95,
        "dureza_min": 1.5,
        "brix_min": 6.0, "brix_max": 10.5, "brix_g": 0.12,
        "dureza_0_default": 12, "brix_0_default": 7.5,
        "qual_firm_threshold": 4.5, "qual_brix_target": 9.0
    },
    "uva": {
        "label": "Uva",
        "Tref_C": 2.0, "Ea_J": 45000, "k_firm_ref": 0.020, "alpha_E": 0.05,
        "beta_RH": 1.8, "RH_ref": 92,
        "dureza_min": 3,
        "brix_min": 14.0, "brix_max": 22.0, "brix_g": 0.05,
        "dureza_0_default": 20, "brix_0_default": 16.0,
        "qual_firm_threshold": 7, "qual_brix_target": 18.0
    },
    "figo": {
        "label": "Figo",
        "Tref_C": 2.0, "Ea_J": 52000, "k_firm_ref": 0.110, "alpha_E": 0.20,
        "beta_RH": 1.8, "RH_ref": 95,
        "dureza_min": 1.2,
        "brix_min": 14.0, "brix_max": 26.0, "brix_g": 0.18,
        "dureza_0_default": 10, "brix_0_default": 16.0,
        "qual_firm_threshold": 3.5, "qual_brix_target": 20.0
    },
    "melao": {
        "label": "Melão",
        "Tref_C": 7.0, "Ea_J": 52000, "k_firm_ref": 0.060, "alpha_E": 0.9,
        "beta_RH": 0.9, "RH_ref": 90,
        "dureza_min": 2.0,
        "brix_min": 9.0, "brix_max": 16.0, "brix_g": 0.22,
        "dureza_0_default": 25, "brix_0_default": 10.5,
        "qual_firm_threshold": 6.0, "qual_brix_target": 13.5
    },
}


def k_temp_scaling(Ea, T, Tref):
    R = 8.314
    return np.exp((-Ea / R) * (1.0 / T - 1.0 / Tref))


def run_simulation(fruit_key, T_c, E_ppm, RH_pct, days, dureza_0_user, brix_0_user):
    dt = 0.05

    p = PRESETS[fruit_key]
    t = np.arange(0.0, days, dt)

    T_K = T_c + 273.15
    Tref_K = p["Tref_C"] + 273.15
    kT = p["k_firm_ref"] * k_temp_scaling(p["Ea_J"], T_K, Tref_K)
    kE = 1.0 + p["alpha_E"] * E_ppm

    RH_ref = p["RH_ref"]
    RH_deficit = max(0.0, (RH_ref - RH_pct) / 100.0)
    kRH = 1.0 + p["beta_RH"] * RH_deficit

    k = kT * kE * kRH

    dureza_min = p["dureza_min"]
    dureza_0 = max(dureza_min + 1e-6, float(dureza_0_user))
    dureza = dureza_min + (dureza_0 - dureza_min) * np.exp(-k * t)

    brix_min = p["brix_min"]
    brix_max = p["brix_max"]
    g = p["brix_g"]
    eps = 1e-6

    brix_0 = float(brix_0_user)
    brix_0 = min(brix_max - eps, max(brix_min + eps, brix_0))

    t0_base = (
        -0.05 * (T_c - p["Tref_C"])
        - 2.0 * np.log1p(E_ppm)
        + 0.06 * max(0.0, RH_ref - RH_pct)
    )

    y = (brix_0 - brix_min) / (brix_max - brix_min)
    t0_from_b0 = (1.0 / g) * np.log((1.0 / y) - 1.0)

    t0_eff = t0_from_b0 + t0_base
    brix = brix_min + (brix_max - brix_min) / (1.0 + np.exp(-g * (t - t0_eff)))
    if len(brix) > 0:
        brix[0] = brix_0

    firm_score = 1.0 / (1.0 + np.exp(-0.35 * (dureza - p["qual_firm_threshold"])))
    brix_score = np.exp(-((brix - p["qual_brix_target"]) ** 2) / 2.0)
    quality = 100.0 * (0.65 * firm_score + 0.35 * brix_score)

    return {
        "t": t,
        "dureza": dureza,
        "brix": brix,
        "quality": quality,
        "k": k,
        "p": p,
        "dureza_0": dureza_0,
        "brix_0": brix_0,
    }


def main():
    st.set_page_config(page_title="Simulador de Frutas", layout="wide")

    if "fruit_key" not in st.session_state:
        st.session_state.fruit_key = "kiwi_hayward"
        st.session_state.last_loaded_fruit = None

    logo_dir = Path(__file__).resolve().parent / "logos"
    main_logo = logo_dir / "RETAILL_LC.jpg"
    other_logos = [
        logo_dir / "b0_Eureka_logo.png",
        logo_dir / "b1_feup_logo.jpg",
        logo_dir / "b2_liacc_logo.png",
        logo_dir / "b3_PPorto_logo.png",
        logo_dir / "b4_retail-logo.svg",
        logo_dir / "b5_logo_ITEA4.svg",
    ]

    top_right = st.columns([3.2], vertical_alignment="top")[0]

    with top_right:
        logo_cols = st.columns(len(other_logos))
        for col, logo_path in zip(logo_cols, other_logos):
            with col:
                if logo_path.exists():
                    st.image(str(logo_path), use_container_width=True)
                else:
                    st.caption(logo_path.name)

    st.markdown("---")

    with st.sidebar:
        if main_logo.exists():
            st.image(str(main_logo), width=120)
        else:
            st.info("Logo principal não encontrado.")

    st.title("Simulador de qualidade e firmeza de frutas")

    with st.sidebar:
        st.header("Parâmetros")
        fruit_key = st.selectbox(
            "Fruta",
            options=list(PRESETS.keys()),
            format_func=lambda key: PRESETS[key]["label"],
            key="fruit_key",
        )

        p = PRESETS[fruit_key]

        if st.session_state.get("last_loaded_fruit") != fruit_key:
            st.session_state.last_loaded_fruit = fruit_key
            st.session_state.dureza_0_input = float(p["dureza_0_default"])
            st.session_state.brix_0_input = float(p["brix_0_default"])

        T_c = st.slider("Temperatura (°C)", 0.0, 25.0, 10.0, 0.5)
        E_ppm = st.slider("Etileno (ppm)", 0.0, 10.0, 0.2, 0.1)
        RH_pct = st.slider("Humidade (%)", 40, 100, 90, 1)
        days = st.slider("Dias", 5, 180, 40, 5)

        default_dureza = float(p["dureza_0_default"])
        default_brix = float(p["brix_0_default"])

        dureza_0 = st.number_input(
            "Dureza no dia 0",
            min_value=0.0,
            value=st.session_state.get("dureza_0_input", default_dureza),
            step=0.1,
            key="dureza_0_input",
        )
        brix_0 = st.number_input(
            "°Brix no dia 0",
            min_value=0.0,
            value=st.session_state.get("brix_0_input", default_brix),
            step=0.1,
            key="brix_0_input",
        )

        st.session_state.dureza_0_input = float(dureza_0)
        st.session_state.brix_0_input = float(brix_0)

        st.markdown("---")
        st.write("Preset atual:", p["label"])
        st.write("Dureza mínima:", p["dureza_min"])
        st.write("Faixa de °Brix:", f"{p['brix_min']}–{p['brix_max']}")

    if st.button("Executar simulação", use_container_width=True):
        result = run_simulation(fruit_key, T_c, E_ppm, RH_pct, days, dureza_0, brix_0)

        t = result["t"]
        dureza = result["dureza"]
        brix = result["brix"]
        quality = result["quality"]

        st.subheader(f"Resultado para {result['p']['label']}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Dureza inicial", f"{dureza[0]:.1f}")
        col2.metric("Dureza final", f"{dureza[-1]:.1f}")
        col3.metric("Qualidade final", f"{quality[-1]:.1f}/100")

        col4, col5 = st.columns(2)
        col4.metric("°Brix inicial", f"{brix[0]:.1f}")
        col5.metric("°Brix final", f"{brix[-1]:.1f}")

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(t, dureza, label="Dureza")
        ax.plot(t, brix, label="°Brix")
        ax.set_xlabel("Dias")
        ax.set_ylabel("Valor")
        ax.set_title(f"{result['p']['label']} | T={T_c:.1f}°C | E={E_ppm:.1f} ppm | RH={RH_pct}%")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)

        fig2, ax2 = plt.subplots(figsize=(10, 4))
        ax2.plot(t, quality)
        ax2.set_ylabel("Qualidade (0–100)")
        ax2.set_xlabel("Dias")
        ax2.set_title("Índice de qualidade")
        ax2.grid(True, alpha=0.3)
        st.pyplot(fig2)

        with st.expander("Parâmetros usados"):
            st.json({
                "fruta": result['p']['label'],
                "T_C": T_c,
                "E_ppm": E_ppm,
                "RH_pct": RH_pct,
                "dias": days,
                "dureza_0": dureza_0,
                "brix_0": brix_0,
            })
    else:
        st.info("Ajuste os parâmetros à esquerda e clique em “Executar simulação” para gerar os gráficos.")


if __name__ == "__main__":
    main()
