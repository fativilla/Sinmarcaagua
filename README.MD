# 🖼️ Imperfection Remover - Eliminador imperfecciones en fotografias
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Una aplicación de escritorio con interfaz gráfica moderna para eliminar imperfecciones de imágenes de manera selectiva y precisa.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Vista Previa](#-vista-previa)
- [Requisitos del Sistema](#-requisitos-del-sistema)
- [Instalación](#-instalación)
- [Guía de Uso](#-guía-de-uso)
- [Cómo Funciona](#-cómo-funciona)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Agradecimientos](#-agradecimientos)
- [Usalo responsablemente](#-Usalo-responsablemente)

---

## ✨ Características

- 🎨 **Interfaz moderna** con tema oscuro y diseño responsive
- 🖱️ **Selección interactiva** con mouse sobre la imagen
- 📂 **Carga de imágenes** mediante diálogo nativo
- 🔄 **Procesamiento en segundo plano** sin bloquear la interfaz
- 📊 **Contador en tiempo real** de áreas seleccionadas
- ⌨️ **Atajos de teclado** para acciones rápidas
- 💾 **Guardado automático** con sufijo `_sm` en el mismo directorio
- 🔔 **Notificaciones** al finalizar el proceso
- 👁️ **Opción para abrir** la imagen procesada
- 🎯 **Precisión milimétrica** en la selección
- 🧹 **Limpieza de selección** con un solo clic

---

## 🖼️ Vista Previa

### Interfaz Principal

+----------------------------------------------------------+
| 🖼️ Eliminador de Marca de imperfecciones |
| +---------+ +----------------------------------------+ |
| | 📁 CARGAR | | [Área de la imagen] | |
| | IMAGEN | | | |
| | | | ______________ | |
| | 📂 Sele- | | | | | |
| | ccionar | | | MARCA DE | ← Selección con | |
| | Imagen | | | imagen | mouse | |
| | | | |______________| | |
| | ✏️ INST- | | | |
| | RUCCIO- | | | |
| | NES | | | |
| | | | | |
| | ⚡ ACCIO- | | | |
| | NES | | | |
| | [PROCESAR]| | | |
| | [LIMPIAR] | | | |
| | | | | |
| | 📊 ESTADO | | | |
| | ✅ Listo | | | |
| +---------+ +----------------------------------------+ |
+----------------------------------------------------------+

## 💻 Requisitos del Sistema

### Hardware Mínimo
- **Procesador:** Intel Core i3 o equivalente
- **RAM:** 4 GB
- **Almacenamiento:** 100 MB disponibles
- **Resolución de pantalla:** 1280x720

### Hardware Recomendado
- **Procesador:** Intel Core i5 o superior
- **RAM:** 8 GB o más
- **Almacenamiento:** SSD

### Sistema Operativo
- **Windows:** 10/11 (64 bits)
- **Linux:** Ubuntu 20.04+ o similar
- **macOS:** 11 (Big Sur) o superior

---

## 📦 Instalación

### 1. Clonar el Repositorio


## 🚀 Guía de Uso
Paso 1: Cargar una Imagen
Haz clic en "Seleccionar Imagen"

Navega hasta la ubicación de tu imagen

Selecciona el archivo (formatos: JPG, PNG, BMP, TIFF, WEBP)

Paso 2: Seleccionar las imperfecciones a eliminar
Haz clic izquierdo en una esquina de la imperfeccion

Arrastra el mouse hasta la esquina opuesta

Suelta el click para confirmar la selección

Repite el proceso para cada línea de texto

Paso 3: Procesar la Imagen
Presiona "PROCESAR" o la tecla ENTER

Espera a que termine el procesamiento

Recibirás una notificación con la ruta del archivo guardado

Paso 4: Ver el Resultado
Haz clic en "Sí" cuando pregunte si quieres abrir la imagen

O navega manualmente a la carpeta de la imagen original

Atajos de Teclado
Tecla	Acción
ENTER	Procesar imagen
ESC	Limpiar selección

## 🔧 Cómo Funciona
Algoritmo de Eliminación
Detección de Áreas: El usuario selecciona manualmente las áreas 

Creación de Máscara: Se genera una máscara binaria donde las áreas seleccionadas son blancas

Inpainting: OpenCV aplica el algoritmo de INPAINT_TELEA que:

Analiza los píxeles alrededor del área a rellenar

Propaga la información de los bordes hacia el interior

Reconstruye la imagen de manera natura

## 🛠️ Tecnologías Utilizadas
Tecnología	Versión	Propósito
Python	3.8+	Lenguaje base
CustomTkinter	5.0+	Interfaz gráfica moderna
OpenCV	4.5+	Procesamiento de imágenes
NumPy	1.19+	Operaciones con arrays
Pillow	9.0+	Manejo de imágenes
Threading	-	Procesamiento en segundo plano

## 🙏 Agradecimientos
OpenCV - Procesamiento de imágenes

CustomTkinter - Interfaz moderna

NumPy - Operaciones matemáticas

 ⭐ Muestra tu Apoyo
Si este proyecto te ha sido útil, ¡considera darle una estrella ⭐ en GitHub!

 ⭐⭐⭐⭐⭐ Usalo responsablemente.

 Hecho con ❤️ por fativilla
