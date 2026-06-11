from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


LANGUAGES = {
    "pt": "Português",
    "en": "English",
    "es": "Español",
    "tr": "Türkçe",
}


TEXT = {
    "pt": {
        "page_title": "Simulador de Frutas",
        "missing_main_logo": "Logo principal não encontrado.",
        "app_title": "Simulador de qualidade e firmeza de frutas",
        "language": "Idioma",
        "parameters": "Parâmetros",
        "fruit": "Fruta",
        "temperature": "Temperatura (°C)",
        "ethylene": "Etileno (ppm)",
        "humidity": "Humidade (%)",
        "days": "Dias",
        "initial_firmness": "Dureza no dia 0",
        "initial_brix": "°Brix no dia 0",
        "current_preset": "Preset atual:",
        "minimum_firmness": "Dureza mínima:",
        "brix_range": "Faixa de °Brix:",
        "run_simulation": "Executar simulação",
        "result_for": "Resultado para {fruit}",
        "initial_firmness_metric": "Dureza inicial",
        "final_firmness_metric": "Dureza final",
        "final_quality_metric": "Qualidade final",
        "initial_brix_metric": "°Brix inicial",
        "final_brix_metric": "°Brix final",
        "firmness": "Dureza",
        "value": "Valor",
        "quality_index": "Índice de qualidade",
        "quality_axis": "Qualidade (0-100)",
        "used_parameters": "Parâmetros usados",
        "json_fruit": "fruta",
        "json_days": "dias",
        "empty_state": "Ajuste os parâmetros à esquerda e clique em \"Executar simulação\" para gerar os gráficos.",
    },
    "en": {
        "page_title": "Fruit Simulator",
        "missing_main_logo": "Main logo not found.",
        "app_title": "Fruit quality and firmness simulator",
        "language": "Language",
        "parameters": "Parameters",
        "fruit": "Fruit",
        "temperature": "Temperature (°C)",
        "ethylene": "Ethylene (ppm)",
        "humidity": "Humidity (%)",
        "days": "Days",
        "initial_firmness": "Firmness on day 0",
        "initial_brix": "°Brix on day 0",
        "current_preset": "Current preset:",
        "minimum_firmness": "Minimum firmness:",
        "brix_range": "°Brix range:",
        "run_simulation": "Run simulation",
        "result_for": "Result for {fruit}",
        "initial_firmness_metric": "Initial firmness",
        "final_firmness_metric": "Final firmness",
        "final_quality_metric": "Final quality",
        "initial_brix_metric": "Initial °Brix",
        "final_brix_metric": "Final °Brix",
        "firmness": "Firmness",
        "value": "Value",
        "quality_index": "Quality index",
        "quality_axis": "Quality (0-100)",
        "used_parameters": "Parameters used",
        "json_fruit": "fruit",
        "json_days": "days",
        "empty_state": "Adjust the parameters on the left and click \"Run simulation\" to generate the charts.",
    },
    "es": {
        "page_title": "Simulador de Frutas",
        "missing_main_logo": "No se encontró el logotipo principal.",
        "app_title": "Simulador de calidad y firmeza de frutas",
        "language": "Idioma",
        "parameters": "Parámetros",
        "fruit": "Fruta",
        "temperature": "Temperatura (°C)",
        "ethylene": "Etileno (ppm)",
        "humidity": "Humedad (%)",
        "days": "Días",
        "initial_firmness": "Firmeza en el día 0",
        "initial_brix": "°Brix en el día 0",
        "current_preset": "Preset actual:",
        "minimum_firmness": "Firmeza mínima:",
        "brix_range": "Rango de °Brix:",
        "run_simulation": "Ejecutar simulación",
        "result_for": "Resultado para {fruit}",
        "initial_firmness_metric": "Firmeza inicial",
        "final_firmness_metric": "Firmeza final",
        "final_quality_metric": "Calidad final",
        "initial_brix_metric": "°Brix inicial",
        "final_brix_metric": "°Brix final",
        "firmness": "Firmeza",
        "value": "Valor",
        "quality_index": "Índice de calidad",
        "quality_axis": "Calidad (0-100)",
        "used_parameters": "Parámetros usados",
        "json_fruit": "fruta",
        "json_days": "días",
        "empty_state": "Ajuste los parámetros de la izquierda y haga clic en \"Ejecutar simulación\" para generar los gráficos.",
    },
    "tr": {
        "page_title": "Meyve Simülatörü",
        "missing_main_logo": "Ana logo bulunamadı.",
        "app_title": "Meyve kalite ve sertlik simülatörü",
        "language": "Dil",
        "parameters": "Parametreler",
        "fruit": "Meyve",
        "temperature": "Sıcaklık (°C)",
        "ethylene": "Etilen (ppm)",
        "humidity": "Nem (%)",
        "days": "Gün",
        "initial_firmness": "0. gün sertliği",
        "initial_brix": "0. gün °Brix",
        "current_preset": "Geçerli preset:",
        "minimum_firmness": "Minimum sertlik:",
        "brix_range": "°Brix aralığı:",
        "run_simulation": "Simülasyonu çalıştır",
        "result_for": "{fruit} sonucu",
        "initial_firmness_metric": "Başlangıç sertliği",
        "final_firmness_metric": "Son sertlik",
        "final_quality_metric": "Son kalite",
        "initial_brix_metric": "Başlangıç °Brix",
        "final_brix_metric": "Son °Brix",
        "firmness": "Sertlik",
        "value": "Değer",
        "quality_index": "Kalite endeksi",
        "quality_axis": "Kalite (0-100)",
        "used_parameters": "Kullanılan parametreler",
        "json_fruit": "meyve",
        "json_days": "gün",
        "empty_state": "Grafikleri oluşturmak için soldaki parametreleri ayarlayın ve \"Simülasyonu çalıştır\" düğmesine tıklayın.",
    },
}


