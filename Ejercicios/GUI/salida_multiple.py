import PySimpleGUI as psg


def run():
    nombre = psg.popup_get_text('Ingrese su nombre:')
    edad = int(psg.popup_get_text('Ingrese su edad:'))
    direccion = psg.popup_get_text('Ingrese su dirección:')

    psg.Popup('Bienvenido...', f'Nombre: {nombre}', f'Edad: {edad}', f'Dirección: {direccion}', title='Datos')
    psg.popup_scrolled('Bienvenido...', f'Nombre: {nombre}', f'Edad: {edad}', f'Dirección: {direccion}', title='Datos')


if __name__ == '__main__':
    run()
