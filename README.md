
# Proyecto Final "*Algoritmia y Programaciòn*"


## Integrantes:

### Leibman Andrade Cancio, (Estudiante de Ingenieria Industrial)
Es una persona con muy buena actitud y abierta al aprendizaje continuo, siempre buscando mejorar, adquir nuevos conocimientos y adaptarse a los cambios. Es muy disciplinado y entiende la importancia de la constancia y la organizacion para alcanzar sus metas. Le gusta relacionarse con las personas, establecer vinculos positivos y crear ambientes de trabajo colaborativo. Actualmente estoy cursando el sexto semestre y soy de la seccional de Urabà.

### Jhoiner Andres Rodriguez, (Estudiante de Ingenieria Industrial)
Soy una persona proactiva que siempre busca a mejorar en todos los aspectos, tengo la habilidad de adaptarme a los cambios y sacar lo mejor de cada uno de ellos, me gusta analizar problemas y encontrar soluciones, tambien me gusta trabajar de manera efectiva en equipo.

### Wilber Manco Rodríguez (Estudiante de Ingeniería Industrial)
Se considera una persona con un constante aprendizaje, quien se destaca por tener una mente positiva, buscando soluciones a los problemas de manera calmada y con coherencia, y el cual busca ser una persona ejemplar y cumplir todas sus metas.

## Nombre del proyecto: EasyParking "¡Rapido, sencillo y a tu medida!"
### El proyecto consiste en el desarrollo de un software de consola en Python para gestionar el parqueadero de la *Universidad de Antioquia*, *permitiendo solo el ingreso de automoviles* "no motos". El software tiene funcionales para:
* Registrar usuarios (con validacion estrictas de datos).
* Ingresar y retirar vehiculos (resgistrando horas y generando cobros segun el tiempo del parqueo).
* Administrar reportes detallados (vehiculos ingresados, retirados, pagos, promedios, etc.).
* Exportar los resultados de las operaciones a un archivo CSV.
* Mantener un log de eventos detallado (registro de acciones con tiempos de ejecucion y metadatos del sistema).
* Incluir un modo de acceso especial para administradores mediante usuarios y contraseña.

### El Objetivo de este proyecto es ofrecer un sistema robusto, eficiente y amigable que facilite la adminictracion diaria del parqueadero, elimine la gestion manual en papel, mejore el control del flujo vehicular y permita una facil auditoria administrativa.

## Logo del Proyecto 

<img width="280" height="220" src="https://i.postimg.cc/Qt3MNscL/Logo-Easyparking.jpg"> 


  ## Licencia del software
EasyParking "¡Rápido, sencillo ya tu medida!"está licenciada bajo CC BY-ND 4.0© 2 por Leibman Andrade Cancio, Jhoiner Rodríguez, Wilber Rodríguez 

## Reporte de visión
Este proyecto consiste en el desarrollo de una aplicación web que permite a estudiantes y personal universitario gestionar sus actividades en la universidad de forma eficiente. El parqueadero presta servicio exclusivamente a vehículos automóviles y dispone de 64 espacios de parqueo. Actualmente, el registro de usuarios y cobros se realiza de forma manual, lo que genera ineficiencias y falta de documentación formal en las transacciones.

### Objetivos
- Automatizar el registro de usuarios que ingresan y retiran vehículos del parqueadero.
- Facilitar la generación de cobros, facturas y reportes administrativos.
- Reducir errores y tiempos de atención al usuario mediante un sistema digital.

### Beneficios
- Mejora en la eficiencia y organización del parqueadero mediante la digitalización del proceso.
- Eliminación del uso de papel y sellos para el registro de usuarios.
- Facilita el trabajo del personal encargado, permitiendo un servicio más rápido y preciso.
- Asegura un control más riguroso de las entradas, salidas y cobros realizados.
- Provee documentación formal y confiable de las transacciones realizadas.

El sistema será desarrollado en grupos de tres integrantes, gestionado por el líder del equipo.

## Especificación de Requisitos

