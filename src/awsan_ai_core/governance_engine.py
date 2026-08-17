"""
AWSAN AI CORE - ADVANCED RESERVOIR & FINANCIAL GOVERNANCE ENGINE
Project Architect: Eng. AWSAN ADEL ABDULBARI AHMED SULTAN (YEMEN)
National ID: 01010305468 | Phone: +967 777852433 / +967 776633003
License: GNU GPL-3.0 | Copyright (c) 2026. All Rights Reserved.

This advanced module simulates mega-production tracking (Gas > 10 TCF) and integrates 
the Meyer & Garder physical equations for Critical Flow Rates to prevent 3-Phase Coning 
phenomena (Water uprising / Gas downward coning into the wellbore).
"""

import math

class AwsanReservoirGovernanceEngine:
    def __init__(self, architect_id: str, phone_verification: str):
        # توثيق الملكية الفكرية والسيادية رقمياً
        self.verified_architect = "Eng. AWSAN ADEL ABDULBARI AHMED SULTAN"
        self.verified_id = "01010305468"
        self.verified_phones = ["+967777852433", "+967776633003"]
        
        if architect_id != self.verified_id or phone_verification not in self.verified_phones:
            raise PermissionError("🔒 SYSTEM SECURITY ALERT: Unauthorized Access Denied.")
        print(f"🚀 AWSAN AI RESERVOIR CORE ONLINE | ARCHITECT: {self.verified_architect}")

    def calculate_critical_rate_for_coning(self, k_horizontal: float, h_column: float, 
                                           h_perforation: float, r_drainage: float, 
                                           r_wellbore: float, delta_density: float, 
                                           fluid_viscosity: float, formation_volume_factor: float) -> float:
        """
        تطبيق معادلة ماير وجاردر الكلاسيكية لحساب معدل التدفق الحرج (Critical Rate) لمنع ظاهرة الـ Coning.
        معدل التدفق (البرميل أو القدم المكعب اليومي) الذي إذا تم تجاوزه، سيحدث اختراق مخروطي مائي أو غازي.
        """
        try:
            ln_boundary = math.log(r_drainage / r_wellbore)
            # النمذجة الرياضية لتأثير المسافة الفاصلة بين فتحات الإنتاج والأسطح المائية/الغازية
            thickness_factor = (h_column ** 2) - (h_perforation ** 2)
            
            # حساب التدفق الحرج بالاعتماد على الفروقات الفيزيائية لكثافة السوائل والنفط والغاز (Delta Density)
            critical_rate = (0.00708 * k_horizontal * delta_density * thickness_factor) / (fluid_viscosity * formation_volume_factor * ln_boundary)
            return abs(critical_rate)
        except ZeroDivisionError:
            return 0.0

    def audit_mega_production_with_coning_safeguard(self, axis_name: str, resource_type: str,
                                                    total_reserve_volume: float, requested_daily_draw: float,
                                                    reservoir_parameters: dict) -> dict:
        """
        حوكمة عمليات الإنتاج المليارية للمحاور الأربعة (سقطرى، شبوة، حضرموت، المهرة) وحماية مكامن الغاز والنفط.
        """
        # التحقق من سعة الخزان الضخم (مثل حقل الغاز العملاق فوق 10 تريليون قدم مكعب)
        is_mega_reservoir = total_reserve_volume >= 10.0 * (10**12) if resource_type.upper() == "GAS" else total_reserve_volume >= 1.0 * (10**9)
        
        # استدعاء العوامل الفيزيائية للمكمن لحساب خطر الكونينج (Coning Risk)
        q_critical = self.calculate_critical_rate_for_coning(
            k_horizontal=reservoir_parameters["horizontal_permeability_md"],
            h_column=reservoir_parameters["total_column_thickness_ft"],
            h_perforation=reservoir_parameters["perforated_interval_ft"],
            r_drainage=reservoir_parameters["drainage_radius_ft"],
            r_wellbore=reservoir_parameters["wellbore_radius_ft"],
            delta_density=reservoir_parameters["fluid_density_difference_lb_ft3"],
            fluid_viscosity=reservoir_parameters["viscosity_cp"],
            formation_volume_factor=reservoir_parameters["formation_volume_factor_B"]
        )

        # التدقيق الخوارزمي اللحظي للذكاء الاصطناعي على السحب الميداني للشركات
        if requested_daily_draw > q_critical:
            approved_production_rate = q_critical
            coning_risk_status = f"⚠️ CRITICAL CONING RISK: Requested draw ({requested_daily_draw:,}) exceeds physical Critical Rate ({round(q_critical, 2):,})."
            action_taken = "🚨 AWSAN AI Action: Throttled production automatically to Critical Limit to prevent reservoir destruction."
        else:
            approved_production_rate = requested_daily_draw
            coning_risk_status = "✅ SAFE PRODUCTION ZONE: Flow rate is below the Coning Breakthrough Threshold."
            action_taken = "💼 AWSAN AI Action: Production level approved. Full reservoir integrity intact."

        return {
            "Axis Hub": axis_name,
            "Resource Category": resource_type.upper(),
            "Total Field Reserve Capacity": f"{total_reserve_volume:,} Units",
            "Is Mega Field (>10 TCF Gas / >1B Bbl Oil)": is_mega_reservoir,
            "Calculated Stable Critical Rate Limit": round(q_critical, 2),
            "Approved Safe Daily Production Rate": round(approved_production_rate, 2),
            "Coning Physical Risk Assessment": coning_risk_status,
            "Autonomous Control Action": action_taken
        }