FRUIT_LABELS = {
    "pt": {
        "kiwi_hayward": "Kiwi (Hayward)",
        "kiwi_baby": "Kiwi (Baby / Kiwi Berry)",
        "maca_golden": "Maçã (Golden)",
        "maca_reineta": "Maçã (Reineta)",
        "maca_gala": "Maçã (Gala)",
        "maca_fuji": "Maçã (Fuji)",
        "laranja": "Laranja",
        "banana": "Banana",
        "mirtilo": "Mirtilo",
        "framboesa": "Framboesa",
        "pera": "Pera",
        "ameixa": "Ameixa",
        "pessego": "Pêssego",
        "cereja": "Cereja",
        "morango": "Morango",
        "uva": "Uva",
        "figo": "Figo",
        "melao": "Melão",
    },
    "en": {
        "kiwi_hayward": "Kiwi (Hayward)",
        "kiwi_baby": "Kiwi berry",
        "maca_golden": "Apple (Golden)",
        "maca_reineta": "Apple (Reineta)",
        "maca_gala": "Apple (Gala)",
        "maca_fuji": "Apple (Fuji)",
        "laranja": "Orange",
        "banana": "Banana",
        "mirtilo": "Blueberry",
        "framboesa": "Raspberry",
        "pera": "Pear",
        "ameixa": "Plum",
        "pessego": "Peach",
        "cereja": "Cherry",
        "morango": "Strawberry",
        "uva": "Grape",
        "figo": "Fig",
        "melao": "Melon",
    },
    "es": {
        "kiwi_hayward": "Kiwi (Hayward)",
        "kiwi_baby": "Kiwi baby",
        "maca_golden": "Manzana (Golden)",
        "maca_reineta": "Manzana (Reineta)",
        "maca_gala": "Manzana (Gala)",
        "maca_fuji": "Manzana (Fuji)",
        "laranja": "Naranja",
        "banana": "Banana",
        "mirtilo": "Arándano",
        "framboesa": "Frambuesa",
        "pera": "Pera",
        "ameixa": "Ciruela",
        "pessego": "Melocotón",
        "cereja": "Cereza",
        "morango": "Fresa",
        "uva": "Uva",
        "figo": "Higo",
        "melao": "Melón",
    },
    "tr": {
        "kiwi_hayward": "Kivi (Hayward)",
        "kiwi_baby": "Mini kivi",
        "maca_golden": "Elma (Golden)",
        "maca_reineta": "Elma (Reineta)",
        "maca_gala": "Elma (Gala)",
        "maca_fuji": "Elma (Fuji)",
        "laranja": "Portakal",
        "banana": "Muz",
        "mirtilo": "Yaban mersini",
        "framboesa": "Ahududu",
        "pera": "Armut",
        "ameixa": "Erik",
        "pessego": "Şeftali",
        "cereja": "Kiraz",
        "morango": "Çilek",
        "uva": "Üzüm",
        "figo": "İncir",
        "melao": "Kavun",
    },
}


