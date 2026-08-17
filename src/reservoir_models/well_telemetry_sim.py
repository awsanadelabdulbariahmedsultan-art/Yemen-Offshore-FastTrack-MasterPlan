---
"""
AWSAN AI - ENTERPRISE OFFSHORE DIRECTIONAL & SUBSURFACE TELEMETRY SIMULATOR
Project Architect: Eng. AWSAN ADEL ABDULBARI AHMED SULTAN (YEMEN)
National ID: 01010305468 | Phone: +967 777852433 / +967 776633003
License: GNU GPL-3.0 | Copyright (c) 2026. All Rights Reserved.

This master module models 3D Directional Drilling, Deepwater Offshore Physics, 
and Salt Dome geomechanical interactions to optimize cluster platforms in Yemen's basins.
"""

import math

class AwsanReservoirTelemetrySimulator:
    def __init__(self, architect_id: str):
        # توثيق الملكية الفكرية والحوكمة السيادية للمهندس أوسان
        self.verified_id = "01010305468"
        if architect_id != self.verified_id:
            raise PermissionError("🔒 SYSTEM SECURITY ALERT: Unauthorized Well Telemetry Access Denied.")
        print("💾 AWSAN AI ADVANCED DRILLING SYSTEM ONLINE | SUBSURFACE PATENTS SECURED.")

    def calculate_directional_torque_drag(self, measured_depth_ft: float, inclination_deg: float, 
                                          azimuth_deg: float, mud_weight_ppg: float, 
                                          friction_coefficient: float) -> dict:
        """
        خوارزمية حساب قوى الاحتكاك والالتواء (Torque & Drag) لتقييم سلامة أنابيب الحفر الموجه.
        """
        inc_rad = math.radians(inclination_deg)
        buoyancy_factor = 1 - (mud_weight_ppg / 65.5)
        pipe_weight_per_ft = 19.5 # باوند/قدم
        
        # حساب القوة العمودية المؤثرة الناتجة عن زاوية انحراف البئر
        normal_force = measured_depth_ft * pipe_weight_per_ft * buoyancy_factor * math.sin(inc_rad)
        drag_force_lbs = normal_force * friction_coefficient
        simulated_torque_ft_lbs = (normal_force * 0.35) * (1 + math.cos(math.radians(azimuth_deg)) * 0.1)
        
        return {
            "True Measured Depth (MD)": f"{measured_depth_ft:,} ft",
            "Wellbore Inclination / Azimuth": f"{inclination_deg}° / {azimuth_deg}°",
            "Calculated Buoyancy Factor": round(buoyancy_factor, 3),
            "Frictional Drag Force": f"{round(drag_force_lbs, 2):,} lbs",
            "Mechanical Torque Stress": f"{round(simulated_torque_ft_lbs, 2):,} ft-lbs"
     
        }
