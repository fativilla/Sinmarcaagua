import customtkinter as ctk
import cv2
import numpy as np
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

# Configurar tema de CustomTkinter
ctk.set_appearance_mode("dark")  # Modos: "dark", "light"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

class WatermarkRemoverApp:
    def __init__(self):
        # Configuración de la ventana principal
        self.root = ctk.CTk()
        self.root.title("🖼️ Eliminador de Marca de Agua")
        self.root.geometry("1100x750")
        self.root.minsize(900, 650)
        
        # Variables
        self.ruta_imagen = None
        self.imagen_original = None
        self.imagen_cv = None
        self.imagen_mostrada = None
        self.areas = []
        self.rectangulo_actual = None
        self.inicio_x = None
        self.inicio_y = None
        self.zoom_factor = 1.0
        self.offset_x = 0
        self.offset_y = 0
        
        # Configurar grid
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Crear la interfaz
        self.crear_barra_lateral()
        self.crear_area_principal()
        
        # Estado inicial
        self.actualizar_estado("🔄 Esperando imagen...", "gray")
        
        # Bind de teclas
        self.root.bind('<Return>', lambda e: self.procesar_imagen())
        self.root.bind('<Escape>', lambda e: self.limpiar_seleccion())
        
        # Iniciar
        self.root.mainloop()
    
    def crear_barra_lateral(self):
        """Crea la barra lateral con controles"""
        
        self.sidebar = ctk.CTkFrame(self.root, width=280, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        
        # Título
        titulo = ctk.CTkLabel(
            self.sidebar,
            text="🖼️ Eliminador de\nMarca de Agua",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        titulo.pack(pady=(30, 20))
        
        # Línea separadora
        ctk.CTkFrame(self.sidebar, height=2, fg_color="#3a3a3a").pack(fill="x", padx=20, pady=10)
        
        # ============================================
        # SECCIÓN: CARGAR IMAGEN
        # ============================================
        ctk.CTkLabel(
            self.sidebar,
            text="📁 CARGAR IMAGEN",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(20, 5), anchor="w", padx=20)
        
        # Botón para seleccionar imagen
        self.btn_cargar = ctk.CTkButton(
            self.sidebar,
            text="📂 Seleccionar Imagen",
            command=self.seleccionar_imagen,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.btn_cargar.pack(pady=(5, 10), padx=20, fill="x")
        
        # Mostrar ruta de la imagen
        self.label_ruta = ctk.CTkLabel(
            self.sidebar,
            text="Ninguna imagen seleccionada",
            font=ctk.CTkFont(size=11),
            wraplength=250,
            text_color="gray"
        )
        self.label_ruta.pack(pady=(0, 15), padx=20)
        
        # Línea separadora
        ctk.CTkFrame(self.sidebar, height=2, fg_color="#3a3a3a").pack(fill="x", padx=20, pady=10)
        
        # ============================================
        # SECCIÓN: INSTRUCCIONES
        # ============================================
        ctk.CTkLabel(
            self.sidebar,
            text="✏️ INSTRUCCIONES",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(20, 5), anchor="w", padx=20)
        
        instrucciones = """
        1. Carga una imagen
        2. Arrastra el mouse para seleccionar
           las áreas con marca de agua
        3. Presiona "PROCESAR" o ENTER
        4. La imagen se guardará con "_sm"
        """
        
        ctk.CTkLabel(
            self.sidebar,
            text=instrucciones,
            font=ctk.CTkFont(size=12),
            justify="left",
            text_color="#b0b0b0"
        ).pack(pady=(5, 15), padx=20)
        
        # Línea separadora
        ctk.CTkFrame(self.sidebar, height=2, fg_color="#3a3a3a").pack(fill="x", padx=20, pady=10)
        
        # ============================================
        # SECCIÓN: ACCIONES
        # ============================================
        ctk.CTkLabel(
            self.sidebar,
            text="⚡ ACCIONES",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(20, 5), anchor="w", padx=20)
        
        # Botón procesar
        self.btn_procesar = ctk.CTkButton(
            self.sidebar,
            text="✅ PROCESAR (ENTER)",
            command=self.procesar_imagen,
            height=40,
            font=ctk.CTkFont(size=14),
            fg_color="#2e7d32",
            hover_color="#1b5e20",
            state="disabled"
        )
        self.btn_procesar.pack(pady=(5, 10), padx=20, fill="x")
        
        # Botón limpiar selección
        self.btn_limpiar = ctk.CTkButton(
            self.sidebar,
            text="🗑️ Limpiar Selección",
            command=self.limpiar_seleccion,
            height=35,
            font=ctk.CTkFont(size=13),
            fg_color="#b71c1c",
            hover_color="#880e4f",
            state="disabled"
        )
        self.btn_limpiar.pack(pady=(0, 10), padx=20, fill="x")
        
        # Línea separadora
        ctk.CTkFrame(self.sidebar, height=2, fg_color="#3a3a3a").pack(fill="x", padx=20, pady=10)
        
        # ============================================
        # SECCIÓN: ESTADO
        # ============================================
        ctk.CTkLabel(
            self.sidebar,
            text="📊 ESTADO",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(20, 5), anchor="w", padx=20)
        
        # Frame para estado
        self.frame_estado = ctk.CTkFrame(self.sidebar, fg_color="#1e1e1e")
        self.frame_estado.pack(pady=(5, 10), padx=20, fill="x")
        
        self.label_estado = ctk.CTkLabel(
            self.frame_estado,
            text="⏳ Esperando imagen...",
            font=ctk.CTkFont(size=13),
            text_color="#808080"
        )
        self.label_estado.pack(pady=15)
        
        # Info de áreas seleccionadas
        self.label_areas = ctk.CTkLabel(
            self.sidebar,
            text="Áreas seleccionadas: 0",
            font=ctk.CTkFont(size=12),
            text_color="#808080"
        )
        self.label_areas.pack(pady=(0, 15))
        
        # ============================================
        # BOTÓN SALIR
        # ============================================
        ctk.CTkFrame(self.sidebar, height=2, fg_color="#3a3a3a").pack(fill="x", padx=20, pady=10)
        
        self.btn_salir = ctk.CTkButton(
            self.sidebar,
            text="🚪 Salir",
            command=self.root.quit,
            height=35,
            font=ctk.CTkFont(size=13),
            fg_color="#424242",
            hover_color="#212121"
        )
        self.btn_salir.pack(pady=(10, 20), padx=20, fill="x")
    
    def crear_area_principal(self):
        """Crea el área donde se muestra la imagen"""
        
        # Frame principal para la imagen
        self.frame_imagen = ctk.CTkFrame(self.root, corner_radius=10)
        self.frame_imagen.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        self.frame_imagen.grid_columnconfigure(0, weight=1)
        self.frame_imagen.grid_rowconfigure(0, weight=1)
        
        # Canvas para mostrar la imagen
        self.canvas = tk.Canvas(
            self.frame_imagen,
            bg='#1a1a1a',
            highlightthickness=1,
            highlightbackground="#2a2a2a"
        )
        self.canvas.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Texto de bienvenida en el canvas
        self.canvas.create_text(
            self.frame_imagen.winfo_width() // 2,
            self.frame_imagen.winfo_height() // 2,
            text="🖼️ Carga una imagen para comenzar",
            fill="#404040",
            font=("Arial", 20),
            tags="placeholder"
        )
        
        # Bind eventos del canvas
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        
        # Configurar que el canvas se redimensione
        self.frame_imagen.bind("<Configure>", self.on_resize)
    
    def on_resize(self, event):
        """Redimensiona la imagen cuando cambia el tamaño de la ventana"""
        if self.imagen_mostrada:
            self.mostrar_imagen()
    
    def seleccionar_imagen(self):
        """Abre diálogo para seleccionar imagen"""
        ruta = filedialog.askopenfilename(
            title="Selecciona una imagen",
            filetypes=[
                ("Imágenes", "*.jpg *.jpeg *.png *.bmp *.tiff *.webp"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if ruta:
            self.ruta_imagen = ruta
            self.label_ruta.configure(text=os.path.basename(ruta))
            self.cargar_imagen(ruta)
    
    def cargar_imagen(self, ruta):
        """Carga la imagen seleccionada"""
        try:
            # Cargar con OpenCV
            self.imagen_cv = cv2.imread(ruta)
            if self.imagen_cv is None:
                raise ValueError("No se pudo cargar la imagen")
            
            # Cargar con PIL para mostrar
            self.imagen_original = Image.open(ruta)
            self.imagen_original = self.imagen_original.convert("RGB")
            
            # Limpiar selecciones anteriores
            self.areas = []
            self.label_areas.configure(text="Áreas seleccionadas: 0")
            
            # Mostrar imagen
            self.mostrar_imagen()
            
            # Habilitar botones
            self.btn_procesar.configure(state="normal")
            self.btn_limpiar.configure(state="normal")
            
            # Actualizar estado
            self.actualizar_estado("✅ Imagen cargada correctamente", "green")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen:\n{str(e)}")
            self.actualizar_estado("❌ Error al cargar imagen", "red")
    
    def mostrar_imagen(self):
        """Muestra la imagen en el canvas con ajuste de tamaño"""
        if self.imagen_original is None:
            return
        
        # Obtener tamaño del canvas
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1 or canvas_height <= 1:
            canvas_width = 600
            canvas_height = 500
        
        # Calcular tamaño para ajustar
        img_width, img_height = self.imagen_original.size
        ratio = min(canvas_width / img_width, canvas_height / img_height)
        new_width = int(img_width * ratio * 0.95)
        new_height = int(img_height * ratio * 0.95)
        
        # Redimensionar imagen
        img_resized = self.imagen_original.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.imagen_mostrada = ImageTk.PhotoImage(img_resized)
        
        # Guardar escala para convertir coordenadas
        self.escala_x = new_width / img_width
        self.escala_y = new_height / img_height
        
        # Limpiar canvas
        self.canvas.delete("all")
        
        # Mostrar imagen
        x_centro = (canvas_width - new_width) // 2
        y_centro = (canvas_height - new_height) // 2
        self.canvas.create_image(x_centro, y_centro, anchor="nw", image=self.imagen_mostrada)
        
        # Dibujar áreas seleccionadas
        for x1, y1, x2, y2 in self.areas:
            # Convertir coordenadas
            px1 = int(x1 * self.escala_x) + x_centro
            py1 = int(y1 * self.escala_y) + y_centro
            px2 = int(x2 * self.escala_x) + x_centro
            py2 = int(y2 * self.escala_y) + y_centro
            self.canvas.create_rectangle(px1, py1, px2, py2, outline='#00ff00', width=2)
        
        # Guardar offset para conversión de coordenadas
        self.offset_x = x_centro
        self.offset_y = y_centro
    
    def on_press(self, event):
        """Inicia la selección con el mouse"""
        if self.imagen_original is None:
            return
        
        self.inicio_x = event.x
        self.inicio_y = event.y
        self.rectangulo_actual = self.canvas.create_rectangle(
            event.x, event.y, event.x, event.y,
            outline='#ff6b6b', width=2, dash=(4, 2)
        )
    
    def on_drag(self, event):
        """Arrastra para seleccionar área"""
        if self.rectangulo_actual:
            self.canvas.coords(
                self.rectangulo_actual,
                self.inicio_x, self.inicio_y,
                event.x, event.y
            )
    
    def on_release(self, event):
        """Finaliza la selección"""
        if self.rectangulo_actual and self.imagen_original:
            # Obtener coordenadas
            x1 = min(self.inicio_x, event.x)
            y1 = min(self.inicio_y, event.y)
            x2 = max(self.inicio_x, event.x)
            y2 = max(self.inicio_y, event.y)
            
            # Convertir a coordenadas de la imagen original
            img_x1 = int((x1 - self.offset_x) / self.escala_x)
            img_y1 = int((y1 - self.offset_y) / self.escala_y)
            img_x2 = int((x2 - self.offset_x) / self.escala_x)
            img_y2 = int((y2 - self.offset_y) / self.escala_y)
            
            # Asegurar que estén dentro de la imagen
            img_x1 = max(0, min(img_x1, self.imagen_original.width))
            img_y1 = max(0, min(img_y1, self.imagen_original.height))
            img_x2 = max(0, min(img_x2, self.imagen_original.width))
            img_y2 = max(0, min(img_y2, self.imagen_original.height))
            
            if (img_x2 - img_x1) > 10 and (img_y2 - img_y1) > 10:
                self.areas.append((img_x1, img_y1, img_x2, img_y2))
                self.label_areas.configure(text=f"Áreas seleccionadas: {len(self.areas)}")
                self.actualizar_estado(f"✅ Área {len(self.areas)} seleccionada", "green")
                
                # Cambiar color del rectángulo
                self.canvas.itemconfig(self.rectangulo_actual, outline='#00ff00', width=2, dash=())
            else:
                # Eliminar rectángulo si es muy pequeño
                self.canvas.delete(self.rectangulo_actual)
            
            self.rectangulo_actual = None
    
    def limpiar_seleccion(self):
        """Limpia todas las selecciones"""
        if self.imagen_original is None:
            return
        
        self.areas = []
        self.label_areas.configure(text="Áreas seleccionadas: 0")
        self.actualizar_estado("🔄 Selección limpiada", "yellow")
        self.mostrar_imagen()
    
    def procesar_imagen(self):
        """Procesa la imagen eliminando las marcas de agua"""
        if self.imagen_cv is None:
            messagebox.showwarning("Advertencia", "Primero carga una imagen")
            return
        
        if not self.areas:
            messagebox.showwarning("Advertencia", "Selecciona al menos un área con marca de agua")
            return
        
        # Mostrar progreso
        self.actualizar_estado("⏳ Procesando imagen...", "yellow")
        self.btn_procesar.configure(state="disabled")
        self.btn_limpiar.configure(state="disabled")
        self.btn_cargar.configure(state="disabled")
        
        # Procesar en hilo separado
        threading.Thread(target=self.procesar_en_hilo, daemon=True).start()
    
    def procesar_en_hilo(self):
        """Procesa la imagen en un hilo separado"""
        try:
            # Crear máscara
            mascara = np.zeros(self.imagen_cv.shape[:2], dtype=np.uint8)
            for x1, y1, x2, y2 in self.areas:
                cv2.rectangle(mascara, (x1, y1), (x2, y2), 255, -1)
            
            # Aplicar inpainting
            resultado = cv2.inpaint(self.imagen_cv, mascara, 3, cv2.INPAINT_TELEA)
            
            # Guardar imagen
            nombre, extension = os.path.splitext(self.ruta_imagen)
            ruta_salida = f"{nombre}_sm{extension}"
            cv2.imwrite(ruta_salida, resultado, [cv2.IMWRITE_JPEG_QUALITY, 95])
            
            # Actualizar UI
            self.root.after(0, lambda: self.finalizar_procesamiento(ruta_salida))
            
        except Exception as e:
            self.root.after(0, lambda: self.error_procesamiento(str(e)))
    
    def finalizar_procesamiento(self, ruta_salida):
        """Finaliza el procesamiento exitoso"""
        self.actualizar_estado("✅ ¡Procesamiento completado!", "green")
        self.btn_procesar.configure(state="normal")
        self.btn_limpiar.configure(state="normal")
        self.btn_cargar.configure(state="normal")
        
        messagebox.showinfo(
            "¡Éxito!",
            f"✅ Imagen procesada exitosamente\n\n"
            f"📁 Guardada en:\n{ruta_salida}\n\n"
            f"📊 Áreas eliminadas: {len(self.areas)}"
        )
        
        # Preguntar si quiere ver la imagen
        if messagebox.askyesno("Ver resultado", "¿Quieres abrir la imagen procesada?"):
            os.startfile(ruta_salida)
    
    def error_procesamiento(self, error):
        """Maneja errores durante el procesamiento"""
        self.actualizar_estado(f"❌ Error: {error}", "red")
        self.btn_procesar.configure(state="normal")
        self.btn_limpiar.configure(state="normal")
        self.btn_cargar.configure(state="normal")
        messagebox.showerror("Error", f"Error al procesar la imagen:\n{error}")
    
    def actualizar_estado(self, mensaje, color="gray"):
        """Actualiza el estado en la interfaz"""
        colores = {
            "red": "#e74c3c",
            "green": "#2ecc71",
            "yellow": "#f1c40f",
            "gray": "#808080",
            "blue": "#3498db"
        }
        self.label_estado.configure(
            text=mensaje,
            text_color=colores.get(color, "#808080")
        )


# ============================================
# EJECUTAR APLICACIÓN
# ============================================

if __name__ == "__main__":
    app = WatermarkRemoverApp()