import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Tema
        sg.theme('DarkAmber')
        # Layout
        layout = [
            [sg.Text('Valor do Produto', size=(15,0)), sg.Input(size=(15,0),do_not_clear=False,key='vprod')],
            [sg.Text('Informe o PST', size=(15,0)), sg.Input(size=(15,0),key='pst')],
            [sg.Button('Gerar Chave', size=(30,1))],
            [sg.Output(size=(32,5))]
        ]
        # Janela
        self.janela = sg.Window('ICMS Key_Generator').layout(layout)

    
    def iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.read()
            vprod = float(self.values['vprod'])
            pst = float(self.values['pst'])
            psts = (pst/10)
            vBCSTRet = 38.85
            icms = (vprod/100*psts)
            icmsret = (icms/2) * 3

            print('<vBCSTRet>{}</vBCSTRet><pST>{:.3f}</pST><vICMSSubstituto>{:.2f}</vICMSSubstituto><vICMSSTRet>{:.2f}</vICMSSTRet>'
            .format(vBCSTRet, pst, icms, icmsret))
            

tela = TelaPython()
tela.iniciar()