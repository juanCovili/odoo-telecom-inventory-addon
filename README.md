# 🌐 Odoo Telecom & Network Inventory Addon
> **Módulo Personalizado de Odoo 17 y Entorno Docker para Gestión de Equipamiento de Redes, Fibra Óptica y Enlaces.**

[![Odoo](https://img.shields.io/badge/Odoo-17.0%20Community-purple?logo=odoo)](https://odoo.com)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue?logo=python)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL%2015-336791?logo=postgresql)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Deployment-Docker%20Compose-2496ED?logo=docker)](https://docker.com)
[![Author](https://img.shields.io/badge/Author-Juan%20Covili-red)](https://juancovili.com)

---

## 📋 Descripción del Proyecto

Este repositorio implementa una solución lista para producción que combina:
1. **Entorno Contenerizado con Docker Compose:** Levanta Odoo 17 Community junto con PostgreSQL 15 en un solo comando para pruebas, staging o despliegue local.
2. **Módulo Personalizado (`telecom_inventory`):** Extiende el ERP para llevar el control, trazabilidad, números de serie y estados operativos de equipos de telecomunicaciones (ONUs GPON, routers, antenas punto a punto, switches y cámaras IP).
3. **Script de Ingesta Automatizada (`scripts/import_inventory.py`):** Demuestra integración vía API XML-RPC de Odoo para importar catálogos de hardware masivamente desde planillas Excel / CSV.

---

## 🏛️ Estructura del Repositorio

```text
odoo-telecom-inventory-addon/
├── addons/
│   └── telecom_inventory/               # Módulo personalizado de Odoo
│       ├── __init__.py
│       ├── __manifest__.py              # Metadatos y dependencias
│       ├── models/
│       │   ├── __init__.py
│       │   └── telecom_device.py        # Modelo ORM (Python) de equipos y ciclo de vida
│       ├── views/
│       │   └── telecom_device_views.xml # Vistas Tree, Form, Botones de acción y Menús
│       └── security/
│           └── ir.model.access.csv      # Permisos y control de acceso (ACL)
├── config/
│   └── odoo.conf                        # Configuración de servidor Odoo y base de datos
├── sample_data/
│   └── equipos_telecom.csv              # Datos de ejemplo para importación
├── scripts/
│   └── import_inventory.py              # Script Python para carga masiva vía XML-RPC
├── docker-compose.yml                   # Orquestación de servicios Odoo + PostgreSQL
└── README.md                            # Documentación técnica
```

---

## 🚀 Inicio Rápido (Despliegue Local con Docker)

### 1. Clonar el repositorio
```bash
git clone https://github.com/juanCovili/odoo-telecom-inventory-addon.git
cd odoo-telecom-inventory-addon
```

### 2. Levantar el entorno
```bash
docker compose up -d
```
El servicio estará disponible de inmediato en tu navegador en:  
👉 **`http://localhost:8069`**

### 3. Activar el Módulo
1. Inicia sesión en Odoo con las credenciales de administrador.
2. Activa el **Modo Desarrollador** en Ajustes.
3. Ve a **Aplicaciones**, presiona **Actualizar lista de aplicaciones**, busca `telecom_inventory` y haz clic en **Activar**.

---

## ⚙️ Características Técnicas del Módulo

- **Modelo de Datos (`telecom.device`):**
  - Número de Serie único (`serial_number`) con constraint a nivel de base de datos (`_sql_constraints`).
  - Dirección MAC (`mac_address`) y dirección IP asignada (`ip_address`).
  - Clasificación por tipo de hardware: *ONU Fibra*, *Router WiFi*, *Switch Gigabit*, *Antena Punto a Punto*, *CCTV IP*.
  - Ciclo de vida operativo con badges dinámicos: *En Bodega*, *Asignado a Cuadrilla*, *Instalado en Cliente*, *En Taller*, *Baja Técnica*.
- **Vistas y Experiencia de Usuario:**
  - Vista lista (Tree) con colores condicionales según el estado.
  - Vista formulario (Form) con chatter integrado (`mail.thread`) para historial de auditoría y notas de soporte en terreno.
  - Botones de acción rápida: *"Marcar como Instalado"* y *"Devolver a Bodega"*.

---

## 👨‍💻 Autor

**Juan Covili**  
*Ingeniero en Informática y Analista Programador (INACAP Sede Los Ángeles)*  
🌐 Portafolio: [juancovili.com](https://juancovili.com)  
💼 LinkedIn: [linkedin.com/in/juan-covili-02b2a114b](https://www.linkedin.com/in/juan-covili-02b2a114b)

---

## Autor y Copyright

**Juan Covili** — Copyright (c) 2026 Juan Covili  
- **GitHub:** [github.com/juanCovili/odoo-telecom-inventory-addon](https://github.com/juanCovili/odoo-telecom-inventory-addon)  
- **Portafolio:** [juancovili.com](https://juancovili.com)  
- **Licencia:** Ver [`LICENSE`](./LICENSE) (disponible para evaluación técnica y revisión de portafolio con atribución obligatoria a Juan Covili; prohibido eliminar marcas de autoría o reclamar autoría).
