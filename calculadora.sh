#!/bin/bash

echo "Instalando Python3 caso necessário"
sudo apt update
sudo apt install python3

echo "Iniciando Script calculadora.py"

python3 /home/bryan/modulo1/exercicio_sh_linux/calculadora.py

echo "Script Executado"
