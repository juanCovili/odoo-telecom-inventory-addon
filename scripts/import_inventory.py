#!/usr/bin/env python3
"""
Script de importación y sincronización masiva de inventario telecom a Odoo vía XML-RPC.
Permite cargar catálogos desde archivos CSV exportados de Excel.
"""

import csv
import xmlrpc.client
from pathlib import Path

# Configuración de conexión Odoo
ODOO_URL = "http://localhost:8069"
ODOO_DB = "odoo_telecom_db"
ODOO_USER = "admin"
ODOO_PASSWORD = "admin_master_secret"

def import_csv_to_odoo(csv_file_path: Path):
    print(f"[*] Leyendo archivo de inventario: {csv_file_path}")
    if not csv_file_path.exists():
        print(f"[!] Archivo {csv_file_path} no encontrado.")
        return

    # Leer CSV
    records = []
    with open(csv_file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)

    print(f"[+] Se encontraron {len(records)} registros para importar.")

    try:
        # Autenticación con Odoo
        common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
        uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASSWORD, {})
        if not uid:
            print("[!] Error de autenticación con Odoo.")
            return

        models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
        
        imported_count = 0
        for rec in records:
            device_id = models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                'telecom.device', 'create',
                [{
                    'name': rec['name'],
                    'serial_number': rec['serial_number'],
                    'mac_address': rec.get('mac_address', ''),
                    'device_type': rec.get('device_type', 'router'),
                    'ip_address': rec.get('ip_address', ''),
                    'status': rec.get('status', 'in_stock')
                }]
            )
            print(f"  ✓ Equipo '{rec['name']}' registrado con ID: {device_id}")
            imported_count += 1

        print(f"\n[OK] Importación finalizada exitosamente: {imported_count} equipos cargados en Odoo.")

    except ConnectionRefusedError:
        print("[!] No se pudo conectar al servidor de Odoo. Asegúrese de que el contenedor Docker esté corriendo:")
        print("    docker compose up -d")

if __name__ == "__main__":
    sample_csv = Path(__file__).resolve().parent.parent / "sample_data" / "equipos_telecom.csv"
    import_csv_to_odoo(sample_csv)
