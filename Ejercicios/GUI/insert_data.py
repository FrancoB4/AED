import PySimpleGUI as psg


def run():
    nombre = psg.popup_get_text('Ingrese su nombre:')
    fecha = psg.popup_get_date()
    psg.Popup(f'Hola {nombre}, hoy es {fecha[0]}/{fecha[1]}/{fecha[2]}')


if __name__ == '__main__':
    run()
