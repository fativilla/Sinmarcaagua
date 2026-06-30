# 🖼️ Watermark Remover - Eliminador de Marcas de Agua

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Una aplicación de escritorio con interfaz gráfica moderna para eliminar marcas de agua de imágenes de manera selectiva y precisa.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Vista Previa](#-vista-previa)
- [Requisitos del Sistema](#-requisitos-del-sistema)
- [Instalación](#-instalación)
- [Guía de Uso](#-guía-de-uso)
- [Cómo Funciona](#-cómo-funciona)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Personalización](#-personalización)
- [Solución de Problemas](#-solución-de-problemas)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

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
| 🖼️ Eliminador de Marca de Agua |
| +---------+ +----------------------------------------+ |
| | 📁 CARGAR | | [Área de la imagen] | |
| | IMAGEN | | | |
| | | | ______________ | |
| | 📂 Sele- | | | | | |
| | ccionar | | | MARCA DE | ← Selección con | |
| | Imagen | | | AGUA | mouse | |
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
