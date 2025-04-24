@echo off
title Batch I
set /P cont="Ingresa la contraseña: "

if %cont%=="coding for fun" (goto bien) else (goto mal)

:bien
cls
echo Felicitaciones!
echo Acceso concedido
echo Ingresa la respuesta '%cont%' en el reto Batch I
pause > nul
cls
exit

:mal
cls
echo Vas por el camino equivocado!
echo Acceso denegado
echo Intenta nuevamente
pause > nul
cls

:exit