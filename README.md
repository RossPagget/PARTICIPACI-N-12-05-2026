# Sistema de Gestión de Clínica Médica

Proyecto desarrollado con Flask y SQLAlchemy utilizando arquitectura MVC.

## Descripción

La aplicación permite administrar:

- Médicos
- Pacientes
- Consultas médicas

El sistema implementa operaciones CRUD completas y relaciones entre tablas.

---

# Tecnologías Utilizadas

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML
- CSS

---

# Arquitectura MVC

## Modelo (Model)

Archivo:

```python
models.py
```

Contiene las tablas y relaciones de la base de datos.

---

## Vista (View)

Carpeta:

```txt
templates/
```

Contiene las páginas HTML del sistema.

---

## Controlador (Controller)

Archivo:

```python
app.py
```

Controla las rutas y lógica de la aplicación.

---

# Funcionalidades

✅ Registrar médicos  
✅ Registrar pacientes  
✅ Registrar consultas  
✅ Editar registros  
✅ Eliminar registros  
✅ Visualizar relaciones entre tablas  
✅ Validar campos obligatorios  

---

# Extra Implementado

✅ Filtro de consultas por fecha

---

# Estructura del Proyecto

```txt
Clinica_Medica/
│
├── app.py
├── models.py
├── requirements.txt
│
├── templates/
│   ├── medicos/
│   ├── pacientes/
│   └── consultas/
│
└── static/
```

---

# Instalación

## Crear entorno virtual

```bash
python -m venv venv
```

## Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

---

# Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecutar el proyecto

```bash
python app.py
```

Abrir navegador:

```txt
http://127.0.0.1:5000
```

---

# Base de Datos

La base de datos SQLite se genera automáticamente:

```txt
clinic.db
```

---

# Autor


Proyecto desarrollado para la materia TEM-742.