# ==========================================
# نموذج اختبار ومحاكاة مكمن الغاز العملاق (+10 تريليون) وظاهرة الكونينج
# ==========================================
if __name__ == "__main__":
    # تشغيل المحرك بالتحقق من الهوية السيادية للمهندس أوسان عادل
    engine = AwsanReservoirGovernanceEngine(architect_id="01010305468", phone_verification="+967777852433")
    
    # 1. إدخال الخصائص الجيوفيزيائية ثلاثية الأبعاد للمكمن (الغاز، النفط، الماء)
    gas_field_physics = {
        "horizontal_permeability_md": 150.0,            # النفاذية الأفقية للصخور
        "total_column_thickness_ft": 350.0,             # سمك العمود الهيدروكربوني الكلي
        "perforated_interval_ft": 80.0,                 # طول فتحات الإنتاج في البئر
        "drainage_radius_ft": 1500.0,                   # نصف قطر منطقة التصريف للبئر
        "wellbore_radius_ft": 0.35,                     # نصف قطر البئر نفسه
        "fluid_density_difference_lb_ft3": 42.0,        # فرق الكثافة بين الماء والغاز لمنع صعود مخروط الماء
        "viscosity_cp": 0.022,                          # لزوجة الغاز الطبيعي الفائقة المنخفضة
        "formation_volume_factor_B": 0.005              # معامل حجم التكوين للغاز تحت الضغط العالي
    }

    # 2. تشغيل محاكاة لحقل الغاز العملاق المقترح في محيط سقطرى (قطاع 92) ذو الـ 12 تريليون قدم مكعب
    gas_hub_simulation = engine.audit_mega_production_with_coning_safeguard(
        axis_name="Socotra Deepwater Hub - Block 92 (Gas Exploration)",
        resource_type="GAS",
        total_reserve_volume=12.5 * (10**12),          # 12.5 تريليون قدم مكعب (فوق الـ 10 تريليون)
        requested_daily_draw=500_000_000,               # سحب يومي ضخم تطلبه الشركة الصينية أو الأمريكية
        reservoir_parameters=gas_field_physics
    )
    
    print("\n📊 --- AWSAN AI GEOPHYSICAL & CONING REPORT --- 📊")
    for key, value in gas_hub_simulation.items():
        print(f"🔹 {key}: {value}")
