from cefpython3 import cefpython as cef

# Configuração do CEF Python
cef.Initialize()

# Classe para manipulação de eventos do navegador
class BrowserHandler(object):
    def OnLoadEnd(self, browser, **_):
        # Executa um script JavaScript após o carregamento da página
        browser.ExecuteJavascript("alert('A página foi carregada com sucesso!');")
    
    def OnBeforeClose(self, browser, **_):
        # Ao fechar a janela, encerra o loop de eventos
        cef.QuitMessageLoop()

# Criando a janela do navegador e definindo o manipulador de eventos
window_info = cef.WindowInfo()
window_info.SetAsChild(0, [0, 0, 800, 600])  # Defina as dimensões da janela aqui
browser = cef.CreateBrowserSync(window_info, url="http://127.0.0.1:5500/relatorio.html", window_title="Exemplo CEF Python")
handler = BrowserHandler()
browser.SetClientHandler(handler)

# Loop de eventos do CEF Python
cef.MessageLoop()

# Finalização do CEF Python
cef.Shutdown()




def main():
    cef.Initialize()
    cef.Shutdown()

if __name__ == '__main__':
    main()