def tr(lang, key, **kwargs):
    value = TEXT[lang][key]
    return value.format(**kwargs) if kwargs else value


def fruit_label(lang, fruit_key):
    return FRUIT_LABELS[lang].get(fruit_key, PRESETS[fruit_key]["label"])


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
    st.set_page_config(page_title=tr("pt", "page_title"), layout="wide")

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
            st.info(tr("pt", "missing_main_logo"))

        lang = st.selectbox(
            tr("pt", "language"),
            options=list(LANGUAGES.keys()),
            format_func=lambda code: LANGUAGES[code],
            index=0,
            key="language",
        )

    st.title(tr(lang, "app_title"))

    with st.sidebar:
        st.header(tr(lang, "parameters"))
        fruit_key = st.selectbox(
            tr(lang, "fruit"),
            options=list(PRESETS.keys()),
            format_func=lambda key: fruit_label(lang, key),
            key="fruit_key",
        )

        p = PRESETS[fruit_key]

        T_c = st.slider(tr(lang, "temperature"), 0.0, 25.0, 10.0, 0.5)
        E_ppm = st.slider(tr(lang, "ethylene"), 0.0, 10.0, 0.2, 0.1)
        RH_pct = st.slider(tr(lang, "humidity"), 40, 100, 90, 1)
        days = st.slider(tr(lang, "days"), 5, 180, 40, 5)

        default_dureza = float(p["dureza_0_default"])
        default_brix = float(p["brix_0_default"])

        dureza_0 = st.number_input(
            tr(lang, "initial_firmness"),
            min_value=0.0,
            value=default_dureza,
            step=0.1,
            key=f"dureza_0_{fruit_key}",
        )
        brix_0 = st.number_input(
            tr(lang, "initial_brix"),
            min_value=0.0,
            value=default_brix,
            step=0.1,
            key=f"brix_0_{fruit_key}",
        )

        st.markdown("---")
        st.write(tr(lang, "current_preset"), fruit_label(lang, fruit_key))
        st.write(tr(lang, "minimum_firmness"), p["dureza_min"])
        st.write(tr(lang, "brix_range"), f"{p['brix_min']}-{p['brix_max']}")

    if st.button(tr(lang, "run_simulation"), use_container_width=True):
        result = run_simulation(fruit_key, T_c, E_ppm, RH_pct, days, dureza_0, brix_0)

        t = result["t"]
        dureza = result["dureza"]
        brix = result["brix"]
        quality = result["quality"]
        current_fruit_label = fruit_label(lang, fruit_key)

        st.subheader(tr(lang, "result_for", fruit=current_fruit_label))

        col1, col2, col3 = st.columns(3)
        col1.metric(tr(lang, "initial_firmness_metric"), f"{dureza[0]:.1f}")
        col2.metric(tr(lang, "final_firmness_metric"), f"{dureza[-1]:.1f}")
        col3.metric(tr(lang, "final_quality_metric"), f"{quality[-1]:.1f}/100")

        col4, col5 = st.columns(2)
        col4.metric(tr(lang, "initial_brix_metric"), f"{brix[0]:.1f}")
        col5.metric(tr(lang, "final_brix_metric"), f"{brix[-1]:.1f}")

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(t, dureza, label=tr(lang, "firmness"))
        ax.plot(t, brix, label="°Brix")
        ax.set_xlabel(tr(lang, "days"))
        ax.set_ylabel(tr(lang, "value"))
        ax.set_title(f"{current_fruit_label} | T={T_c:.1f}°C | E={E_ppm:.1f} ppm | RH={RH_pct}%")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)

        fig2, ax2 = plt.subplots(figsize=(10, 4))
        ax2.plot(t, quality)
        ax2.set_ylabel(tr(lang, "quality_axis"))
        ax2.set_xlabel(tr(lang, "days"))
        ax2.set_title(tr(lang, "quality_index"))
        ax2.grid(True, alpha=0.3)
        st.pyplot(fig2)

        with st.expander(tr(lang, "used_parameters")):
            st.json({
                tr(lang, "json_fruit"): current_fruit_label,
                "T_C": T_c,
                "E_ppm": E_ppm,
                "RH_pct": RH_pct,
                tr(lang, "json_days"): days,
                "dureza_0": dureza_0,
                "brix_0": brix_0,
            })
    else:
        st.info(tr(lang, "empty_state"))


if __name__ == "__main__":
    main()
