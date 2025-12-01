
import pandas as pd

clientes = pd.read_csv("clientes.csv")
prestamos = pd.read_csv("prestamos.csv")
pagos = pd.read_csv("pagos.csv")

df = prestamos.merge(clientes, on="cliente_id", how="left")
pagos_agg = pagos.groupby("prestamo_id")["monto_pagado"].sum().reset_index()
df_full = df.merge(pagos_agg, on="prestamo_id", how="left")

df_full["monto_pagado"] = df_full["monto_pagado"].fillna(0)
df_full["saldo"] = df_full["monto"] - df_full["monto_pagado"]

df_full.to_csv("prestamos_enriquecidos.csv", index=False)

print("Archivo generado: prestamos_enriquecidos.csv")
