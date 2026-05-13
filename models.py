from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# =========================
# TABLA MEDICOS
# =========================
class Medico(db.Model):
    __tablename__ = 'medicos'

    id_medico = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), nullable=False)

    consultas = db.relationship('Consulta', backref='medico', lazy=True)

# =========================
# TABLA PACIENTES
# =========================
class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id_paciente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    consultas = db.relationship('Consulta', backref='paciente', lazy=True)

# =========================
# TABLA CONSULTAS
# =========================
class Consulta(db.Model):
    __tablename__ = 'consultas'

    id_consulta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(20), nullable=False)
    diagnostico = db.Column(db.String(200), nullable=False)
    tratamiento = db.Column(db.String(200), nullable=False)

    id_medico = db.Column(
        db.Integer,
        db.ForeignKey('medicos.id_medico'),
        nullable=False
    )

    id_paciente = db.Column(
        db.Integer,
        db.ForeignKey('pacientes.id_paciente'),
        nullable=False
    )