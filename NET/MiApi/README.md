# MiApi (.NET 8 Web API)

Este proyecto contiene una API REST desarrollada con .NET 8, ubicada en la carpeta `MiApi`. Su objetivo es proporcionar un punto de inicio para el desarrollo de servicios web modernos, incluyendo documentación automática con Swagger.

## Estructura del proyecto

```
MiApi/
├── appsettings.Development.json   # Configuración para entorno de desarrollo
├── appsettings.json              # Configuración general de la aplicación
├── Dockerfile                    # Archivo para construir la imagen Docker
├── MiApi.csproj                  # Archivo de proyecto .NET
├── MiApi.http                    # Ejemplos de peticiones HTTP
├── Program.cs                    # Punto de entrada de la API
├── Properties/
│   └── launchSettings.json       # Configuración de lanzamiento
├── bin/                          # Archivos compilados
└── obj/                          # Archivos temporales de compilación
```

## Introducción de uso

1. **Ejecutar localmente**
   - Abre una terminal en la carpeta `MiApi`.
   - Ejecuta el comando:
     ```
     dotnet run
     ```
   - Accede a la documentación Swagger en:  
     [http://localhost:5000/swagger/index.html](http://localhost:5000/swagger/index.html)  
     *(puede variar el puerto según configuración)*

2. **Construir y ejecutar con Docker**
   - Desde la carpeta `MiApi`, ejecuta:
     ```
     docker build -t miapi .
     docker run -p 80:80 miapi
     ```
   - Accede a la API en [http://localhost/swagger/index.html](http://localhost/swagger/index.html)

## Endpoints de ejemplo

- `/weatherforecast`  
  Devuelve un listado de pronósticos del clima en formato JSON.

## Dependencias principales

- [.NET 8](https://dotnet.microsoft.com/)
- [Swashbuckle.AspNetCore](https://github.com/domaindrivendev/Swashbuckle.AspNetCore) (Swagger para documentación)

---

> Para más detalles, revisa el archivo [`Program.cs`](NET/MiApi/Program.cs)