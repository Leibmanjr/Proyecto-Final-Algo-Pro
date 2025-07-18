
# Proyecto Final "*Algoritmia y Programaciòn*"


## Integrantes:

### Leibman Andrade Cancio, (Estudiante de Ingenieria Industrial)
Es una persona con muy buena actitud y abierta al aprendizaje continuo, siempre buscando mejorar, adquir nuevos conocimientos y adaptarse a los cambios. Es muy disciplinado y entiende la importancia de la constancia y la organizacion para alcanzar sus metas. Le gusta relacionarse con las personas, establecer vinculos positivos y crear ambientes de trabajo colaborativo. Actualmente estoy cursando el sexto semestre y soy de la seccional de Urabà.

### Jhoiner Andres Rodriguez, (Estudiante de Ingenieria Industrial)
Soy una persona proactiva que siempre busca a mejorar en todos los aspectos, tengo la habilidad de adaptarme a los cambios y sacar lo mejor de cada uno de ellos, me gusta analizar problemas y encontrar soluciones, tambien me gusta trabajar de manera efectiva en equipo.

### Wilber Manco Rodríguez (Estudiante de Ingeniería Industrial)
Perteneciente a la seccional Occidente en Santa Fe de Antioquia, actualmente está cursando el 3er semestre de Ingeniería Industrial. Se considera una persona con un constante aprendizaje, quien se destaca por tener una mente positiva, buscando soluciones a los problemas de manera calmada y con coherencia, y el cual busca ser una persona ejemplar y cumplir todas sus metas.

## Nombre del proyecto: EasyParking "¡Rapido, sencillo y  a tu medida!"
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
Se digitalizará el proceso completo de registro, ingreso, salida y cobro de vehículos, permitiendo mayor control, trazabilidad y organización.
- Los reportes administrativos podrán exportarse en formato .CSV
- Solo los usuarios registrados podrán registrar vehículos y hacer uso del parqueadero.
- La aplicación será ejecutada localmente en consola, y el acceso se realizará mediante inicio de sesión con credenciales validadas.
- Los superusuarios contarán con un menú especial con opciones administrativas y generación de reportes.
- Usuarios generales: Registran su vehículo, ingresan o retiran el mismo, y visualizan su recibo.
- Superusuarios: Gestionan reportes, acceden al historial del sistema y exportan los datos.