### Requisitos funcionales
- El sistema debe permitir registrar la entrada de un vehículo, capturando la placa, fecha y hora de llegada.
- El sistema debe permitir registrar la salida de un vehículo y calcular automáticamente el valor a pagar basado en el tiempo de permanencia.
- El sistema debe generar un recibo con los detalles de la transacción (placa, tiempo de permanencia, monto a pagar).
- El sistema debe permitir consultar los vehículos actualmente dentro del parqueadero.
- El sistema debe generar un reporte diario con el resumen de ingresos, vehículos atendidos y espacios disponibles.

### Requisitos no funcionales
- El sistema debe estar desarrollado como una aplicación de consola en Python.
- La interfaz debe ser clara y fácil de usar para los empleados del parqueadero.
- El sistema debe ser capaz de procesar el registro de entrada o salida de un vehículo en menos de 5 segundos.
- Los reportes exportados deben ser compatibles con programas de hoja de cálculo como Microsoft Excel o Google Sheets.
- El sistema debe evitar pérdidas de información en caso de cierre inesperado.
- La aplicación debe funcionar correctamente en sistemas operativos Windows, macOS y Linux.

### Plan de proyecto
![WhatsApp Image 2025-05-02 at 7 55 23 AM](https://github.com/user-attachments/assets/2bbac9f8-5c74-4231-ad9d-18d0abff1713)

## Objetivos y Propositos
### ¿Cual es el objetivo principal de esta aplicacion?
Desarrollar un *programa de consola en Python* para gestionar un parqueadero universitario que permita lo siguiente:
- Registrar usuarios y vehiculos.
- Gestionar ingresos y salidas.
- calcular cobros.
- Generar reportes administrativos.
- Exportar datos a archivos CSV.

### ¿Que problemas especificos estamos tratando de resolver con esta aplicacion?
La administracion manual e ineficiente del parqueadero "registro en papel, sin facturacion ni reportes"
La app automatiza el proceso, mejora la trazabilidad y elimina errores humanos.

### ¿Quienes son los usuarios finales y que necesidades especificas tienen?
- Usuarios del parqueadero (conductores de carros): necesitan ingresar y retirar vehiculos de forma rapida y recibir comprobantes.
- Personal administrativo: necesitan reportes y control eficiente de usuarios, cobros, tiempos y disponibilidad.

## Funcionalidades y Requisitos
### ¿Puedes detallar las funcionalidades clave que debe tener la aplicacion?
- Registro de usuarios con validaciones estrictas.
- Registro de vehiculo vinculado al usuario.
- Ingreso de vehiculos (solo si el usuario esta registrado).
- Registro de vehiculos con calculo de cobros por hora y fracciòn.
- Generacion de recibos o factura en consola.
- Acceso restringido a administrador con reportes;
    - Total de vehiculos registrados, retirados y activos.
    - Total de pagos.
    - Tiempo promedio de permanencia.
    - Vehiculo con tiempo maximo y minimo de parqueo.
- Exportaciòn de reportes a CSV.
- Registro de logs detallados de todas las operaciones.
 
### ¿Hay alguna funcionalidad opcional o deseada que no sea esencial?
El diseño visualmente amigable en consola puede ser mejorado pero no es esencial. Tambien, incluir graficos en los reportes podria ser deseable, pero no obligatorio.

## Prioridades y Alcance
### ¿Cuales son las caracteristicas mas criticas que debe tener la aplicaciòn en su primera versiòn?
- Registro de usuario y validacion.
- Registro de vehiculo y control de entrada o salida.
- Calculo de cobros con reglas claras.
- Generaciòn de recibos.
- Reportes basicos de administraciòn.
 
### ¿Como preorizamos las diferentes caracteristicas y funcionalidades?
Preoridad alta: Flujo completo de ingreso y retiro con cobro.
Prioridad media: Funcionalidades administrativas.
Prioridad baja: aspectos visuales, funcionalidades avanzadas no solicitadas por ejemoplo, interfaz grafica.

### ¿Existe un roadmap o plan de desarrollo a largo plazo para la aplicaciòn?
Si, el documento lo dividimos en dos entregas:
- Primera entrega (semana 8): se entro del punto 1 al 7, incluyendo requisitos y plan de proyecto.
- Segunda entrega (semana 16): Sofware conpleto completo con codigo, documentaciòn, manual, repositorio GitHub y la sustentacion.
    
