# PUMAVISION
Plataforma web centralizada para la gestión de videovigilancia y denuncias institucionales, desarrollada por la consultora NITRA tech. Su objetivo principal es digitalizar el flujo de trabajo entre el departamento de Soporte Técnico y el área Jurídica, permitiendo el registro de usuarios, autenticación segura y la gestión de evidencias sin depender de dispositivos físicos de almacenamiento (USB).

---
## Tecnologías utilizadas
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla).
* **Backend y Base de Datos (BaaS):** Supabase (Manejo de autenticación y persistencia de usuarios).
* **Gestión de Estado:** `localStorage` (API nativa del navegador para persistencia de sesión).
* **Testing Automatizado (QA):** Python 3, Selenium WebDriver, Pytest.
* **Control de Versiones y Despliegue:** Git, GitHub, GitHub Pages.

---
## Instalación
Para descargar y configurar el entorno de pruebas automatizadas del proyecto localmente, sigue estos pasos:

### 1. Clonar el repositorio
Abre tu terminal y ejecuta:
`git clone https://github.com/rom0612/SistemaDeCamaras.git`

### 2. Crear y activar el entorno virtual de Python
Navega a la carpeta del proyecto y crea el entorno:
* En Windows: `python -m venv .venv` y luego actívalo con `.venv\Scripts\activate`
* En Mac/Linux: `python3 -m venv .venv` y actívalo con `source .venv/bin/activate`

### 3. Instalar las librerías necesarias
Con el entorno activado, instala Selenium y Pytest:
`pip install selenium pytest`

---
## Ejecutar sistema
El sistema principal se encuentra desplegado y accesible en línea a través de GitHub Pages:
**🔗 URL de Producción:** [https://rom0612.github.io/SistemaDeCamaras/](https://rom0612.github.io/SistemaDeCamaras/)

Para **ejecutar las pruebas automatizadas localmente**, asegúrate de tener activado el entorno virtual y utiliza los siguientes comandos en tu terminal:
* Para los scripts individuales: `python nombre_del_script.py` (ej. `python ejemplo_2_ingreso_correcto.py`)
* Para ejecutar la suite completa de pruebas: `pytest pumavision_test.py`

---
## Uso del sistema
1. **Acceso:** Al ingresar a la plataforma, el usuario visualizará la pantalla de Login. Debe ingresar su correo y contraseña registrados.
2. **Registro:** Si no cuenta con credenciales, debe hacer clic en "Registrar nuevo usuario", lo cual lo redirigirá al formulario conectado con Supabase.
3. **Persistencia:** Al iniciar sesión con éxito, el sistema validará los datos y redirigirá a `principal.html`, guardando la sesión activa mediante `localStorage`.
4. **Cerrar sesión:** En la vista principal, el usuario puede terminar su sesión de forma segura, limpiando la memoria del navegador.

---
## Funcionalidades principales
* Módulo de Inicio de Sesión seguro.
* Módulo de Registro de Usuarios.
* Conexión en tiempo real con Supabase para validación de credenciales.
* Persistencia básica de sesión simulada hacia el Dashboard (`principal.html`).
* Suite de pruebas QA automatizadas (validación de carga, login exitoso/fallido y navegación).

---
## Evidencias
Todas las capturas de pantalla generadas automáticamente por los scripts de Selenium durante las pruebas (éxitos, fallos de aserción y renderizado de vistas) se almacenan localmente en la carpeta raíz dentro del directorio llamado **`evidencias/`**. El sistema está programado mediante la librería `os` para crear esta carpeta automáticamente si no existe.

---
## Estructura del proyecto
La organización principal de los archivos y directorios del repositorio es la siguiente:

```text
SistemaDeCamaras/
│
├── css/
│   └── style.css
├── JS/
│   ├── script.js
│   └── supabase.js
├── pages/
│   └── registro.html
├── evidencias/                  # Generada automáticamente por las pruebas
│   ├── login_exitoso.png
│   ├── pytest_vista_registro.png
│   └── ...
├── .venv/                       # Entorno virtual de Python (Oculto/Ignorado)
├── index.html                   # Vista principal (Login)
├── principal.html               # Dashboard / Home simulado
├── ejemplo_1_carga.py           # Script QA individual
├── ejemplo_2_ingreso_correcto.py # Script QA individual
├── pumavision_test.py           # Suite principal estructurada en Pytest
└── README.md                    # Documentación técnica