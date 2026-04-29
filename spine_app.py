import streamlit as st
import time
import random
import plotly.graph_objects as go
from datetime import datetime

# --- PAGE CONFIGURATION & ERGONOMIC CSS ---
st.set_page_config(page_title="S.P.I.N.E. Core Command", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    /* Ergonomic Slate Dark Theme */
    .stApp { background-color: #0F172A; color: #E2E8F0; font-family: 'Inter', 'Segoe UI', sans-serif; }
    h1, h2, h3, h4 { color: #38BDF8 !important; font-weight: 500; }
    
    /* Panel Styling - Softer borders and shadows */
    .css-1d391kg { padding: 2rem; }
    .st-emotion-cache-1y4p8pa { padding: 2rem; border-radius: 8px; background: #1E293B; border: 1px solid #334155; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
    
    /* Alerts - Muted pastels instead of harsh neon */
    .alert-critical { background: rgba(239, 68, 68, 0.1); border-left: 4px solid #EF4444; color: #FCA5A5; padding: 15px; border-radius: 4px; font-weight: 500; }
    .alert-safe { background: rgba(34, 197, 94, 0.1); border-left: 4px solid #22C55E; color: #86EFAC; padding: 15px; border-radius: 4px; font-weight: 500; }
    
    /* Terminal Console - Deep dark blue with soft mint text */
    .terminal-box { background-color: #020617; color: #A7F3D0; padding: 12px; border-radius: 6px; font-family: 'Fira Code', Consolas, monospace; border: 1px solid #1E293B; height: 150px; overflow-y: auto; white-space: pre-wrap; }
    
    /* Make standard text highly legible */
    p, div, span { color: #CBD5E1; }
    </style>
""", unsafe_allow_html=True)

# --- EDGE AI MODEL ---
class AdvancedEdgePINN:
    def __init__(self):
        self.precision = "INT8"
        
    def predict(self, z_axis, impact_vel, bond_force, ultrasonic, pad_temp, efo):
        kinematic_risk = (z_axis / 250) * 0.4 + (impact_vel / 10) * 0.6
        mechanical_risk = ((80 - bond_force) / 70) * 0.8 + ((120 - ultrasonic) / 100) * 0.2
        thermal_risk = ((260 - pad_temp) / 110) * 0.7 + (efo / 50) * 0.3
        
        fluid_multiplier = (kinematic_risk * mechanical_risk) * 1.5 
        raw_svi = (kinematic_risk * 30) + (mechanical_risk * 50) + (thermal_risk * 10) + (fluid_multiplier * 10)
        return max(0.0, min(100.0, raw_svi + random.uniform(-0.5, 0.5)))

edge_model = AdvancedEdgePINN()

# --- SIDEBAR: SECS/GEM TELEMETRY INJECTION (Machine A) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #38BDF8;'>S.P.I.N.E.</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #334155; margin-top: 0;'>", unsafe_allow_html=True)
    
    st.markdown("### 📡 SECS/GEM Injection")
    st.caption("Override Machine A (Wire Bonder) Telemetry")
    
    st.markdown("**Kinematic**")
    z_axis = st.slider("Z-Axis Trajectory (µm)", 50, 250, 200, 1)
    impact_vel = st.slider("Impact Velocity (mm/s)", 1.0, 10.0, 8.5, 0.1)
    
    st.markdown("**Mechanical**")
    bond_force = st.slider("Bonding Force (g)", 10, 80, 20, 1)
    ultrasonic = st.slider("Ultrasonic Impedance (Ω)", 20, 120, 40, 1)
    
    st.markdown("**Thermal**")
    pad_temp = st.slider("Bond Pad Temp (°C)", 150, 260, 170, 1)
    efo = st.slider("EFO Metrics (mA)", 10, 50, 20, 1)

# --- MAIN DASHBOARD HEADER ---
st.title("S.P.I.N.E. EDGE COMMAND CENTER")
st.markdown("Multivariate Advanced Process Control | Sub-50ms Network Latency")
st.divider()

# Compute Edge AI Inference
start_time = time.perf_counter()
svi_score = edge_model.predict(z_axis, impact_vel, bond_force, ultrasonic, pad_temp, efo)
latency_ms = (time.perf_counter() - start_time) * 1000 + random.uniform(8.0, 14.0)
threshold = 75.0

# --- ROW 1: TOP LEVEL KPIS ---
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Network Status", "SEC/GEM LINKED", "0% Packet Loss")
kpi2.metric("Edge Node Latency", f"{latency_ms:.2f} ms", "-2.1ms from avg", delta_color="inverse")
kpi3.metric("Quantization", "INT8", "Optimized")
kpi4.metric("Process Phase", "ENCAPSULATION", "Active")

st.markdown("<br>", unsafe_allow_html=True)

# --- ROW 2: VISUALIZATION COMMAND DECK ---
col_radar, col_gauge, col_action = st.columns([1, 1, 1.2])

# 1. Radar Chart: The Data Tensor
with col_radar:
    st.markdown("<h4 style='text-align: center;'>Multivariate Tensor Map</h4>", unsafe_allow_html=True)
    categories = ['Z-Axis', 'Velocity', 'Force Inv.', 'Impedance Inv.', 'Temp Inv.', 'EFO']
    values = [z_axis/250, impact_vel/10, (80-bond_force)/70, (120-ultrasonic)/100, (260-pad_temp)/110, efo/50]
    
    fig_radar = go.Figure(data=go.Scatterpolar(
      r=values, theta=categories, fill='toself', line_color='#38BDF8', fillcolor='rgba(56, 189, 248, 0.2)'
    ))
    fig_radar.update_layout(polar=dict(radialaxis=dict(visible=False, range=[0, 1])), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#E2E8F0'), margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig_radar, use_container_width=True)

# 2. Gauge Chart: SVI Score
with col_gauge:
    st.markdown("<h4 style='text-align: center;'>Predictive SVI Index</h4>", unsafe_allow_html=True)
    gauge_color = "#EF4444" if svi_score > threshold else "#22C55E"
    
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = svi_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        delta = {'reference': threshold, 'increasing': {'color': "#EF4444"}, 'decreasing': {'color': "#22C55E"}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
            'bar': {'color': gauge_color},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "#334155",
            'steps': [
                {'range': [0, 75], 'color': "rgba(34, 197, 94, 0.1)"},
                {'range': [75, 100], 'color': "rgba(239, 68, 68, 0.1)"}],
            'threshold': {'line': {'color': "#F8FAFC", 'width': 4}, 'thickness': 0.75, 'value': threshold}
        }
    ))
    fig_gauge.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#E2E8F0'), margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig_gauge, use_container_width=True)

# 3. Dynamic Actuation Control Logic
with col_action:
    st.markdown("<h4 style='text-align: center;'>Downstream Actuation API</h4>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    if svi_score > threshold:
        st.markdown('<div class="alert-critical">⚠️ CRITICAL: MICRO-VARIANCE COLLISION IMMINENT</div>', unsafe_allow_html=True)
        st.write("")
        st.markdown("**EXECUTING DYNAMIC OVERRIDE [MACHINE B]:**")
        st.write("Target Fluid Dynamic Velocity (v): **-4.2% (Decelerating)**")
        st.progress(0.40, text="Ram Transfer Speed (Throttled)")
        st.write("Target Pre-Heat Duration (p): **+1.5s (Viscosity Drop)**")
        st.progress(0.85, text="Mold Tool Temp Gradient (Elevated)")
    else:
        st.markdown('<div class="alert-safe">✅ CLEAR: STRUCTURAL INTEGRITY OPTIMAL</div>', unsafe_allow_html=True)
        st.write("")
        st.markdown("**OPERATIONAL STATUS [MACHINE B]:**")
        st.write("Target Fluid Dynamic Velocity (v): **Standard**")
        st.progress(0.75, text="Ram Transfer Speed (Baseline)")
        st.write("Target Pre-Heat Duration (p): **Standard**")
        st.progress(0.50, text="Mold Tool Temp Gradient (Baseline)")

# --- ROW 3: SIMULATED TERMINAL LOG ---
st.divider()
st.markdown("### 🖥️ Edge AI Sub-Routine Logs")

current_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]

log_content = f"""[SYS.TIME] {current_time} | SECS/GEM connection verified.
[INFERENCE] Ingesting multi-node tensor: [{z_axis}, {impact_vel}, {bond_force}, {ultrasonic}, {pad_temp}, {efo}]
[MODEL] Applying INT8 Quantized weights... Latency: {latency_ms:.2f}ms.
[PHYSICS_LAYER] Computing generalized fluid dynamic drag... 
[OUTPUT] Structural Vulnerability Index (SVI) computed at {svi_score:.2f}.
"""

if svi_score > threshold:
    log_content += "[ACTUATION] Threshold breached. Transmitting feed-forward velocity reduction to Machine B Logic Controller via API...\n[ACTUATION] Signal acknowledged. Modulating density parameters."
else:
    log_content += "[ACTUATION] Passing parameters. Maintaining Machine B baseline recipe."

st.markdown(f'<div class="terminal-box">{log_content}</div>', unsafe_allow_html=True)
