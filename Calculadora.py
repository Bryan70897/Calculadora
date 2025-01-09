import sympy
import matplotlib.pyplot as plt # Plota o grafico
import numpy as np
from math import log # Biblioteca para calcular o logaritmo
import tkinter as tk # Biblioteca para a interface gráfica
from tkinter import messagebox 


# Classe base 
class Função:
    def executar(self):
        raise NotImplementedError("Função inexistente.")


class CalculadoraBasica(Função):
    def __init__(self, historico):
        self.historico = historico

    def executar(self): # Implementa a interface gráfica, sobrescrevendo o método da classe base (se repete a cada classe)
        self.window = tk.Toplevel()
        self.window.title("Calculadora Básica")
        self.window.geometry("300x250")

        tk.Label(self.window, text="Digite o primeiro valor:").pack(pady=5)
        self.valor1_entry = tk.Entry(self.window)
        self.valor1_entry.pack(pady=5)

        tk.Label(self.window, text="Digite o segundo valor:").pack(pady=5)
        self.valor2_entry = tk.Entry(self.window)
        self.valor2_entry.pack(pady=5)

        tk.Label(self.window, text="Escolha a operação:").pack(pady=5)
        self.operacao_var = tk.StringVar(value="Adição")
        opcoes = ["Adição", "Subtração", "Multiplicação", "Divisão"]
        tk.OptionMenu(self.window, self.operacao_var, *opcoes).pack(pady=5)

        tk.Button(self.window, text="Calcular", command=self.calcular).pack(pady=10)

    # Função que calcula as operações basicas
    def calcular(self):
        try:
            valor1 = float(self.valor1_entry.get())
            valor2 = float(self.valor2_entry.get())
            operacao = self.operacao_var.get()

            if operacao == "Adição":
                resultado = valor1 + valor2
            elif operacao == "Subtração":
                resultado = valor1 - valor2
            elif operacao == "Multiplicação":
                resultado = valor1 * valor2
            elif operacao == "Divisão":
                if valor2 != 0:
                    resultado = valor1 / valor2
                else:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
            else:
                raise ValueError("Operação inválida.")
            
            self.historico.adicionar(f"{valor1} {operacao} {valor2}", resultado)  # Adiciona ao histórico
            messagebox.showinfo("Resultado", f"{resultado:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "insira valores numéricos válidos.")
        except ZeroDivisionError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

class Conversor(Função): # Converte medidas
    def __init__(self, historico):
        self.historico = historico

    def executar(self):
        self.window = tk.Toplevel()
        self.window.title("Conversor de Unidades")
        self.window.geometry("300x200")

        tk.Label(self.window, text="Digite o valor a converter:").pack(pady=5)
        self.valor_entry = tk.Entry(self.window)
        self.valor_entry.pack(pady=5)

        tk.Label(self.window, text="Escolha a conversão:").pack(pady=5)
        self.conversao_var = tk.StringVar(value="km para m")
        opcoes = ["km para m", "m para km", "kg para g", "g para kg", "Celsius para Fahrenheit", "Fahrenheit para Celsius"]
        tk.OptionMenu(self.window, self.conversao_var, *opcoes).pack(pady=5)

        tk.Button(self.window, text="Converter", command=self.converter).pack(pady=10)
    # Função para converter as medidas
    def converter(self):
        try:
            valor = float(self.valor_entry.get())
            tipo = self.conversao_var.get()

            if tipo == "km para m":
                resultado = valor * 1000
            elif tipo == "m para km":
                resultado = valor / 1000
            elif tipo == "kg para g":
                resultado = valor * 1000
            elif tipo == "g para kg":
                resultado = valor / 1000
            elif tipo == "Celsius para Fahrenheit":
                resultado = (valor * 9/5) + 32
            elif tipo == "Fahrenheit para Celsius":
                resultado = (valor - 32) * 5/9
            else:
                raise ValueError("Conversão inválida.")
            
            self.historico.adicionar(f"{valor} para {tipo}", resultado)  # Adiciona ao histórico
            messagebox.showinfo("Resultado", f"{resultado:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "insira um valor numérico válido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao realizar conversão: {str(e)}")

class raizQuadrada(Função):
    def __init__(self, historico):
        self.historico = historico

    def executar(self): 
        self.window = tk.Toplevel()
        self.window.title("Cálculo de Raiz")
        self.window.geometry("300x200")

        tk.Label(self.window, text="Digite o Número que vai ser calculada a raiz:").pack(pady=5)
        self.numero_entry = tk.Entry(self.window)
        self.numero_entry.pack(pady=5)

        tk.Button(self.window, text="Calcular", command=self.calcular_raiz).pack(pady=10)
        # Função para calcular raiz quadrada
    def calcular_raiz(self):
        try:
            base = float(self.numero_entry.get())

            resultado =  base ** (1/2)
            
            self.historico.adicionar(f"Raiz Quadrada de {base}", resultado)  # Adiciona ao histórico
            messagebox.showinfo("Resultado", f"{resultado:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Insira um número válido")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular a raiz quadra: {str(e)}")        
   
class Exponencial(Função):
    def __init__(self, historico):
        self.historico = historico

    def executar(self):
        self.window = tk.Toplevel()
        self.window.title("Cálculo Exponencial")
        self.window.geometry("300x200")

        tk.Label(self.window, text="Digite o Número (Base):").pack(pady=5)
        self.numero_entry = tk.Entry(self.window)
        self.numero_entry.pack(pady=5)

        tk.Label(self.window, text="Digite o Expoente:").pack(pady=5)
        self.expoente_entry = tk.Entry(self.window)
        self.expoente_entry.pack(pady=5)

        tk.Button(self.window, text="Calcular", command=self.calcular_exponencial).pack(pady=10)
    # Função para realizar calculos exponenciais
    def calcular_exponencial(self):
        try:
            base = float(self.numero_entry.get())
            expoente = float(self.expoente_entry.get())

            resultado = base ** expoente
            
            self.historico.adicionar(f"{base} ^ {expoente}", resultado)  # Adiciona ao histórico
            messagebox.showinfo("Resultado", f"{resultado:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Insira valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular o expoente: {str(e)}")
            
class Logaritmo(Função):
    def __init__(self, historico):
        self.historico = historico

    def executar(self):
        self.window = tk.Toplevel()
        self.window.title("Cálculo de logaritmo")
        self.window.geometry("300x200")

        tk.Label(self.window, text="Digite o número: ").pack(pady=5)
        self.numero_entry = tk.Entry(self.window)
        self.numero_entry.pack(pady=5)

        tk.Label(self.window, text="Digite a base: ").pack(pady=5)
        self.base_entry = tk.Entry(self.window)
        self.base_entry.pack(pady=5)

        tk.Button(self.window, text="Calcular", command=self.calcular_logaritmo).pack(pady=10)  
        # Função para Calcular logaritmo
    def calcular_logaritmo(self):
        try:
            numero = float(self.numero_entry.get())
            base = self.base_entry.get()


            if base:
                base = float(base)
                resultado = log(numero, base)
            else:
                resultado = log(numero)  

            self.historico.adicionar(f"O Log de {numero} {base} ", resultado)  # Adiciona ao histórico
            messagebox.showinfo("Resultado", f"Logaritmo: {resultado:.5f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular logaritmo: {str(e)}")      

class DesenharFunção(Função):
    def __init__(self, historico):
        self.historico = historico

    def executar(self):
        self.window = tk.Toplevel()
        self.window.title("Desenhar Função")
        self.window.geometry("300x200")
       
        tk.Label(self.window, text="Digite a função (ex: x**2, sin(x), cos(x)):").pack(pady=5)
        self.funcao_entry = tk.Entry(self.window)
        self.funcao_entry.pack(pady=5)

        tk.Label(self.window, text="Intervalo de x (ex: -10,10):").pack(pady=5)
        self.intervalo_entry = tk.Entry(self.window)
        self.intervalo_entry.pack(pady=5)

        tk.Button(self.window, text="Desenhar", command=self.desenhar).pack(pady=10)
    # Função para desenhar as funções e plotar em um gráfico 
    def desenhar(self):
        try:
            funcao = self.funcao_entry.get()
            intervalo = self.intervalo_entry.get().split(',')
            x_min, x_max = float(intervalo[0]), float(intervalo[1])
            x = np.linspace(x_min, x_max, 500)
            y = eval(funcao, {"x": x, "np": np, "sin": np.sin, "cos": np.cos, "log": np.log, "exp": np.exp})

            plt.plot(x, y, label=f"y = {funcao}")
            plt.title("Gráfico da Função")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.legend()
            plt.grid(True)
            plt.show()

            self.historico.adicionar(f"Gráfico de {funcao} no intervalo [{x_min}, {x_max}]", "Registrada")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao desenhar função: {str(e)}")

class Historico(Função): # Armazena os calculos feitos na calculadora
    def __init__(self):
        self.registros = []  # Lista para armazenar o histórico

    def adicionar(self, operacao, resultado):
        # Formata e adiciona a operação ao histórico
        self.registros.append(f"{operacao} = {resultado}")

    def exibir(self):
        # Cria uma janela para mostrar o histórico
        window = tk.Toplevel()
        window.title("Histórico")
        window.geometry("300x400")
        
        tk.Label(window, text="Histórico de Operações", font=("Arial", 14)).pack(pady=10)
        
        # Exibe cada registro no histórico
        for registro in self.registros:
            tk.Label(window, text=registro).pack(anchor="w", padx=10)
        
        tk.Button(window, text="Fechar", command=window.destroy).pack(pady=10)
    
            

class Sair:
    def __init__(self, root):
        self.root = root
    def executar(self):
        self.root.destroy()  

# Menu principal 
class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora by:Bryan Smith")
        self.root.geometry("300x500")  # Define o tamanho da janela
        
        self.historico = Historico()
           
        label = tk.Label(root, text="----------MENU----------", font=("Arial", 16)) 
        label.pack(pady=10)
        # Mostra as opções
        self.opcoes = [
            ("Calculadora Básica", CalculadoraBasica(self.historico)),
            ("Conversor", Conversor(self.historico)),
            ("Exponencial", Exponencial(self.historico)),
            ("Logaritmo", Logaritmo(self.historico)),
            ("Desenhar Função", DesenharFunção(self.historico)),
            ("Raiz Quadrada", raizQuadrada(self.historico)),
            ("Historico", self.historico.exibir),
            ("Sair", Sair(root))
        ]

        #Criação dos botões
        for nome, funcao in self.opcoes: # lambda implementado para adaptar a chamada das funções ou de um objeto
            botao = tk.Button(root, text=nome, command=(lambda f=funcao: f() if callable(f) else f.executar()))
            botao.pack(pady=5)

# Inicializa o programa e exibe o menu principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrincipal(root)
    root.mainloop()