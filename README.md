# Bot de Discord

## Proposito

Este bot tiene como proposito permitir votaciones al sistema de decide a traves de Discord.

## Comandos


<table style="width: 100%; text-align: center;">
  <tr>
    <td style="width: 33%;">Comando</td>
    <td style="width: 33%;">Parámetros de entrada </td>
    <td style="width: 33%;">Funcionalidad</td>
  </tr>
  <tr>
    <td style="width: 33%;">!info </td>
    <td style="width: 33%;">... </td>
    <td style="width: 33%;">Muestra un compendio de todos los comandos existentes</td>
  </tr>
  <tr>
    <td style="width: 33%;">!loginAsUser</td>
    <td style="width: 33%;">Nombre de usuario y contraseña </td>
    <td style="width: 33%;">Te permite logearte, introduce el comando seguido de tu nombre de usuario y contraseña en decide</td>
  </tr>
    <tr>
    <td style="width: 33%;">!clean</td>
    <td style="width: 33%;">... </td>
    <td style="width: 33%;">Borra todos los mensajes, solo en canales de texto</td>
  </tr>
    <tr>
    <td style="width: 33%;">!votings</td>
    <td style="width: 33%;">... </td>
    <td style="width: 33%;">Te permite ver las votaciones disponibles </td>
  </tr>
  <tr>
    <td style="width: 33%;">!voting</td>
    <td style="width: 33%;">Id de la votación (Se puede obtener con !votings)</td>
    <td style="width: 33%;">Te permite obtener detalles concretos de una votación. Escribe !voting espacio y el ID de la votación. </td>
  </tr>
  <tr>
    <td style="width: 33%;">!vote </td>
    <td style="width: 33%;">Id de la votación y opción elegida </td>
    <td style="width: 33%;">Permite realizar una votación. Escribe !vote espacio el id de la votación y la opción elegida. </td>
  </tr>
</table>

## Flujo de uso

### ¿Qué puedo hacer?
Se esperá que el primer paso de un usuario novel sea ejecutar el comando !info. 
![](Images/Img1.png "")

### Login
Para poder disfrutar de las demás funcionalidades el usuario deberá darse de alta. Una vez realizado podrá seguir consultando.
![](Images/Img2.png "")

### ¿Qué puedo votar?.
Tras logearse el usuario debería ver todas las votaciones disponibles.
![](Images/Img3.png "")

### Me interesa esta votación
El usuario podrá conseguir más información sobre la votación ue le interese.
![](Images/Img4.png "")

### Voto a ...
El usuario podrá votar lo que decida a la votación que le interese.
![](Images/Img5.png "")
