"""
AWSAN AI - ADVANCED MULTI-LATERAL RESERVOIR TELEMETRY SIMULATOR
Project Architect: Eng. AWSAN ADEL ABDULBARI AHMED SULTAN (YEMEN)
National ID: 01010305468 | Phone: +967 777852433 / +967 776633003
License: GNU GPL-3.0 | Copyright (c) 2026. All Rights Reserved.

This module simulates physical hydrodynamics, localized drawdown, and multi-branch 
production modeling for advanced cluster platforms across Yemen's main basins.
"""

import math

class AwsanReservoirTelemetrySimulator:
    def __init__(self, architect_id: str):
        self.verified_id = "01010305468"
        if architect_id != self.verified_id:
            raise PermissionError("🔒 SYSTEM SECURITY ALERT: Unauthorized Well Telemetry Access.")
        print("💾 AWSAN AI WELL TELEMETRY MODULE ACTIVATED | SUBSURFACE PATENTS SECURED.")

    def simulate_lateral_branch_flow(self, branch_id: int, permeability_md: float, 
                                     lateral_length_ft: float, drawdown_pressure_psi: float, 
                                     fluid_viscosity_cp: float, r_drainage_ft: float, 
                                     r_wellbore_ft: float) -> float:
        """
        تطبيق معادلة "جوشي" (Joshi's Equation) الشهيرة لحساب معدل التدفق من فرع أفقي ممتد.
        """
        try:
            # حساب المعاملات الهندسية للتدفق الأفقي والمحيط البيضاوي للتصريف
            ln_ratio = math.log(r_drainage_ft / r_wellbore_ft)
            denominator = fluid_viscosity_cp * ln_ratio
            
            # حساب التدفق الأساسي بالاعتماد على طول الفرع الممتد (Lateral Length) والنفاذية الصخرية
            flow_rate_barrels_day = (0.00708 * permeability_md * lateral_length_ft * drawdown_pressure_psi) / denominator
            return abs(flow_rate_barrels_day)
        except ZeroDivisionError:
            return 0.0

    def analyze_platform_multilateral_cluster(self, platform_id: str, axis_hub: str, 
                                              number_of_laterals: int, base_physics: dict) -> dict:
        """
        نمذجة ومحاكاة الإنتاج الكلي المتوازي لمنصة واحدة تتفرع منها آبار متعددة الفروع.
        """
        total_cluster_production = 0.0
        branches_telemetry = {}

        # محاكاة وحساب الإنتاج المنفصل لكل فرع أفقي ينطلق من المنصة البحرية/البرية
        for i in range(1, number_of_laterals + 1):
            # إضافة تفاوت جيولوجي طفيف محاكي لطبيعة الطبقات الصخرية لكل فرع (Variability)
            adjusted_permeability = base_physics["avg_permeability_md"] * (1.0 + (i * 0.05) - 0.1)
            adjusted_length = base_physics["avg_lateral_length_ft"] * (1.0 - (i * 0.02))

            branch_output = self.simulate_lateral_branch_flow(
                branch_id=i,
                permeability_md=adjusted_permeability,
                lateral_length_ft=adjusted_length,
                drawdown_pressure_psi=base_physics["drawdown_pressure_psi"],
                fluid_viscosity_cp=base_physics["viscosity_cp"],
                r_drainage_ft=base_physics["drainage_radius_ft"],
                r_wellbore_ft=base_physics["wellbore_radius_ft"]
            )
            
            total_cluster_production += branch_output
            branches_telemetry[f"Branch_{i}_Output"] = f"{round(branch_output, 2):,} Units/Day"

        # تقييم الكفاءة الهيدروليكية ومنع الضغط الزائد لتجنب مشاكل المكامن
        avg_output_per_lateral = total_cluster_production / number_of_laterals
        integrity_status = "✅ OPTIMAL HYDRAULIC PRESSURE: Lateral flow rates are balancing stresses." if avg_output_per_lateral < 15000 \
                           else "⚠️ HIGH RESERVOIR DRAWDOWN: Structural stress detected. Recommend choke adjustments."

        return {
            "Platform Identifier": platform_id,
            "Sovereign Axis Hub": axis_hub,
            "Active Multilateral Branches Connected": number_of_laterals,
            "Individual Branches Output Telemetry": branches_telemetry,
            "Total Combined Platform Production": f"{round(total_cluster_production, 2):,} Units/Day",
            "Makin Structural Integrity Status": integrity_status
        }

if __name__ == "__main__":
    simulator = AwsanReservoirTelemetrySimulator(architect_id="01010305468")
    
    # محاكاة خصائص مكمن الغاز والنفط لمنصة بحرية متطورة في حوض سقطرى
    platform_cluster_physics = {
        "avg_permeability_md": 120.0,       # متوسط نفاذية صخور الحقل
        "avg_lateral_length_ft": 4000.0,    # طول الامتداد الأفقي لكل فرع (4000 قدم)
        "drawdown_pressure_psi": 450.0,     # فرق الضغط المفروض للسحب
        "viscosity_cp": 0.15,               # لزوجة المائع في هذه الطبقة
        "drainage_radius_ft": 2000.0,       # نصف قطر تصريف المكمن
        "wellbore_radius_ft": 0.35          # نصف قطر البئر
    }

    # تشغيل محاكاة لمنصة غاز ريادية (Platform-A1) تتفرع منها 6 مسارات أفقية
    print("\n--- 🔋 RUNNING MULTI-LATERAL WELL TELEMETRY SIMULATION ---")
    platform_report = simulator.analyze_platform_multilateral_cluster(
        platform_id="Platform_A1_Gas",
        axis_hub="Socotra Offshore Hub - Block 92",
        number_of_laterals=6, # 6 أفرع محفورة من نفس المنصة لتعظيم الكفاءة
        base_physics=platform_cluster_physics
    )
    for k, v in platform_report.items():
        if k != "Individual Branches Output Telemetry":
            print(f"🔹 {k}: {v}")
        else:
            print(f"🔹 {k}:")
            for b_name, b_val in v.items(): print(f"    🔸 {b_name}: {b_val}")