El equipo de desarrollo está compuesto por tres integrantes. El líder del equipo es Jhoiner Andrés Rodriguéz, quien se encarga de la coordinación de tareas, control de versiones y comunicación general.

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
![Diagrama de grant](https://github.com/user-attachments/assets/ecf23210-4765-4dcd-8114-c5ff0fdbe886)

## ¿Qué tecnologías se usan para este proyecto?
### Este proyecto está construido con:
- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS

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
    
## Limitaciones y restricciones
### ¿Hay limitaciones tecnológicas que debamos considerar?
Se han identificado limitaciones como que el sistema se desarrolla en tecnologías básicas como Python, cosa que no deja ir más allá que a un sistema complejo.
La aplicación está diseñada para ejecutarse en entorno de consola, lo que limita la experiencia visual y la interacción con el usuario.

### ¿Existen restricciones de presupuesto o tiempo para el desarrollo?
Sí, el desarrollo se realizará dentro del tiempo académico asignado, con dos entregas clave (semana 8 y semana 16).
No se cuenta con un presupuesto económico. Todo el desarrollo se basa en herramientas y recursos gratuitos.
El equipo está conformado por estudiantes con tiempo limitado fuera del horario de clases.

### ¿Hay normativas de cumplimiento o seguridad que debemos seguir?
Como se trata de un proyecto académico, no se requiere cumplir con normativas oficiales, sin embargo, se implementarán buenas prácticas de seguridad, como la validación estricta de datos del usuario, el control de acceso básico para reportes administrativos y el registro de logs de actividad para fines de auditoría interna.

## Interfaz y experiencia del usuario
### ¿Hay diseños o prototipos ya creados para la interfaz de usuario?
La aplicación se desarrollará inicialmente como una interfaz de línea de comandos (CLI), por lo que el diseño se enfocará en una estructura clara de menús y mensajes informativos para facilitar la navegación.

### ¿Cómo imaginas la experiencia del usuario al interactuar con la aplicación?
La experiencia será sencilla, directa y funcional:
- El usuario interactuará mediante opciones numeradas y entradas de texto.
- Se prioriza la claridad de las instrucciones y la validación inmediata de errores.
- El flujo será guiado, con pasos bien definidos para cada acción (registro, ingreso, cobro, etc.).
- Se buscará reducir al mínimo los comandos necesarios por parte del usuario.

### ¿Existen estándares de accesibilidad o internacionalización que debemos cumplir?
Dado que se trata de un proyecto académico en consola, no se aplicarán estándares formales de accesibilidad ni de internacionalización.

## Pruebas y calidad
### ¿Qué nivel de calidad se espera de la aplicación?
Se espera que la aplicación cumpla con los siguientes estándares básicos de calidad:
- Correcto funcionamiento de todas las funcionalidades principales (registro, ingreso, cobro, reportes).
- Interfaz clara y sin errores en la consola.
- Validación de entradas y manejo adecuado de errores.
- Resultados consistentes y confiables en cálculos y reportes.

### ¿Cuáles son los criterios para las pruebas de aceptación del usuario?
Un conjunto mínimo de criterios incluye:
- El flujo completo de ingreso y salida de vehículos debe realizarse sin fallos.
- Los cobros calculados deben ser precisos de acuerdo con las reglas definidas.
- La aplicación debe permitir generar recibos y exportar reportes CSV correctamente.
- Todas las opciones del menú deben estar accesibles y funcionar como se espera.
- Validaciones deben impedir entradas incorrectas (por ejemplo, registrar un vehículo sin usuario).

### ¿Cómo gestionaremos las pruebas y la solución de errores durante el desarrollo?
Se realizarán pruebas manuales después de cada módulo (por ejemplo, después del módulo de registro o cobro).
Se mantendrá una lista de errores detectados con su estado (pendiente/resuelto) en una hoja compartida o repositorio.
Se utilizarán casos de prueba simples, definidos previamente, para validar entradas válidas e inválidas.
Se realizarán revisiones en equipo antes de cada entrega parcial para garantizar la calidad general del sistema.

## Riesgos y mitigación
### ¿Qué riesgos potenciales ves en el proyecto?
Retrasos en el desarrollo por carga académica o falta de tiempo.
Errores en la lógica de cobro o validaciones.
Falta de experiencia del equipo con ciertas tecnologías.
Desacuerdos en la coordinación del equipo.

### ¿Cómo podemos mitigar estos riesgos de manera proactiva?
Dividir el trabajo por actas y asignar responsables claros.
Establecer reuniones semanales para revisar avances.
Validar funcionalidades críticas (registro, cobros) con múltiples pruebas.
Documentar el código para facilitar su comprensión entre compañeros.

### ¿Hay planes de contingencia en caso de problemas críticos durante el desarrollo?
Sí. Tener copias de seguridad del proyecto en la nube y en local. Si hay un fallo crítico en una entrega, presentar una versión funcional mínima (MVP) aunque falten detalles. Mantener una lista de bugs y tareas pendientes para priorizar en caso de contratiempos.

## Colaboración y comunicación
### ¿Cómo será la comunicación entre el equipo de desarrollo y tú?
La comunicación se realizará principalmente por WhatsApp y/o Google Meet para reuniones rápidas. Se organizarán reuniones semanales o según necesidad para revisar avances, dividir tareas y resolver dudas.
Se utilizará una herramienta como GitHub y WhatsApp para registrar el progreso, bugs y pendientes.

### ¿Dónde se almacenará el proyecto y como será su versionado?
El proyecto se almacenará en un repositorio en GitHub para asegurar el acceso y control de versiones.
Cada integrante trabajará en ramas separadas (por módulo o funcionalidad), usando Git como sistema de control de versiones.
Habrá copias de seguridad periódicas en la nube.
