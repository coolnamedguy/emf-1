import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# إعداد عنوان صفحة الويب
st.title('Interactive Model: Uniformly Charged Sphere (Gauss Law)')
st.write("غير قيم نصف قطر الكرة (a) ونقطة القياس (r) ولاحظ التغير بكثافة الفيض الكهربائي (D).")

# إضافة أشرطة التمرير (Sliders) في واجهة الويب
a = st.slider('Sphere Radius (a)', min_value=0.1, max_value=5.0, value=2.0, step=0.1)
r_point = st.slider('Observation Point (r)', min_value=0.1, max_value=10.0, value=1.0, step=0.1)
rho_0 = 1.0  # فرضنا كثافة الشحنة 1 لتبسيط الرسم

# دالة حساب كثافة الفيض
def calculate_D(r, a, rho_0):
    if r <= a:
        return (r * rho_0) / 3
    else:
        return (a**3 * rho_0) / (3 * r**2)

# إعداد الرسم البياني
fig, ax = plt.subplots(figsize=(8, 5))
r_vals = np.linspace(0.1, 10, 500)
D_vals = [calculate_D(rv, a, rho_0) for rv in r_vals]

# رسم المنحنى
ax.plot(r_vals, D_vals, lw=2, color='blue', label='Electric Flux Density (D)')

# رسم النقطة الحالية
current_D = calculate_D(r_point, a, rho_0)
ax.plot(r_point, current_D, 'ro', markersize=8, label=f'r = {r_point}, D = {current_D:.2f}')

# تنسيق المخطط
ax.set_xlim(0, 10)
ax.set_ylim(0, max(D_vals) + 0.2)
ax.set_xlabel('Distance (r)')
ax.set_ylabel('Electric Flux Density (D)')
ax.grid(True)
ax.legend()

# عرض المخطط في واجهة Streamlit
st.pyplot(fig)
