import streamlit as st
import pandas as pd

# --- Configuración de la página ---
st.set_page_config(
    page_title="Registro de Movimientos - CEREFAS",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Estilos CSS Personalizados ---
def load_css():
    st.markdown("""
        <style>
        /* Estilos generales */
        .stApp {
            background-color: #faece1;
        }
        
        /* Ocultar header de Streamlit por defecto */
        header {visibility: hidden !important;}
        
        /* Ajuste de padding de la app */
        .block-container {
            padding-top: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }

        /* Estilos para el Encabezado Personalizado */
        .custom-header {
            background-color: #0f766e; /* Verde Azulado */
            padding: 15px 40px;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .custom-header h1 {
            color: #ffffff;
            margin: 0;
            font-size: 26px;
            font-weight: 700;
        }

        /* Contenedor principal con padding */
        .main-content {
            padding: 0 40px;
        }

        /* Estilos para el Panel de Inventario (Derecha) */
        .inventory-panel {
            background-color: #eaddcf; /* Madera clara base */
            background-image: repeating-linear-gradient(
                90deg,
                transparent,
                transparent 20px,
                rgba(200, 180, 150, 0.15) 20px,
                rgba(200, 180, 150, 0.15) 40px
            ); /* Textura de madera simulada */
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            border: 1px solid #d4c0ab;
        }
        .inventory-panel h3 {
            color: #000;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 15px;
            margin-top: 0;
            padding-bottom: 5px;
            line-height: 1.2;
        }
        .inventory-item {
            margin-bottom: 15px;
            font-size: 14px;
            color: #333;
        }
        .inventory-item strong {
            font-size: 16px;
            color: #000;
            float: right;
        }

        /* Ajustes botones y filtros */
        .stButton>button {
            background-color: #40e0d0; /* Verde turquesa */
            color: #0d3b3b;
            border-radius: 20px;
            border: none;
            font-weight: 600;
            padding: 5px 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            background-color: #35cfc0;
            color: white;
        }
        
        .stTextInput>div>div>input {
            border-radius: 20px;
        }
        .stSelectbox>div>div>div {
            border-radius: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

load_css()

# --- Encabezado ---
st.markdown("""
    <div class="custom-header">
        <h1>Registro de Movimientos de Fauna Silvestre - Panel de Control</h1>
    </div>
""", unsafe_allow_html=True)

# Layout Principal con márgenes
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Col1: Tabla y Filtros (80%) | Col2: Inventario (20%)
col_main, col_sidebar = st.columns([4.2, 1])

with col_main:
    # --- Filtros y Búsqueda ---
    search_col, _, btn_col = st.columns([1.5, 3, 1.5])
    with search_col:
        search_query = st.text_input("Busca", placeholder="🔍 Busca", label_visibility="collapsed")
    
    st.write("") # Spacer
    
    filter_col1, filter_col2, filter_col3, empty_space, btn_col_new = st.columns([1.2, 1.2, 1.5, 0.5, 1.2])
    with filter_col1:
        st.selectbox("Filtro por Fecha", ["Filtro por Fecha (rango)"], label_visibility="collapsed")
    with filter_col2:
        st.selectbox("Filtro por Especie", ["Filtro por Especie"], label_visibility="collapsed")
    with filter_col3:
        st.selectbox("Filtro por Tipo de Evento", ["Filtro por Tipo de Evento (Ingreso/Egreso)"], label_visibility="collapsed")
    with btn_col_new:
        st.button("Crear Nuevo Registro", use_container_width=True)

    # --- Generación de Datos Simulados ---
    data = [
        {"FECHA": "03-01-2025", "N° FICHA": "2025-001", "NOMBRE COMÚN": "Peuco", "NOMBRE CIENTÍFICO": "Parabuteo unicinctus", "N° ACTA MOVI.": "60963", "N° EJEMPLAR": "1", "TIPO EVENTO": "⬆️ Ingreso", "CATEGORÍA EVENTO": "Recepción", "SALDO ANTERIOR": "0", "SALDO ACTUAL": "1", "DESTINO": "SAG Rio Neg", "OBSERVACIONES": "Obs: Encontrado con ala fracturada Ver más"},
        {"FECHA": "03-01-2025", "N° FICHA": "2025-001", "NOMBRE COMÚN": "Peuco", "NOMBRE CIENTÍFICO": "Parabuteo unicinctus", "N° ACTA MOVI.": "60963", "N° EJEMPLAR": "1", "TIPO EVENTO": "⬇️ Egreso", "CATEGORÍA EVENTO": "Defunción", "SALDO ANTERIOR": "1", "SALDO ACTUAL": "0", "DESTINO": "SAG Rio Neg", "OBSERVACIONES": "Obs: Necropsia posterior Ver más"},
        {"FECHA": "06-01-2025", "N° FICHA": "2025-197", "NOMBRE COMÚN": "Pudú", "NOMBRE CIENTÍFICO": "Pudu puda", "N° ACTA MOVI.": "29-12-2024", "N° EJEMPLAR": "1", "TIPO EVENTO": "⬇️ Egreso", "CATEGORÍA EVENTO": "Liberación", "SALDO ANTERIOR": "1", "SALDO ACTUAL": "0", "DESTINO": "PN Alerce Andino", "OBSERVACIONES": "Obs: En PN Alerce Andino Ver más"},
        {"FECHA": "06-01-2025", "N° FICHA": "2025-160", "NOMBRE COMÚN": "LORO CHICA", "NOMBRE CIENTÍFICO": "Enicognathus leptorhynchus", "N° ACTA MOVI.": "60929", "N° EJEMPLAR": "1", "TIPO EVENTO": "⬆️ Ingreso", "CATEGORÍA EVENTO": "Recepción", "SALDO ANTERIOR": "2", "SALDO ACTUAL": "3", "DESTINO": "SAG Puerto Montt", "OBSERVACIONES": "Obs: Atacado por perro... Ver más"},
        {"FECHA": "07-01-2025", "N° FICHA": "2025-160", "NOMBRE COMÚN": "CHACA CHOROY", "NOMBRE CIENTÍFICO": "Enicognathus ferrugineus", "N° ACTA MOVI.": "60932", "N° EJEMPLAR": "2", "TIPO EVENTO": "⬆️ Ingreso", "CATEGORÍA EVENTO": "Recepción", "SALDO ANTERIOR": "0", "SALDO ACTUAL": "2", "DESTINO": "SAG Puerto Montt", "OBSERVACIONES": "Obs: Atacado por perro... Ver más"},
        {"FECHA": "08-01-2025", "N° FICHA": "2025-007", "NOMBRE COMÚN": "GAVIOTA DOMINICANA", "NOMBRE CIENTÍFICO": "Larus dominicanus", "N° ACTA MOVI.": "62010", "N° EJEMPLAR": "1", "TIPO EVENTO": "⬇️ Egreso", "CATEGORÍA EVENTO": "Defunción", "SALDO ANTERIOR": "1", "SALDO ACTUAL": "0", "DESTINO": "SAG Puerto Montt", "OBSERVACIONES": "Obs: Encontrado on fía... Ver más"},
        {"FECHA": "08-01-2025", "N° FICHA": "2025-008", "NOMBRE COMÚN": "GAVIOTA", "NOMBRE CIENTÍFICO": "Larus dominicanus", "N° ACTA MOVI.": "62010", "N° EJEMPLAR": "1", "TIPO EVENTO": "⬇️ Egreso", "CATEGORÍA EVENTO": "Defunción", "SALDO ANTERIOR": "1", "SALDO ACTUAL": "0", "DESTINO": "SAG Puerto Montt", "OBSERVACIONES": "Obs: Encontrado on Se... Ver más"},
        {"FECHA": "08-01-2025", "N° FICHA": "2025-008", "NOMBRE COMÚN": "BANDURRIA", "NOMBRE CIENTÍFICO": "Theristicus melanopis", "N° ACTA MOVI.": "62010", "N° EJEMPLAR": "1", "TIPO EVENTO": "⬆️ Ingreso", "CATEGORÍA EVENTO": "Recepción", "SALDO ANTERIOR": "0", "SALDO ACTUAL": "1", "DESTINO": "SAG Puerto Montt", "OBSERVACIONES": "Obs: Encontrado en Se... Ver más"},
        {"FECHA": "09-01-2025", "N° FICHA": "2025-011", "NOMBRE COMÚN": "BANDURRIA", "NOMBRE CIENTÍFICO": "Theristicus melanopis", "N° ACTA MOVI.": "62010", "N° EJEMPLAR": "1", "TIPO EVENTO": "⬇️ Egreso", "CATEGORÍA EVENTO": "Defunción", "SALDO ANTERIOR": "1", "SALDO ACTUAL": "0", "DESTINO": "SAG Puerto Montt", "OBSERVACIONES": "Obs: Ala lacrada Ver más"},
        {"FECHA": "09-01-2025", "N° FICHA": "2025-013", "NOMBRE COMÚN": "TIUQUE", "NOMBRE CIENTÍFICO": "Milvago chimango", "N° ACTA MOVI.": "60935", "N° EJEMPLAR": "1", "TIPO EVENTO": "⬆️ Ingreso", "CATEGORÍA EVENTO": "Recepción", "SALDO ANTERIOR": "0", "SALDO ACTUAL": "1", "DESTINO": "SAG Osorno", "OBSERVACIONES": "Obs: mieontrado poste... Ver más"},
    ]
    df = pd.DataFrame(data)

    # --- Renderizado de Tabla ---
    html_table = f"""
    <style>
    .custom-table-container {{
        background: #f7ede2;
        border-radius: 10px;
        padding: 10px;
        margin-top: 15px;
        border: 1px solid #e0d0c0;
    }}
    .custom-table {{
        width: 100%;
        border-collapse: collapse;
        font-family: sans-serif;
        font-size: 13px;
    }}
    .custom-table th {{
        background-color: #dfc6ad;
        padding: 8px 10px;
        text-align: left;
        border-bottom: 2px solid #c9a888;
        font-weight: 700;
        color: #000;
    }}
    .custom-table tr:nth-child(even) {{
        background-color: #faece1;
    }}
    .custom-table tr:nth-child(odd) {{
        background-color: #f7ede2;
    }}
    .custom-table td {{
        padding: 8px 10px;
        color: #000;
    }}
    .ver-mas {{
        color: #1a3a5c;
        text-decoration: underline;
        cursor: pointer;
        font-size: 12px;
    }}
    .event-icon {{
        color: #27ae60;
    }}
    .event-icon-down {{
        color: #c0392b;
    }}
    </style>
    <div class="custom-table-container">
    <table class="custom-table">
        <tr>
            <th>FECHA</th>
            <th>N° FICHA</th>
            <th>NOMBRE COMÚN</th>
            <th>NOMBRE CIENTÍFICO</th>
            <th>N° ACTA MOVI.</th>
            <th>N° EJEMPLAR</th>
            <th>TIPO EVENTO</th>
            <th>CATEGORÍA EVENTO</th>
            <th>SALDO ANTERIOR</th>
            <th>SALDO ACTUAL</th>
            <th>DESTINO</th>
            <th>OBSERVACIONES</th>
        </tr>
    """
    for index, row in df.iterrows():
        # Dar formato a la palabra 'Ver más' si existe
        obs_text = row['OBSERVACIONES'].replace("Ver más", "<span class='ver-mas'>Ver más</span>")
        
        # Color en el ícono de evento (círculos verde y rojo)
        circle_green = "<span style='display:inline-block; width:12px; height:12px; border-radius:50%; background-color:#27ae60; margin-right:6px; vertical-align:middle;'></span>"
        circle_red = "<span style='display:inline-block; width:12px; height:12px; border-radius:50%; background-color:#e74c3c; margin-right:6px; vertical-align:middle;'></span>"
        evento_fmt = row['TIPO EVENTO'].replace("⬆️", circle_green).replace("⬇️", circle_red)

        html_table += f"<tr>"
        html_table += f"<td>{row['FECHA']}</td>"
        html_table += f"<td>{row['N° FICHA']}</td>"
        html_table += f"<td><strong>{row['NOMBRE COMÚN']}</strong></td>"
        html_table += f"<td><span style='font-style: italic;'>{row['NOMBRE CIENTÍFICO']}</span></td>"
        html_table += f"<td>{row['N° ACTA MOVI.']}</td>"
        html_table += f"<td>{row['N° EJEMPLAR']}</td>"
        html_table += f"<td>{evento_fmt}</td>"
        html_table += f"<td>{row['CATEGORÍA EVENTO']}</td>"
        html_table += f"<td>{row['SALDO ANTERIOR']}</td>"
        html_table += f"<td>{row['SALDO ACTUAL']}</td>"
        html_table += f"<td>{row['DESTINO']}</td>"
        html_table += f"<td>{obs_text}</td>"
        html_table += f"</tr>"
    html_table += "</table></div>"
    st.markdown(html_table, unsafe_allow_html=True)
    
    # --- Paginación Footer ---
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px; font-size: 14px; font-family: sans-serif;">
        <div style="display: flex; gap: 5px;">
            <button style="border: 1px solid #ccc; background: #f0f0f0; padding: 4px 10px; border-radius: 4px; color: #888; cursor: not-allowed;">Anterior</button>
            <button style="border: none; background: #1a3a5c; color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold;">1</button>
            <button style="border: none; background: transparent; padding: 4px 10px; color: #1a3a5c;">2</button>
            <button style="border: none; background: transparent; padding: 4px 10px; color: #1a3a5c;">3</button>
            <span style="padding: 4px 5px;">...</span>
            <button style="border: 1px solid #ccc; background: #fff; padding: 4px 10px; border-radius: 4px; color: #1a3a5c; cursor: pointer;">Siguiente</button>
        </div>
        <div style="font-weight: 700; color: #000;">
            Suma total ejemplares view: 21
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_sidebar:
    st.write("") # Spacer for alignment
    st.markdown("""
        <div class="inventory-panel">
            <h3>Estado Actual de<br>Inventario</h3>
            <div class="inventory-item">
                Animales en<br>Rehabilitación: <strong>15</strong>
            </div>
            <hr style="border: 0; border-top: 1px solid #e0d0c0; margin: 12px 0;">
            <div class="inventory-item">
                Animales Liberados<br>este mes: <strong>5</strong>
            </div>
            <hr style="border: 0; border-top: 1px solid #e0d0c0; margin: 12px 0;">
            <div class="inventory-item">
                Total Especies<br>Registradas: <strong>21</strong>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
