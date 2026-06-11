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
        "page_title": "Simulador de Índice de Qualidade de Frutas",
        "missing_main_logo": "Logo principal não encontrado.",
        "app_title": "Simulador de Índice de Qualidade de Frutas",
        "language": "Idioma",
        "parameters": "Parâmetros",
        "fruit": "Fruta",
        "temperature": "Temperatura (°C)",
        "ethylene": "Etileno (ppm)",
        "humidity": "Humidade (%)",
        "co2": "CO2 (%)",
        "days": "Dias",
        "initial_firmness": "Dureza no dia 0",
        "firmness_note": "Dureza expressa em Newton (N). Para frutos pequenos, representa força de compressão/penetração aproximada e deve ser calibrada com o protocolo experimental usado.",
        "initial_brix": "°Brix no dia 0",
        "model_modules": "Módulos do modelo",
        "use_temperature": "Usar temperatura",
        "use_humidity": "Usar humidade",
        "use_ethylene": "Usar etileno",
        "use_co2": "Usar CO2",
        "use_mold": "Usar bolor na qualidade",
        "advanced_profiles": "Usar perfis temporais ambientais",
        "temporal_profile": "Perfil temporal",
        "profile_model": "Modelo",
        "profile_constant": "Constante",
        "profile_linear_increase": "Aumento linear",
        "profile_linear_decrease": "Diminuição linear",
        "profile_exponential": "Aproximação exponencial",
        "profile_sinusoidal": "Oscilação diária",
        "profile_step": "Degrau",
        "profile_pulse": "Pulso",
        "profile_slope": "Variação por dia",
        "profile_target": "Valor alvo",
        "profile_rate": "Taxa",
        "profile_amplitude": "Amplitude",
        "profile_period": "Período (dias)",
        "profile_phase": "Fase",
        "profile_step_day": "Dia do degrau",
        "profile_step_value": "Valor após degrau",
        "profile_pulse_start": "Início do pulso",
        "profile_pulse_end": "Fim do pulso",
        "profile_pulse_value": "Valor do pulso",
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
        "mold": "Bolor",
        "mold_axis": "Bolor / carga microbiológica (0-1)",
        "mold_index": "Bolor / carga microbiológica",
        "environment_profiles": "Perfis ambientais",
        "value": "Valor",
        "quality_index": "Índice de qualidade",
        "quality_axis": "Qualidade (0-100)",
        "used_parameters": "Parâmetros usados",
        "json_fruit": "fruta",
        "json_days": "dias",
        "empty_state": "Ajuste os parâmetros à esquerda e clique em \"Executar simulação\" para gerar os gráficos.",
    },
    "en": {
        "page_title": "Fruit Quality Index Simulator",
        "missing_main_logo": "Main logo not found.",
        "app_title": "Fruit Quality Index Simulator",
        "language": "Language",
        "parameters": "Parameters",
        "fruit": "Fruit",
        "temperature": "Temperature (°C)",
        "ethylene": "Ethylene (ppm)",
        "humidity": "Humidity (%)",
        "co2": "CO2 (%)",
        "days": "Days",
        "initial_firmness": "Firmness on day 0",
        "firmness_note": "Firmness is expressed in Newtons (N). For small fruits, it represents approximate compression/penetration force and should be calibrated with the experimental protocol used.",
        "initial_brix": "°Brix on day 0",
        "model_modules": "Model modules",
        "use_temperature": "Use temperature",
        "use_humidity": "Use humidity",
        "use_ethylene": "Use ethylene",
        "use_co2": "Use CO2",
        "use_mold": "Use mold in quality",
        "advanced_profiles": "Use temporal environmental profiles",
        "temporal_profile": "Temporal profile",
        "profile_model": "Model",
        "profile_constant": "Constant",
        "profile_linear_increase": "Linear increase",
        "profile_linear_decrease": "Linear decrease",
        "profile_exponential": "Exponential approach",
        "profile_sinusoidal": "Daily oscillation",
        "profile_step": "Step change",
        "profile_pulse": "Pulse",
        "profile_slope": "Change per day",
        "profile_target": "Target value",
        "profile_rate": "Rate",
        "profile_amplitude": "Amplitude",
        "profile_period": "Period (days)",
        "profile_phase": "Phase",
        "profile_step_day": "Step day",
        "profile_step_value": "Value after step",
        "profile_pulse_start": "Pulse start",
        "profile_pulse_end": "Pulse end",
        "profile_pulse_value": "Pulse value",
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
        "mold": "Mold",
        "mold_axis": "Mold / microbial load (0-1)",
        "mold_index": "Mold / microbial load",
        "environment_profiles": "Environmental profiles",
        "value": "Value",
        "quality_index": "Quality index",
        "quality_axis": "Quality (0-100)",
        "used_parameters": "Parameters used",
        "json_fruit": "fruit",
        "json_days": "days",
        "empty_state": "Adjust the parameters on the left and click \"Run simulation\" to generate the charts.",
    },
    "es": {
        "page_title": "Simulador de Índice de Calidad de Frutas",
        "missing_main_logo": "No se encontró el logotipo principal.",
        "app_title": "Simulador de Índice de Calidad de Frutas",
        "language": "Idioma",
        "parameters": "Parámetros",
        "fruit": "Fruta",
        "temperature": "Temperatura (°C)",
        "ethylene": "Etileno (ppm)",
        "humidity": "Humedad (%)",
        "co2": "CO2 (%)",
        "days": "Días",
        "initial_firmness": "Firmeza en el día 0",
        "firmness_note": "Firmeza expresada en Newtons (N). Para frutos pequeños, representa fuerza aproximada de compresión/penetración y debe calibrarse con el protocolo experimental usado.",
        "initial_brix": "°Brix en el día 0",
        "model_modules": "Módulos del modelo",
        "use_temperature": "Usar temperatura",
        "use_humidity": "Usar humedad",
        "use_ethylene": "Usar etileno",
        "use_co2": "Usar CO2",
        "use_mold": "Usar moho en la calidad",
        "advanced_profiles": "Usar perfiles ambientales temporales",
        "temporal_profile": "Perfil temporal",
        "profile_model": "Modelo",
        "profile_constant": "Constante",
        "profile_linear_increase": "Aumento lineal",
        "profile_linear_decrease": "Disminución lineal",
        "profile_exponential": "Aproximación exponencial",
        "profile_sinusoidal": "Oscilación diaria",
        "profile_step": "Escalón",
        "profile_pulse": "Pulso",
        "profile_slope": "Cambio por día",
        "profile_target": "Valor objetivo",
        "profile_rate": "Tasa",
        "profile_amplitude": "Amplitud",
        "profile_period": "Período (días)",
        "profile_phase": "Fase",
        "profile_step_day": "Día del escalón",
        "profile_step_value": "Valor después del escalón",
        "profile_pulse_start": "Inicio del pulso",
        "profile_pulse_end": "Fin del pulso",
        "profile_pulse_value": "Valor del pulso",
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
        "mold": "Moho",
        "mold_axis": "Moho / carga microbiológica (0-1)",
        "mold_index": "Moho / carga microbiológica",
        "environment_profiles": "Perfiles ambientales",
        "value": "Valor",
        "quality_index": "Índice de calidad",
        "quality_axis": "Calidad (0-100)",
        "used_parameters": "Parámetros usados",
        "json_fruit": "fruta",
        "json_days": "días",
        "empty_state": "Ajuste los parámetros de la izquierda y haga clic en \"Ejecutar simulación\" para generar los gráficos.",
    },
    "tr": {
        "page_title": "Meyve Kalite İndeksi Simülatörü",
        "missing_main_logo": "Ana logo bulunamadı.",
        "app_title": "Meyve Kalite İndeksi Simülatörü",
        "language": "Dil",
        "parameters": "Parametreler",
        "fruit": "Meyve",
        "temperature": "Sıcaklık (°C)",
        "ethylene": "Etilen (ppm)",
        "humidity": "Nem (%)",
        "co2": "CO2 (%)",
        "days": "Gün",
        "initial_firmness": "0. gün sertliği",
        "firmness_note": "Sertlik Newton (N) cinsinden ifade edilir. Küçük meyveler için yaklaşık sıkıştırma/penetrasyon kuvvetini temsil eder ve kullanılan deney protokolüyle kalibre edilmelidir.",
        "initial_brix": "0. gün °Brix",
        "model_modules": "Model modülleri",
        "use_temperature": "Sıcaklığı kullan",
        "use_humidity": "Nemi kullan",
        "use_ethylene": "Etileni kullan",
        "use_co2": "CO2 kullan",
        "use_mold": "Kalitede küfü kullan",
        "advanced_profiles": "Zamana bağlı çevresel profilleri kullan",
        "temporal_profile": "Zamansal profil",
        "profile_model": "Model",
        "profile_constant": "Sabit",
        "profile_linear_increase": "Doğrusal artış",
        "profile_linear_decrease": "Doğrusal azalış",
        "profile_exponential": "Üstel yaklaşım",
        "profile_sinusoidal": "Günlük salınım",
        "profile_step": "Basamak değişimi",
        "profile_pulse": "Darbe",
        "profile_slope": "Günlük değişim",
        "profile_target": "Hedef değer",
        "profile_rate": "Oran",
        "profile_amplitude": "Genlik",
        "profile_period": "Periyot (gün)",
        "profile_phase": "Faz",
        "profile_step_day": "Basamak günü",
        "profile_step_value": "Basamak sonrası değer",
        "profile_pulse_start": "Darbe başlangıcı",
        "profile_pulse_end": "Darbe bitişi",
        "profile_pulse_value": "Darbe değeri",
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
        "mold": "Küf",
        "mold_axis": "Küf / mikrobiyal yük (0-1)",
        "mold_index": "Küf / mikrobiyal yük",
        "environment_profiles": "Çevresel profiller",
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


PROFILE_MODEL_LABEL_KEYS = {
    "constant": "profile_constant",
    "linear_increase": "profile_linear_increase",
    "linear_decrease": "profile_linear_decrease",
    "exponential_approach": "profile_exponential",
    "sinusoidal": "profile_sinusoidal",
    "step": "profile_step",
    "pulse": "profile_pulse",
}


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


FIRMNESS_NEWTON_CALIBRATION = {
    "kiwi_hayward": {"dureza_0_default": 75.0, "dureza_min": 5.0, "qual_firm_threshold": 12.0},
    "kiwi_baby": {"dureza_0_default": 35.0, "dureza_min": 2.0, "qual_firm_threshold": 8.0},
    "maca_golden": {"dureza_0_default": 72.0, "dureza_min": 12.0, "qual_firm_threshold": 35.0},
    "maca_reineta": {"dureza_0_default": 65.0, "dureza_min": 10.0, "qual_firm_threshold": 30.0},
    "maca_gala": {"dureza_0_default": 60.0, "dureza_min": 9.0, "qual_firm_threshold": 28.0},
    "maca_fuji": {"dureza_0_default": 80.0, "dureza_min": 15.0, "qual_firm_threshold": 40.0},
    "laranja": {"dureza_0_default": 55.0, "dureza_min": 30.0, "qual_firm_threshold": 38.0},
    "banana": {"dureza_0_default": 25.0, "dureza_min": 2.0, "qual_firm_threshold": 8.0},
    "mirtilo": {"dureza_0_default": 3.0, "dureza_min": 0.5, "qual_firm_threshold": 1.5},
    "framboesa": {"dureza_0_default": 1.5, "dureza_min": 0.2, "qual_firm_threshold": 0.7},
    "pera": {"dureza_0_default": 60.0, "dureza_min": 4.0, "qual_firm_threshold": 12.0},
    "ameixa": {"dureza_0_default": 35.0, "dureza_min": 3.0, "qual_firm_threshold": 8.0},
    "pessego": {"dureza_0_default": 35.0, "dureza_min": 2.0, "qual_firm_threshold": 8.0},
    "cereja": {"dureza_0_default": 6.0, "dureza_min": 1.0, "qual_firm_threshold": 3.0},
    "morango": {"dureza_0_default": 3.0, "dureza_min": 0.5, "qual_firm_threshold": 1.5},
    "uva": {"dureza_0_default": 5.0, "dureza_min": 1.0, "qual_firm_threshold": 2.5},
    "figo": {"dureza_0_default": 2.0, "dureza_min": 0.2, "qual_firm_threshold": 0.8},
    "melao": {"dureza_0_default": 40.0, "dureza_min": 3.0, "qual_firm_threshold": 12.0},
}

for fruit_key, calibration in FIRMNESS_NEWTON_CALIBRATION.items():
    PRESETS[fruit_key].update(calibration)
    PRESETS[fruit_key]["firmness_unit"] = "N"


def k_temp_scaling(Ea, T, Tref):
    R = 8.314
    return np.exp((-Ea / R) * (1.0 / T - 1.0 / Tref))


def constant_profile(value):
    return {"model": "constant", "x0": float(value)}


def generate_profile(t, cfg, min_value=None, max_value=None):
    model = cfg.get("model", "constant")
    x0 = float(cfg.get("x0", 0.0))

    if model == "constant":
        values = np.full_like(t, x0, dtype=float)
    elif model == "linear_increase":
        values = x0 + float(cfg.get("slope", 0.0)) * t
    elif model == "linear_decrease":
        values = x0 - float(cfg.get("slope", 0.0)) * t
    elif model == "exponential_approach":
        x_inf = float(cfg.get("x_inf", x0))
        rate = max(0.0, float(cfg.get("rate", 1.0)))
        values = x_inf + (x0 - x_inf) * np.exp(-rate * t)
    elif model == "sinusoidal":
        amplitude = float(cfg.get("amplitude", 0.0))
        period = max(1e-6, float(cfg.get("period", 1.0)))
        phase = float(cfg.get("phase", 0.0))
        values = x0 + amplitude * np.sin(2.0 * np.pi * t / period + phase)
    elif model == "step":
        t_step = float(cfg.get("t_step", 0.0))
        x1 = float(cfg.get("x1", x0))
        values = np.where(t < t_step, x0, x1)
    elif model == "pulse":
        t_start = float(cfg.get("t_start", 0.0))
        t_end = float(cfg.get("t_end", t_start))
        x_pulse = float(cfg.get("x_pulse", x0))
        values = np.where((t >= t_start) & (t <= t_end), x_pulse, x0)
    else:
        values = np.full_like(t, x0, dtype=float)

    if min_value is not None or max_value is not None:
        values = np.clip(
            values,
            -np.inf if min_value is None else min_value,
            np.inf if max_value is None else max_value,
        )

    return values


def mold_load_curve(p, T_profile, RH_profile, t, use_temperature=True, use_humidity=True):
    T_effective = T_profile if use_temperature else np.full_like(t, p["Tref_C"], dtype=float)
    RH_effective = RH_profile if use_humidity else np.full_like(t, p["RH_ref"], dtype=float)

    r_ref = p.get("mold_r_ref", 0.015)
    rh_crit = p.get("mold_RH_crit", 88.0)
    q10 = p.get("mold_Q10", 2.0)

    temp_factor = q10 ** ((T_effective - p["Tref_C"]) / 10.0)
    humidity_factor = 1.0 / (1.0 + np.exp(-0.25 * (RH_effective - rh_crit)))
    r_mold = r_ref * temp_factor * humidity_factor

    if len(t) > 1:
        dt = t[1] - t[0]
    else:
        dt = 0.05
    mold_pressure = np.cumsum(r_mold) * dt
    mold = 1.0 - np.exp(-mold_pressure)
    return np.clip(mold, 0.0, 1.0), r_mold


def run_simulation(
    fruit_key,
    T_c,
    E_ppm,
    RH_pct,
    CO2_pct,
    days,
    dureza_0_user,
    brix_0_user,
    use_temperature=True,
    use_humidity=True,
    use_ethylene=True,
    use_co2=True,
    use_mold=True,
    temperature_cfg=None,
    humidity_cfg=None,
    ethylene_cfg=None,
    co2_cfg=None,
):
    dt = 0.05

    p = PRESETS[fruit_key]
    t = np.arange(0.0, days, dt)

    T_profile = generate_profile(t, temperature_cfg or constant_profile(T_c), min_value=0.0, max_value=40.0)
    RH_profile = generate_profile(t, humidity_cfg or constant_profile(RH_pct), min_value=0.0, max_value=100.0)
    E_profile = generate_profile(t, ethylene_cfg or constant_profile(E_ppm), min_value=0.0)
    CO2_profile = generate_profile(t, co2_cfg or constant_profile(CO2_pct), min_value=0.0, max_value=20.0)

    T_K = T_profile + 273.15
    Tref_K = p["Tref_C"] + 273.15
    kT = k_temp_scaling(p["Ea_J"], T_K, Tref_K) if use_temperature else np.ones_like(t)
    kE = 1.0 + p["alpha_E"] * E_profile if use_ethylene else np.ones_like(t)

    RH_ref = p["RH_ref"]
    RH_deficit = np.maximum(0.0, (RH_ref - RH_profile) / 100.0)
    kRH = 1.0 + p["beta_RH"] * RH_deficit if use_humidity else np.ones_like(t)
    beta_CO2 = p.get("beta_CO2", 0.08)
    kCO2 = 1.0 / (1.0 + beta_CO2 * CO2_profile) if use_co2 else np.ones_like(t)

    k = p["k_firm_ref"] * kT * kE * kRH * kCO2

    dureza_min = p["dureza_min"]
    dureza_0 = max(dureza_min + 1e-6, float(dureza_0_user))
    dureza = np.empty_like(t)
    if len(dureza) > 0:
        dureza[0] = dureza_0
        for i in range(1, len(t)):
            dureza[i] = dureza_min + (dureza[i - 1] - dureza_min) * np.exp(-k[i - 1] * dt)

    brix_min = p["brix_min"]
    brix_max = p["brix_max"]
    g = p["brix_g"]
    eps = 1e-6

    brix_0 = float(brix_0_user)
    brix_0 = min(brix_max - eps, max(brix_min + eps, brix_0))

    t0_base = (
        (-0.05 * (float(T_profile[0]) - p["Tref_C"]) if use_temperature else 0.0)
        + (-2.0 * np.log1p(float(E_profile[0])) if use_ethylene else 0.0)
        + (0.06 * max(0.0, RH_ref - float(RH_profile[0])) if use_humidity else 0.0)
        + (0.35 * beta_CO2 * float(CO2_profile[0]) if use_co2 else 0.0)
    )

    y = (brix_0 - brix_min) / (brix_max - brix_min)
    t0_from_b0 = (1.0 / g) * np.log((1.0 / y) - 1.0)

    t0_eff = t0_from_b0 + t0_base
    brix_speed = (
        np.sqrt(np.maximum(kT, 1e-6))
        * np.maximum(kE, 1e-6) ** 0.25
        * np.maximum(kRH, 1e-6) ** 0.15
        * np.maximum(kCO2, 1e-6) ** 0.25
    )
    maturity_t = np.cumsum(brix_speed) * dt
    if len(maturity_t) > 0:
        maturity_t = maturity_t - maturity_t[0]
    brix = brix_min + (brix_max - brix_min) / (1.0 + np.exp(-g * (maturity_t - t0_eff)))
    if len(brix) > 0:
        brix[0] = brix_0

    firm_score = 1.0 / (1.0 + np.exp(-0.35 * (dureza - p["qual_firm_threshold"])))
    brix_score = np.exp(-((brix - p["qual_brix_target"]) ** 2) / 2.0)
    base_quality = 100.0 * (0.65 * firm_score + 0.35 * brix_score)
    mold, r_mold = mold_load_curve(p, T_profile, RH_profile, t, use_temperature, use_humidity)
    mold_penalty = p.get("mold_quality_weight", 0.55) * mold if use_mold else 0.0
    quality = np.clip(base_quality * (1.0 - mold_penalty), 0.0, 100.0)

    return {
        "t": t,
        "dureza": dureza,
        "brix": brix,
        "quality": quality,
        "base_quality": base_quality,
        "mold": mold,
        "r_mold": r_mold,
        "profiles": {
            "T_C": T_profile,
            "RH_pct": RH_profile,
            "E_ppm": E_profile,
            "CO2_pct": CO2_profile,
        },
        "k": k,
        "k_factors": {
            "kT": kT,
            "kE": kE,
            "kRH": kRH,
            "kCO2": kCO2,
        },
        "p": p,
        "dureza_0": dureza_0,
        "brix_0": brix_0,
    }


def profile_model_label(lang, model):
    return tr(lang, PROFILE_MODEL_LABEL_KEYS[model])


def render_profile_config(lang, key, label, base_value, days, min_value, max_value, step):
    with st.expander(f"{label} - {tr(lang, 'temporal_profile')}"):
        model = st.selectbox(
            tr(lang, "profile_model"),
            options=list(PROFILE_MODEL_LABEL_KEYS.keys()),
            format_func=lambda item: profile_model_label(lang, item),
            key=f"{key}_profile_model",
        )

        cfg = {"model": model, "x0": float(base_value)}

        if model in {"linear_increase", "linear_decrease"}:
            cfg["slope"] = st.number_input(
                tr(lang, "profile_slope"),
                min_value=0.0,
                value=0.0,
                step=step,
                key=f"{key}_profile_slope",
            )
        elif model == "exponential_approach":
            cfg["x_inf"] = st.number_input(
                tr(lang, "profile_target"),
                min_value=float(min_value),
                max_value=float(max_value),
                value=float(base_value),
                step=step,
                key=f"{key}_profile_target",
            )
            cfg["rate"] = st.number_input(
                tr(lang, "profile_rate"),
                min_value=0.0,
                value=1.0,
                step=0.1,
                key=f"{key}_profile_rate",
            )
        elif model == "sinusoidal":
            cfg["amplitude"] = st.number_input(
                tr(lang, "profile_amplitude"),
                min_value=0.0,
                value=0.0,
                step=step,
                key=f"{key}_profile_amplitude",
            )
            cfg["period"] = st.number_input(
                tr(lang, "profile_period"),
                min_value=0.1,
                value=1.0,
                step=0.1,
                key=f"{key}_profile_period",
            )
            cfg["phase"] = st.number_input(
                tr(lang, "profile_phase"),
                value=0.0,
                step=0.1,
                key=f"{key}_profile_phase",
            )
        elif model == "step":
            cfg["t_step"] = st.number_input(
                tr(lang, "profile_step_day"),
                min_value=0.0,
                max_value=float(days),
                value=min(1.0, float(days)),
                step=0.5,
                key=f"{key}_profile_step_day",
            )
            cfg["x1"] = st.number_input(
                tr(lang, "profile_step_value"),
                min_value=float(min_value),
                max_value=float(max_value),
                value=float(base_value),
                step=step,
                key=f"{key}_profile_step_value",
            )
        elif model == "pulse":
            cfg["t_start"] = st.number_input(
                tr(lang, "profile_pulse_start"),
                min_value=0.0,
                max_value=float(days),
                value=min(1.0, float(days)),
                step=0.5,
                key=f"{key}_profile_pulse_start",
            )
            cfg["t_end"] = st.number_input(
                tr(lang, "profile_pulse_end"),
                min_value=0.0,
                max_value=float(days),
                value=min(2.0, float(days)),
                step=0.5,
                key=f"{key}_profile_pulse_end",
            )
            cfg["x_pulse"] = st.number_input(
                tr(lang, "profile_pulse_value"),
                min_value=float(min_value),
                max_value=float(max_value),
                value=float(base_value),
                step=step,
                key=f"{key}_profile_pulse_value",
            )

    return cfg


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
        firmness_unit = p.get("firmness_unit", "N")

        T_c = st.slider(tr(lang, "temperature"), 0.0, 25.0, 10.0, 0.5)
        E_ppm = st.slider(tr(lang, "ethylene"), 0.0, 10.0, 0.2, 0.1)
        RH_pct = st.slider(tr(lang, "humidity"), 40, 100, 90, 1)
        CO2_pct = st.slider(tr(lang, "co2"), 0.0, 20.0, 0.04, 0.01)
        days = st.slider(tr(lang, "days"), 5, 180, 40, 5)

        st.subheader(tr(lang, "model_modules"))
        use_temperature = st.checkbox(tr(lang, "use_temperature"), value=True)
        use_humidity = st.checkbox(tr(lang, "use_humidity"), value=True)
        use_ethylene = st.checkbox(tr(lang, "use_ethylene"), value=True)
        use_co2 = st.checkbox(tr(lang, "use_co2"), value=True)
        use_mold = st.checkbox(tr(lang, "use_mold"), value=True)
        advanced_profiles = st.checkbox(tr(lang, "advanced_profiles"), value=False)

        temperature_cfg = None
        humidity_cfg = None
        ethylene_cfg = None
        co2_cfg = None

        if advanced_profiles:
            temperature_cfg = render_profile_config(
                lang, "temperature", tr(lang, "temperature"), T_c, days, 0.0, 40.0, 0.5
            )
            humidity_cfg = render_profile_config(
                lang, "humidity", tr(lang, "humidity"), RH_pct, days, 0.0, 100.0, 1.0
            )
            ethylene_cfg = render_profile_config(
                lang, "ethylene", tr(lang, "ethylene"), E_ppm, days, 0.0, 50.0, 0.1
            )
            co2_cfg = render_profile_config(
                lang, "co2", tr(lang, "co2"), CO2_pct, days, 0.0, 20.0, 0.1
            )

        default_dureza = float(p["dureza_0_default"])
        default_brix = float(p["brix_0_default"])

        dureza_0 = st.number_input(
            f"{tr(lang, 'initial_firmness')} ({firmness_unit})",
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
        st.write(tr(lang, "minimum_firmness"), f"{p['dureza_min']} {firmness_unit}")
        st.write(tr(lang, "brix_range"), f"{p['brix_min']}-{p['brix_max']}")
        st.caption(tr(lang, "firmness_note"))

    if st.button(tr(lang, "run_simulation"), use_container_width=True):
        result = run_simulation(
            fruit_key,
            T_c,
            E_ppm,
            RH_pct,
            CO2_pct,
            days,
            dureza_0,
            brix_0,
            use_temperature=use_temperature,
            use_humidity=use_humidity,
            use_ethylene=use_ethylene,
            use_co2=use_co2,
            use_mold=use_mold,
            temperature_cfg=temperature_cfg,
            humidity_cfg=humidity_cfg,
            ethylene_cfg=ethylene_cfg,
            co2_cfg=co2_cfg,
        )

        t = result["t"]
        dureza = result["dureza"]
        brix = result["brix"]
        quality = result["quality"]
        mold = result["mold"]
        profiles = result["profiles"]
        current_fruit_label = fruit_label(lang, fruit_key)
        firmness_unit = result["p"].get("firmness_unit", "N")

        st.subheader(tr(lang, "result_for", fruit=current_fruit_label))

        col1, col2, col3 = st.columns(3)
        col1.metric(tr(lang, "initial_firmness_metric"), f"{dureza[0]:.1f} {firmness_unit}")
        col2.metric(tr(lang, "final_firmness_metric"), f"{dureza[-1]:.1f} {firmness_unit}")
        col3.metric(tr(lang, "final_quality_metric"), f"{quality[-1]:.1f}/100")

        col4, col5 = st.columns(2)
        col4.metric(tr(lang, "initial_brix_metric"), f"{brix[0]:.1f}")
        col5.metric(tr(lang, "final_brix_metric"), f"{brix[-1]:.1f}")

        fig_firm, ax_firm = plt.subplots(figsize=(10, 4))
        ax_firm.plot(t, dureza, label=f"{tr(lang, 'firmness')} ({firmness_unit})")
        ax_firm.set_xlabel(tr(lang, "days"))
        ax_firm.set_ylabel(f"{tr(lang, 'firmness')} ({firmness_unit})")
        ax_firm.set_title(
            f"{current_fruit_label} | T={T_c:.1f}°C | E={E_ppm:.1f} ppm | "
            f"RH={RH_pct}% | CO2={CO2_pct:.2f}%"
        )
        ax_firm.legend()
        ax_firm.grid(True, alpha=0.3)
        st.pyplot(fig_firm)

        fig_brix, ax_brix = plt.subplots(figsize=(10, 4))
        ax_brix.plot(t, brix, label="°Brix", color="tab:orange")
        ax_brix.set_xlabel(tr(lang, "days"))
        ax_brix.set_ylabel("°Brix")
        ax_brix.set_title(f"{current_fruit_label} | °Brix")
        ax_brix.legend()
        ax_brix.grid(True, alpha=0.3)
        st.pyplot(fig_brix)

        if advanced_profiles:
            fig_env, axes = plt.subplots(4, 1, figsize=(10, 7), sharex=True)
            axes[0].plot(t, profiles["T_C"])
            axes[0].set_ylabel("T (°C)")
            axes[1].plot(t, profiles["RH_pct"])
            axes[1].set_ylabel("RH (%)")
            axes[2].plot(t, profiles["E_ppm"])
            axes[2].set_ylabel("E (ppm)")
            axes[3].plot(t, profiles["CO2_pct"])
            axes[3].set_ylabel("CO2 (%)")
            axes[3].set_xlabel(tr(lang, "days"))
            fig_env.suptitle(tr(lang, "environment_profiles"))
            for env_ax in axes:
                env_ax.grid(True, alpha=0.3)
            fig_env.tight_layout()
            st.pyplot(fig_env)

        fig2, ax2 = plt.subplots(figsize=(10, 4))
        ax2.plot(t, quality)
        ax2.set_ylabel(tr(lang, "quality_axis"))
        ax2.set_xlabel(tr(lang, "days"))
        ax2.set_title(tr(lang, "quality_index"))
        ax2.grid(True, alpha=0.3)
        st.pyplot(fig2)

        if use_mold:
            fig3, ax3 = plt.subplots(figsize=(10, 4))
            ax3.plot(t, mold)
            ax3.set_ylabel(tr(lang, "mold_axis"))
            ax3.set_xlabel(tr(lang, "days"))
            ax3.set_title(tr(lang, "mold_index"))
            ax3.grid(True, alpha=0.3)
            st.pyplot(fig3)

        with st.expander(tr(lang, "used_parameters")):
            st.json({
                tr(lang, "json_fruit"): current_fruit_label,
                "T_C": T_c,
                "E_ppm": E_ppm,
                "RH_pct": RH_pct,
                "CO2_pct": CO2_pct,
                tr(lang, "json_days"): days,
                "firmness_unit": firmness_unit,
                "dureza_0": dureza_0,
                "brix_0": brix_0,
                "use_temperature": use_temperature,
                "use_humidity": use_humidity,
                "use_ethylene": use_ethylene,
                "use_co2": use_co2,
                "use_mold": use_mold,
                "advanced_profiles": advanced_profiles,
                "profile_models": {
                    "T_C": (temperature_cfg or constant_profile(T_c))["model"],
                    "RH_pct": (humidity_cfg or constant_profile(RH_pct))["model"],
                    "E_ppm": (ethylene_cfg or constant_profile(E_ppm))["model"],
                    "CO2_pct": (co2_cfg or constant_profile(CO2_pct))["model"],
                },
                "profile_final_values": {
                    "T_C": float(profiles["T_C"][-1]),
                    "RH_pct": float(profiles["RH_pct"][-1]),
                    "E_ppm": float(profiles["E_ppm"][-1]),
                    "CO2_pct": float(profiles["CO2_pct"][-1]),
                },
                "k_total_mean": float(np.mean(result["k"])),
                "k_total_final": float(result["k"][-1]),
                "k_factors_mean": {
                    "kT": float(np.mean(result["k_factors"]["kT"])),
                    "kE": float(np.mean(result["k_factors"]["kE"])),
                    "kRH": float(np.mean(result["k_factors"]["kRH"])),
                    "kCO2": float(np.mean(result["k_factors"]["kCO2"])),
                },
                "mold_rate_mean": float(np.mean(result["r_mold"])),
                "final_mold": float(mold[-1]),
            })
    else:
        st.info(tr(lang, "empty_state"))


if __name__ == "__main__":
    main()
