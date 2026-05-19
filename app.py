#ASIGNATURA: TECNOLOGIAS EMERGENTES II
#NOMBRE: ROSMERY ARUNI PAYE
from flask import Flask, render_template, request, redirect, url_for
from models import db, Medico, Paciente, Consulta

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/medicos')
def listar_medicos():
    medicos = Medico.query.all()
    return render_template('medicos/listar.html', medicos=medicos)

@app.route('/medicos/agregar', methods=['GET', 'POST'])
def agregar_medico():
    if request.method == 'POST':
        nuevo = Medico(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad'],
            telefono=request.form['telefono'],
            correo=request.form['correo']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('listar_medicos'))

    return render_template('medicos/agregar.html')

@app.route('/medicos/editar/<int:id>', methods=['GET', 'POST'])
def editar_medico(id):
    medico = Medico.query.get_or_404(id)

    if request.method == 'POST':
        medico.nombre = request.form['nombre']
        medico.especialidad = request.form['especialidad']
        medico.telefono = request.form['telefono']
        medico.correo = request.form['correo']

        db.session.commit()
        return redirect(url_for('listar_medicos'))

    return render_template('medicos/editar.html', medico=medico)

@app.route('/medicos/eliminar/<int:id>')
def eliminar_medico(id):
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    return redirect(url_for('listar_medicos'))

@app.route('/pacientes')
def listar_pacientes():
    pacientes = Paciente.query.all()
    return render_template('pacientes/listar.html', pacientes=pacientes)

@app.route('/pacientes/agregar', methods=['GET', 'POST'])
def agregar_paciente():
    if request.method == 'POST':
        nuevo = Paciente(
            nombre=request.form['nombre'],
            edad=request.form['edad'],
            direccion=request.form['direccion'],
            telefono=request.form['telefono']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('listar_pacientes'))

    return render_template('pacientes/agregar.html')

@app.route('/pacientes/editar/<int:id>', methods=['GET', 'POST'])
def editar_paciente(id):
    paciente = Paciente.query.get_or_404(id)

    if request.method == 'POST':
        paciente.nombre = request.form['nombre']
        paciente.edad = request.form['edad']
        paciente.direccion = request.form['direccion']
        paciente.telefono = request.form['telefono']

        db.session.commit()
        return redirect(url_for('listar_pacientes'))

    return render_template('pacientes/editar.html', paciente=paciente)

@app.route('/pacientes/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    
    if request.method == 'POST':

        if paciente.consultas:
            return redirect(url_for('listar_pacientes'))
        
        db.session.delete(paciente)
        db.session.commit()
        return redirect(url_for('listar_pacientes'))
        
    return render_template('pacientes/eliminar.html', paciente=paciente)

@app.route('/pacientes/historial/<int:id>')
def historial_paciente(id):

    paciente = Paciente.query.get_or_404(id)
    consultas = paciente.consultas
    return render_template('pacientes/historial.html', paciente=paciente, consultas=consultas)

@app.route('/consultas', methods=['GET', 'POST'])
def listar_consultas():
    if request.method == 'POST':
        fecha = request.form.get('fecha')
        if fecha:
            consultas = Consulta.query.filter_by(fecha=fecha).all()
        else:
            consultas = Consulta.query.all()
    else:
        consultas = Consulta.query.all()
        
    return render_template('consultas/listar.html', consultas=consultas)

@app.route('/consultas/agregar', methods=['GET', 'POST'])
def agregar_consulta():
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == 'POST':
        nueva = Consulta(
            fecha=request.form['fecha'],
            diagnostico=request.form['diagnostico'],
            tratamiento=request.form['tratamiento'],  
            id_medico=request.form['id_medico'],
            id_paciente=request.form['id_paciente']
        )
        db.session.add(nueva)
        db.session.commit()
        return redirect(url_for('listar_consultas'))

    return render_template('consultas/agregar.html', medicos=medicos, pacientes=pacientes)

@app.route('/consultas/editar/<int:id>', methods=['GET', 'POST'])
def editar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == 'POST':
        consulta.fecha = request.form['fecha']
        consulta.diagnostico = request.form['diagnostico']
        consulta.tratamiento = request.form['tratamiento']
        consulta.id_medico = request.form['id_medico']
        consulta.id_paciente = request.form['id_paciente']

        db.session.commit()
        return redirect(url_for('listar_consultas'))

    return render_template('consultas/editar.html', consulta=consulta, medicos=medicos, pacientes=pacientes)

@app.route('/consultas/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    db.session.delete(consulta)
    db.session.commit()
    return redirect(url_for('listar_consultas'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)