## Array de atributos que se utilizan para realizar la predicción
lab_attributes = [
            "pH", "PaCO2", "AST", "BUN", "Alkalinephos", "Chloride", "Creatinine",
            "Lactate", "Magnesium", "Potassium", "Bilirubin_total", "PTT", "WBC",
            "Fibrinogen", "Platelets"
        ]
vital_attributes = ["HR", "O2Sat", "Temp",
                            "SBP", "MAP", "DBP", "Resp", "EtCO2"]

demographic_attributes = ["Age", "ICULOS","Gender"]

EXPECTED_KEYS = lab_attributes + vital_attributes + demographic_attributes