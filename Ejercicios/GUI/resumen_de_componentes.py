import PySimpleGUI as psg


layout = [
    [psg.Text('Texto Fijo y Campo para Ingreso de Texto -->'), psg.Input()],
    [psg.Checkbox('Checkbox 1'), psg.Checkbox('Checkbox 2', default=True),
        psg.Radio('Radio 1', 1), psg.Radio('Radio 2', 1, default=True)],
    [psg.Multiline('Ingreso de Texto\nen múltiples líneas', autoscroll=True)],
    [psg.Listbox(['Listbox con materias', 'AED', 'PPR', 'GDA'], size=(35, 4))],
    [psg.Combo(['AED', 'PPR', 'GDA'], default_value='Combobox con materias...', size=(35, 4))],
    [psg.Text('Selector vertical... --> '), psg.Slider((50, 10), default_value=25)],
    [psg.Text('Selector horizontal... --> '), psg.Slider((50, 10), orientation='horizontal', default_value=25)],
    [psg.Spin(['AED', 'PPR', 'GDA'], initial_value='Spinbox con materias', size=(35, 4))],
    [psg.Text('Despliegue de imagen -->'), psg.Image('image.PNG'), psg.ColorChooserButton('Colores...')],
    [psg.FileBrowse('Seleccione UN archivo...'), psg.FilesBrowse('Seleccione VARIOS Archivos...')],
    [psg.InputText('Fecha --> ', disabled=True), psg.CalendarButton('Fecha...'), psg.Button('Enviar'),
        psg.OK(), psg.Cancel()],
]


def run():
    window = psg.Window('Resumen de componentes', layout)
    event, values = window.read()
    window.close()


if __name__ == '__main__':
    run()
