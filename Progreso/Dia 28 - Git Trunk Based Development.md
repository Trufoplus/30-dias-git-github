# Que es Trunk Based Development (TBD)
TBD es una práctica de gestión de control de versiones en la que los desarrolladores crean ramas de características pequeñas y desarrollan en estas ramas. Una vez que una característica está lista, se fusiona en la rama principal. Esto se llama desarrollo basado en troncales (Trunk Based Development). Los desarrolladores fusionan su código frecuentemente con 
el tronco (rama main) para obtener retroalimentación temprana.

![tbd-1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/tbd-1.png)

## Los beneficios principales del TBD:

1. **Retroalimentación temprana**: Al crear y fusionar ramas de características de forma rápida, se obtiene retroalimentación temprana sobre el trabajo realizado.

2. **Revisión de código en equipo**: Como parte del proceso de desarrollo en ramas pequeñas, se fomenta la revisión de código entre los miembros del equipo, lo que promueve la propiedad colectiva del código.

3. **Propiedad colectiva**: Al trabajar en ramas pequeñas y fusionarlas rápidamente, se promueve un sentido de propiedad colectiva del código dentro del equipo.

4. **Liberación más rápida de características**: Al liberar pequeños fragmentos de código de forma más rápida, los clientes pueden disfrutar de las características nuevas más pronto.

5. **Confianza del equipo**: Al incluir casos de prueba como parte de la característica, se aumenta la confianza del equipo en la estabilidad del código.

6. **Evitar conflictos de fusión**: Dado que los cambios de código son pequeños y se fusionan con frecuencia, se evitan los conflictos de fusión masivos y se reduce el tiempo dedicado a resolverlos.

## Paso a Paso implementando TBD


1. **Crear una rama para una nueva característica o tarea**:
   ```bash
   git checkout -b feature-login
   ```
   Esto crea una nueva rama llamada "feature-login" y te cambia a ella para que puedas comenzar a trabajar en la implementación del inicio de sesión.

2. **Desarrollar en la rama la característica**:
   ```python
    def login(username, password):
        if username == "dani" and password == "123":
            return "Sesion iniciada"
        else:
            return "Contraseña o usuario incorrecto"
    ```

3. **Realizar pruebas y revisión de código**:
   - Realizar pruebas unitarias para la función `login`.
   ````python
    import unittest
    from login import login

    class TestLoginFunction(unittest.TestCase):
        def test_login_success(self):
            # Prueba para inicio de sesión exitoso
            username = "dani"
            password = "123"
            result = login(username, password)
            self.assertEqual(result, "Sesion iniciada")

        def test_login_failure_username(self):
            # Prueba para nombre de usuario incorrecto
            username = "usuario_incorrecto"
            password = "123"
            result = login(username, password)
            self.assertEqual(result, "Contraseña o usuario incorrecto")

        def test_login_failure_password(self):
            # Prueba para contraseña incorrecta
            username = "dani"
            password = "contraseña_incorrecta"
            result = login(username, password)
            self.assertEqual(result, "Contraseña o usuario incorrecto")

        def test_login_failure_both(self):
            # Prueba para nombre de usuario y contraseña incorrectos
            username = "usuario_incorrecto"
            password = "contraseña_incorrecta"
            result = login(username, password)
            self.assertEqual(result, "Contraseña o usuario incorrecto")

        if __name__ == '__main__':
            unittest.main()
    ````

   - Solicitar a un compañero de equipo que revise tu código.
   - Utiliza linea de comando para ejecutar las pruebas

   ```bash
    python -m unittest tests
   ```
   
4. **Fusionar la rama de la característica con el tronco principal**:
   ```bash
   git checkout main
   git merge feature-login
   ```
   Esto fusiona los cambios de la rama "feature-login" con la rama principal "master".

5. **Resolver cualquier conflicto de fusión**:
   Si hay conflictos de fusión, edita los archivos afectados para resolver los conflictos y luego agrega los archivos modificados a la etapa y completa la fusión.
   ```bash
   git add .
   git commit -m "Resolución de conflictos de fusión"
   ```

6. **Probar y validar en el entorno de desarrollo**:
   Después de la fusión, ejecuta pruebas adicionales para asegurarte de que el código integrado funcione correctamente en el entorno de desarrollo.
   ```bash
   python -m unittest tests
   ```

# Git Flow
En Git Flow, hay dos ramas principales: la rama principal (main) y la rama de desarrollo ('development'). Todas las nuevas características se desarrollan en la rama de desarrollo y, una vez probadas e implementadas, se crea una rama de release para preparar la versión que se desplegará en producción. Esta rama de release permite ajustes finales y correcciones de errores antes de la implementación en el entorno de producción. Una vez que la versión ha sido probada y aprobada, se fusiona con la rama principal para reflejar los cambios en la versión estable del software.

Además de estas ramas principales, Git Flow también incluye ramas de soporte para arreglos de emergencia, conocidas como "hotfix branches". Estas ramas se utilizan para abordar problemas críticos que surgen en producción y requieren una corrección rápida sin interferir con el desarrollo de nuevas características en la rama de desarrollo.

![gitflow-1](https://github.com/Trufoplus/30-dias-git-github/blob/main/Progreso/img/gitflow-1.jpg)

## Git FLow vs Trunk Based Development (TBD):
1. **Git Flow**: Es conocido por su complejidad debido al número de ramas que utiliza. Tiene ramas principales de ciclo de vida largo (main y develop) y ramas de ciclo de vida corto para características específicas. Adecuado para equipos grandes, con releases fijas y donde se necesita un alto nivel de control sobre el flujo de trabajo.

2. **Trunk Based Development (TBD)**: Es mucho más simple, con una sola rama principal donde se desarrollan y prueban las características. Las integraciones son rápidas. Adecuado para equipos pequeños, con un enfoque en la entrega continua y la agilidad, y donde se requiere flexibilidad y rapidez en los despliegues.
