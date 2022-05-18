import PySimpleGUI as psg

layout = [
    # Para cada fila del layout utilizamos una lista distinta, en este caso las primeras dos filas solo tienen un
    # elemento
    [psg.Text('ingrese su nombre')],
    [psg.Input()],
    # Como La tercera fila (layout[2]) tiene dos elementos, los incluimos a ambos dentro de la lista
    [psg.Ok(), psg.Cancel()]
]


def run():
    # Instanciamos la clase Window que representa a la ventana (creamos el objeto window)
    window = psg.Window('Ejemplo de control de layout', layout)

    # Para poder visualizar la ventana debemos utilizar el método Window.read() que devuelve dos valores
    # devolverá los eventos ocurridos (interacciones del usuario con la interfaz) y los datos asignados a las variables.
    event, values = window.read()

    # Por último cerramos la ventana
    window.close()

    psg.Popup(event, values)


if __name__ == '__main__':
    run()
