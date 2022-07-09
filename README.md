# Project "Easy to Schedule"

![Easy to Schedule](Proyecto/"Easy to Schedule/.jpg.webp)

Este proyecto esta diseñado para resolver problemas cotidianos a la hora de programar visitas para pacientes que se encuentran realizando ensayos clínicos.
La mayoría de los ensayos clínicos suelee tener multiples visitas. Para mantener la integridad de los datos, es fundamental que las visitas de los distintos ensayos clínicos ocurran dentro de cierto período de tiempo (días/ semanas). 

Por medio de "Easy to Schedule" el usuario podrá ahorrar tiempo a la hora de organizar la agenda del médico o provedor. Ademaás, podrá agendar todas las visitas subsiguientes una vez que el paciente haya sido enrolado en el ensayo clínico, evitando desvíos en el cumplimiento del protocolo. También servirá para registrar de todas las visitas relacionadas a investigacion en la agende del médico, lo cual servirá a la hora de presentar a una tercera parte el tiempo y esfuerzo que el provedor ha dedicada a cada ensayo clínico.

Inicialmente se ingresara el "Screening Day", luego el preguntara si el paciente es "elegible" para ser enrolado en el ensayo. Si el usuario contestase "Si" debera ingresarse el "Baseline Day". Una vez the "Baseline visit" haya sido ingresado el programa calculara las visitas subsiguientes. El programa proveerá el "Target Day". Ese día debera ser verificado en el calendario del medico o proveedor. Si el día esta disponible se agendará el día en la agenda del médico. Si el día no esta disponible en la agenda sistema buscará el día donde inicia la ventana de la visita ("Beginning of the Window") y luego el fin de la ventana para esa visita ("End of the Window").

Luego de que la primer "Follow-up visit" se agende el programa buscar encontrar la segunda y asi sucesivamente hasta agendar todas las visitas del estudio clínico.