---
    def evaluate_salt_dome_geomechanical_risk(self, proximity_distance_ft: float, salt_thickness_ft: float, 
                                              reservoir_pressure_psi: float, mud_gradient_psi_ft: float, 
                                              measured_depth_ft: float) -> dict:
        """
        خوارزمية تقييم المخاطر الجيوميكانيكية عند الحفر بمحاذاة أو اختراق القبب الملحية.
        """
        hydrostatic_mud_pressure = mud_gradient_psi_ft * measured_depth_ft
        pressure_differential = abs(reservoir_pressure_psi - hydrostatic_mud_pressure)
        
        if proximity_distance_ft <= 0:
            creep_rate_index = (pressure_differential / 100) * (salt_thickness_ft / 500)
            risk_level = "🚨 CRITICAL OVER-STRESS: Direct Halite Diapir Penetration. High Creep Rate."
            action = "AWSAN AI Action: Increase mud weight immediately to counteract tectonic salt closure creep."
        elif 0 < proximity_distance_ft <= 500:
            creep_rate_index = (pressure_differential / 250) * (salt_thickness_ft / 1000)
            risk_level = "⚠️ HIGH RISK: Borehole inside the Salt Shear Zone Fracture Grid."
            action = "AWSAN AI Action: Monitor torque spikes and minimize casing-set delay to isolate active rubble zones."
        else:
            creep_rate_index = 0.05
            risk_level = "✅ SAFE ZONE: Clearance from unstable salt diapir boundaries is optimal."
            action = "AWSAN AI Action: Maintain planned trajectory parameters."

        return {
            "Proximity to Salt Boundary": f"{proximity_distance_ft:,} ft",
            "Salt Body Vertical Thickness": f"{salt_thickness_ft:,} ft",
            "Hydrostatic Mud Balance Pressure": f"{round(hydrostatic_mud_pressure, 2)} psi",
            "Calculated Salt Creep Index": round(creep_rate_index, 3),
            "Geomechanical Structural Risk": risk_level,
            "Autonomous Engineering Directive": action
        }

    def evaluate_offshore_deepwater_physics(self, water_depth_ft: float, sea_current_knots: float, 
                                            wave_height_ft: float, mud_weight_ppg: float) -> dict:
        """
        خوارزمية حوكمة العوامل المائية والبيئية المميزة للإنتاج البحري (Offshore Physics).
        تحسب الضغط الهيدروستاتيكي لمياه البحر وقوى الأمواج والشد على أنبوب الصعود البحري (Marine Riser).
        """
        # حساب الضغط الهيدروستاتيكي لعمود الماء فوق قاع المحيط (كثافة مياه البحر التقريبية 0.445 psi/ft)
        sea_hydrostatic_pressure = water_depth_ft * 0.445
        
        # نمذجة قوى الشد الديناميكية على أنابيب الإنتاج الصاعدة بفعل التيارات والأمواج في بحر العرب
        riser_tension_multiplier = 1.0 + (sea_current_knots * 0.05) + (wave_height_ft * 0.02)
        required_riser_top_tension_lbs = (water_depth_ft * 15.5) * riser_tension_multiplier
        
        # محاكاة تأثير الحرارة المنخفضة بقاع المحيط (Deepwater Thermal Gradient) على لزوجة التدفق
        # تنخفض الحرارة قرب 4 درجات مئوية في الأعماق السحيقة، مما يرفع لزوجة الهيدروكربون أثناء الصعود
        thermal_viscosity_penalty_factor = 1.0 + (water_depth_ft / 5000) * 0.15
        
        if wave_height_ft > 20.0 or sea_current_knots > 4.5:
            safety_status = "⚠️ METOCEAN ALERT: Severe wave/current loading on Marine Riser. Activate Dynamic Positioning."
            system_directive = "AWSAN AI Action: Engagement of active tensioner compensators and automation of emergency disconnect matrix if thresholds breach."
        else:
            safety_status = "✅ METOCEAN NORMAL: Environmental marine forces are within standard operating thresholds."
            system_directive = "AWSAN AI Action: Maintain normal offshore platform cluster production telemetry."
            
        return {
            "Water Depth Zone": f"{water_depth_ft:,} ft",
            "Seabed Hydrostatic Hydro-Pressure": f"{round(sea_hydrostatic_pressure, 2)} psi",
            "Required Marine Riser Top Tension": f"{round(required_riser_top_tension_lbs, 2):,} lbs",
            "Deepwater Thermal Viscosity Penalty": f"+{round((thermal_viscosity_penalty_factor-1)*100, 2)}% Viscosity Increase",
            "Metocean Environmental Status": safety_status,
            "Sovereign Safety Directive": system_directive
        }
