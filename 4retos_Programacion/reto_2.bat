@echo off
title Batch II
set abc=qazxswedcvfrtgbnhyujmkiolp
set var=%abc:~14,1%%abc:~-25,1%%abc:~12,1%%abc:~8,1%%abc:~16,1%%abc:~8,1%%abc:~23,1%%abc:~7,1%
set var2=%var%%abc:~-2,1%%abc:~23,1%%abc:~13,1%
set var2=%var2:a=4%
set var3=%var2:o=0%

set /P clave="Ingrese la contraseña: "
if "%clave%"=="%var3%" (goto bien) else (goto mal)

:bien
cls
echo Felicitaciones!
echo Acceso concedido
echo Ingresa la respuesta '%clave%' en el reto Batch II
pause > nul
cls
goto exit

:mal
cls
echo Vas por el camino equivocado!
echo Acceso denegado
echo Intenta nuevamente
pause > nul
cls

:exit