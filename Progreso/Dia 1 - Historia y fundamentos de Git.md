# Historia y Fundamentos de Git

## Historia:

- **Creador:**
  - Git fue creado por Linus Torvalds, el creador del kernel de Linux, en 2005. Torvalds comenzó a trabajar en Git para gestionar el desarrollo del kernel de Linux después de que se volviera demasiado difícil mantener el control de las versiones con el sistema de control de versiones existente, BitKeeper.

- **Desarrollo y Adopción:**
  - Git se desarrolló rápidamente con contribuciones de la comunidad de desarrolladores de software de código abierto.
  - La facilidad de uso, la velocidad y la capacidad de trabajar de forma distribuida hicieron que Git se volviera extremadamente popular no solo para el desarrollo de software de código abierto, sino también en empresas y proyectos comerciales.

## Fundamentos:

- **Sistema de Control de Versiones Distribuido:**
  - Git es un sistema de control de versiones distribuido, lo que significa que cada usuario tiene una copia completa del repositorio, incluido el historial de cambios, en su propio sistema.
  - Esto permite a los desarrolladores trabajar de forma independiente y colaborar de manera eficiente sin depender de una conexión a internet constante.

- **Instantáneas (Snapshots):**
  - En lugar de almacenar cambios como diferencias entre archivos, Git guarda instantáneas de archivos en el momento en que se realiza un commit.
  - Esto proporciona una representación completa y coherente del estado del proyecto en cada punto en el tiempo.

- **Ramas (Branches):**
  - Git permite la creación de ramas independientes que permiten a los desarrolladores trabajar en nuevas características o correcciones de errores sin afectar el código base.
  - Las ramas pueden fusionarse posteriormente para incorporar los cambios en la rama principal del proyecto.

- **Área de Staging (Staging Area):**
  - Git utiliza un área de staging, también conocida como índice, donde se preparan los cambios antes de realizar un commit.
  - Esto proporciona un control preciso sobre qué cambios se incluirán en el próximo commit.

- **Historial de Cambios (History):**
  - Git mantiene un historial completo de todos los cambios realizados en el repositorio, lo que permite retroceder en el tiempo para ver cómo evolucionó el código y quién realizó cada cambio.

- **Integridad y Seguridad:**
  - Git utiliza un sistema de hash SHA-1 para garantizar la integridad de los datos almacenados en el repositorio.
  - Además, Git admite la firma de commits y etiquetas, lo que proporciona una capa adicional de seguridad y verificación de la autenticidad de los cambios.

