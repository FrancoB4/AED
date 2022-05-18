import PySimpleGUI as psg


def run():
    psg.Popup('Hola mundo! Ahora en una ventana',
              text_color='green',
              background_color='black',
              button_color=('black', 'gray')
              )


if __name__ == '__main__':
    run()
