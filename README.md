# 🌍 Energy-Efficient Design of Geothermal Heat Exchanger for Thermal Performance Analysis
---

## 📌 Problem Statement

Geothermal heat exchangers (HEX) play a critical role in sustainable heating and cooling systems by utilizing underground thermal energy. However, suboptimal geometric configurations can lead to inefficiencies such as poor heat transfer, increased fouling, and higher pumping requirements. The geometry of the double helical coil—particularly the pitch-to-diameter (p/D) ratio—has a significant impact on performance, yet is often poorly optimized in commercial applications.

---

## 💡 Objective

To identify the optimal **Pitch/Coil Diameter (p/D) ratio** for a **Double Helical Geothermal Heat Exchanger** loop to maximize heat transfer efficiency using both simulation and analytical methods.

---

## 🛠️ Methodology

- **Literature Review**
  - Surveyed previous work to understand the influence of geometry on thermal performance and flow behavior.
  - Narrowed down relevant p/D ratios and boundary conditions.

- **CAD Modeling**
  - Designed double helical coil heat exchanger using SolidWorks with accurate dimensions for parametric testing.

- **CFD Simulation**
  - Used ANSYS Fluent for steady-state thermal-fluid analysis across various p/D values.
  - Applied constant wall temperature and mass flow inlet boundary conditions.

- **Analytical Evaluation**
  - Created a Python script to compute the heat transfer rate ( Q = dot{m} C_p (T_{out} - T_{in}) ) and plotted Q vs p/D.

- **Validation**
  - Compared results from ANSYS simulations and analytical calculations to ensure consistency.

---

## 📊 Results & Conclusion

- The optimal **p/D ratio was found to be < 2.5**, delivering superior outlet temperatures and heat transfer rates.
- Analytical and simulation results aligned closely, validating the computational approach.
- Recommendations for future work include simulating longer pipe lengths using high-performance computing and assessing the contribution of inner coil flow to secondary heat transfer effects.

---
