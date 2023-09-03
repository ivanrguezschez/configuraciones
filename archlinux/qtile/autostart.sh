#!/bin/sh

# Configuracion Teclado Español
setxkbmap es &

#
# Iconos del Sistema
#

# Pendrive
udiskie -t &

# Red & Wifi
nm-applet &

# Volumen
#volumeicon &

# Bateria Portatil
cbatticon -u 5 &

# Fondo de Pantalla
nitrogen --restore &