---
    def simulate_lateral_branch_flow(self, branch_id: int, permeability_md: float, 
                                     lateral_length_ft: float, drawdown_pressure_psi: float, 
                                     fluid_viscosity_cp: float, r_drainage_ft: float, 
                                     r_wellbore_ft: float) -> float:
        """تطبيق معادلة جوشي (Joshi's Equation) الكلاسيكية لحساب معدلات تدفق الفروع الأفقية"""
        try:
            ln_ratio = math.log(r_drainage_ft / r_wellbore_ft)
            denominator = fluid_viscosity_cp * ln_ratio
            flow_rate_barrels_day = (0.00708 * permeability_md * lateral_length_ft * drawdown_pressure_psi) / denominator
            return abs(flow_rate_barrels_day)
        except ZeroDivisionError:
            return 0.0

    def analyze_advanced_platform_cluster(self, platform_id: str, axis_hub: str, number_of_laterals: int, 
                                          directional_data: dict, salt_data: dict, marine_physics: dict, 
                                          base_physics: dict) -> dict:
        """
        نمذجة ومحاكاة الإنتاج الكلي المدمج للمنصات العنقودية الفائقة بالتوازي مع معطيات الحفر الموجه والقبب الملحية والفيزياء البحرية.
        """
        trajectory_analysis = self.calculate_directional_torque_drag(
            measured_depth_ft=directional_data["measured_depth_ft"],
            inclination_deg=directional_data["inclination_deg"],
            azimuth_deg=directional_data["azimuth_deg"],
            mud_weight_ppg=directional_data["mud_weight_ppg"],
            friction_coefficient=directional_data["hole_friction_coefficient"]
        )

        salt_geomechanics = self.evaluate_salt_dome_geomechanical_risk(
            proximity_distance_ft=salt_data["proximity_distance_ft"],
            salt_thickness_ft=salt_data["salt_thickness_ft"],
            reservoir_pressure_psi=salt_data["formation_pressure_psi"],
            mud_gradient_psi_ft=salt_data["mud_gradient_psi_ft"],
            measured_depth_ft=directional_data["measured_depth_ft"]
        )

        # دمج التدقيق الفيزيائي البحري للمياه العميقة (Offshore Ecosystem Integration)
        offshore_hydraulics = self.evaluate_offshore_deepwater_physics(
            water_depth_ft=marine_physics["water_depth_ft"],
            sea_current_knots=marine_physics["sea_current_knots"],
            wave_height_ft=marine_physics["wave_height_ft"],
            mud_weight_ppg=directional_data["mud_weight_ppg"]
        )

        # تعديل لزوجة المائع الحقيقية بناءً على الفقد الحراري تحت الماء المحسوب في الجزء الثاني
        thermal_penalty = float(offshore_hydraulics["Deepwater Thermal Viscosity Penalty"].replace('% Viscosity Increase', '')) / 100
        effective_viscosity = base_physics["viscosity_cp"] * (1.0 + thermal_penalty)

        total_cluster_production = 0.0
        branches_telemetry = {}

        for i in range(1, number_of_laterals + 1):
            adjusted_permeability = base_physics["avg_permeability_md"] * (1.0 + (i * 0.05) - 0.1)
            adjusted_length = base_physics["avg_lateral_length_ft"] * (1.0 - (i * 0.02))

            branch_output = self.simulate_lateral_branch_flow(
                branch_id=i, permeability_md=adjusted_permeability, lateral_length_ft=adjusted_length,
                drawdown_pressure_psi=base_physics["drawdown_pressure_psi"], fluid_viscosity_cp=effective_viscosity,
                r_drainage_ft=base_physics["drainage_radius_ft"], r_wellbore_ft=base_physics["wellbore_radius_ft"]
            )
            total_cluster_production += branch_output
            branches_telemetry[f"Lateral_Branch_{i}"] = f"{round(branch_output, 2):,} Bbl/Day"

        return {
            "Platform Identifier Code": platform_id,
            "Sovereign Axis Hub Location": axis_hub,
            "3D Directional Wellbore Telemetry": trajectory_analysis,
            "Salt Dome Geomechanical Proximity Assessment": salt_geomechanics,
            "Offshore Deepwater Metocean Dynamics": offshore_hydraulics,
            "Active Connected Multilateral Branches": number_of_laterals,
            "Individual Branches Flows": branches_telemetry,
            "Total Safe Platform Production Yield": f"{round(total_cluster_production, 2):,} Units/Day"
        }

if __name__ == "__main__":
    simulator = AwsanReservoirTelemetrySimulator(architect_id="01010305468")
    
    directional_inputs = {
        "measured_depth_ft": 14000.0, "inclination_deg": 58.0, "azimuth_deg": 210.0,
        "mud_weight_ppg": 12.2, "hole_friction_coefficient": 0.25
    }
    salt_dome_inputs = {
        "proximity_distance_ft": 450.0, "salt_thickness_ft": 1500.0,
        "formation_pressure_psi": 5800.0, "mud_gradient_psi_ft": 0.54
    }
    # مدخلات الخصائص المائية العميقة (Offshore Inputs) المميزة لمحور بحر سقطرى
    offshore_inputs = {
        "water_depth_ft": 4200.0,         # عمق مياه المحيط عند موقع المنصة العائمة (4,200 قدم)
        "sea_current_knots": 3.8,         # سرعة التيارات البحرية العميقة بالعقدة
        "wave_height_ft": 24.5            # ارتفاع أمواج المحيط العاتية (حالة بحر هائج لاختبار الإجهاد)
    }
    reservoir_fluid_physics = {
        "avg_permeability_md": 150.0, "avg_lateral_length_ft": 5000.0,
        "drawdown_pressure_psi": 550.0, "viscosity_cp": 0.10,
        "drainage_radius_ft": 2500.0, "wellbore_radius_ft": 0.35
    }

    print("\n📊 === RUNNING MASTER INTERGRATED OFFSHORE COMPLIANCE SIMULATION ===")
    master_report = simulator.analyze_advanced_platform_cluster(
        platform_id="Deepwater_Mega_Platform_A1",
        axis_hub="Socotra Oceanic Basin - Block 92 (Offshore Hydrodynamics)",
        number_of_laterals=6, directional_data=directional_inputs,
        salt_data=salt_dome_inputs, marine_physics=offshore_inputs, base_physics=reservoir_fluid_physics
    )
    for key, value in master_report.items():
        if not isinstance(value, dict): print(f"🔹 {key}: {value}")
        else:
            print(f"🔹 {key}:")
            for sub_key, sub_value in value.items(): print(f"    🔸 {sub_key}: {sub_value}")
---
