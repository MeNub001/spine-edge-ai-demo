# 🧠 Project S.P.I.N.E.
**Sequential Process Intelligence & Networked Evaluation**

*Developed for the Micron x ESUM Case Study Competition 2026 by Team UTP Teletubbies.*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/) ## 🏭 Overview
In high-density semiconductor packaging, **"wire sweep"** is a critical reliability failure where the viscous flow of epoxy molding compound deforms delicate interconnect wires. Historically, this has been detected retroactively, violating the manufacturing "Rule of 10" and resulting in massive sunk costs.

Project S.P.I.N.E. introduces a paradigm shift from reactive Statistical Process Control (SPC) to proactive, closed-loop **Advanced Process Control (APC)**. 

By establishing a "Digital Thread" between upstream wire bonding (Machine A) and downstream encapsulation (Machine B), S.P.I.N.E. utilizes Edge AI to detect **Micro-Variance Collisions** in real-time, mathematically modulating downstream fluid dynamics to prevent the defect before the epoxy cures.

## 🚀 Core Architecture
1. **Telemetry Acquisition:** Ingests high-frequency SECS/GEM time-series data from upstream machinery without disrupting nominal operations.
2. **Multivariate Edge AI Processor:** Utilizes an 8-bit quantized Physics-Informed Neural Network (PINN) and Temporal Convolutional Networks (TCN) to compute a Structural Vulnerability Index (SVI).
3. **Dynamic Actuation API:** Operates within a strict sub-50ms latency window to transmit feed-forward parameter modulations (velocity $v$ and density $\rho$) to the downstream Encapsulator, mitigating viscous drag forces.

## 💻 The Dashboard Demonstration
This repository contains the interactive Streamlit dashboard designed to simulate the S.P.I.N.E. Edge Command Center. It allows operators (and judges) to manually inject telemetry overrides and watch the predictive SVI model execute downstream actuations in real-time.

### Features
* **Live Telemetry Injection:** Adjust kinematic, mechanical, and thermal parameters to simulate physically weak wire bonds.
* **Real-Time SVI Computation:** Watch the Physics-Informed Neural Network dynamically calculate structural risk.
* **Automated Actuation Protocol:** Observe the system automatically throttle ram transfer speeds and extend pellet pre-heat durations when the SVI threshold is breached.
* **Simulated Edge Terminal:** Features a live, timestamped event log tracking inference latency and API handshakes.

## 🛠️ Installation & Usage

### Prerequisites
Ensure you have Python 3.8+ installed. 

### Local Setup
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/YourUsername/spine-edge-ai-demo.git](https://github.com/YourUsername/spine-edge-ai-demo.git)
   cd spine-edge-ai-demo
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the Edge Command Center:
   ```bash
   streamlit run spine_app.py
   ```
   *The dashboard will automatically open in your default web browser at `http://localhost:8501`.*

## 👥 Team: UTP Teletubbies
* **Geoffrey Lee Jin Yau** * **Kelvin Law Yun Hong** * **Ng Yao Yang** * **Nicholas Tan Hong Junn** *Universiti Teknologi PETRONAS (UTP) - Faculty of Engineering*
```
