import sys
from cefpython3 import cefpython as cef

html_code = '''
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        input {
            margin-bottom: 10px;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        output {
            font-size: 24px;
        }
    </style>
</head>
<body>
    <h2>Soma de Dois Numeros</h2>
    <input type="number" id="num1" placeholder="Digite o primeiro numero"><br>
    <input type="number" id="num2" placeholder="Digite o segundo numero"><br>
    <button onclick="sumNumbers()">Somar</button><br>
    <output id="result"></output>

    <script>
        function sumNumbers() {
            var num1 = parseFloat(document.getElementById('num1').value);
            var num2 = parseFloat(document.getElementById('num2').value);
            var result = num1 + num2;
            document.getElementById('result').textContent = result;
        }
    </script>
</body>
</html>
'''

class SimpleBrowser:
    def __init__(self):
        self.browser = None

    def create_browser(self):
        sys.excepthook = cef.ExceptHook
        cef.Initialize()

        window_info = cef.WindowInfo()
        window_info.SetAsChild(0, [0, 0, 600, 400])

        self.browser = cef.CreateBrowserSync(url='data:text/html,' + html_code, window_title="CEFPython Example")
        self.browser.SetClientHandler(FocusHandler())

        cef.MessageLoop()
        cef.Shutdown()

class FocusHandler:
    def OnSetFocus(self, **_):
        return False

def main():
    browser = SimpleBrowser()
    browser.create_browser()

if __name__ == '__main__':
    main()
