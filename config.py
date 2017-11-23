
import re
import sys

from project import *
import project.dti as DTI
import project.f_m as F_M

Setting(name = 'APP_NUMBER_OF_INJECTORS_CPV', value = '4')
Setting(name = 'P_L_INJ_NUMBER_OF_BANKS_CPV', value = '2')
Setting(name = 'APP_NUMBER_OF_ACCEL_CPV', value = '2')
Setting(name = 'I_C_ACC_NUMBER_MDP_ZONE_CPV', value = '4')
Setting(name = 'ESM_ADC_SAFETY_NUMBER_CPV', value = '1')

Setting(name = 'PROJECT_NUMBER', value = 'SG7513')

# Include file paths
Setting(name = 'CPPPATH', value = AsList('''
gill_dcm624_code/Software/include
hwi_vob/hwi/hwi_core/src
hwi_vob/hwi/hwi_tpu/src
blois_soft_vob/Software/S_S/s_s_lib/src
src/appli/rtw/src
'''))

# Force include files
Setting(name = 'CPPAUTOINC', value = AsList('''
hwi_memory_section.h
'''))

# C pre-processor macro definitions
Setting(name = 'CPPDEFINES', value = AsList('''
MKF_SW_ID=$PACKAGE
_HWI_BASE_
INTEGER_CODE
NO_FLOATS
$PROJECT_NUMBER
_NO_I_C_SPC_RPC_LP_DEMAND_CALC
S_S_STARTEND_MEASURE=1
'''))

# Source file attribute list
# Files have a field name which is compulsory
# optional fields include
# CCFLAGS which are file specific compiler flags
# CC_TYPE which is the file type in clearcase branches, e.g spec, project, hwi
# this is used to check if there are possible bug fixes available for spec files etc.
# CC_TYPE is a flag to potentially use for version control branch analysis
# CCFLAGS adds the ability to append to the standard compiler flags, either singular or multiple list items

# Autocode Information (library, additional paths
Setting(name = 'AUT_LIB_PATH', value = '../../tcg_misc_tool_vob/tools/autocode/lib')
Setting(name = 'AUT_ADD_PATH', value = '../../tcg_misc_tool_vob/tools/autocode/lib;../../tcg_misc_tool_vob/tools/autocode/lib/reactis;../../tcg_misc_tool_vob/tools/autocode/lib/reactis/create_reactis_suite\Debug')
Setting(name = 'AUT_REPORT_PATH', value = '../5_sw_design/appli/_appli/doc')
Setting(name = 'AUT_DDTOOLS_PATH', value = '../../tcg_misc_tool_vob/tools/autocode/dd_tools')
xmlFile('../5_sw_design/appli/_appli/doc/types.xml')

# Below are applciation settings from the project file which we require auto constructed
# t55 entries for

# This configuration file...
ProjectFile(re.match('(.*\.py).*', __file__).group(1), OWNER='gillingham',
            description = 'Project configuration file.')
#
#   Build tools
#

ProjectFile('build.bat', OWNER = 'gillingham',
            description = 'Top-level build batch file.',
            notes = 'Use this to build the project.')
ProjectFile('blois_soft_vob/Software/S_S/s_s_scheduler/src/s_s_scheduler.pl', OWNER = 'gillingham',
            description = 'Scheduler generation script. Converts tasklist.asc to source code.',
            notes       = 'Gillingham implementation to allow specification of output directory')
ProjectFile('blois_soft_vob/Software/Environnement/exe/ddump.exe', OWNER = 'blois',
            description = 'Used to extract symbol information from the elf file.')
ProjectFile('blois_soft_vob/Software/Environnement/exe/Header_A2L.txt', OWNER = 'gillingham',
            description = 'ASAP2 file header text')
ProjectFile('blois_soft_vob/Software/Environnement/exe/asap2.pl', OWNER = 'blois',
            description = 'ASAP2 environment generator')
ProjectFile('blois_soft_vob/Software/Environnement/exe/int2ulp.exe', OWNER = 'blois',
            description = 'ULP generation utility.')
            
#
#   Autogen files
#
ProjectFile('gill_vob/6_coding/autogen/app/app_base.t55', OWNER = 'gillingham',
            description = 'Template for APP autogeneration')
ProjectFile('gill_vob/6_coding/autogen/dti/dti.c', OWNER = 'gillingham',
            description = 'Template for DTI autogeneration')
ProjectFile('gill_vob/6_coding/autogen/dti/dti.h', OWNER = 'gillingham',
            description = 'Template for DTI autogeneration')
ProjectFile('gill_vob/6_coding/autogen/dti/dti.t55', OWNER = 'gillingham',
            description = 'Template for DTI autogeneration')
ProjectFile('gill_vob/6_coding/autogen/f_m/f_m_fault.c', OWNER = 'gillingham',
            description = 'Template for F_M autogeneration')
ProjectFile('gill_vob/6_coding/autogen/f_m/f_m_fault.h', OWNER = 'gillingham',
            description = 'Template for F_M autogeneration')
ProjectFile('gill_vob/6_coding/autogen/f_m/f_m_fault.t55', OWNER = 'gillingham',
            description = 'Template for F_M autogeneration')
            
            
            
#
#   Build tool configuration settings
#

ProjectFile('blois_soft_vob/Software/Environnement/exe/Merge_A2L_List.lst', OWNER = 'gillingham',
            description = 'External A2L file list for ASAP2 generation')
ProjectFile('gill_dcm624_code/Software/S_S/s_s_scheduler/src/tasklist.asc', OWNER = 'gillingham',
            description = 'Scheduler configuration file.')
ProjectFile('hwi_vob/hwi/hwi_core/src/hwi_memory_map.dld', OWNER = 'blois',
            description = 'Project linker file.')
ProjectFile('blois_soft_vob/Software/Environnement/exe/int2ulp.rsp', OWNER = 'blois',
            description = 'Configuration file for ulp generation.')
#
#   Sources
#
SourceFile('blois_code_p_l/p_l/p_l_com/MSG/src/P_L_Cc_Bus_Fault.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/MSG/src/P_L_Cc_Can0_Error.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/MSG/src/P_L_Cc_Can1_Error.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Com_Actuator_Routine.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Com_Clear_Diag_Info.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Com_Cntrl_Dtc_Setting.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Com_Diag_Mngt_Routine.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Com_Ecu_Reset.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Com_Obd_Interface.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Com_Read_Dtc_Info_Frame.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Com_Rst_Jmp_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Uds_Computation_Method.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Uds_Did_Conf_Table.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Uds_Rdbi_Autocode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/OBD/src/P_L_Obd_Mod10.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_com/Misc/src/P_L_Cds_Msg.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])

SourceFile('blois_code_p_l/p_l/p_l_ecu/Misc/src/P_L_Dig_Outp_Cu_Relay_Drv.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_ecu/Misc/src/P_L_Ecu_Case_Temp_Aqui.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_ecu/Misc/src/P_L_Ecu_Hw_Tag_Read.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/SMC/src/P_L_Lp_Relay_Drive.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_ecu/NVM/src/P_L_Nvm_Data.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_ecu/Self_diag/src/P_L_Swt.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Driver/src/P_L_Neutral_Gear_Sw_State.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Amf_Freq_Handler.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Egrh_Feedback_Position.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Batt_Current_Acqu.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Batt_Temp_Acqu.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Engine_Inj_Counter_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Thrtl_Feedback_Position.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Lambda/src/P_L_Wraf_Dfco_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Lambda/src/P_L_Wraf_Global_Condition.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Lambda/src/P_L_Wraf_Interface_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Lambda/src/P_L_Wraf_Plausibility_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Lambda/src/P_L_Wraf_Snapshot_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Px/src/P_L_Atm_Pres_Aquisition.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Px/src/P_L_Baro_Sensor_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Px/src/P_L_Map_Acquisition.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Px/src/P_L_P3_Acquisition.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Px/src/P_L_P3_Processing.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Dpf_In_Temp_Aquisition.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Intake_Plenum_Temp_Aqui.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Inlet_Air_Temp_Deter.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Inlet_Digital_Acq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Inlet_Digital_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Turb_In_Temp_Aquisition.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Vehicle/src/P_L_Battery_Voltage.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_in/Vehicle/src/P_L_Blower_Swith_Input.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/ACM/src/P_L_Egrh_Cool_Bypass_Driver.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Adtrig_Sub_Dec.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Atp1_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Atp2_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Atp3_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Atp4_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Atp5_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Atp6_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Atp7_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Atp8_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Background_2.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Ctp1_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Ctp2_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Ctp3_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Ctp4_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Ctp5_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Ctp6_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Ctp7_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Ctp8_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Fuel_Rate_Sync.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/ICI/src/P_L_Ici_Glow_Plug_Lamp_Out.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/Misc/src/P_L_Electrical_Tests.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_code_p_l/p_l/p_l_out/SAC/src/P_L_Glow_Plug_Diagnosis.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/acm.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Egr_Hp_Vlv_Pos_Ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Egrh_Valve_Power_On.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Egrh_Valve_Antistuck.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Egrh_Valve_Cleaning.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Egr_Hp_Vlv_Learning.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Egr_Hp_Vlv_Run_Learning.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Egr_Hp_Valve_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Egrh_Pos_Ctrl_Sched.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Ext_Pratio_Limit_Corr.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Valve_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Valve_Antistuck.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Valve_Cleaning.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Vlv_Pos_Ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Vlv_Learning.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Valve_Power_On.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Pos_Ctrl_Sched.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/afc/src/afc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/afc/src/AFC_Total_Fuel_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/asm/src/asm.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/asm/src/ASM_Charge_Mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/asm/src/ASM_Diagnostic.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/asm/src/ASM_Performance_Mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/asm/src/ASM_Regulate_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/asm/src/ASM_Soc_Rationality.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/asm/src/ASM_Soc_Refresh.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/c_c/src/c_c.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/c_i/_c_i/src/C_I_Maps.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/c_i/c_i_sec/src/C_I_Sec_Async_Interface.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/c_i/c_i_sec/src/C_I_Sec_Sync_Interface.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Ac_Relay_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/dti_alloc_output_async.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/dti_alloc_output_sync.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/dti_allocate_output_data.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Comp_Test_Begin_Meas.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Comp_Test_End_Meas.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Compression_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Fan_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Fault_Controler.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Fuel_Lift_Pump_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Glow_Plug_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Imv_Buzzing_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Injector_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dpf_Regen_Idle.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dpf_Regen_Key_Req.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/dti_iso_dpf_rgn_veh_run_mod.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Alternator_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Apc_Starting.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/dti_iso_dyn_diag_railp_ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Eol_Imv_Ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/dti_iso_dyn_hydraulic_test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Imv_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Inj_Shut_Off.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Inj_Start_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Injector_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Prim_Rvd_Chk_St.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Prim_Rvd_Tst.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Rpc_Pid_Calib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/dti_iso_dyn_supervisor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Inj_Tst_Cond_Chk.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_State_Machine_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/dti_iso_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Mdp_Upd_Period_Adjust.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Power_Balance_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Starter_Relay_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Vgth_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/dti/src/DTI_Lamp_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Actual_Torque_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Anti_Oscillation_Plau.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Asg_Plausibility.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Battery_Voltage_Mon.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Brake_Plausibility.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Camshaft_Inf_Record.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Can_J1939_Rxdiag_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Control_Inj_Locking.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Crank_Event_Record.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Cruise_Control_Monitor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Cruise_Driver_Switch.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Cvn_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Deter_Clutch_State.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Electrical_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Eng_Cool_Temp_Plau.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Engine_Speed_Plau_Chk.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Env_Param_Interface.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Env_Param_Plausibility.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Gear_Ratio_Monitor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Gsa_Plausibility.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Ignition_Switch_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Keyword_Serv_Plau_Chk.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2_Scheduler.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2p_Torque_Manager.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_L3_Scheduler.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Md_Zero_Torque_Dmnd_Detect.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Mdp_Supervisor_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Memory_Integrity_Global.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Memory_Integrity_Test.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Mic_Callback_Update.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Monitoring_Mod_Rst_Ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Open_Delay_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Foot_Pedal_Validity_Check.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Permissible_Torque_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pedal_Filtering.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_PMC_Offset_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Program_Flow_Check.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Brc_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Brsc_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_C2i_Off_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Cyl_Bal_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Cylp_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Fuel_T_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Fvc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Mdp_Trim.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Tuned_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_To_Fuel_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulses_Correlation.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Pulses_Plausibility.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Qadc_Test_Deter.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Rail_Pressure_Plau_Chk.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Torque_Demand_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Torque_Manager.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Vehicle_Speed_Plau.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Vss_Callback.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Zero_Pulse_Detection.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/esm/src/ESM_Zero_Torque_Dmnd_Detect.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/Appli/etc/src/etc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/fdc/src/FDC_Normal_Mode_Select.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/fqd/src/fqd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/fqd/src/FQD_Cumul_Inj_Fuel_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/fqd/src/FQD_Interface_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_background_sync.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_background_task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Bal_Enabling_Async.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_balance_injectors.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Brsc_Offset_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_calc_c2i_pulse_offset.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_c_calc_mdp_ton_correction.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Calc_Pmc_Corrections.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Calc_Pulse_Link.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Calc_Pulse_Timing_Pos.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Calc_Pulse_Ton.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Calc_Ton_Corrected.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Calc_Ton_Estimated.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Cylinder_Bal_Supervisor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_cylp_bkg_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_cylp_sync_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Hw_Driver_Ton_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Inj_Alloc_Pulse_Dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Inj_Dmnd_Sel.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_inj_input_interf.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_inj_sub_dec.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Inj_Tuning_Maps.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Inj_Tuning_Maps_Cond.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Mdp_Corr_Map_Update.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Mdp_Interface_Inputs.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Off_Mode_Det.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Pulse_Trim_Cor_Strat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Pwc_Fuel_Background.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Pwc_Fuel_Strat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Pwc_Railp_Background.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Pwc_Railp_Strat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Rail_Pressure_Estimator.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Speed_Conversion.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Tooth_Enable.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Tooth_Error_Corr.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/I_C_Acc_Async_Inf_Task_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/i_c_acc_background_task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/i_c_acc_calib_mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/i_c_acc_check_strat_cond.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/i_c_acc_control_strategy.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/I_C_Acc_Mdp_Correction_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/I_C_Acc_Mdp_Upd_Functions.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/i_c_acc_supervisor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/i_c_acc_test_mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/i_c_acc_update_mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/I_C_Accel_Data.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/i_c_accel_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spc_Bias_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spc_Cyl_Temp_Fac_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spc_Data_Display.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spc_In_Signal_F_Tp_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spc_Main.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spc_Manager.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spc_Nvm_Reset.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spc_Speed_Acq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spc_Speed_Process.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/i_c_spc_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spc_Trim_Process.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spci_Bias_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spci_Calc_Mode_Req.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spci_Man_Async.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spci_Manager.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spcs_Bias_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spcs_Calc_Cond.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spcs_Calc_Mode_Req.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spcs_Manager.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spcx_Manager.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/I_C_Spcx_Param_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/ici/src/ici.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/ici/src/ici_lamp_flasher_control.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/ici/src/ICI_Mi_Lamp_Output_Dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/ici/src/ICI_Mi_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/ici/src/ici_wif_lamp_control.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/ici/src/ici_lop_lamp_control.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/icv.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Air_Temp_Selection_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Alternator_Torque_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/icv_coolant_temp_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Clutch_Top_Bottom_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Cruise_Target_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Deter_Clutch_State.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Eng_Temp_Selection_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Exh_Gas_Characteristics.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Exhaust_Temp_Selection.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Foot_Off_Supervisor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Gsi_Activation_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Gsi_Display_Management.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Gsi_Driver_Behavior.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Gsi_Eng_Pow_Optim_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Gsi_Inhibition_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Gsi_Law_Select_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Gsi_Pedal_Position_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Gsi_Raw_Gear_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Interface_Gsi_Strategy.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Interface_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Key_Position_Deter.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/icv_monitor_brake_switches.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/icv/src/ICV_Vspdl_Target.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/itd/src/itd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/itd/src/ITD_Bkg_Snapshot.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/itd/src/ITD_After_Timing_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/p_t/src/p_t.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/rpc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/rpc_bkg_async_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/RPC_Bkg_Overpress_Dur_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/RPC_Bkg_Overpress_Flt_Det.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/rpc_bkg_sync_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/RPC_Hp_Async_Cntrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/RPC_Hp_Crt_Dmnd_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/rpc_imv_async_cntrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/rpc_imv_reset_sync_cntrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/rpc_imv_sync_cntrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/rpc_imv_temp_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/RPC_Lift_Pump_Control.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/RPC_Rvd_Async_Cntrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/RPC_Rvd_Pls_Period_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpc/src/RPC_Vlc_Control.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpd/src/rpd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/rpd/src/RPD_Rail_Pres_Dmnd_Filter.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/sac/src/sac.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/sac/src/SAC_Activation_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/sac/src/sac_glow_plug_control.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/sac/src/SAC_Glow_Plug_Control_Async.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/sac/src/SAC_Glow_Plug_Ena_Key_On.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/sac/src/SAC_Glow_Plug_Ena_Pw_Latch.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/smc/src/smc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/smc/src/SMC_Control_Function_Call.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/smc/src/smc_control_system_mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/smc/src/smc_determine_engine_state.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/smc/src/SMC_Determine_Engine_Time.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/smc/src/SMC_Dfco_Id_Allowed_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/smc/src/SMC_Sens_Act_Supply.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/smc/src/SMC_Starter_Relay_Cond_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/ste/src/ste.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/ste/src/ste_railp_tst_cntrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/ste/src/ste_supervisor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/t_d/src/t_d.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_acc_calc_timing_posn.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_acc_check_prog.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/P_L_ACC_Fill_Buffer.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_acc_gen_win_tables.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_acc_gen_win1_seq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_acc_gen_win2_seq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_acc_launch_win_seq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_acc_program_asic.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_acc_ratio_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_acc_read_intout_level.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_acc_signal_processing.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/P_L_Accel_Data.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_accel_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/t_d/src/T_D_Aos_Enabling.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/t_d/src/T_D_Aos_Interface.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/t_d/src/t_d_aos_torque_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/t_d/src/T_D_Idle_Target_Offset.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/t_d/src/T_D_Vsl_High_Pres_System.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/t_d/src/T_D_Vsl_Inj_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/t_d/src/T_D_Vsl_Low_Pres_System.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/t_d/src/T_D_Vag_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/Appli/t_d/src/T_D_Vag_Virtual_Pedal_Pos.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_amf/src/P_L_Amf_Chip_Heating.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_amf/src/P_L_Amf_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_amf/src/P_L_Amf_Acq_Supervisor.c', CC_TYPE = 'spec', OWNER = 'gillingham', CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_coolant_temp_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_dpf_diff_press_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Ext_Faults_Management.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_fuel_temp_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_ignition_sw_start_st.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_ignition_switch_state.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_ignition_switch_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Map_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_rail_pres_cal_check.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_rail_pres_calc_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_rail_pres_calc_sub_dec.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Railp_Async_Meas.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Railp_Get_Pres_Autoscan.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Railp_Get_Pressure.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Railp_Pressure_Fb_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Railp_Pulse_Delta_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Railp_Pulse_Meas.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Railp_Tdc_Meas.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Railp_Tfilt_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Railp_Tfilt_Meas.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Railp_Tooth_Meas.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Async_Scheduler.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Background.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/p_l_aps_cam_spd_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Camless_Activation.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Crank_Array_Mngt.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Crankless_Act.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/p_l_aps_eng_cyc_spd_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Engine_Speed_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Flt_Chk_On_Cam_Ev.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Flt_Chk_On_Crank_Ev.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Ic_Interface.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Init.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Inj_Calc_Cyl_Number.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Inj_Spd_Inj_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/p_l_aps_inj_spd_table_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Injection_Spd_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Learning_Activation.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/p_l_aps_no_sync_spd_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_On_Sync_Scheduler.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Speed_Diagnosis.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_St_Back_Rotation.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_St_Cam_Management.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_St_Coherency_Check.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_St_Crank_Management.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_St_Inc_Cam_Index.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_St_Lost_Signal_Det.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_St_Reset.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_St_Reverse_Firing.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/p_l_aps_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/p_l_aps_sub_generic.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Sync_Diag_Sched.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Sync_Scheduler.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Sync_Spd_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Sync_Tasks_Enable.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_aps/src/P_L_Aps_Tdc_Angle_Cor_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_c2i_encoding/src/p_l_c2i_bkg_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_c2i_encoding/src/p_l_c2i_encoding_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_c2i_encoding/src/p_l_c2i_expander.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_c2i_encoding/src/p_l_c2i_ram_check.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_c2i_encoding/src/p_l_c2i_read_label.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/_p_l_com/src/p_l_com.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/_p_l_cc/src/p_l_cc_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_ccp/src/p_l_cc_ccp_rx_ccp_cro.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_ccp/src/p_l_cc_ccp_services.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_dcan/src/p_l_cc_dcan_dl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_dcan/src/p_l_cc_dcan_nl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_dcan/src/p_l_cc_dcan_sds.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_dcan/src/p_l_cc_dcan_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_msg/src/p_l_cc_di_read.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_msg/src/p_l_cc_do_drive.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_msg/src/p_l_cc_msg.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_msg/src/p_l_cc_msg_esm.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_dpf.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_dt.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_edp.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_c2i.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_esd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_eud.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_ident.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_obd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/P_L_Cds_Obd_Mod01.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/P_L_Cds_Obd_Mod02.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/P_L_Cds_Obd_Mod03.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/P_L_Cds_Obd_Mod04.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/P_L_Cds_Obd_Mod06.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/P_L_Cds_Obd_Mod07.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/P_L_Cds_Obd_Mod09.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_rd_meas_val.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_sa.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_sup.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_vc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_digital_input/src/P_L_Brk_Light_Sw_State.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_digital_input/src/P_L_Brk_Safety_Sw_State.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_digital_input/src/P_L_Clutch_Sw_Bot_State.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_digital_input/src/P_L_Clutch_Sw_Top_State.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_digital_input/src/P_L_Di_Lib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_digital_output/src/p_l_digital_output_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_digital_output/src/p_l_digital_output_driver.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_digital_output/src/p_l_digital_output_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_s16s32.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr9.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_boostp_acq_data.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sat.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_output/src/p_l_mil_output_diag.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_output/src/P_L_Check_Engine_Lamp_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_output/src/P_L_Oil_Pressure_Lamp_Diag.c', CC_TYPE = 'spec', OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_output/src/p_l_starter_relay_driver.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Ecu_Error.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Ecu_Reboot.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Ecu_Sys_Diag_Bkg.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Ecu_Warning.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Low_Prio_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Low_Prio_Dtc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Mm_Trip_Detection.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Pls_Ring_Bf_Chk_Act.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Pls_Ring_Buf_Meas.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Power_Latch_Mngt.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Query_Reply_Mgnt.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Reset_Info_Deter.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Hard_Lock_Mon.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Tpu_Diag_Ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_calc_bal_delta_speed.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_event_input/src/P_L_Clock_Drift_Monitor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_vss_event_handler.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_vss_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_hbridge_output/src/P_L_Hbridge.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])

SourceFile('blois_soft_vob/Software/P_L/p_l_hbridge_output/src/P_L_Hbridge_Phdl_Act_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_hbridge_output/src/P_L_Hbridge_Phdl_Act_Drive.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/P_l_inj_abort_pulse.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_add_pls_pg_buf.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_adtrig_callback.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_adtrig_get_meas.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_adtrig_new_trig.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_adtrig_pfilt_req.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/P_L_Inj_Adtrig_Plow_Filt_Rq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_adtrig_pls_aborted.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_adtrig_ptdc_req.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_adtrig_ptooth_req.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_adtrig_server.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_background.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_brc_controller.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_brc_res_meas_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_calc_brc_per_offset.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_cancel_rvd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_count_pulse.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_count_reset.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_ecu_temp_limit.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_end_bank_config_cb.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_end_pulse_call_back.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_eval_inj_fault.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_gen_pulse_tables.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_get_inj_diag_state.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_hard_lock_mon.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_injector_avail_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_launch_diag_pulse.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_launch_iso_pulse.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_launch_pulse.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_launch_pulse_seq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_launch_rvd_pulse.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_rvd_bkg_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_rvd_burst_cntrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_rvd_ton_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_spi_controller.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_start_new_inj_cycle.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_test_supervisor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_timer_callback.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_timer_prog.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/P_L_INJ_Tst_Superv_Act_Chk.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_unjam_bkg_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_unjam_launch_pulse.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_injection_data.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_injection_sub_dec.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_inlet_air_temp/src/P_L_Inlet_Air_Temp_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_nvm/src/p_l_nvm_client.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_nvm/src/P_l_nvm_crypt.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_nvm/src/P_L_Nvm_Immediate_Write_Lib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_nvm/src/p_l_nvm_server.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_nvm/src/p_l_nvm_server_report_fault.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_nvm/src/p_l_nvm_signal_write_end.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_nvm/src/p_l_nvm_sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Alternator_Driver.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Hpv_Bkg_Cl_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Hpv_Cl_Drv.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Hpv_Vsep_Outp_Drv.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Imv_Bkg_Cl_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Imv_Cl_Drv.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Imv_Interface.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_pwm_output/src/p_l_pwm_output_sub.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_pwm_output/src/p_l_pwm_std_output_driver.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_self_diag/src/P_L_C2mio_Spi_Conf_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_self_diag/src/p_l_c2ps_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_self_diag/src/P_L_Cpu_Load_Measure.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_self_diag/src/P_L_Stack_Size_Measure.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_self_diag/src/p_l_test_memory_integrity.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_wraf/src/P_L_Wraf_Heater_Mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_wraf/src/P_L_Wraf_Resp_Diag_Fuel_Cut.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_wraf/src/P_L_Wraf_Sensor_Read.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/P_L/p_l_wraf/src/P_L_Wraf_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/f_m.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Add_Fault_Snap_Dat_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_B1_Counters_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Bulb_Chk_Lamp_Flash_Det.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Conf_Time_Counter_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Conf_Wo_Dcy_Enable_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Config_Hd_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Config_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Deletion_Services_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Eobd_Mode_03_07_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Etc_Config_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Etc_State_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Etc_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Event_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Extract_Did.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Extract_Lib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Fault_Clearing_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Fault_Counters_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/f_m_fault_init.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Fault_Log_Position_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Fault_Logging_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Fault_Snapshot_Dat_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Fid_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Flt_Fid_Function_Lib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Flt_Group_Function_Lib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Flt_Group_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Function_Lib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Function_Lib_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Gen_Monitor_Cond_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Hd_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Log_Sort_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Ignition_Cycle_Detect.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Induc_Detection_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Induc_Scan_Tool.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Induc_Service_Reset.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Log_Disable_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mil_Handling_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Func_Lib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Func_Lib_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Func_Lib_Tid.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Func_Lib_Tid_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Missing_Value.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Monitor_Driving_Cycle.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Nts_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Obd_Dynamic_Counters.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Obd_Dynamic_Fault.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Obd_Dynamic_State_Int.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Obd_Etc_Dynamic.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Obd_Lib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Obd_Readiness_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Act_Cond_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Cond_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Structure.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Swc_Id.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Track_Report_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Read_Dtc_Info.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Report_Fault_Group_Status.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Report_Fid_Status.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Reset_And_Mil_Counters.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Scheduling_Task.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Similar_Conditions_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Sub.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Veh_Time_Power_Off_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Vehicle_Total_Time_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Warm_Up_Cycle_Detect.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Permanent_Fault_Manager.c', CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Perm_Sub.c', CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])

SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_autocode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_average.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_band_stop_filter.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_band_stop_filter_lt.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_basic.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_bitfield_tab.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_chronometer.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_clock.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_cumul_sum.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_debounce.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_gain_v1.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_gain_v2.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_rate_v1.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_rate_v2.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_rte_gain_v1.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_rte_gain_v2.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_v1.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_v2.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_edc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_edge.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_enable_state.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_exp_minus.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_grad_filter_t.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_hist_table.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_hyst.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_interp.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_interval_det_hyst.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_low_pass_filter_f.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_low_pass_filter_k.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_low_pass_filter_t.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_map.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_map_out_high_res.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_osc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_pid_boost.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_pid_dterms_v1.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_pid_v1.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_pjt_specific.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_pulse_dt_t.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_resource.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_round.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_rst_v1.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_sbpa.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_slew.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_soft_transition.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_switch_slew.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_switch_slew_pr_nxt.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_switch_slew_rate.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_tab.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/S_S_LIB_Tab_Rollover_Read.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_timeout_rising_edge.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_timer.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_trigo.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_turn_x_delay.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_scheduler/src/S_S.c',CC_TYPE = 'project_auto' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_scheduler/src/s_s_background.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_scheduler/src/S_S_Lp_Sync_Th_Gain_Sync.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_scheduler/src/S_S_Lp_Sync_Tooth_Sync.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('blois_soft_vob/Software/S_S/s_s_scheduler/src/S_S_Lp_Sync_Tooth_Det.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/_Software/src/pack_id.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/Appli/_Appli/src/app.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/Appli/_Appli/src/application_stub.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/Appli/dti/src/dti.c',CC_TYPE = 'project_auto' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/P_L/_P_l/src/p_l.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Adc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Di.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Do.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Ei.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Eo.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Hb.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Pwm.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Sci.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Spi.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/S_S/s_s_fault_manager/src/F_M_Fault.c',CC_TYPE = 'project_auto' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/S_S/s_s_scheduler/src/s_s_scheduler.c',CC_TYPE = 'project_auto' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('gill_dcm624_code/Software/S_S/s_s_scheduler/src/S_S_Wrapper_Functions.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/ici/src/ICI_Flashing_Lamp_Codes.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/ici/src/ici_ce_lamp_control.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/ici/src/ici_glow_plug_lamp_control.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_a3944.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_adc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_api_macros.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_aps.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_aps_cam_management.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_aps_crank_management.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_baro.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_c2mio.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_c2ps.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_c2wraf.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_callbacks.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_can.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_dev_ram.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_diagnostics.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_discrete_io.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_dma.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_dma_adc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_dma_emios.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_dma_spi.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_ecu_startup.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_esci.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_etk_capture.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_etpu_resource_manager.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_event_capture.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_event_generation.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_exceptions.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_extern_inter_handler.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_extern_inter_vector.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_hbridge.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_lib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_lin.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_dma_lin.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_machine.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_memory_map.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_mic.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_nvm.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_nvm_nef.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_nvm_nef_driver.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_nvm_spi.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_pwm.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_rm_emios.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_scheduler.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_self_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_siu_init.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_sol.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_spi.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_spi_dph.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_core/src/hwi_timer_system.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_microcode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_2st_vgt_bst_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_2st_vgt_comp_prd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_2st_vgt_pos_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_2st_vgt_prot.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_2st_vgt_temp_prot.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_amf_cor_diag.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_amf_cor_err_calc.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_amf_cor_lrn.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_amf_cor_lrn_data.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_amf_corr_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_amf_filter.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_anti_surge.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_desired_air.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_desired_map.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_egr_flow_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_egr_misfire.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_egr_rate_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_egr_rate_limit.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_egr_st_est.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_egrh_cool_byp.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_egrh_flow_est.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_egrh_pos_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_eng_brk_enable.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/acm/src/acm_exh_brk_pres_ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_exh_flow_est_bkg.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_exh_flow_est_sync.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_flow_corr.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_flow_corr_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_intake_flow_est.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_throt_enable.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_throt_fl_lrn.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_throt_map_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_throt_pos_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_valve_comp.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_vgt_bst_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_vgt_max_pratio.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_vgth_pos_ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/acm/src/acm_vol_filling.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_air_fuel_ratio.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_dpf_out_afr.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_dsrd_afr.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_post2_control.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_smoke_limit.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_smoke_limit_fuel.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_wraf_blm_enable.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_wraf_blm_learn.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_wraf_blm_learn_data.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_wraf_cl_loop.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_wraf_control.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_wraf_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_wraf_fuel_blm.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/afc/src/afc_wraf_resp_diag.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/c_c/src/c_c_ac_management.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/dti/src/DTI_Iso_Eng_Spd_Rly_Test.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Fuel_Htr_Rly_Test.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Hpv_Test.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Dyn_Reset_Amf_Val.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Dyn_Reset_Aps_Val.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/dti_iso_dyn_reset_atc_val.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Dyn_Reset_Cdpf_Val.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Dyn_Reset_Hpp_Val.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Dyn_Reset_Imv_Val.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Dyn_Reset_Inj_Val.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Dyn_Reset_Tyre_Wear.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/dti_iso_dyn_rst_serv_mon.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Engine_Speed_Freq_Tst.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Exh_brk_pwm_Test.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/DTI_Iso_Mode_Maf_Learning.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/dti_iso_mode_pwr_sup_rly.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/dti_pilot_cut_1inj.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/dti/src/dti_pilot_cut_all_inj.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Brake_Fault_Freeze.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Can_0_Dmnd_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('src/appli/esm/src/ESM_Can_Cc_Buttons.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Can_J1939_Ped_Arb_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('src/appli/esm/src/ESM_Can_Pedal_Eec2.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Can_Pto.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Can_Tsc1_Plaus.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Cc_J1939_Msg_Rx_Diag.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Clutch_Position_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Esc_Decoding.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Exh_Brk_Switch_Req.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Exhaust_Brake_Acq.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Foot_Hand_Pedal_Arbitration.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Hand_Pedal_Validity_Check.c',CC_TYPE = 'spec' , OWNER = 'tcg', CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Injector_Cooling_Monitor.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Park_Brake_Sw_Signal.c',CC_TYPE = 'spec' , OWNER = 'tcg', CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Pedal_Select_Calc.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Pedal_To_Ground_Test.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Vdg_Rpm_Offset_Decode.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/esm/src/ESM_Vehicle_Speed_Sensor.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/etc/src/etc_fan_management_md.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/eud/src/eud.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fdc/src/fdc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fdc/src/fdc_after_mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fdc/src/fdc_background_snapshot.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fdc/src/fdc_dis_pilot_post.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fdc/src/fdc_pilot_mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fqd/src/fqd_after_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fqd/src/fqd_bkg_snapshot.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fqd/src/fqd_desired_fuel.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fqd/src/fqd_pilot_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fqd/src/fqd_post_air_ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fqd/src/fqd_post1_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fqd/src/fqd_post2_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fqd/src/fqd_post2_snapshot.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/fqd/src/fqd_smoke_limit.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/ici/src/ici_engine_speed_output_mdcr.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/ici/src/ICI_Ebrake_Lamp_Drive.c', CC_TYPE = 'spec', OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_cruise_src_select_mdcr.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/icv/src/icv_esc_input_decode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/icv/src/icv_flashing_code_ena.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_gear_state.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/icv/src/icv_interface_decoding.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/icv/src/icv_oil_pressure.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/icv/src/icv_vac_act.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/itd/src/itd_after_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/itd/src/itd_main_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/itd/src/itd_mbt_timing.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/itd/src/itd_pilot_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/itd/src/itd_post1_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/itd/src/itd_post2_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_air_cond_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/p_p/src/p_p_run_dry_strategy.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_comb_mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_comb_trans_reset.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dew_point_dpf.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dew_point_turbine.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dfco_ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_doc_aging.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_doc_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_doc_lightoff.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dpf_diag.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dpf_diag_leak.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dpf_eff_mon.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dpf_in_temp_trgt.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dpf_reg_crit_cond.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dpf_reg_oxy_ctrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dpf_regen_en.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_dpf_regen_en_data.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_engine_out_water.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_exh_air_fuel_trgt.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_nox_flow_acc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/p_t/src/p_t_nox_flow_est.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/pse/src/pse.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/pse/src/pse_2st_press.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/pse/src/pse_2st_vgt_pos_calc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/pse/src/pse_boost_est.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/pse/src/pse_press_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/pse/src/pse_press_est.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/smc/src/smc_starter_cntrl_mdcr.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rpc/src/rpc_interface.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rpd/src/rpd_rail_press_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_ssu32_sat_floor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_us32_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_s32.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_su32.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_s32_floor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_s32_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_s32_sat_floor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_s32_sat_round.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_u32.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_u32_ceiling.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_u32_near.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_u32_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_u32_sat_ceiling.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_repeat_uus32_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_s16u32.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_s16s32_floor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_su32.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/div_s32.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/div_s32_floor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_s32_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_s32_sat_ceiling.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_s32_sat_floor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_s32_sat_round.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_sus32_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_u32.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_us32_floor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_u32_ceiling.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/div_u32_near.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr30_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_s32_u32_sr16_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr12_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr7.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr14.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr15_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr21.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr26.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr28_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr28_zero.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr38_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr4_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr5.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr6_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr8_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr9_zero.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr5.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr10_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr13_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr14_zero.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr15.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr15_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr8.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr8_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_s32_s32_sr12.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_s32_s32_sr15.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_s32_s32_sr1_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_s32_u32_sr10_zero.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr1.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr1_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_s32_u32_sr15.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr15_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr15.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr11.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr16.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_s32_u32_sr26_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr25_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr26_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr2.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr2_near.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr26.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr26_near.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr35.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr38.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr31.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr38_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr38_near.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr6.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr6_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr7_sat.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_wide_s32.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_wide_su32.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_wide_u32.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/rt_enab.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr10.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr10_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr28.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr28_near.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr28_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr29_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr4.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr4_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr4_near.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr20.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr20_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr22_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr45.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr45_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr14.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr14_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr14_near.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr8_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr9.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr30.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_u32_u32_u32_sr30_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_s32_s32_s32_sr7_sat.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr15_zero.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/rtw/src/mul_s32_s32_u32_sr17_zero.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/rtw/src/rt_modu16_f_pw.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/sac/src/sac_fuel_heater_control_mdcr.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_access_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_actual_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_asg_torq_interface.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_bkg_snapshot.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_can_rx_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_comb_limit_torque.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_corr_terms.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_crank_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_dfco.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_driveability.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_driver_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_dsrd_imep_air.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_engine_load.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_engine_load_ref.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/t_d/src/t_d_engine_power.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_engine_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_fuel_fast.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_fuel_slow.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_idle_arbitr.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_idle_cntrl.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_idle_fast.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_idle_gains_ext.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_idle_mode.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_idle_pid.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_idle_setpoint.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_idle_slow.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_idle_spd_error.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_imep_no_aos.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_induced_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_interface_decoding.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_j1939_output.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/t_d/src/t_d_max_brk_trq_ext.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/t_d/src/t_d_max_fuel_torque.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_max_torque.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_pedal_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_reduced_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_retard_torque_calc.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/t_d/src/t_d_smoke_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_th_comb_eff.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_timing_eff.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_torq_conv.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_torq_select.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_torque_fast.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_torque_slow.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_vdg_enable.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_vdg_eng_spd_lim_interface.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_vdg_pid_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_vdg_speed_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/t_d/src/t_d_wheel_torq.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_ambient_air.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_comp_in_limit.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_comp_in_temp_est.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_egrh_cool_temp.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_egrh_temp_est.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_engine_out.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_exh_exo_eff.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_exhaust_temp.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_oil_temp.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_t2_est.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_temp_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_temp_diag_xc.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_temp_diag_xc_data.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_temp_est.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_temp_init.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_temp_sensors.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_turb_dew_temp.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/tse/src/tse_turbine_temp.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/lib/src/lib_queue.c', CC_TYPE = 'library_code', OWNER = 'gillingham', CCFLAGS = ['LIB_CCFLAGS','INTROM','INTRAM'])
SourceFile('src/p_l/_p_l/src/p_l_lib.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/_p_l/src/p_l_interface_decoding.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_2st_vgt_pos_lrn.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_analogue/src/p_l_amf_offset_lrn.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_analogue/src/p_l_cabin_temp_acq.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_cruise_switch_inputs.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_doc_in_temp_acq.c',CC_TYPE = 'spec',OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_doc_in_temp_acq_data.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_doc_in_temp_calc.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_egrh_pos_rd.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_esc_lever_signal_mon.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_fuel_filter_pressure.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_intercooler_out_temp_acq.c',CC_TYPE = 'spec',OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_oil_level_sensor.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_oil_pressure_sensor.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_analogue/src/p_l_oil_temp_mdcr.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_analogue/src/p_l_pedal_foot_posn.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_pedal_hand_posn.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_pressure_lrn.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_analogue/src/p_l_torque_state_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_vgth_pos.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_door_switch.c',CC_TYPE = 'spec',OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_exh_brk_switch_1.c',CC_TYPE = 'spec',OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_eng_brk_switch_1.c',CC_TYPE = 'spec',OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_immo_switch_state.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_low_fuel_level_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_oil_pressure_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_pedal_foot_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_pedal_hand_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_seat_belt_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_pedal_selector_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_starter_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_output/src/p_l_cruise_lamp_driver.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_output/src/p_l_eng_spd_rly_drive.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_output/src/p_l_ac_comp_relay_drive.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_input/src/p_l_flash_lamp_code_switch.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_hbridge_output/src/P_L_Hbridge_Tle_Act_Drive.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])

SourceFile('src/p_l/p_l_digital_output/src/p_l_oil_level_lamp_driver.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_pwm_output/src/p_l_coolant_temp_output.c',CC_TYPE = 'spec',OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_can/src/p_l_can.c', CC_TYPE = 'spec', OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_m_i_lamp/src/P_L_Mi_lamp_output_driver.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/_p_l_cc/src/P_L_Cc_Tx_Can_Frame_Compl_Cnt.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_Efl_P2_Tx_Frm.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_engine_op_status.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_idle_shutdown_timers.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_A1doc_Rx.c', CC_TYPE = 'spec', OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_A1doc_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_A1defi_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_A1scrdsi1_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_A1scrdsr1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_A1scrdsr2_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_A1scregt1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Acl_Analysis.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Amb_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Amb_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1ig2_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1ig2_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1igc2.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1ogc2.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1ig1_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1igc1_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1img_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1og1_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1og2_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1og2_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1ogc1_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1t1i_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_At1t1i_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Ccvs1_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Ccvs1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Cm1_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Csa_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Dd_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Delphi_Interface.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_J1939_Dcu_Dm01_Flt_Det.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Dm1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Dm1_Rx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Dm13_Rx.c', CC_TYPE = 'spec', OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Dpfc1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Ebc1_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Ebc2_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Ec1_Tx_Frm.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_CC_J1939_Eec1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Eec2_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Eec2_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Eec3_Data_Arb.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Eec3_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Eec3_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Eec5_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Eec7_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Efl_P1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Efs_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Egf1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Ei_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Eoi_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Erc1_Tx_Frm.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Erc1_Rx_Frm.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Et1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Et2_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Et3_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Etc1_Rx_Frm.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Etc2_Rx_Frm.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Etc7_Rx_Frm.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Fd1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Hours_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Ic1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Imt1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Lfe_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Msg_Rx_Diag.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Pto_Rx_Frame.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Reset_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_tx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rq.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Ccss_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Ci_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Dm2_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Dm3_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Dm4_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Dm12_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Dm19_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Eo1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Io_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Lfc_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Lfi_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Soft_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Tavg_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Rq_Vh_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_diag_enabler.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu000.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu222.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu223.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu224.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_pdu232.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_pdu234.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu235.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu236.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu238.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu240.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu253.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu254.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_pdu255.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Shutdn_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_sub.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Tci3_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Tci4_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Tco1_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Tco1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_tp.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Vd_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Vep1_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Vdhr_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Oi_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Syspm3_Tx_Frm.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Syspm4_Rx.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cds/src/P_L_Cds_Systec_Maf.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_com/p_l_cds/src/p_l_cds_eeprom_adj_dds.c', CC_TYPE = 'spec', OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_security_access/src/sec_manage_security_access.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
ObjectFile('src/p_l/p_l_security_access/src/sec_reprog_lib.a',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_pwm_output/src/p_l_veh_spd_output.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_output/src/p_l_fuel_heater_driver.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_event_input/src/p_l_vss_loss_detection.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE']) 
SourceFile('src/p_l/p_l_event_input/src/p_l_tyre_wear_adjust.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_event_input/src/p_l_vss_raw_speed_calc.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE']) 
SourceFile('src/p_l/p_l_event_input/src/p_l_vss_validate.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE']) 
SourceFile('src/p_l/p_l_hbridge_output/src/P_L_Egrh_Hb_Drive_Diag_Md.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_hbridge_output/src/P_L_Thrtl_Hb_Drive_Diag_Md.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_water_in_fuel/src/p_l_water_in_fuel.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_wraf/src/p_l_wraf_acquis.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_wraf/src/p_l_wraf_acquis_data.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_wraf/src/p_l_wraf_config.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_wraf/src/p_l_wraf_config_data.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_wraf/src/p_l_wraf_control.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_wraf/src/p_l_wraf_diagnostic.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/p_l/p_l_wraf/src/p_l_wraf_htr_diag.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/smc/src/smc_system_mode_dmnd.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_amf_selection.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_ac_eng_cool_req_sw_select.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_cc_asl_interface.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])


SourceFile('src/appli/icv/src/icv_oil_level_monitor.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_oil_temp.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_eng_brk_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/icv/src/icv_exh_brk_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])
SourceFile('src/appli/icv/src/icv_exh_over_temp_monitor.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_ext_temp.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_fuel_consumption.c', CC_TYPE = 'spec', OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_fuel_filter_pressure.c', CC_TYPE = 'spec', OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_calc_veh_speed_data.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_calc_agb_output.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_cruise_req_md.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_kickdown_detection.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_low_fuel_level_detection.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_pedal_arbitration_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_pedal_foot_fault_wrapper.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_pedal_hand_fault_wrapper.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_pedal_foot_pos.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_pedal_hand_pos.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_torque_state_switch.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_veh_spd_limit_interface.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])

SourceFile('src/appli/eud/src/eud_crank_revolutions.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/eud/src/eud_distance_calculations.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/eud/src/eud_fuel_calculations.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/eud/src/eud_hp_opening_counter.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/eud/src/eud_save_eng_hrs.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/eud/src/eud_timer_calculations.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])

SourceFile('src/p_l/p_l_aps/src/p_l_aps_tdc_angle_correction.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])



SourceFile('src/s_s/s_s_fault_manager/src/F_M_Flashing_Code_Output.c', CC_TYPE = 'spec', OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/s_s/s_s_fault_manager/src/f_m_gen_monitor_cond_eol.c',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['INTROM','INTRAM'])
SourceFile('src/appli/c_c/src/c_c_ac_comp_torque_consump.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/ici/src/ici_oil_pressure_gauge.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_pwm_output/src/p_l_oilp_gauge_drv_diag.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_digital_output/src/p_l_fan_drive_diag.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])

SourceFile('src/p_l/p_l_pwm_output/src/p_l_pwm_hp_turbo_driver.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_ac_request_arb.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_analogue/src/p_l_ac_fluid_press_ana_sig_acq.c',CC_TYPE = 'spec',OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_ac_fluid_pres_input_arbit.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_pwm_output/src/p_l_imv_drv_diag.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_pwm_output/src/p_l_ebrake_diag.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_pwm_output/src/p_l_exh_brk_vlv_drv.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/p_l/p_l_pwm_output/src/p_l_engine_speed_gauge_drv_diag.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/_appli/src/app_interface_decode.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])

SourceFile('src/p_l/p_l_analogue/src/p_l_boostp_acq.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_boostp_calc.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/icv/src/icv_vehicle_distance.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])

SourceFile('src/p_l/p_l_water_in_fuel/src/p_l_wif_lamp_drv_diag.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])
SourceFile('src/appli/t_d/src/t_d_idle_target_ext_calc_md.c',CC_TYPE = 'spec',OWNER = 'gillingham', CCFLAGS = ['EXTROM','INTRAM'])

# ==================Object files--==================

# ==================Assembly Files==================
AsmFile('hwi_vob/hwi/hwi_core/src/hwi_processor_startup.s', CC_TYPE = 'hwi', OWNER = 'blois')

# ==================Header Files===================                                                                                       

HeaderFile('blois_code_p_l/p_l/p_l_ecu/NVM/src/P_L_Nvm_Data.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_code_p_l/p_l/p_l_com/Misc/src/P_L_Cds_Msg.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Uds_Array_Types.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Uds_Rdbi_Autocode.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_code_p_l/p_l/p_l_out/I_C/src/P_L_Inj_Adtrig_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/_Software/src/lib_filter.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/_Software/src/lib_macros.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/_Software/src/lib_map.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/_Software/src/lib_mem.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/_Software/src/lib_table.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/_Software/src/types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/acm/src/acm.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/afc/src/afc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/asm/src/asm.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/atc/src/atc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/c_c/src/c_c.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/c_i/_c_i/src/c_i.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/c_i/_c_i/src/C_I_Maps.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/dti/src/dti_iso_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_Inputs_Monitor_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/esm.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2_Scheduler.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2p_Actual_Trq_Calc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2p_Pedal_Plau_Check.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2p_Permis_Trq_Calc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2p_Pulse_Conv_Calc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2p_Torque_Coordinator.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2p_Torque_Manager.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2p_Zero_Pulse_Detect.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_L2p_Zero_Trq_Dmd_Detect.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_L3_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_Zero_Torque_Monitor_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/esm/src/ESM_Torque_Monitor_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/etc/src/etc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/fqd/src/fqd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_inj_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/i_c_acc_mode.h', OWNER = 'tcbl')
HeaderFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/I_C_Accel_Data.h', OWNER = 'tcbl')
HeaderFile('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/i_c_accel_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/i_c/i_c_spc/src/i_c_spc_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/ici/src/ici.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/ici/src/ici.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/ici/src/ICI_Mi_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/icv/src/icv.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/itd/src/itd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/p_t/src/p_t.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/rpc/src/rpc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/rpd/src/rpd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/sac/src/sac.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/smc/src/smc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/ste/src/ste.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/Appli/t_d/src/t_d.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/P_L_Accel_Data.h', OWNER = 'tcbl')
HeaderFile('blois_soft_vob/Software/P_L/p_l_accelerometer/src/p_l_accel_sub.h', OWNER = 'tcbl')
HeaderFile('blois_soft_vob/Software/P_L/p_l_amf/src/P_L_Amf_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_ignition_switch_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_rail_pres_calc_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_aps/src/p_l_aps_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_aps/src/p_l_aps_sub_generic.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_c2i_encoding/src/p_l_c2i_encoding_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_com/_p_l_com/src/p_l_com.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/_p_l_cc/src/p_l_cc_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_dcan/src/p_l_cc_dcan_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_diag/src/p_l_cc_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/p_l_cc_msg/src/p_l_cc_msg.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/P_L_Cds_Computation_Method.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_data_conv_lib.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_digital_input/src/P_L_DI_Lib.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Ecu_Error_Code_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Ecu_Error_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_vss_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_injection_data.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_injection_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_inlet_air_temp/src/P_L_Inlet_Air_Temp_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_nvm/src/p_l_nvm_sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('gill_vob/6_coding/src/p_l/p_l_security_access/src/sec_manage_security_access.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('gill_vob/6_coding/src/p_l/p_l_security_access/src/sec_reprog_lib.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_self_diag/src/p_l_self_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_self_diag/src/p_l_test_memory_integrity.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/P_L/p_l_wraf/src/P_L_Wraf_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/_S_s/src/s_s.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/_S_s/src/s_s_os.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/_S_s/src/s_s_timers.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/f_m.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Add_Fault_Snap_Dat_Calc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_B1_Counters_Calc.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Config_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Cal_Def_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Diag_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Etc_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Event_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Fid_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Extract_Lib.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Flt_Group_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Flt_Grp_Index_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Hd_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Perm_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Include_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Diag_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Missing_Value.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Tid_Diag_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Tid_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Module_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Project_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Act_Cond_Calc.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Structure.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Track_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Read_Dtc_Info.h',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Sub.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_autocode.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_average.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_band_stop_filter.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_band_stop_filter_lt.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_basic.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_bit.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_bitfield_tab.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_chronometer.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_clock.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_cumul_sum.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_debounce.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_gain_v1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_gain_v2.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_rate_v1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_rate_v2.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_rte_gain_v1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_rte_gain_v2.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_v1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dt_filt_v2.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_dti.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_edc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_edge.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_enable_state.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_exp_minus.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_grad_filter_t.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_hist_table.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_hyst.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_interp.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_interval_det_hyst.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_low_pass_filter_f.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_low_pass_filter_k.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_low_pass_filter_t.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_macros_unused_def.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_map.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_map_out_high_res.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_osc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_pid_boost.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_pid_dterms_v1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_pid_v1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_pjt_specific.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_pulse_dt_t.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_resource.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_round.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_rst_v1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_sbpa.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_slew.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_soft_transition.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_switch_slew.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_switch_slew_pr_nxt.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_switch_slew_rate.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_tab.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/S_S_LIB_Tab_Rollover_Read.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_timeout_rising_edge.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_timer.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_trigo.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_turn_x_delay.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('blois_soft_vob/Software/S_S/s_s_lib/src/s_s_lib_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('gill_dcm624_code/Software/Appli/_Appli/src/app.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('gill_dcm624_code/Software/Appli/dti/src/dti.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('gill_dcm624_code/Software/P_L/_P_l/src/p_l.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Callback_Mapping.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Hwi_Config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Io_Types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])

HeaderFile('gill_dcm624_code/Software/S_S/s_s_fault_manager/src/F_M_Fault.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])

HeaderFile('gill_dcm624_code/Software/S_S/s_s_scheduler/src/s_s_scheduler.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_a3944.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_a3944_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_a3944_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_adc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_adc_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_adc_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_api_macros.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_aps.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_aps_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_aps_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_baro.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_baro_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_baro_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_c2mio.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_c2mio_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_c2mio_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_c2ps.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_c2ps_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_c2ps_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_c2wraf.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_c2wraf_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_c2wraf_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_callbacks.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_callbacks_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_callbacks_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_can.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_can_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_can_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_cylp_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dev_ram.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dev_ram_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dev_ram_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_diag_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_diag_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_diagnostics.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dio_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dio_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_discrete_io.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dma.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dma_adc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dma_adc_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dma_adc_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dma_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dma_emios.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dma_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_dma_spi.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_ecu_startup.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_ei_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_ei_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_eo_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_eo_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_epwm_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_epwm_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_esci.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_etpu_resource_manager.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_event_capture.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_event_generation.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_exceptions.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_extern_inter_handler.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_hbridge.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_hbridge_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_hbridge_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_intdefs.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_lib.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_machine.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_macro_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_macro_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_memory_map.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_memory_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_memory_section.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_mic.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_mic_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_mic_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_mios_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_mios_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_nvm.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_nvm_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_nvm_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_nvm_nef.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_nvm_nef_driver.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_nvm_spi.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_nvm_spi_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_pwm.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_pwm_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_pwm_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_register.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_rm_emios.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_scheduler.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_scheduler_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_scheduler_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_sci_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_sci_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_self_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_self_diag_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_self_diag_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_siu_init.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_sol.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_sol_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_sol_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_spi.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_spi_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_spi_dph.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_spi_dph_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_spi_dph_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_spi_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_timer_system.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_timers_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_timers_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_tpu_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_tpu_methods.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_core/src/hwi_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_came.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_ece.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_eppbe.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_eppe.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_fie.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_icpce.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_injprot.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_mask.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_oce.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_pwmie.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_pwmoe.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_qode.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_rqomde.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_rqome.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('hwi_vob/hwi/hwi_tpu/src/hwi_etpu_sente.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_bst_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_bst_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_bst_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_comp_prd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_comp_prd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_comp_prd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_pos_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_pos_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_pos_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_prot.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_prot_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_prot_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_temp_prot.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_temp_prot_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_2st_vgt_temp_prot_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_cor_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_cor_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_cor_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_cor_err_calc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_cor_err_calc_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_cor_err_calc_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_cor_lrn.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_cor_lrn_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_cor_lrn_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_corr_calc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_corr_calc_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_corr_calc_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_filter.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_filter_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_amf_filter_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_anti_surge.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_anti_surge_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_anti_surge_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_desired_air.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_desired_air_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_desired_air_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_desired_map.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_desired_map_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_desired_map_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_flow_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_flow_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_flow_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_misfire.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_misfire_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_misfire_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_rate_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_rate_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_rate_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_rate_limit.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_rate_limit_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_rate_limit_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_st_est.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_st_est_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egr_st_est_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egrh_cool_byp.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egrh_cool_byp_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egrh_cool_byp_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egrh_flow_est.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egrh_flow_est_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egrh_flow_est_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egrh_pos_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egrh_pos_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_egrh_pos_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_eng_brk_enable.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_eng_brk_enable_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_eng_brk_enable_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_exh_brk_pres_ctrl.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_exh_brk_pres_ctrl_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_exh_brk_pres_ctrl_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_exh_flow_est_bkg.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_exh_flow_est_bkg_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_exh_flow_est_bkg_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_exh_flow_est_sync.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_exh_flow_est_sync_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_exh_flow_est_sync_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_flow_corr.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_flow_corr_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_flow_corr_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_flow_corr_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_flow_corr_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_flow_corr_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_intake_flow_est.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_intake_flow_est_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_intake_flow_est_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_enable.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_enable_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_enable_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_fl_lrn.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_fl_lrn_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_fl_lrn_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_map_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_map_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_map_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_pos_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_pos_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_throt_pos_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_valve_comp.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_valve_comp_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_valve_comp_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vgt_bst_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vgt_bst_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vgt_bst_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vgt_max_pratio.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vgt_max_pratio_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vgt_max_pratio_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vgth_pos_ctrl.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vgth_pos_ctrl_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vgth_pos_ctrl_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_ac_fluid_press_ana_sig_acq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_ac_fluid_press_ana_sig_acq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_ac_fluid_press_ana_sig_acq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vol_filling.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vol_filling_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/acm/src/acm_vol_filling_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_air_fuel_ratio.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_air_fuel_ratio_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_air_fuel_ratio_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_dpf_out_afr.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_dpf_out_afr_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_dpf_out_afr_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_dsrd_afr.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_dsrd_afr_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_dsrd_afr_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_post2_control.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_post2_control_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_post2_control_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_smoke_limit.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_smoke_limit_fuel.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_smoke_limit_fuel_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_smoke_limit_fuel_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_smoke_limit_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_smoke_limit_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_blm_enable.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_blm_enable_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_blm_enable_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_blm_learn.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_blm_learn_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_blm_learn_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_cl_loop.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_cl_loop_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_cl_loop_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_control.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_control_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_control_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_fuel_blm.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_fuel_blm_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_fuel_blm_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_resp_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_resp_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/afc/src/afc_wraf_resp_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/c_c/src/c_c_ac_management.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/c_c/src/c_c_ac_management_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/c_c/src/c_c_ac_management_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/etc/src/etc_fan_management_md.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/etc/src/etc_fan_management_md_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/etc/src/etc_fan_management_md_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/eud/src/eud.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_crank_revolutions.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_crank_revolutions_types.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_crank_revolutions_private.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_distance_calculations.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_distance_calculations_types.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_distance_calculations_private.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_fuel_calculations.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_fuel_calculations_types.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_fuel_calculations_private.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_hp_opening_counter.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_hp_opening_counter_types.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_hp_opening_counter_private.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_timer_calculations.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_timer_calculations_types.h', OWNER = 'tcg')
HeaderFile('src/appli/eud/src/eud_timer_calculations_private.h', OWNER = 'tcg')
HeaderFile('src/appli/fdc/src/fdc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fdc/src/fdc_after_mode.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fdc/src/fdc_after_mode_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fdc/src/fdc_after_mode_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fdc/src/fdc_dis_pilot_post.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fdc/src/fdc_dis_pilot_post_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fdc/src/fdc_dis_pilot_post_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fdc/src/fdc_pilot_mode.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fdc/src/fdc_pilot_mode_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fdc/src/fdc_pilot_mode_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_after_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_after_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_after_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_bkg_snapshot.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_bkg_snapshot_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_bkg_snapshot_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_desired_fuel.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_desired_fuel_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_desired_fuel_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_pilot_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_pilot_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_pilot_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post_air_ctrl.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post_air_ctrl_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post_air_ctrl_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post1_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post1_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post1_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post2_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post2_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post2_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post2_snapshot.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post2_snapshot_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_post2_snapshot_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_smoke_limit.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_smoke_limit_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/fqd/src/fqd_smoke_limit_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/ici/src/ici_ce_lamp_control.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/ici/src/ici_ce_lamp_control_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/ici/src/ici_ce_lamp_control_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/ici/src/ici_engine_speed_output_mdcr.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/ici/src/ici_engine_speed_output_mdcr_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/ici/src/ici_engine_speed_output_mdcr_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/ici/src/ici_glow_plug_lamp_control.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/ici/src/ici_glow_plug_lamp_control_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/ici/src/ici_glow_plug_lamp_control_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_cc_asl_interface.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_cc_asl_interface_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_cc_asl_interface_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_calc_agb_output.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_calc_agb_output_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_calc_agb_output_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_calc_veh_speed_data.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_calc_veh_speed_data_private.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_calc_veh_speed_data_types.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_cruise_req_md.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_cruise_req_md_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_cruise_req_md_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_cruise_src_select_mdcr.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_cruise_src_select_mdcr_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_cruise_src_select_mdcr_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_eng_brk_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_eng_brk_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_eng_brk_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_exh_brk_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_exh_brk_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_exh_brk_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_exh_over_temp_monitor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_exh_over_temp_monitor_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_exh_over_temp_monitor_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_ext_temp.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_ext_temp_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_ext_temp_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_flashing_code_ena.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_flashing_code_ena_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_flashing_code_ena_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_fuel_consumption.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_fuel_consumption_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_fuel_consumption_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_fuel_filter_pressure.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_fuel_filter_pressure_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_fuel_filter_pressure_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_fuel_level_low_calc_enum.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_gear_state.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_gear_state_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_gear_state_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_interface_decoding.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_interface_decoding_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_interface_decoding_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_kickdown_detection.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_kickdown_detection_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_kickdown_detection_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_low_fuel_level_detection.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_low_fuel_level_detection_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_low_fuel_level_detection_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_oil_level_monitor.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_oil_level_monitor_private.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_oil_level_monitor_types.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_oil_pressure.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_oil_pressure_private.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_oil_pressure_types.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_oil_temp.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_oil_temp_private.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_oil_temp_types.h', OWNER = 'tcg')
HeaderFile('src/appli/icv/src/icv_pedal_arbitration_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_arbitration_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_arbitration_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_foot_fault_wrapper.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_foot_fault_wrapper_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_foot_fault_wrapper_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_hand_fault_wrapper.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_hand_fault_wrapper_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_hand_fault_wrapper_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_foot_pos.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_foot_pos_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_foot_pos_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_hand_pos.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_hand_pos_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_pedal_hand_pos_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_torque_state_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_torque_state_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_torque_state_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_vac_act.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_vac_act_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_vac_act_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_veh_spd_limit_interface.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_veh_spd_limit_interface_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_veh_spd_limit_interface_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_after_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_after_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_after_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_main_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_main_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_main_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_mbt_timing.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_mbt_timing_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_mbt_timing_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_pilot_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_pilot_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_pilot_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_post1_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_post1_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_post1_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_post2_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_post2_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/itd/src/itd_post2_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_air_cond_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_air_cond_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_air_cond_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/_p_l/src/p_l_lib.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_p/src/p_p.h',OWNER = 'tcg', CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_p/src/p_p_run_dry_strategy.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_p/src/p_p_run_dry_strategy_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_p/src/p_p_run_dry_strategy_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_comb_mode.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_comb_mode_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_comb_mode_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_comb_trans_reset.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_comb_trans_reset_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_comb_trans_reset_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dew_point_turbine.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dew_point_turbine_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dew_point_turbine_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dfco_ctrl.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dfco_ctrl_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dfco_ctrl_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_doc_aging.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_doc_aging_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_doc_aging_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_doc_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_doc_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_doc_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_doc_lightoff.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_doc_lightoff_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_doc_lightoff_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dew_point_dpf.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dew_point_dpf_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dew_point_dpf_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_diag_leak.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_diag_leak_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_diag_leak_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_eff_mon.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_eff_mon_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_eff_mon_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_in_temp_trgt.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_in_temp_trgt_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_in_temp_trgt_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_reg_crit_cond.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_reg_crit_cond_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_reg_crit_cond_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_reg_oxy_ctrl.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_reg_oxy_ctrl_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_reg_oxy_ctrl_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_regen_en.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_regen_en_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_dpf_regen_en_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_engine_out_water.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_engine_out_water_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_engine_out_water_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_exh_air_fuel_trgt.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_exh_air_fuel_trgt_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_exh_air_fuel_trgt_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_nox_flow_acc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_nox_flow_acc_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_nox_flow_acc_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_nox_flow_est.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_nox_flow_est_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/p_t/src/p_t_nox_flow_est_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_2st_press.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_2st_press_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_2st_press_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_2st_vgt_pos_calc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_2st_vgt_pos_calc_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_2st_vgt_pos_calc_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_boost_est.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_boost_est_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_boost_est_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_press_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_press_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_press_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_press_est.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_press_est_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/pse/src/pse_press_est_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rpc/src/rpc_interface.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rpc/src/rpc_interface_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rpc/src/rpc_interface_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/BINARYSEARCH_U32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s16s32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s16s32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s16su32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s16u32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s16us32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s16us32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s32_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s32_sat_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s32_sat_round.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_s32_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_ssu32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_ssu32_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_ssu32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_ssu32_sat_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_su32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_sus32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_sus32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_sus32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_sus32_sat_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_u32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_u32_ceiling.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_u32_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_u32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_u32_sat_ceiling.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_u32_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_us32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_us32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_us32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_usu32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_usu32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_uus32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_repeat_uus32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s16s32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s16s32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s16s32_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s16s32_SR_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s16su32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s16su32_SR_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s16u32.h', CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s16u32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s16us32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32_sat_ceiling.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32_sat_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32_sat_round.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32_SR.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32_SR_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_s32_SR_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_ssu32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_ssu32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_ssu32_SR_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_su32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_sus32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_sus32_sat_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_u32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_us32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_u32_ceiling.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_u32_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_u32_SR.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_us32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_us32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_us32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_usu32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_usu32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_uus32_floor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/div_uus32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/LookUp_S16_U32_SAT.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/LookUp_U32_U32_SAT.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/LookUp2e7_S16_S16.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr1_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr10.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr10_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr10_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr11_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr11_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr11_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr12.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr12_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr12_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr13.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr13_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr13_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr13_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr14.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr14_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr14_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr15.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr15_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr15_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr15_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr16.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr16_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr16_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr18.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr18_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr18_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr19.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr2.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr2_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr2_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr2_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr20.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr20_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr20_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr20_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr20_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr21.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr21_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr22_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr22_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr23_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr24.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr24_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr26.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr28.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr28_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr28_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr28_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr29_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr29_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr29_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr3_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr3_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr3_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr16_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr30.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr30_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr30_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr30_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr31.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr31_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr34.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr34_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr34_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr35_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr37.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr38.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr38_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr39_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr4.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr4_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr4_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr4_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr41.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr41_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr41_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr41_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr42_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr43.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr48_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr49_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr49_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr5.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr5_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr5_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr6.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr6_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr6_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr6_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr7.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr7_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr7_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr7_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr8.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr8_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr8_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr8_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr9.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr9_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr9_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_s32_sr9_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr1_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr1_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr10_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr10_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr10_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr11_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr11_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr11_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr12_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr12_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr13.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr13_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr13_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr14.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr14_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr14_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr14_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr14_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr15.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr15_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr15_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr15_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr16.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr16_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr16_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr16_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr17_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr17_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr17_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr19.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr19_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr2.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr2_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr2_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr2_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr20.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr20_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr22.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr22_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr27_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr29.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr29_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr29_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr3_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr31_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr4_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr4_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr4_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr5_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr5_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr5_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr6.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr6_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr6_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr6_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr7.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr7_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr7_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr7_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr8.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr8_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr8_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr8_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr9_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr9_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_s32_s32_u32_sr9_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr1_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr12.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr15.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr15_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr2_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr33.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr38.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr4_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr4_sat_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr5.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr5_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_s32_sr7_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr10_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr10_zero.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr12.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr13.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr13_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr14.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr14_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr15.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr15_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr2.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr2_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr26.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr26_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr27_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr4.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr7.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_s32_u32_sr7_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr1_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr10.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr10_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr11.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr11_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr12.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr12_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr13.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr13_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr14.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr14_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr14_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr14_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr15.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr15_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr15_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr15.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr16.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr16_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr17.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr17_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr17_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr18_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr19.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr19_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr2.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr2_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr2_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr2_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr20.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr20_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr21_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr22.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr22_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr23.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr23_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr24_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr25_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr26.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr26_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr26_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr27_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr28.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr28_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr28_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr28_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr29.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr29_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr3_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr30.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr30_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr30_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr31.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr31_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr31_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr31_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr32_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr33.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr33_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr34.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr34_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr35.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr35_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr35_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr35_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr36.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr36_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr37.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr37_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr37_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr38.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr38_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr38_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr38_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr39.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr4.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr4_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr4_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr4_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr40_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr41.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr44_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr45.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr45_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr46.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr47.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr48.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr5.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr5_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr50.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr6.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr6_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr7.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr7_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr7_sat_near.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr8.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr8_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr9.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_u32_u32_u32_sr9_sat.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_wide_s32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_wide_su32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/mul_wide_u32.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/rt_defines.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/rtlibsrc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/rt_modu16_f_pw.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/rtw_shared_utils.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/rtwtypes.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/rtw/src/TuneParamCast_S16_U16_SAT.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/sac/src/sac_fuel_heater_control_mdcr.h', OWNER = 'tcg')
HeaderFile('src/appli/sac/src/sac_fuel_heater_control_mdcr_private.h', OWNER = 'tcg')
HeaderFile('src/appli/sac/src/sac_fuel_heater_control_mdcr_types.h', OWNER = 'tcg')
HeaderFile('src/appli/smc/src/smc_starter_cntrl_mdcr.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/smc/src/smc_starter_cntrl_mdcr_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/smc/src/smc_starter_cntrl_mdcr_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/smc/src/smc_system_mode_dmnd.h', OWNER = 'tcg')
HeaderFile('src/appli/smc/src/smc_system_mode_dmnd_private.h', OWNER = 'tcg')
HeaderFile('src/appli/smc/src/smc_system_mode_dmnd_types.h', OWNER = 'tcg')
HeaderFile('src/appli/t_d/src/t_d_access_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_access_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_access_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_actual_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_actual_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_actual_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_asg_torq_interface.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_asg_torq_interface_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_asg_torq_interface_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_bkg_snapshot.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_bkg_snapshot_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_bkg_snapshot_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_can_rx_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_can_rx_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_can_rx_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_comb_limit_torque.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_comb_limit_torque_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_comb_limit_torque_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_corr_terms.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_corr_terms_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_corr_terms_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_crank_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_crank_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_crank_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_dfco.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_dfco_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_dfco_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_driveability.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_driveability_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_driveability_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_driver_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_driver_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_driver_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_dsrd_imep_air.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_dsrd_imep_air_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_dsrd_imep_air_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_load.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_load_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_load_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_load_ref.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_load_ref_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_load_ref_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_power.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_power_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_power_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_engine_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_fuel_fast.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_fuel_fast_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_fuel_fast_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_fuel_slow.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_fuel_slow_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_fuel_slow_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_arbitr.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_arbitr_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_arbitr_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_cntrl.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_cntrl_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_cntrl_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_fast.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_fast_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_fast_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_gains_ext.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_gains_ext_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_gains_ext_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_mode.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_pid.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_pid_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_pid_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_setpoint.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_slow.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_slow_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_slow_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_spd_error.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_spd_error_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_idle_spd_error_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_imep_no_aos.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_imep_no_aos_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_imep_no_aos_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_induced_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_induced_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_induced_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_interface_decoding.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_interface_decoding_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_interface_decoding_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_j1939_output.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_j1939_output_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_j1939_output_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_max_brk_trq_ext.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_max_brk_trq_ext_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_max_brk_trq_ext_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_max_fuel_torque.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_max_fuel_torque_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_max_fuel_torque_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_max_torque.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_max_torque_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_max_torque_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_pedal_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_pedal_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_pedal_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_reduced_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_reduced_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_reduced_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_retard_torque_calc.h')
HeaderFile('src/appli/t_d/src/t_d_retard_torque_calc_types.h')
HeaderFile('src/appli/t_d/src/t_d_retard_torque_calc_private.h')
HeaderFile('src/appli/t_d/src/t_d_smoke_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_smoke_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_smoke_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_th_comb_eff.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_th_comb_eff_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_th_comb_eff_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_timing_eff.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_timing_eff_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_timing_eff_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torq_conv.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torq_conv_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torq_conv_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torq_select.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torq_select_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torq_select_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torque_fast.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torque_fast_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torque_fast_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torque_slow.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torque_slow_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_torque_slow_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_enable.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_enable_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_enable_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_eng_spd_lim_interface.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_eng_spd_lim_interface_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_eng_spd_lim_interface_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_pid_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_pid_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_pid_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_speed_dmnd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_speed_dmnd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_vdg_speed_dmnd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_wheel_torq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_wheel_torq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/t_d/src/t_d_wheel_torq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_ambient_air.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_ambient_air_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_ambient_air_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_comp_in_limit.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_comp_in_limit_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_comp_in_limit_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_comp_in_temp_est.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_comp_in_temp_est_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_comp_in_temp_est_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_egrh_cool_temp.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_egrh_cool_temp_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_egrh_cool_temp_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_egrh_temp_est.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_egrh_temp_est_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_egrh_temp_est_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_engine_out.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_engine_out_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_engine_out_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_exh_exo_eff.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_exh_exo_eff_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_exh_exo_eff_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_exhaust_temp.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_exhaust_temp_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_exhaust_temp_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_oil_temp.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_oil_temp_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_oil_temp_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_t2_est.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_t2_est_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_t2_est_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_diag_xc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_diag_xc_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_diag_xc_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_est.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_est_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_est_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_init.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_init_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_init_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_sensors.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_sensors_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_temp_sensors_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])

HeaderFile('src/appli/tse/src/tse_turb_dew_temp.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_turb_dew_temp_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_turb_dew_temp_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_turbine_temp.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_turbine_temp_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/tse/src/tse_turbine_temp_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/lib/src/lib_queue.h', OWNER = 'tcbl')
HeaderFile('src/p_l/_p_l/src/p_l_interface_decoding.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/_p_l/src/p_l_interface_decoding_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/_p_l/src/p_l_interface_decoding_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_2st_vgt_pos_lrn.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_2st_vgt_pos_lrn_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_2st_vgt_pos_lrn_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_amf_offset_lrn.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_amf_offset_lrn_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_amf_offset_lrn_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_cruise_switch_inputs.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_cruise_switch_inputs_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_cruise_switch_inputs_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_doc_in_temp_acq.h')
HeaderFile('src/p_l/p_l_analogue/src/p_l_doc_in_temp_acq_types.h')
HeaderFile('src/p_l/p_l_analogue/src/p_l_doc_in_temp_acq_private.h')
HeaderFile('src/p_l/p_l_analogue/src/p_l_doc_in_temp_calc.h')
HeaderFile('src/p_l/p_l_analogue/src/p_l_doc_in_temp_calc_types.h')
HeaderFile('src/p_l/p_l_analogue/src/p_l_doc_in_temp_calc_private.h')
HeaderFile('src/p_l/p_l_analogue/src/p_l_egrh_pos_rd.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_egrh_pos_rd_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_egrh_pos_rd_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_esc_lever_signal_mon.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_esc_lever_signal_mon_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_esc_lever_signal_mon_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_esc_lever_signal_mon.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_esc_lever_signal_mon_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_esc_lever_signal_mon_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_fuel_filter_pressure.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_fuel_filter_pressure_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_fuel_filter_pressure_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_intercooler_out_temp_acq.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_intercooler_out_temp_acq_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_intercooler_out_temp_acq_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_oil_level_sensor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_oil_level_sensor_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_oil_level_sensor_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_oil_pressure_sensor.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_oil_pressure_sensor_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_oil_pressure_sensor_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_oil_temp_mdcr.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_oil_temp_mdcr_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_oil_temp_mdcr_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_pedal_foot_posn.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_pedal_foot_posn_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_pedal_foot_posn_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_pedal_hand_posn.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_pedal_hand_posn_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_pedal_hand_posn_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_pedal_selector_switch.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_digital_input/src/p_l_pedal_selector_switch_private.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_digital_input/src/p_l_pedal_selector_switch_types.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_analogue/src/p_l_pressure_lrn.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_pressure_lrn_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_pressure_lrn_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_torque_state_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_torque_state_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_torque_state_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_vgth_pos.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_vgth_pos_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_analogue/src/p_l_vgth_pos_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])

HeaderFile('src/p_l/p_l_can/src/p_l_can.h', OWNER = 'tcg')
HeaderFile('gill_dcm624_code/Software/include/p_l_cc_j1939.h', OWNER = 'tcg')
HeaderFile('gill_dcm624_code/Software/include/icv_esc_input_decode.h', OWNER = 'tcg')
HeaderFile('gill_dcm624_code/Software/include/icv_esc_input_decode_private.h', OWNER = 'tcg')
HeaderFile('gill_dcm624_code/Software/include/icv_esc_input_decode_types.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_aps/src/p_l_aps_tdc_angle_correction.h',OWNER = 'tcg')
HeaderFile('src/p_l/p_l_aps/src/p_l_aps_tdc_angle_correction_private.h',OWNER = 'tcg')
HeaderFile('src/p_l/p_l_aps/src/p_l_aps_tdc_angle_correction_types.h',OWNER = 'tcg')
HeaderFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_engine_op_status.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_engine_op_status_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_engine_op_status_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_idle_shutdown_timers.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_idle_shutdown_timers_private.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_idle_shutdown_timers_types.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_diag_enabler.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_diag_enabler_private.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_diag_enabler_types.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_digital_input/src/P_L_DI_Lib.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_door_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_door_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_door_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_exh_brk_switch_1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_exh_brk_switch_1_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_exh_brk_switch_1_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_eng_brk_switch_1.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_eng_brk_switch_1_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_eng_brk_switch_1_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_flash_lamp_code_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_flash_lamp_code_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_flash_lamp_code_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_immo_switch_state.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_immo_switch_state_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_immo_switch_state_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_low_fuel_level_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_low_fuel_level_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_low_fuel_level_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_oil_pressure_switch.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_digital_input/src/p_l_oil_pressure_switch_private.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_digital_input/src/p_l_oil_pressure_switch_types.h', OWNER = 'tcg')
HeaderFile('src/p_l/p_l_digital_input/src/p_l_pedal_foot_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_pedal_foot_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_pedal_foot_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_pedal_hand_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_pedal_hand_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_pedal_hand_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_seat_belt_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_seat_belt_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_seat_belt_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_starter_switch.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_starter_switch_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_input/src/p_l_starter_switch_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_output/src/p_l_cruise_lamp_driver.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_output/src/p_l_cruise_lamp_driver_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_output/src/p_l_cruise_lamp_driver_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_output/src/p_l_eng_spd_rly_drive.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_output/src/p_l_eng_spd_rly_drive_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_output/src/p_l_eng_spd_rly_drive_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_output/src/p_l_fuel_heater_driver.h')
HeaderFile('src/p_l/p_l_digital_output/src/p_l_fuel_heater_driver_types.h')
HeaderFile('src/p_l/p_l_digital_output/src/p_l_fuel_heater_driver_private.h')
HeaderFile('src/p_l/p_l_digital_output/src/p_l_oil_level_lamp_driver.h')
HeaderFile('src/p_l/p_l_digital_output/src/p_l_oil_level_lamp_driver_types.h')
HeaderFile('src/p_l/p_l_digital_output/src/p_l_oil_level_lamp_driver_private.h')
HeaderFile('src/p_l/p_l_event_input/src/p_l_tyre_wear_adjust.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_event_input/src/p_l_tyre_wear_adjust_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_event_input/src/p_l_tyre_wear_adjust_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_output/src/p_l_ac_comp_relay_drive.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_output/src/p_l_ac_comp_relay_drive_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_digital_output/src/p_l_ac_comp_relay_drive_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_coolant_temp_output.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_coolant_temp_output_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_coolant_temp_output_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_veh_spd_output.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_veh_spd_output_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_veh_spd_output_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_water_in_fuel/src/p_l_water_in_fuel.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_water_in_fuel/src/p_l_water_in_fuel_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_water_in_fuel/src/p_l_water_in_fuel_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/c_c/src/c_c_ac_comp_torque_consump.h')
HeaderFile('src/appli/c_c/src/c_c_ac_comp_torque_consump_types.h')
HeaderFile('src/appli/c_c/src/c_c_ac_comp_torque_consump_private.h')
HeaderFile('src/appli/icv/src/icv_ac_fluid_pres_input_arbit.h')
HeaderFile('src/appli/icv/src/icv_ac_fluid_pres_input_arbit_types.h')
HeaderFile('src/appli/icv/src/icv_ac_fluid_pres_input_arbit_private.h')
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_acquis.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_acquis_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_acquis_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_config.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_config_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_config_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_control.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_control_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_control_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_diagnostic.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_diagnostic_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_diagnostic_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_htr_diag.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_htr_diag_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/p_l/p_l_wraf/src/p_l_wraf_htr_diag_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])
HeaderFile('src/appli/icv/src/icv_amf_selection.h')
HeaderFile('src/appli/icv/src/icv_amf_selection_types.h')
HeaderFile('src/appli/icv/src/icv_amf_selection_private.h')
HeaderFile('src/appli/icv/src/icv_ac_eng_cool_req_sw_select.h')
HeaderFile('src/appli/icv/src/icv_ac_eng_cool_req_sw_select_types.h')
HeaderFile('src/appli/icv/src/icv_ac_eng_cool_req_sw_select_private.h')
HeaderFile('src/p_l/p_l_analogue/src/p_l_boostp_acq.h')
HeaderFile('src/p_l/p_l_analogue/src/p_l_boostp_acq_types.h')
HeaderFile('src/p_l/p_l_analogue/src/p_l_boostp_acq_private.h')
HeaderFile('src/appli/icv/src/icv_boostp_calc.h')
HeaderFile('src/appli/icv/src/icv_boostp_calc_types.h')
HeaderFile('src/appli/icv/src/icv_boostp_calc_private.h')

HeaderFile('src/p_l/p_l_event_input/src/p_l_vss_validate.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM']) 
HeaderFile('src/p_l/p_l_event_input/src/p_l_vss_validate_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])  
HeaderFile('src/p_l/p_l_event_input/src/p_l_vss_validate_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])  
HeaderFile('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_vss_raw_speed_calc.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])  
HeaderFile('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_vss_raw_speed_calc_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])  
HeaderFile('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_vss_raw_speed_calc_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM']) 
HeaderFile('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_vss_loss_detection.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])  
HeaderFile('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_vss_loss_detection_private.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])  
HeaderFile('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_vss_loss_detection_types.h',CC_TYPE = 'spec' , OWNER = 'tcg' , CCFLAGS = ['EXTROM','INTRAM'])  
HeaderFile('src/appli/ici/src/ici_oil_pressure_gauge.h')
HeaderFile('src/appli/ici/src/ici_oil_pressure_gauge_types.h')
HeaderFile('src/appli/ici/src/ici_oil_pressure_gauge_private.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_oilp_gauge_drv_diag.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_oilp_gauge_drv_diag_types.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_oilp_gauge_drv_diag_private.h')
HeaderFile('src/p_l/p_l_digital_output/src/p_l_fan_drive_diag.h')
HeaderFile('src/p_l/p_l_digital_output/src/p_l_fan_drive_diag_types.h')
HeaderFile('src/p_l/p_l_digital_output/src/p_l_fan_drive_diag_private.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_pwm_hp_turbo_driver.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_pwm_hp_turbo_driver_types.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_pwm_hp_turbo_driver_private.h')

HeaderFile('src/appli/icv/src/icv_ac_request_arb.h')
HeaderFile('src/appli/icv/src/icv_ac_request_arb_types.h')
HeaderFile('src/appli/icv/src/icv_ac_request_arb_private.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_imv_drv_diag.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_imv_drv_diag_types.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_imv_drv_diag_private.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_ebrake_diag.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_ebrake_diag_types.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_ebrake_diag_private.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_exh_brk_vlv_drv.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_exh_brk_vlv_drv_types.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_exh_brk_vlv_drv_private.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_engine_speed_gauge_drv_diag.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_engine_speed_gauge_drv_diag_types.h')
HeaderFile('src/p_l/p_l_pwm_output/src/p_l_engine_speed_gauge_drv_diag_private.h')
HeaderFile('src/appli/_appli/src/app_interface_decode.h')
HeaderFile('src/appli/_appli/src/app_interface_decode_types.h')
HeaderFile('src/appli/_appli/src/app_interface_decode_private.h')
HeaderFile('src/appli/icv/src/icv_vehicle_distance.h')
HeaderFile('src/appli/icv/src/icv_vehicle_distance_types.h')
HeaderFile('src/appli/icv/src/icv_vehicle_distance_private.h')
HeaderFile('src/p_l/p_l_water_in_fuel/src/p_l_wif_lamp_drv_diag.h')
HeaderFile('src/p_l/p_l_water_in_fuel/src/p_l_wif_lamp_drv_diag_types.h')
HeaderFile('src/p_l/p_l_water_in_fuel/src/p_l_wif_lamp_drv_diag_private.h')
HeaderFile('src/appli/t_d/src/t_d_idle_target_ext_calc_md.h')
HeaderFile('src/appli/t_d/src/t_d_idle_target_ext_calc_md_types.h')
HeaderFile('src/appli/t_d/src/t_d_idle_target_ext_calc_md_private.h')
HeaderFile('src/s_s/s_s_fault_manager/src/f_m_gen_monitor_cond_eol.h')
HeaderFile('src/s_s/s_s_fault_manager/src/f_m_gen_monitor_cond_eol_private.h')
HeaderFile('src/s_s/s_s_fault_manager/src/f_m_gen_monitor_cond_eol_types.h')

# ==================T55 Files======================
T55File('blois_code_p_l/p_l/p_l_com/MSG/src/P_L_Cc_Bus_Fault.t55')
T55File('blois_code_p_l/p_l/p_l_com/MSG/src/P_L_Cc_Can0_Error.t55')
T55File('blois_code_p_l/p_l/p_l_com/MSG/src/P_L_Cc_Can1_Error.t55')
T55File('blois_code_p_l/p_l/p_l_com/UDS/src/P_L_Com_Rst_Jmp_Calc.t55')
T55File('blois_code_p_l/p_l/p_l_ecu/Misc/src/P_L_Dig_Outp_Cu_Relay_Drv.t55')
T55File('blois_code_p_l/p_l/p_l_ecu/Misc/src/P_L_Ecu_Case_Temp_Aqui.t55')
T55File('blois_code_p_l/p_l/p_l_ecu/Misc/src/P_L_Ecu_Hw_Tag_Read.t55')
T55File('blois_code_p_l/p_l/p_l_ecu/NVM/src/P_L_Nvm_Data.t55')
T55File('blois_code_p_l/p_l/p_l_in/Driver/src/P_L_Neutral_Gear_Sw_State.t55')
T55File('blois_code_p_l/p_l/p_l_in/Engine/src/p_l_amf_freq_handler_dd.t55')
T55File('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Egrh_Feedback_Position.t55')
T55File('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Batt_Current_Acqu.t55')
T55File('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Batt_Temp_Acqu.t55')
T55File('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Engine_Inj_Counter_Calc.t55')
T55File('blois_code_p_l/p_l/p_l_in/Lambda/src/P_L_Wraf_Dfco_Calc.t55')
T55File('blois_code_p_l/p_l/p_l_in/Engine/src/P_L_Thrtl_Feedback_Position.t55')
T55File('blois_code_p_l/p_l/p_l_in/Vehicle/src/P_L_Battery_Voltage.t55')
T55File('blois_code_p_l/p_l/p_l_in/Lambda/src/P_L_Wraf_Global_Condition.t55')
T55File('blois_code_p_l/p_l/p_l_in/Lambda/src/P_L_Wraf_Interface_Calc.t55')
T55File('blois_code_p_l/p_l/p_l_in/Lambda/src/P_L_Wraf_Plausibility_Test.t55')
T55File('blois_code_p_l/p_l/p_l_in/Lambda/src/P_L_Wraf_Snapshot_Calc.t55')
T55File('blois_code_p_l/p_l/p_l_in/Px/src/P_L_Atm_Pres_Aquisition.t55')
T55File('blois_code_p_l/p_l/p_l_in/Px/src/P_L_Baro_Sensor_Diag.t55')
T55File('blois_code_p_l/p_l/p_l_in/Px/src/P_L_Map_Acquisition.t55')
T55File('blois_code_p_l/p_l/p_l_in/Px/src/P_L_P3_Acquisition.t55')
T55File('blois_code_p_l/p_l/p_l_in/Px/src/P_L_P3_Processing.t55')
T55File('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Dpf_In_Temp_Aquisition.t55')
T55File('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Intake_Plenum_Temp_Aqui.t55')
T55File('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Inlet_Air_Temp_Deter.t55')
T55File('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Inlet_Digital_Acq.t55')
T55File('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Inlet_Digital_Diag.t55')
T55File('blois_code_p_l/p_l/p_l_in/Tx/src/P_L_Turb_In_Temp_Aquisition.t55')
T55File('blois_code_p_l/p_l/p_l_out/ICI/src/P_L_Ici_Glow_Plug_Lamp_Out.t55')
T55File('blois_code_p_l/p_l/p_l_out/Misc/src/P_L_Electrical_Tests.t55')
T55File('blois_code_p_l/p_l/p_l_out/SAC/src/P_L_Glow_Plug_Diagnosis.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Egrh_Pos_Ctrl_Sched.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Egr_Hp_Vlv_Pos_Ctrl.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Egrh_Valve_Power_On.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Egrh_Valve_Antistuck.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Egrh_Valve_Cleaning.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Egr_Hp_Vlv_Learning.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Egr_Hp_Vlv_Run_Learning.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Egr_Hp_Valve_Diag.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Ext_Pratio_Limit_Corr.t55')
T55File('blois_soft_vob/Software/Appli/afc/src/AFC_Total_Fuel_Calc.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Valve_Antistuck.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Valve_Cleaning.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Vlv_Learning.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Vlv_Pos_Ctrl.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Valve_Diag.t55')
T55File('blois_soft_vob/Software/Appli/acm/src/ACM_Thrtl_Valve_Power_On.t55')

T55File('blois_soft_vob/Software/Appli/asm/src/ASM_Charge_Mode.t55')
T55File('blois_soft_vob/Software/Appli/asm/src/ASM_Diagnostic.t55')
T55File('blois_soft_vob/Software/Appli/asm/src/ASM_Performance_Mode.t55')
T55File('blois_soft_vob/Software/Appli/asm/src/ASM_Regulate_Calc.t55')
T55File('blois_soft_vob/Software/Appli/asm/src/ASM_Soc_Rationality.t55')
T55File('blois_soft_vob/Software/Appli/asm/src/ASM_Soc_Refresh.t55')
T55File('blois_soft_vob/Software/Appli/c_c/src/c_c.t55')
T55File('blois_soft_vob/Software/Appli/c_i/_c_i/src/C_I_Maps.t55')
T55File('blois_soft_vob/Software/Appli/c_i/c_i_sec/src/C_I_Sec_Async_Interface.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/DTI_Fault_Controler.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/DTI_Fuel_Lift_Pump_Test.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dpf_Regen_Idle.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/dti_iso_dpf_rgn_veh_run_mod.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/dti_iso_dyn_prim_rvd_tst_dd.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/dti_iso_dyn_rpc_pid_calib_dd.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Dyn_Sub.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_Inj_Tst_Cond_Chk.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/DTI_Iso_State_Machine_Calc.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/dti_iso_sub.t55')
T55File('blois_soft_vob/Software/Appli/dti/src/DTI_Lamp_Test.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Actual_Torque_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Anti_Oscillation_Plau.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Battery_Voltage_Mon.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Brake_Plausibility.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Can_J1939_Rxdiag_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Control_Inj_Locking.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Cruise_Control_Monitor.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Cruise_Driver_Switch.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Deter_Clutch_State.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Electrical_Test.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Eng_Cool_Temp_Plau.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Engine_Speed_Plau_Chk.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Env_Param_Interface.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Env_Param_Plausibility.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Gear_Ratio_Monitor.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Gsa_Plausibility.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Ignition_Switch_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Keyword_Serv_Plau_Chk.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_L2_Scheduler.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_L2p_Torque_Manager.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_L3_Scheduler.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Mdp_Supervisor_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Memory_Integrity_Global.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Memory_Integrity_Test.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Md_Zero_Torque_Dmnd_Detect.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Mic_Callback_Update.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Monitoring_Mod_Rst_Ctrl.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Open_Delay_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_PMC_Offset_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Program_Flow_Check.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Foot_Pedal_Validity_Check.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Permissible_Torque_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Brc_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Brsc_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_C2i_Off_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Cyl_Bal_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Cylp_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Fuel_T_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Fvc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Mdp_Trim.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_Mon_Tuned_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulse_To_Fuel_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulses_Correlation.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Pulses_Plausibility.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Qadc_Test_Deter.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Rail_Pressure_Plau_Chk.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Torque_Demand_Calc.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Torque_Manager.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Vehicle_Speed_Plau.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Vss_Callback.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Asg_Plausibility.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Zero_Pulse_Detection.t55')
T55File('blois_soft_vob/Software/Appli/esm/src/ESM_Zero_Torque_Dmnd_Detect.t55')
T55File('blois_soft_vob/Software/Appli/fqd/src/FQD_Cumul_Inj_Fuel_Calc.t55')
T55File('blois_soft_vob/Software/Appli/fdc/src/FDC_Normal_Mode_Select.t55')
T55File('blois_soft_vob/Software/Appli/i_c/i_c_accelerometer/src/I_C_Accel_Data.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_background_sync.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_background_task.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Bal_Enabling_Async.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_balance_injectors.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Brsc_Offset_Calc.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_calc_c2i_pulse_offset.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Calc_Pulse_Link.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Calc_Pulse_Ton.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Calc_Ton_Corrected.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Calc_Ton_Estimated.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_cylp_bkg_calc.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/i_c_cylp_sync_calc.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Inj_Alloc_Pulse_Dmnd.t55')
T55File('blois_soft_vob/Software/Appli/i_c/_i_c/src/I_C_Inj_Dmnd_Sel.t55')
T55File('blois_soft_vob/Software/Appli/ici/src/ICI_Mi_Lamp_Output_Dmnd.t55')
T55File('blois_soft_vob/Software/Appli/ici/src/ici_lop_lamp_control.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/icv.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Air_Temp_Selection_Calc.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Alternator_Torque_Calc.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Clutch_Top_Bottom_Diag.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/icv_coolant_temp_calc.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Cruise_Target_Calc.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Deter_Clutch_State.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Exh_Gas_Characteristics.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Exhaust_Temp_Selection.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Gsi_Activation_Calc.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Interface_Calc.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Key_Position_Deter.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/icv_monitor_brake_switches.t55')
T55File('blois_soft_vob/Software/Appli/icv/src/ICV_Vspdl_Target.t55')
T55File('blois_soft_vob/Software/Appli/p_t/src/p_t.t55')
T55File('blois_soft_vob/Software/Appli/rpc/src/rpc.t55')
T55File('blois_soft_vob/Software/Appli/rpc/src/rpc_bkg_overpress_dur_calc_dd.t55')
T55File('blois_soft_vob/Software/Appli/rpc/src/rpc_bkg_overpress_flt_det_dd.t55')
T55File('blois_soft_vob/Software/Appli/rpc/src/rpc_bkg_async_calc_dd.t55')
T55File('blois_soft_vob/Software/Appli/rpc/src/rpc_bkg_sync_calc_dd.t55')
T55File('blois_soft_vob/Software/Appli/rpc/src/RPC_Hp_Async_Cntrl.t55')
T55File('blois_soft_vob/Software/Appli/rpc/src/RPC_Hp_Crt_Dmnd_Calc.t55')
T55File('blois_soft_vob/Software/Appli/rpc/src/rpc_vlc_control_dd.t55')
T55File('blois_soft_vob/Software/Appli/sac/src/sac_glow_plug_control.t55')
T55File('blois_soft_vob/Software/Appli/smc/src/SMC_Control_Function_Call.t55')
T55File('blois_soft_vob/Software/Appli/smc/src/smc_control_system_mode.t55')
T55File('blois_soft_vob/Software/Appli/smc/src/SMC_Determine_Engine_State.t55')
T55File('blois_soft_vob/Software/Appli/smc/src/SMC_Determine_Engine_Time.t55')
T55File('blois_soft_vob/Software/Appli/smc/src/SMC_Dfco_Id_Allowed_Calc.t55')
T55File('blois_soft_vob/Software/Appli/smc/src/SMC_Sens_Act_Supply.t55')
T55File('blois_soft_vob/Software/Appli/ste/src/ste_supervisor.t55')
T55File('blois_soft_vob/Software/Appli/t_d/src/T_D_Aos_Interface.t55')
T55File('blois_soft_vob/Software/Appli/t_d/src/T_D_Idle_Target_Offset.t55')
T55File('blois_soft_vob/Software/Appli/t_d/src/t_d_vsl_high_pres_system_dd.t55')
T55File('blois_soft_vob/Software/Appli/t_d/src/t_d_vsl_inj_calc_dd.t55')
T55File('blois_soft_vob/Software/Appli/t_d/src/T_D_Vag_Calc.t55')
T55File('blois_soft_vob/Software/Appli/t_d/src/T_D_Vag_Virtual_Pedal_Pos.t55')
T55File('blois_soft_vob/Software/P_L/p_l_amf/src/P_L_Amf_Chip_Heating.t55')
T55File('blois_soft_vob/Software/P_L/p_l_amf/src/P_L_Amf_Acq_Supervisor.t55')

T55File('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Boostp_Calc.t55')
T55File('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_coolant_temp_calc.t55')
T55File('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_dpf_diff_press_calc.t55')
T55File('blois_soft_vob/Software/P_L/p_l_analogue/src/p_l_fuel_temp_calc.t55')
T55File('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Map_Calc.t55')
T55File('blois_soft_vob/Software/P_L/p_l_analogue/src/P_L_Monitor_Rail_Pressure.t55')
T55File('blois_soft_vob/Software/P_L/p_l_com/_p_l_com/src/p_l_com.t55')
T55File('blois_soft_vob/Software/P_L/p_l_com/p_l_cc/_p_l_cc/src/p_l_cc_sub.t55')
T55File('blois_soft_vob/Software/P_L/p_l_com/p_l_cds/src/p_l_cds_sub.t55')
T55File('blois_soft_vob/Software/P_L/p_l_digital_input/src/P_L_Brk_Light_Sw_State.t55')
T55File('blois_soft_vob/Software/P_L/p_l_digital_input/src/P_L_Brk_Safety_Sw_State.t55')
T55File('blois_soft_vob/Software/P_L/p_l_digital_input/src/P_L_Clutch_Sw_Bot_State.t55')
T55File('blois_soft_vob/Software/P_L/p_l_digital_input/src/P_L_Clutch_Sw_Top_State.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Ecu_Reboot.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Low_Prio_Calc.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Low_Prio_Dtc.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Mm_Trip_Detection.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Pls_Ring_Bf_Chk_Act.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Pls_Ring_Buf_Meas.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Power_Latch_Mngt.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Query_Reply_Mgnt.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Reset_Info_Deter.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Hard_Lock_Mon.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Sub.t55')
T55File('blois_soft_vob/Software/P_L/p_l_esm/src/P_L_Esm_Tpu_Diag_Ctrl.t55')
T55File('blois_soft_vob/Software/P_L/p_l_event_input/src/p_l_calc_bal_delta_speed.t55')
T55File('blois_soft_vob/Software/P_L/p_l_event_input/src/P_L_Clock_Drift_Monitor.t55')
T55File('blois_soft_vob/Software/P_L/p_l_hbridge_output/src/P_L_Hbridge.t55')
T55File('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_ecu_temp_limit.t55')
T55File('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_injection.t55')
T55File('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_injection_data.t55')
T55File('blois_soft_vob/Software/P_L/p_l_injection/src/p_l_inj_hard_lock_mon.t55')
T55File('blois_soft_vob/Software/P_L/p_l_nvm/src/p_l_nvm_sub.t55')
T55File('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Alternator_Driver.t55')
T55File('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Hpv_Bkg_Cl_Calc.t55')
T55File('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Hpv_Cl_Drv.t55')
T55File('blois_soft_vob/Software/P_L/p_l_pwm_output/src/P_L_Pwm_Hpv_Vsep_Outp_Drv.t55')
T55File('blois_soft_vob/Software/P_L/p_l_self_diag/src/P_L_Cpu_Load_Measure.t55')
T55File('blois_soft_vob/Software/P_L/p_l_wraf/src/P_L_Wraf_Heater_Mode.t55')
T55File('blois_soft_vob/Software/P_L/p_l_wraf/src/P_L_Wraf_Resp_Diag_Fuel_Cut.t55')
T55File('blois_soft_vob/Software/P_L/p_l_wraf/src/P_L_Wraf_Sensor_Read.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/f_m.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Add_Fault_Snap_Dat_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_B1_Counters_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Bulb_Chk_Lamp_Flash_Det.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Conf_Time_Counter_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Conf_Wo_Dcy_Enable_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Config_Hd_Sub.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Config_Sub.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Deletion_Services_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Etc_Config_Sub.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Etc_State_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Etc_Sub.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Fault_Counters_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Fid_Sub.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Flt_Fid_Function_Lib.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Flt_Group_Function_Lib.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Function_Lib.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Gen_Monitor_Cond_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Hd_Sub.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Ignition_Cycle_Detect.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Induc_Detection_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Log_Disable_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mil_Handling_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Mode6_Missing_Value.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Monitor_Driving_Cycle.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Obd_Dynamic_Counters.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Obd_Dynamic_Fault.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Obd_Etc_Dynamic.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Obd_Readiness_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Rbm_Track_Report_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Read_Dtc_Info.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Reset_And_Mil_Counters.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Veh_Time_Power_Off_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Vehicle_Total_Time_Calc.t55')
T55File('blois_soft_vob/Software/S_S/s_s_fault_manager/src/F_M_Warm_Up_Cycle_Detect.t55')
T55File('gill_dcm624_code/Software/_Software/src/blois_generic.t55')
T55File('gill_dcm624_code/Software/_Software/src/hwi.t55')
T55File('gill_dcm624_code/Software/Appli/_Appli/src/app.t55')
T55File('gill_dcm624_code/Software/Appli/_Appli/src/application_stub.t55')
T55File('gill_dcm624_code/Software/Appli/dti/src/dti.t55')
T55File('gill_dcm624_code/Software/P_L/_P_l/src/p_l.t55')
T55File('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Adc.t55')
T55File('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Di.t55')
T55File('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Do.t55')
T55File('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Hb.t55')
T55File('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Pwm.t55')
T55File('gill_dcm624_code/Software/P_L/_P_l/src/P_L_Binding_Spi.t55')
T55File('gill_dcm624_code/Software/S_S/s_s_fault_manager/src/F_M_Fault.t55')
T55File('src/appli/_appli/src/app_interface_decoding_dd.t55')
T55File('src/appli/acm/src/acm.t55')
T55File('src/appli/acm/src/acm_2st_vgt_bst_diag_dd.t55')
T55File('src/appli/acm/src/acm_2st_vgt_comp_prd_dd.t55')
T55File('src/appli/acm/src/acm_2st_vgt_pos_dmnd_dd.t55')
T55File('src/appli/acm/src/acm_2st_vgt_prot_dd.t55')
T55File('src/appli/acm/src/acm_2st_vgt_temp_prot_dd.t55')
T55File('src/appli/acm/src/acm_amf_cor_diag_dd.t55')
T55File('src/appli/acm/src/acm_amf_cor_err_calc_dd.t55')
T55File('src/appli/acm/src/acm_amf_cor_lrn_dd.t55')
T55File('src/appli/acm/src/acm_amf_corr_calc_dd.t55')
T55File('src/appli/acm/src/acm_amf_filter_dd.t55')
T55File('src/appli/acm/src/acm_anti_surge_dd.t55')
T55File('src/appli/acm/src/acm_desired_air_dd.t55')
T55File('src/appli/acm/src/acm_desired_map_dd.t55')
T55File('src/appli/acm/src/acm_egr_flow_diag_dd.t55')
T55File('src/appli/acm/src/acm_egr_misfire_dd.t55')
T55File('src/appli/acm/src/acm_egr_rate_dmnd_dd.t55')
T55File('src/appli/acm/src/acm_egr_rate_limit_dd.t55')
T55File('src/appli/acm/src/acm_egr_st_est_dd.t55')
T55File('src/appli/acm/src/acm_egrh_cool_byp_dd.t55')
T55File('src/appli/acm/src/acm_egrh_flow_est_dd.t55')
T55File('src/appli/acm/src/acm_egrh_pos_dmnd_dd.t55')
T55File('src/appli/acm/src/acm_eng_brk_enable_dd.t55')
T55File('src/appli/acm/src/acm_exh_brk_pres_ctrl_dd.t55')
T55File('src/appli/acm/src/acm_exh_flow_est_bkg_dd.t55')
T55File('src/appli/acm/src/acm_exh_flow_est_sync_dd.t55')
T55File('src/appli/acm/src/acm_flow_corr_dd.t55')
T55File('src/appli/acm/src/acm_flow_corr_diag_dd.t55')
T55File('src/appli/acm/src/acm_intake_flow_est_dd.t55')
T55File('src/appli/acm/src/acm_throt_enable_dd.t55')
T55File('src/appli/acm/src/acm_throt_fl_lrn_dd.t55')
T55File('src/appli/acm/src/acm_throt_map_dmnd_dd.t55')
T55File('src/appli/acm/src/acm_throt_pos_dmnd_dd.t55')
T55File('src/appli/acm/src/acm_valve_comp_dd.t55')
T55File('src/appli/acm/src/acm_vgt_bst_dmnd_dd.t55')
T55File('src/appli/acm/src/acm_vgt_max_pratio_dd.t55')
T55File('src/appli/acm/src/acm_vgth_pos_ctrl_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_ac_fluid_press_ana_sig_acq_dd.t55')
T55File('src/appli/acm/src/acm_vol_filling_dd.t55')
T55File('src/appli/afc/src/afc.t55')
T55File('src/appli/afc/src/afc_air_fuel_ratio_dd.t55')
T55File('src/appli/afc/src/afc_dpf_out_afr_dd.t55')
T55File('src/appli/afc/src/afc_dsrd_afr_dd.t55')
T55File('src/appli/afc/src/afc_post2_control_dd.t55')
T55File('src/appli/afc/src/afc_smoke_limit_dd.t55')
T55File('src/appli/afc/src/afc_smoke_limit_fuel_dd.t55')
T55File('src/appli/afc/src/afc_wraf_blm_enable_dd.t55')
T55File('src/appli/afc/src/afc_wraf_blm_learn_dd.t55')
T55File('src/appli/afc/src/afc_wraf_cl_loop_dd.t55')
T55File('src/appli/afc/src/afc_wraf_control_dd.t55')
T55File('src/appli/afc/src/afc_wraf_diag_dd.t55')
T55File('src/appli/afc/src/afc_wraf_fuel_blm_dd.t55')
T55File('src/appli/afc/src/afc_wraf_resp_diag_dd.t55')
T55File('src/appli/c_c/src/c_c_ac_management_dd.t55')
T55File('src/appli/dti/src/DTI_Iso_Eng_Spd_Rly_Test.t55')
T55File('src/appli/dti/src/DTI_Iso_Fuel_Htr_Rly_Test.t55')
T55File('src/appli/dti/src/DTI_Iso_Hpv_Test.t55')
T55File('src/appli/dti/src/dti_iso_dyn_reset_amf_val_dd.t55')
T55File('src/appli/dti/src/dti_iso_dyn_reset_aps_val_dd.t55')
T55File('src/appli/dti/src/dti_iso_dyn_reset_atc_val.t55')
T55File('src/appli/dti/src/dti_iso_dyn_reset_cdpf_val_dd.t55')
T55File('src/appli/dti/src/dti_iso_dyn_reset_hpp_val_dd.t55')
T55File('src/appli/dti/src/dti_iso_dyn_reset_imv_val_dd.t55')
T55File('src/appli/dti/src/dti_iso_dyn_reset_inj_val_dd.t55')
T55File('src/appli/dti/src/DTI_Iso_Engine_Speed_Freq_Tst.t55')
T55File('src/appli/dti/src/DTI_Iso_Exh_Brk_Pwm_Test.t55')
T55File('src/appli/dti/src/DTI_Iso_Mode_Maf_Learning.t55')
T55File('src/appli/dti/src/dti_iso_mode_pwr_sup_rly.t55')
T55File('src/appli/dti/src/dti_pilot_cut_1inj.t55')
T55File('src/appli/dti/src/dti_pilot_cut_all_inj.t55')
T55File('src/appli/esm/src/ESM_Brake_Fault_Freeze.t55') 
T55File('src/appli/esm/src/ESM_Can_0_Dmnd_Calc.t55')
T55File('src/appli/esm/src/ESM_Can_Cc_Buttons.t55')
T55File('src/appli/esm/src/ESM_Can_J1939_Ped_Arb_Calc.t55')
T55File('src/appli/esm/src/ESM_Can_Pedal_Eec2.t55')
T55File('src/appli/esm/src/ESM_Can_Pto.t55')
T55File('src/appli/esm/src/ESM_Can_Tsc1_Plaus_dd.t55')
T55File('src/appli/esm/src/ESM_Clutch_Position_Calc.t55')
T55File('src/appli/esm/src/ESM_Esc_Decoding.t55')
T55File('src/appli/esm/src/ESM_Exh_Brk_Switch_Req.t55')
T55File('src/appli/esm/src/ESM_Exhaust_Brake_Acq.t55')
T55File('src/appli/esm/src/ESM_Foot_Hand_Pedal_Arbitration.t55')
T55File('src/appli/esm/src/ESM_Hand_Pedal_Validity_Check.t55')
T55File('src/appli/esm/src/ESM_Injector_Cooling_Monitor.t55')
T55File('src/appli/esm/src/ESM_Park_Brake_Sw_Signal.t55')
T55File('src/appli/esm/src/ESM_Pedal_Select_Calc.t55')
T55File('src/appli/esm/src/ESM_Pedal_To_Ground_Test.t55')
T55File('src/appli/esm/src/ESM_Vehicle_Speed_Sensor.t55')
T55File('src/appli/esm/src/ESM_Vdg_Rpm_Offset_Decode.t55')
T55File('src/appli/etc/src/etc_fan_management_md_dd.t55')
T55File('src/appli/eud/src/eud.t55')
T55File('src/appli/eud/src/eud_distance_calculations_dd.t55')
T55File('src/appli/eud/src/eud_fuel_calculations_dd.t55')
T55File('src/appli/eud/src/eud_hp_opening_counter_dd.t55')
T55File('src/appli/eud/src/eud_save_eng_hrs_dd.t55')
T55File('src/appli/eud/src/eud_timer_calculations_dd.t55')
T55File('src/appli/fdc/src/fdc.t55')
T55File('src/appli/fdc/src/fdc_after_mode_dd.t55')
T55File('src/appli/fdc/src/fdc_dis_pilot_post_dd.t55')
T55File('src/appli/fdc/src/fdc_pilot_mode_dd.t55')
T55File('src/appli/fqd/src/fqd_after_dmnd_dd.t55')
T55File('src/appli/fqd/src/fqd_bkg_snapshot_dd.t55')
T55File('src/appli/fqd/src/fqd_desired_fuel_dd.t55')
T55File('src/appli/fqd/src/fqd_pilot_dmnd_dd.t55')
T55File('src/appli/fqd/src/fqd_post_air_ctrl_dd.t55')
T55File('src/appli/fqd/src/fqd_post1_dmnd_dd.t55')
T55File('src/appli/fqd/src/fqd_post2_dmnd_dd.t55')
T55File('src/appli/fqd/src/fqd_post2_snapshot_dd.t55')
T55File('src/appli/fqd/src/fqd_smoke_limit_dd.t55')
T55File('src/appli/ici/src/ici_engine_speed_output_mdcr_dd.t55')
T55File('src/appli/ici/src/ici_glow_plug_lamp_control_dd.t55')
T55File('src/appli/icv/src/icv_ac_eng_cool_req_sw_select_dd.t55')
T55File('src/appli/icv/src/icv_cc_asl_interface_dd.t55')
T55File('src/appli/icv/src/icv_calc_agb_output_dd.t55')
T55File('src/appli/icv/src/icv_calc_veh_speed_data_dd.t55')
T55File('src/appli/icv/src/icv_cruise_req_md_dd.t55')
T55File('src/appli/icv/src/icv_cruise_src_select_mdcr_dd.t55')
T55File('src/appli/icv/src/icv_esc_input_decode_dd.t55')
T55File('src/appli/icv/src/icv_eng_brk_switch_dd.t55')
T55File('src/appli/icv/src/icv_exh_brk_switch_dd.t55')
T55File('src/appli/icv/src/icv_exh_over_temp_monitor_dd.t55')
T55File('src/appli/icv/src/icv_ext_temp_dd.t55')
T55File('src/appli/icv/src/icv_flashing_code_ena_dd.t55')
T55File('src/appli/icv/src/icv_fuel_consumption_dd.t55')
T55File('src/appli/icv/src/icv_fuel_filter_pressure_dd.t55')
T55File('src/appli/icv/src/icv_gear_state_dd.t55')
T55File('src/appli/icv/src/ICV_Gsi_Display_Management.t55')
T55File('src/appli/icv/src/ICV_Gsi_Driver_Behavior.t55')
T55File('src/appli/icv/src/ICV_Gsi_Eng_Pow_Optim_Calc.t55')
T55File('src/appli/icv/src/ICV_Gsi_Inhibition_Calc.t55')
T55File('src/appli/icv/src/ICV_Gsi_Law_Select_Calc.t55')
T55File('src/appli/icv/src/ICV_Gsi_Pedal_Position_Calc.t55')
T55File('src/appli/icv/src/ICV_Gsi_Raw_Gear_Calc.t55')
T55File('src/appli/icv/src/icv_interface_decoding_dd.t55')
T55File('src/appli/icv/src/icv_kickdown_detection_dd.t55')
T55File('src/appli/icv/src/ICV_Interface_Gsi_Strategy.t55')
T55File('src/appli/icv/src/icv_low_fuel_level_detection_dd.t55')
T55File('src/appli/icv/src/icv_oil_level_monitor_dd.t55')
T55File('src/appli/icv/src/icv_oil_pressure_dd.t55')
T55File('src/appli/icv/src/icv_oil_temp_dd.t55')
T55File('src/appli/icv/src/icv_pedal_arbitration_switch_dd.t55')
T55File('src/appli/icv/src/icv_pedal_hand_fault_wrapper_dd.t55')
T55File('src/appli/icv/src/icv_pedal_foot_fault_wrapper_dd.t55')
T55File('src/appli/icv/src/icv_pedal_foot_pos_dd.t55')
T55File('src/appli/icv/src/icv_pedal_hand_pos_dd.t55')
T55File('src/appli/icv/src/icv_torque_state_switch_dd.t55')
T55File('src/appli/icv/src/icv_vac_act_dd.t55')
T55File('src/appli/icv/src/icv_veh_spd_limit_interface_dd.t55')
T55File('src/appli/itd/src/itd_after_dmnd_dd.t55')
T55File('src/appli/itd/src/ITD_Bkg_Snapshot.t55')
T55File('src/appli/itd/src/itd_main_dmnd_dd.t55')
T55File('src/appli/itd/src/itd_mbt_timing_dd.t55')
T55File('src/appli/itd/src/itd_pilot_dmnd_dd.t55')
T55File('src/appli/itd/src/itd_post1_dmnd_dd.t55')
T55File('src/appli/itd/src/itd_post2_dmnd_dd.t55')
T55File('src/appli/p_p/src/p_p_run_dry_strategy_dd.t55')
T55File('src/appli/p_t/src/p_t_comb_mode_dd.t55')
T55File('src/appli/p_t/src/p_t_comb_trans_reset_dd.t55')
T55File('src/appli/p_t/src/p_t_dew_point_turbine_dd.t55')
T55File('src/appli/p_t/src/p_t_dew_point_dpf_dd.t55')
T55File('src/appli/p_t/src/p_t_dfco_ctrl_dd.t55')
T55File('src/appli/p_t/src/p_t_doc_aging_dd.t55')
T55File('src/appli/p_t/src/p_t_doc_diag_dd.t55')
T55File('src/appli/p_t/src/p_t_dpf_diag_leak_dd.t55')
T55File('src/appli/p_t/src/p_t_dpf_eff_mon_dd.t55')
T55File('src/appli/p_t/src/p_t_doc_lightoff_dd.t55')
T55File('src/appli/p_t/src/p_t_dpf_diag_dd.t55')
T55File('src/appli/p_t/src/p_t_dpf_in_temp_trgt_dd.t55')
T55File('src/appli/p_t/src/p_t_dpf_reg_crit_cond_dd.t55')
T55File('src/appli/p_t/src/p_t_dpf_reg_oxy_ctrl_dd.t55')
T55File('src/appli/p_t/src/p_t_dpf_regen_en_dd.t55')
T55File('src/appli/p_t/src/p_t_engine_out_water_dd.t55')
T55File('src/appli/p_t/src/p_t_exh_air_fuel_trgt_dd.t55')
T55File('src/appli/p_t/src/p_t_nox_flow_acc_dd.t55')
T55File('src/appli/p_t/src/p_t_nox_flow_est_dd.t55')
T55File('src/appli/pse/src/pse.t55')
T55File('src/appli/pse/src/pse_2st_press_dd.t55')
T55File('src/appli/pse/src/pse_2st_vgt_pos_calc_dd.t55')
T55File('src/appli/pse/src/pse_boost_est_dd.t55')
T55File('src/appli/pse/src/pse_press_diag_dd.t55')
T55File('src/appli/pse/src/pse_press_est_dd.t55')
T55File('src/appli/rpc/src/rpc_interface_dd.t55')
T55File('src/appli/rpd/src/rpd_rail_press_dmnd_dd.t55')
T55File('src/appli/rpd/src/RPD_Rail_Pres_Dmnd_Filter_dd.t55')
T55File('src/appli/sac/src/sac_fuel_heater_control_mdcr_dd.t55')
T55File('src/appli/smc/src/smc_starter_cntrl_mdcr_dd.t55')
T55File('src/appli/smc/src/smc_system_mode_dmnd_dd.t55')
T55File('src/appli/ste/src/ste_railp_tst_cntrl_dd.t55')
T55File('src/appli/t_d/src/t_d.t55')
T55File('src/appli/t_d/src/t_d_access_torq_dd.t55')
T55File('src/appli/t_d/src/t_d_actual_torq_dd.t55')
T55File('src/appli/t_d/src/T_D_Aos_Enabling_dd.t55')
T55File('src/appli/t_d/src/t_d_aos_torque_calc_dd.t55')
T55File('src/appli/t_d/src/t_d_asg_torq_interface_dd.t55')
T55File('src/appli/t_d/src/t_d_bkg_snapshot_dd.t55')
T55File('src/appli/t_d/src/t_d_can_rx_torq_dd.t55')
T55File('src/appli/t_d/src/t_d_comb_limit_torque_dd.t55')
T55File('src/appli/t_d/src/t_d_corr_terms_dd.t55')
T55File('src/appli/t_d/src/t_d_crank_torq_dd.t55')
T55File('src/appli/t_d/src/t_d_dfco_dd.t55')
T55File('src/appli/t_d/src/t_d_driveability_dd.t55')
T55File('src/appli/t_d/src/t_d_driver_torq_dd.t55')
T55File('src/appli/t_d/src/t_d_dsrd_imep_air_dd.t55')
T55File('src/appli/t_d/src/t_d_engine_load_dd.t55')
T55File('src/appli/t_d/src/t_d_engine_load_ref_dd.t55')
T55File('src/appli/t_d/src/t_d_engine_power_dd.t55')
T55File('src/appli/t_d/src/t_d_engine_torq_dd.t55')
T55File('src/appli/t_d/src/t_d_fuel_fast_dd.t55')
T55File('src/appli/t_d/src/t_d_fuel_slow_dd.t55')
T55File('src/appli/t_d/src/t_d_idle_arbitr_dd.t55')
T55File('src/appli/t_d/src/t_d_idle_cntrl_dd.t55')
T55File('src/appli/t_d/src/t_d_idle_fast_dd.t55')
T55File('src/appli/t_d/src/t_d_idle_gains_ext_dd.t55')
T55File('src/appli/t_d/src/t_d_idle_pid_dd.t55')
T55File('src/appli/t_d/src/t_d_idle_slow_dd.t55')
T55File('src/appli/t_d/src/t_d_idle_spd_error_dd.t55')
T55File('src/appli/t_d/src/t_d_imep_no_aos_dd.t55')
T55File('src/appli/t_d/src/t_d_induced_torq_dd.t55')
T55File('src/appli/t_d/src/t_d_interface_decoding_dd.t55')
T55File('src/appli/t_d/src/t_d_j1939_output_dd.t55')
T55File('src/appli/t_d/src/t_d_max_brk_trq_ext_dd.t55')
T55File('src/appli/t_d/src/t_d_max_fuel_torque_dd.t55')
T55File('src/appli/t_d/src/t_d_max_torque_dd.t55')
T55File('src/appli/t_d/src/t_d_pedal_torq_dd.t55')
T55File('src/appli/t_d/src/t_d_reduced_torq_dd.t55')
T55File('src/appli/t_d/src/t_d_retard_torque_calc_dd.t55')
T55File('src/appli/t_d/src/t_d_smoke_torq_dd.t55')
T55File('src/appli/t_d/src/t_d_th_comb_eff_dd.t55')
T55File('src/appli/t_d/src/t_d_timing_eff_dd.t55')
T55File('src/appli/t_d/src/t_d_torq_conv_dd.t55')
T55File('src/appli/t_d/src/t_d_torq_select_dd.t55')
T55File('src/appli/t_d/src/t_d_torque_fast_dd.t55')
T55File('src/appli/t_d/src/t_d_torque_slow_dd.t55')
T55File('src/appli/t_d/src/t_d_vdg_enable_dd.t55')
T55File('src/appli/t_d/src/t_d_vdg_eng_spd_lim_interface_dd.t55')
T55File('src/appli/t_d/src/t_d_vdg_pid_dmnd_dd.t55')
T55File('src/appli/t_d/src/t_d_vdg_speed_dmnd_dd.t55')
T55File('src/appli/t_d/src/t_d_vsl_low_pres_system_dd.t55')
T55File('src/appli/t_d/src/t_d_wheel_torq_dd.t55')
T55File('src/appli/tse/src/tse_ambient_air_dd.t55')
T55File('src/appli/tse/src/tse_comp_in_limit_dd.t55')
T55File('src/appli/tse/src/tse_comp_in_temp_est_dd.t55')
T55File('src/appli/tse/src/tse_egrh_cool_temp_dd.t55')
T55File('src/appli/tse/src/tse_egrh_temp_est_dd.t55')
T55File('src/appli/tse/src/tse_engine_out_dd.t55')
T55File('src/appli/tse/src/tse_exh_exo_eff_dd.t55')
T55File('src/appli/tse/src/tse_exhaust_temp_dd.t55')
T55File('src/appli/tse/src/tse_oil_temp_dd.t55')
T55File('src/appli/tse/src/tse_t2_est_dd.t55')
T55File('src/appli/tse/src/tse_temp_diag_dd.t55')
T55File('src/appli/tse/src/tse_temp_diag_xc_dd.t55')
T55File('src/appli/tse/src/tse_temp_est_dd.t55')
T55File('src/appli/tse/src/tse_temp_init_dd.t55')
T55File('src/appli/tse/src/tse_temp_sensors_dd.t55')
T55File('src/appli/tse/src/tse_turb_dew_temp_dd.t55')
T55File('src/appli/tse/src/tse_turbine_temp_dd.t55')
T55File('src/p_l/_p_l/src/p_l_interface_decoding_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_2st_vgt_pos_lrn_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_amf_offset_lrn_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_cabin_temp_acq_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_cruise_switch_inputs_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_doc_in_temp_acq_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_doc_in_temp_calc_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_esc_lever_signal_mon_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_fuel_filter_pressure_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_intercooler_out_temp_acq_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_oil_level_sensor_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_oil_pressure_sensor_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_oil_temp_mdcr_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_pedal_hand_posn_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_pedal_foot_posn_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_pedal_selector_switch_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_pressure_lrn_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_torque_state_switch_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_vgth_pos_dd.t55')
T55File('src/p_l/p_l_aps/src/p_l_aps_tdc_angle_correction_dd.t55')
T55File('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_engine_op_status_dd.t55')
T55File('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_dd.t55')
T55File('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_Cc_J1939_Delphi_Interface.t55')
T55File('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/P_L_J1939_Dcu_Dm01_Flt_Det.t55')
T55File('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_idle_shutdown_timers_dd.t55')
T55File('src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/src/p_l_cc_j1939_rx_diag_enabler_dd.t55')
T55File('src/p_l/p_l_com/p_l_cds/src/p_l_cds.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_air_cond_switch_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_door_switch_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_exh_brk_switch_1_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_eng_brk_switch_1_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_flash_lamp_code_switch_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_immo_switch_state_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_low_fuel_level_switch_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_oil_pressure_switch_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_pedal_foot_switch_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_pedal_hand_switch_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_seat_belt_switch_dd.t55')
T55File('src/p_l/p_l_digital_input/src/p_l_starter_switch_dd.t55')
T55File('src/p_l/p_l_digital_output/src/p_l_cruise_lamp_driver_dd.t55')
T55File('src/p_l/p_l_digital_output/src/p_l_ac_comp_relay_drive_dd.t55')
T55File('src/p_l/p_l_digital_output/src/p_l_eng_spd_rly_drive_dd.t55')
T55File('src/p_l/p_l_digital_output/src/p_l_fuel_heater_driver_dd.t55')
T55File('src/p_l/p_l_digital_output/src/p_l_oil_level_lamp_driver_dd.t55')
T55File('src/p_l/p_l_digital_output/src/p_l_starter_relay_driver.t55')
T55File('src/p_l/p_l_digital_output/src/p_l_fan_drive_diag_dd.t55')
T55File('src/p_l/p_l_event_input/src/p_l_tyre_wear_adjust_dd.t55')
T55File('src/p_l/p_l_event_input/src/p_l_vss_loss_detection_dd.t55')  
T55File('src/p_l/p_l_event_input/src/p_l_vss_raw_speed_calc_dd.t55')  
T55File('src/p_l/p_l_event_input/src/p_l_vss_validate_dd.t55')
T55File('src/p_l/p_l_hbridge_output/src/P_L_Egrh_Hb_Drive_Diag_Md.t55')
T55File('src/p_l/p_l_hbridge_output/src/P_L_Thrtl_Hb_Drive_Diag_Md.t55')
T55File('src/p_l/p_l_pwm_output/src/p_l_coolant_temp_output_dd.t55')
T55File('src/p_l/p_l_pwm_output/src/p_l_veh_spd_output_dd.t55')
T55File('src/p_l/p_l_water_in_fuel/src/p_l_water_in_fuel_dd.t55')
T55File('src/p_l/p_l_wraf/src/p_l_wraf_acquis_dd.t55')
T55File('src/p_l/p_l_wraf/src/p_l_wraf_config_dd.t55')
T55File('src/p_l/p_l_wraf/src/p_l_wraf_control_dd.t55')
T55File('src/p_l/p_l_wraf/src/p_l_wraf_diagnostic_dd.t55')
T55File('src/p_l/p_l_wraf/src/p_l_wraf_htr_diag_dd.t55')
T55File('src/appli/ici/src/ici_ce_lamp_control_dd.t55')
T55File('src/appli/icv/src/icv_amf_selection_dd.t55')
T55File('src/s_s/s_s_fault_manager/src/f_m_flashing_code_output_dd.t55')
T55File('src/appli/c_c/src/c_c_ac_comp_torque_consump_dd.t55')
T55File('src/appli/ici/src/ici_oil_pressure_gauge_dd.t55')
T55File('src/p_l/p_l_pwm_output/src/p_l_oilp_gauge_drv_diag_dd.t55')
T55File('src/p_l/p_l_pwm_output/src/p_l_pwm_hp_turbo_driver_dd.t55')
T55File('src/appli/icv/src/icv_ac_request_arb_dd.t55')
T55File('src/appli/icv/src/icv_ac_fluid_pres_input_arbit_dd.t55')
T55File('src/p_l/p_l_pwm_output/src/p_l_imv_drv_diag_dd.t55')
T55File('src/p_l/p_l_water_in_fuel/src/p_l_wif_lamp_drv_diag_dd.t55')
T55File('src/p_l/p_l_pwm_output/src/p_l_ebrake_diag_dd.t55')
T55File('src/p_l/p_l_pwm_output/src/p_l_exh_brk_vlv_drv_dd.t55')
T55File('src/p_l/p_l_pwm_output/src/p_l_engine_speed_gauge_drv_diag_dd.t55')
T55File('src/appli/_appli/src/app_interface_decode_dd.t55')
T55File('src/p_l/p_l_analogue/src/p_l_boostp_acq_dd.t55')
T55File('src/appli/icv/src/icv_boostp_calc_dd.t55')
T55File('src/s_s/s_s_fault_manager/src/f_m_gen_monitor_cond_eol_dd.t55')
T55File('src/s_s/s_s_fault_manager/src/F_M_Rbm_Cond_Calc.t55')
T55File('src/s_s/s_s_fault_manager/src/F_M_Rbm_Structure.t55')
T55File('src/appli/icv/src/icv_vehicle_distance_dd.t55')
T55File('src/appli/t_d/src/t_d_idle_target_ext_calc_md_dd.t55')

# #### DCM 2.7 Models ####
ModelFile('../../gill_vob/5_sw_design/appli/_appli/model/app_interface_decoding_autocode.mdl',OUTDIR = 'src/appli/_appli/tests/app_interface_decoding_test')
ModelFile('../../gill_vob/5_sw_design/appli/eud/model/eud_hp_opening_counter_autocode.mdl', OUTDIR = 'src/appli/eud/tests/eud_hp_opening_counter_test')
ModelFile('../../gill_vob/5_sw_design/appli/eud/model/eud_distance_calculations_autocode.mdl', OUTDIR = 'src/appli/eud/tests/eud_distance_calculations_test')
ModelFile('../../gill_vob/5_sw_design/appli/eud/model/eud_timer_calculations_autocode.mdl', OUTDIR = 'src/appli/eud/tests/eud_timer_calculations_test')
ModelFile('../../gill_vob/5_sw_design/appli/ici/model/ici_engine_speed_output_mdcr_autocode.mdl', OUTDIR = 'src/appli/ici/tests/ici_engine_speed_output_mdcr_test')
ModelFile('../../gill_vob/5_sw_design/appli/ici/model/ici_glow_plug_lamp_control_autocode.mdl', OUTDIR = 'src/appli/ici/tests/ici_glow_plug_lamp_control_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_brake_switch_autocode.mdl', OUTDIR = 'src/appli/icv/tests/icv_brake_switch_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_cc_asl_interface_autocode.mdl', OUTDIR = 'src/appli/icv/tests/icv_eng_brk_switch_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_eng_brk_switch_autocode.mdl', OUTDIR = 'src/appli/icv/tests/icv_eng_brk_switch_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_esc_input_decode_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_esc_input_decode_autocode_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_exh_brk_switch_autocode.mdl', OUTDIR = 'src/appli/icv/tests/icv_exh_brk_switch_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_exh_over_temp_monitor_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_exh_over_temp_monitor_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_ext_temp_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_ext_temp_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_fuel_consumption_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_fuel_consumption_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_fuel_filter_pressure_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_fuel_filter_pressure_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_interface_decoding_autocode.mdl', OUTDIR = 'src/appli/icv/tests/icv_interface_decoding_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_low_fuel_level_detection_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_low_fuel_level_detection_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_oil_level_monitor_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_oil_level_monitor_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_oil_pressure_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_oil_pressure_autocode_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_oil_temp_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_oil_temp_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_calc_agb_output_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_calc_agb_output_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_calc_veh_speed_data_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_calc_veh_speed_data_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_cruise_req_md_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_cruise_req_md_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_kickdown_detection_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_kickdown_detection_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_pedal_arbitration_switch_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_pedal_arbitration_switch_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_pedal_foot_fault_wrapper_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_pedal_foot_fault_wrapper_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_pedal_foot_pos_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_pedal_foot_pos_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_pedal_hand_fault_wrapper_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_pedal_hand_fault_wrapper_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_pedal_hand_pos_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_pedal_hand_pos_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_torque_state_switch_autocode.mdl',OUTDIR = 'src/appli/icv/tests/icv_torque_state_switch_test')
ModelFile('../../gill_vob/5_sw_design/appli/smc/model/smc_system_mode_dmnd_autocode.mdl',OUTDIR = 'src/appli/smc/tests/smc_system_mode_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_veh_spd_limit_interface_autocode.mdl', OUTDIR = 'src/appli/icv/tests/icv_veh_spd_limit_interface_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_cabin_temp_acq_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_analogue/model/tests/p_l_cabin_temp_acq_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_cruise_switch_inputs_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_cruise_switch_inputs_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_pedal_foot_posn_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_pedal_foot_posn_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_pedal_hand_posn_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_pedal_hand_posn_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_aps/model/p_l_aps_tdc_angle_correction_autocode.mdl',OUTDIR = 'src/p_l/p_l_aps/tests/p_l_aps_tdc_angle_correction_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_com/p_l_cc/p_l_cc_j1939/model/p_l_cc_engine_op_status_autocode.mdl',OUTDIR = 'src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/tests/p_l_cc_engine_op_status_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_com/p_l_cc/p_l_cc_j1939/model/p_l_cc_idle_shutdown_timers_autocode.mdl',OUTDIR = 'src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/tests/p_l_cc_idle_shutdown_timers_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_com/p_l_cc/p_l_cc_j1939/model/p_l_cc_j1939_rx_diag_enabler_autocode.mdl',OUTDIR = 'src/p_l/p_l_com/p_l_cc/p_l_cc_j1939/tests/p_l_cc_j1939_rx_diag_enabler_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_brake_light_switch_autocode.mdl', OUTDIR = 'p_l/p_l_digital_input/model/p_l_brake_light_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_brake_safety_switch_autocode.mdl', OUTDIR = 'p_l/p_l_digital_input/model/p_l_brake_safety_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_door_switch_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_digital_input/model/tests/p_l_door_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_exh_brk_switch_1_autocode.mdl', OUTDIR = 'src/p_l/p_l_digital_input/tests/p_l_exh_brk_switch_1_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_eng_brk_switch_1_autocode.mdl', OUTDIR = 'src/p_l/p_l_digital_input/tests/p_l_eng_brk_switch_1_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_flash_lamp_code_switch_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_digital_input/model/tests/p_l_flash_lamp_code_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_immo_switch_state_autocode.mdl', OUTDIR = 'src/p_l/p_l_digital_input/tests/p_l_immo_switch_state_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_low_fuel_level_switch_autocode.mdl', OUTDIR = 'src/p_l/p_l_digital_input/tests/p_l_low_fuel_level_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_oil_pressure_switch_autocode.mdl',OUTDIR = 'src/p_l/p_l_digital_input/tests/p_l_oil_pressure_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_pedal_foot_switch_autocode.mdl', OUTDIR = 'p_l/p_l_digital_input/model/p_l_pedal_foot_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_pedal_hand_switch_autocode.mdl', OUTDIR = 'p_l/p_l_digital_input/model/p_l_pedal_hand_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_pedal_selector_switch_autocode.mdl',OUTDIR = 'src/p_l/p_l_digital_input/tests/p_l_pedal_selector_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_seat_belt_switch_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_digital_input/model/tests/p_l_seat_belt_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_starter_switch_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_digital_input/model/tests/p_l_starter_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_event_input/model/p_l_vss_loss_detection_autocode.mdl', OUTDIR = 'src/p_l/p_l_event_input/tests/p_l_vss_loss_detection_test') 
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_event_input/model/p_l_vss_raw_speed_calc_autocode.mdl', OUTDIR = 'src/p_l/p_l_event_input/tests/p_l_vss_raw_speed_calc_test') 
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_event_input/model/p_l_vss_validate_autocode.mdl', OUTDIR = 'src/p_l/p_l_event_input/tests/p_l_vss_validate_test') 
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_pwm_output/model/p_l_coolant_temp_output_autocode.mdl', OUTDIR='src/p_l/p_l_pwm_output/model/tests/p_l_coolant_temp_output_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_pwm_output/model/p_l_veh_spd_output_autocode.mdl', OUTDIR='src/p_l/p_l_pwm_output/model/tests')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_water_in_fuel/model/p_l_water_in_fuel_autocode.mdl', OUTDIR = 'src/p_l/p_l_water_in_fuel/tests/p_l_water_in_fuel_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_wraf/model/p_l_wraf_acquis_autocode.mdl', OUTDIR = 'src/p_l/p_l_wraf/tests/p_l_wraf_acquis_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_wraf/model/p_l_wraf_config_autocode.mdl', OUTDIR = 'src/p_l/p_l_wraf/tests/p_l_wraf_config_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_wraf/model/p_l_wraf_control_autocode.mdl', OUTDIR = 'src/p_l/p_l_wraf/tests/p_l_wraf_control_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_wraf/model/p_l_wraf_diagnostic_autocode.mdl', OUTDIR = 'src/p_l/p_l_wraf/tests/p_l_wraf_diagnostic_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_wraf/model/p_l_wraf_htr_diag_autocode.mdl', OUTDIR = 'src/p_l/p_l_wraf/tests/p_l_wraf_htr_diag_test')
ModelFile('../../gill_vob/5_sw_design/s_s/s_s_fault_manager/model/f_m_gen_monitor_cond_eol_autocode.mdl', OUTDIR = 'src/s_s/s_s_fault_manager/tests/f_m_gen_monitor_cond_eol_test')

# #### SEC Eu6 Models ####
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_2st_vgt_bst_diag_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_2st_vgt_bst_diag_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_2st_vgt_comp_prd_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_2st_vgt_comp_prd_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_2st_vgt_pos_dmnd_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_2st_vgt_pos_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_2st_vgt_prot_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_2st_vgt_prot_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_2st_vgt_temp_prot_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_2st_vgt_temp_prot_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_amf_cor_diag_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_amf_cor_diag_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_amf_cor_err_calc_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_amf_cor_err_calc_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_amf_cor_lrn_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_amf_cor_lrn_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_amf_corr_calc_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_amf_corr_calc_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_anti_surge_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_anti_surge_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_desired_air_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_desired_air_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_desired_map_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_desired_map_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_egr_flow_diag_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_egr_flow_diag_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_egr_misfire_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_egr_misfire_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_egr_rate_dmnd_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_egr_rate_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_egr_rate_limit_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_egr_rate_limit_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_egr_st_est_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_egr_st_est_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_egrh_flow_est_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_egrh_flow_est_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_egrh_pos_dmnd_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_egrh_pos_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_eng_brk_enable_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_eng_brk_enable_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_exh_brk_pres_ctrl_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_exh_brk_pres_ctrl_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_exh_flow_est_bkg_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_exh_flow_est_bkg_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_exh_flow_est_sync_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_exh_flow_est_sync_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_eng_brk_overview_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_eng_brk_overview_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_flow_corr_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_flow_corr_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_flow_corr_diag_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_flow_corr_diag_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_intake_flow_est_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_intake_flow_est_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_throt_enable_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_throt_enable_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_throt_fl_lrn_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_throt_fl_lrn_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_throt_map_dmnd_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_throt_map_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_throt_pos_dmnd_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_throt_pos_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_vgt_bst_dmnd_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_vgt_bst_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_vgt_max_pratio_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_vgt_max_pratio_test')
ModelFile('../../gill_vob/5_sw_design/appli/acm/model/acm_vgth_pos_ctrl_autocode.mdl', OUTDIR = 'src/appli/acm/tests/acm_vgth_pos_ctrl_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_ac_fluid_press_ana_sig_acq_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_vgth_pos_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_dsrd_afr_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_dsrd_afr_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_post2_control_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_post2_control_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_smoke_limit_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_smoke_limit_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_smoke_limit_fuel_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_smoke_limit_fuel_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_wraf_blm_enable_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_wraf_blm_enable_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_wraf_blm_learn_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_wraf_blm_learn_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_wraf_cl_loop_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_wraf_cl_loop_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_wraf_control_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_wraf_control_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_wraf_diag_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_wraf_diag_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_wraf_fuel_blm_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_wraf_fuel_blm_test')
ModelFile('../../gill_vob/5_sw_design/appli/afc/model/afc_wraf_resp_diag_autocode.mdl', OUTDIR = 'src/appli/afc/tests/afc_wraf_resp_diag_test')

ModelFile('../../gill_vob/5_sw_design/appli/c_c/model/c_c_ac_management_autocode.mdl',OUTDIR = 'src/appli/c_c/tests/c_c_ac_management_test')

ModelFile('../../gill_vob/5_sw_design/appli/etc/model/etc_fan_management_md_autocode.mdl', OUTDIR = 'src/appli/etc/tests/etc_fan_management_md_test')
ModelFile('../../gill_vob/5_sw_design/appli/etc/model/eud_fuel_calculations_autocode.mdl', OUTDIR = 'src/appli/etc/tests/eud_fuel_calculations_test')

ModelFile('../../gill_vob/5_sw_design/appli/fdc/model/fdc_after_mode_autocode.mdl', OUTDIR = 'src/appli/fdc/tests/fdc_after_mode_test')
ModelFile('../../gill_vob/5_sw_design/appli/fdc/model/fdc_pilot_mode_autocode.mdl', OUTDIR = 'src/appli/fdc/tests/fdc_pilot_mode_test')

ModelFile('../../gill_vob/5_sw_design/appli/fqd/model/fqd_after_dmnd_autocode.mdl', OUTDIR = 'src/appli/fqd/tests/fqd_after_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/fqd/model/fqd_bkg_snapshot_autocode.mdl', OUTDIR = 'src/appli/fqd/tests/fqd_bkg_snapshot_test')
ModelFile('../../gill_vob/5_sw_design/appli/fqd/model/fqd_desired_fuel_autocode.mdl', OUTDIR = 'src/appli/fqd/tests/fqd_desired_fuel_test')
ModelFile('../../gill_vob/5_sw_design/appli/fqd/model/fqd_pilot_dmnd_autocode.mdl', OUTDIR = 'src/appli/fqd/tests/fqd_pilot_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/fqd/model/fqd_post_air_ctrl_autocode.mdl', OUTDIR = 'src/appli/fqd/tests/fqd_post_air_ctrl_test')
ModelFile('../../gill_vob/5_sw_design/appli/fqd/model/fqd_post1_dmnd_autocode.mdl', OUTDIR = 'src/appli/fqd/tests/fqd_post1_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/fqd/model/fqd_post2_dmnd_autocode.mdl', OUTDIR = 'src/appli/fqd/tests/fqd_post2_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/fqd/model/fqd_smoke_limit_autocode.mdl', OUTDIR = 'src/appli/fqd/tests/fqd_smoke_limit_test')

ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_gear_state_autocode.mdl', OUTDIR = 'src/appli/icv/tests/icv_gear_state_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_flashing_code_ena_autocode.mdl', OUTDIR='src/appli/icv/model/tests/icv_flashing_code_ena_test')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_vac_act_autocode.mdl', OUTDIR = 'src/appli/icv/tests/icv_vac_act_test')
ModelFile('../../gill_vob/5_sw_design/appli/itd/model/itd_after_dmnd_autocode.mdl', OUTDIR = 'src/appli/itd/tests/itd_after_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/itd/model/itd_main_dmnd_autocode.mdl', OUTDIR = 'src/appli/itd/tests/itd_main_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/itd/model/itd_mbt_timing_autocode.mdl', OUTDIR = 'src/appli/itd/tests/itd_mbt_timing_test')
ModelFile('../../gill_vob/5_sw_design/appli/itd/model/itd_pilot_dmnd_autocode.mdl', OUTDIR = 'src/appli/itd/tests/itd_pilot_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/itd/model/itd_post1_dmnd_autocode.mdl', OUTDIR = 'src/appli/itd/tests/itd_post1_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/itd/model/itd_post2_dmnd_autocode.mdl', OUTDIR = 'src/appli/itd/tests/itd_post2_dmnd_test')


ModelFile('../../gill_vob/5_sw_design/appli/p_p/model/p_p_run_dry_strategy_autocode.mdl', OUTDIR = 'src/appli/p_p/tests/p_p_run_dry_strategy_test')

ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_comb_mode_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_comb_mode_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_dfco_ctrl_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_dfco_ctrl_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_doc_diag_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_doc_diag_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_doc_lightoff_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_doc_lightoff_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_dpf_diag_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_dpf_diag_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_dpf_diag_leak_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_dpf_diag_leak_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_dpf_eff_mon_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_dpf_diag_leak_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_dpf_in_temp_trgt_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_dpf_in_temp_trgt_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_dpf_regen_en_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_dpf_regen_en_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_dew_point_dpf_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_dew_point_dpf_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_doc_aging_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_doc_aging_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_exh_air_fuel_trgt_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_exh_air_fuel_trgt_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_nox_flow_acc_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_nox_flow_acc_trgt_test')
ModelFile('../../gill_vob/5_sw_design/appli/p_t/model/p_t_nox_flow_est_autocode.mdl', OUTDIR = 'src/appli/p_t/tests/p_t_nox_flow_est_trgt_test')

ModelFile('../../gill_vob/5_sw_design/appli/pse/model/pse_2st_vgt_pos_calc_autocode.mdl', OUTDIR = 'src/appli/pse/tests/pse_2st_vgt_pos_calc_test')
ModelFile('../../gill_vob/5_sw_design/appli/pse/model/pse_boost_est_autocode.mdl', OUTDIR = 'src/appli/pse/tests/pse_boost_est_test')
ModelFile('../../gill_vob/5_sw_design/appli/pse/model/pse_press_diag_autocode.mdl', OUTDIR = 'src/appli/pse/tests/pse_press_diag_test')
ModelFile('../../gill_vob/5_sw_design/appli/pse/model/pse_press_est_autocode.mdl', OUTDIR = 'src/appli/pse/tests/pse_press_est_test')

ModelFile('../../gill_vob/5_sw_design/appli/rpc/model/rpc_interface_autocode.mdl', OUTDIR = 'src/appli/rpc/tests/rpc_interface_test')

ModelFile('../../gill_vob/5_sw_design/appli/sac/model/sac_fuel_heater_control_mdcr_autocode.mdl', OUTDIR = 'src/appli/sac/tests/sac_fuel_heater_control_mdcr_test')
ModelFile('../../gill_vob/5_sw_design/appli/smc/model/smc_starter_cntrl_mdcr_autocode.mdl', OUTDIR = 'src/appli/smc/tests/smc_starter_cntrl_mdcr_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_actual_torq_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_actual_torq_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_asg_torq_interface_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_asg_torq_interface_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_can_rx_torq_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_can_rx_torq_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_comb_limit_torque_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_comb_limit_torque_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_corr_terms_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_corr_terms_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_dfco_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_dfco_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_driveability_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_driveability_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_driver_torq_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_driver_torq_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_dsrd_imep_air_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_dsrd_imep_air_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_engine_load_ref_autocode.mdl', OUTDIR= 'src/appli/t_d/tests/t_d_engine_load_ref_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_engine_torq_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_engine_torq_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_fuel_fast_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_fuel_fast_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_fuel_slow_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_fuel_slow_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_idle_cntrl_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_idle_cntrl_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_idle_fast_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_idle_fast_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_idle_gains_ext_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_idle_gains_ext_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_induced_torq_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_induced_torq_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_interface_decoding_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_interface_decoding_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_j1939_output_autocode.mdl', OUTDIR= 'src/appli/t_d/tests/t_d_j1939_output_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_max_brk_trq_ext_autocode.mdl',OUTDIR = 'src/appli/t_d/tests/t_d_max_brk_trq_ext_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_max_torque_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_max_torque_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_pedal_torq_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_pedal_torq_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_reduced_torq_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_reduced_torq_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_retard_torque_calc_autocode.mdl', OUTDIR='src/appli/t_d/tests/t_d_retard_torque_calc_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_th_comb_eff_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_th_comb_eff_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_torq_conv_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_torq_conv_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_torq_select_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_torq_select_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_torque_fast_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_torque_fast_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_torque_slow_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_torque_slow_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_vdg_enable_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_vdg_enable_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_vdg_eng_spd_lim_interface_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_vdg_eng_spd_lim_interface_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_vdg_pid_dmnd_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_vdg_pid_dmnd_test')
ModelFile('../../gill_vob/5_sw_design/appli/t_d/model/t_d_vdg_speed_dmnd_autocode.mdl', OUTDIR = 'src/appli/t_d/tests/t_d_vdg_speed_dmnd_test')

ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_ambient_air_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_ambient_air_test')
ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_comp_in_limit_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_comp_in_limit_test')
ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_egrh_temp_est_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_egrh_temp_est_test')
ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_engine_out_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_engine_out_test')
ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_exh_exo_eff_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_exh_exo_eff_test')
ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_exhaust_temp_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_exhaust_temp_test')
ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_oil_temp_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_oil_temp_test')
ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_temp_diag_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_temp_diag_test')
ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_temp_diag_xc_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_temp_diag_xc_test')
ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_temp_sensors_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_temp_sensors_test')
ModelFile('../../gill_vob/5_sw_design/appli/tse/model/tse_turbine_temp_autocode.mdl', OUTDIR = 'src/appli/tse/tests/tse_turbine_temp_test')

ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_input/model/p_l_air_cond_switch_autocode.mdl', OUTDIR = 'p_l/p_l_digital_input/model/p_l_air_cond_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/_p_l/model/p_l_interface_decoding_autocode.mdl',OUTDIR = 'src/p_l/_p_l/tests/p_l_interface_decoding_test')
ModelFile('../5_sw_design/p_l/p_l_analogue/model/p_l_doc_in_temp_acq_autocode.mdl', OUTDIR='src/p_l/p_l_analogue/tests/p_l_doc_in_temp_acq_test')
ModelFile('../5_sw_design/p_l/p_l_analogue/model/p_l_doc_in_temp_calc_autocode.mdl', OUTDIR='src/p_l/p_l_analogue/tests/p_l_doc_in_temp_calc_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_amf_offset_lrn_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_amf_offset_lrn_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_esc_lever_signal_mon_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_esc_lever_signal_mon_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_fuel_filter_pressure_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_fuel_filter_pres_tests')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_intercooler_out_temp_acq_autocode.mdl', OUTDIR='src/p_l/p_l_analogue/tests/p_l_intercooler_out_temp_acq')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_oil_level_sensor_autocode.mdl', OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_oil_level_sensor_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_oil_pressure_sensor_autocode.mdl', OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_oil_pressure_sensor_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_oil_temp_mdcr_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_oil_temp_mdcr_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_pressure_lrn_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_pressure_lrn_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_torque_state_switch_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_torque_state_switch_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_event_input/model/p_l_tyre_wear_adjust_autocode.mdl',OUTDIR = 'src/p_l/p_l_event_input/tests/p_l_tyre_wear_adjust_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_analogue/model/p_l_vgth_pos_autocode.mdl',OUTDIR = 'src/p_l/p_l_analogue/tests/p_l_vgth_pos_test')
ModelFile('../../gill_vob/5_sw_design/appli/ici/model/ici_ce_lamp_control_autocode.mdl', OUTDIR = 'src/appli/ici/tests/ici_ce_lamp_control_test')

ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_output/model/p_l_cruise_lamp_driver_autocode.mdl',OUTDIR = 'src/p_l/p_l_digital_output/tests/p_l_cruise_lamp_driver_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_output/model/p_l_eng_spd_rly_drive_autocode.mdl',OUTDIR = 'src/p_l/p_l_digital_output/tests/p_l_eng_spd_rly_drive_test')
ModelFile('../5_sw_design/p_l/p_l_digital_output/model/p_l_fuel_heater_driver_autocode.mdl', OUTDIR='src/p_l/p_l_digital_output/tests/p_l_fuel_heater_driver_test')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_digital_output/model/p_l_ac_comp_relay_drive_autocode.mdl',OUTDIR = 'src/p_l/_p_l/tests/p_l_ac_comp_relay_drive_test')
ModelFile('../5_sw_design/appli/c_c/model/c_c_ac_comp_torque_consump_autocode.mdl', OUTDIR='../5_sw_design/appli/c_c/model/tests')
ModelFile('../5_sw_design/appli/icv/model/icv_amf_selection_autocode.mdl', OUTDIR='../5_sw_design/appli/icv/model/tests')
ModelFile('../../gill_vob/5_sw_design/appli/icv/model/icv_ac_eng_cool_req_sw_select_autocode.mdl', OUTDIR = 'src/appli/ici/tests/icv_ac_eng_cool_req_sw_select')

ModelFile('../5_sw_design/appli/ici/model/ici_oil_pressure_gauge_autocode.mdl', OUTDIR='../5_sw_design/appli/ici/model/tests')
ModelFile('../5_sw_design/p_l/p_l_pwm_output/model/p_l_oilp_gauge_drv_diag_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_pwm_output/model/tests')
ModelFile('../5_sw_design/p_l/p_l_digital_output/model/p_l_fan_drive_diag_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_digital_output/model/tests')
ModelFile('../5_sw_design/p_l/p_l_digital_output/model/p_l_oil_level_lamp_driver_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_digital_output/model/tests')
ModelFile('../5_sw_design/p_l/p_l_pwm_output/model/p_l_pwm_hp_turbo_driver_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_pwm_output/model/tests')
ModelFile('../5_sw_design/appli/icv/model/icv_ac_request_arb_autocode.mdl', OUTDIR='../5_sw_design/appli/icv/model/tests')
ModelFile('../5_sw_design/appli/icv/model/icv_ac_fluid_pres_input_arbit_autocode.mdl', OUTDIR='../5_sw_design/appli/icv/model/tests')
ModelFile('../5_sw_design/p_l/p_l_pwm_output/model/p_l_imv_drv_diag_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_pwm_output/model/tests')
ModelFile('../5_sw_design/p_l/p_l_pwm_output/model/p_l_ebrake_diag_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_pwm_output/model/tests')
ModelFile('../../gill_vob/5_sw_design/p_l/p_l_pwm_output/model/p_l_exh_brk_vlv_drv_autocode.mdl', OUTDIR='src/p_l/p_l_pwm_output/tests/p_l_exh_brk_vlv_drv_test')
ModelFile('../5_sw_design/p_l/p_l_pwm_output/model/p_l_engine_speed_gauge_drv_diag_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_pwm_output/model/tests')
ModelFile('../5_sw_design/appli/_appli/model/app_interface_decode_autocode.mdl', OUTDIR='../5_sw_design/appli/_appli/model/tests')
ModelFile('../5_sw_design/p_l/p_l_analogue/model/p_l_boostp_acq_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_analogue/model/tests')
ModelFile('../5_sw_design/appli/icv/model/icv_boostp_calc_autocode.mdl', OUTDIR='../5_sw_design/appli/icv/model/tests')
ModelFile('../5_sw_design/appli/icv/model/icv_vehicle_distance_autocode.mdl', OUTDIR='../5_sw_design/appli/icv/model/tests')

ModelFile('../5_sw_design/p_l/p_l_water_in_fuel/model/p_l_wif_lamp_drv_diag_autocode.mdl', OUTDIR='../5_sw_design/p_l/p_l_water_in_fuel/model/tests')
ModelFile('../5_sw_design/appli/t_d/model/t_d_idle_target_ext_calc_md_autocode.mdl', OUTDIR='src/appli/t_d/tests/t_d_idle_target_ext_calc_md_test')

#APP.SCHEMA = "app_base"

#APP.Setting(name = 'P_L_CC_RX_NO_CAN_ECU_CPV', value = 'P_L_CC_RX_NO_CAN_ECU_CPV')
#APP.Setting(name = 'P_L_CC_DIAG_MSG_NODES_CPV', value = 'P_L_CC_DIAG_MSG_NODES_CPV')
#APP.Setting(name = 'APP_NUMBER_OF_INJECTORS_CPV', value = 'APP_NUMBER_OF_INJECTORS_CPV')
#APP.Setting(name = 'APP_MAX_NUMBER_OF_INJECTORS_CPV', value = 'APP_MAX_NUMBER_OF_INJECTORS_CPV')
#APP.Setting(name = 'P_L_INJ_NUMBER_OF_BANKS_CPV', value = 'P_L_INJ_NUMBER_OF_BANKS_CPV')
#APP.Setting(name = 'APP_NUMBER_OF_ACCEL_CPV', value = 'APP_NUMBER_OF_ACCEL_CPV')
#APP.Setting(name = 'I_C_ACC_NUMBER_MDP_ZONE_CPV', value = 'I_C_ACC_NUMBER_MDP_ZONE_CPV')

# #### Fault Manager ####

Setting(name = 'F_M_FLT_GRP_SIZE_A_CPV', value = '15')
Setting(name = 'F_M_FLT_GRP_SIZE_B_CPV', value = '30')
Setting(name = 'F_M_FLT_GRP_SIZE_C_CPV', value = '50')
Setting(name = 'F_M_FLT_GRP_SIZE_D_CPV', value = '70')
Setting(name = 'F_M_FLT_GRP_SIZE_E_CPV', value = '80')
Setting(name = 'F_M_FLT_GRP_SIZE_F_CPV', value = '90')
Setting(name = 'F_M_FLT_GRP_SIZE_G_CPV', value = '100')
Setting(name = 'F_M_FLT_GRP_SIZE_H_CPV', value = '120')
Setting(name = 'F_M_FLT_GRP_SIZE_I_CPV', value = '150')
Setting(name = 'F_M_FLT_GRP_SIZE_J_CPV', value = '255')
Setting(name = 'F_M_FLT_INH_SIZE_A_CPV', value = '1')
Setting(name = 'F_M_FLT_INH_SIZE_B_CPV', value = '5')
Setting(name = 'F_M_FLT_INH_SIZE_C_CPV', value = '5')
Setting(name = 'F_M_FLT_FID_SIZE_A_CPV', value = '5')
Setting(name = 'F_M_FLT_FID_SIZE_B_CPV', value = '10')
Setting(name = 'F_M_FLT_FID_SIZE_C_CPV', value = '15')
Setting(name = 'F_M_FLT_FID_SIZE_D_CPV', value = '20')
Setting(name = 'F_M_FLT_FID_SIZE_E_CPV', value = '30')
Setting(name = 'F_M_FLT_FID_SIZE_F_CPV', value = '40')
Setting(name = 'F_M_FLT_FID_SIZE_G_CPV', value = '50')
Setting(name = 'F_M_FLT_FID_SIZE_H_CPV', value = '60')
Setting(name = 'F_M_FLT_FID_SIZE_I_CPV', value = '80')
Setting(name = 'F_M_FLT_FID_SIZE_J_CPV', value = '100')
Setting(name = 'F_M_FLT_FID_SIZE_K_CPV', value = '120')
Setting(name = 'F_M_FLT_FID_SIZE_L_CPV', value = '150')
Setting(name = 'F_M_FLT_FID_SIZE_M_CPV', value = '200')
Setting(name = 'F_M_FLT_FID_SIZE_N_CPV', value = '255')
Setting(name = 'F_M_FLT_FID_SIZE_O_CPV', value = '255')
Setting(name = 'F_M_FLT_FID_SIZE_P_CPV', value = '255')


# #### Fault Manager ####
# F_M.Fault('Name of Fault', 'Dimension of Fault', 'Name of variable raising Supplementaries faults', 'name_of_sup0_extension', 'name_of_sup1_extension',..., 'name_of_supN_extension')
#
#               Only 'Name of Fault' is compulsory
#
F_M.FaultGroup('F_M_Red_lamp_fast', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Red_lamp_slow', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Red_lamp', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Mi_lamp', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Mi_lamp_slow', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Mi_lamp_fast', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Amb_lamp_fast', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Amb_lamp_slow', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Amb_lamp', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Prot_lamp_fast', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Prot_lamp_slow', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Prot_lamp', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_J1939_eng_speed', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Ac_off', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Acc_dec_strat', 'F_M_FLT_GRP_SIZE_I_CPV')
F_M.FaultGroup('F_M_Adc', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Alt_bat_diag', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Alt_bs_invld', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Alt_charge', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Alt_ctrl_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Alt_discharg', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Amf_corr_learn', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Aps_camless', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Aps_crankless', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Atmosp_sensor_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Batt_curr_sens', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Batt_temp_sens', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Brake_switch', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Blower_sens', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Brc_res_read', 'F_M_FLT_GRP_SIZE_B_CPV','APP_NUMBER_OF_INJECTORS_CPV')
F_M.FaultGroup('F_M_Ce_lamp_flash', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Ce_lamp', 'F_M_FLT_GRP_SIZE_I_CPV')
F_M.FaultGroup('F_M_Cool_temp_sensor', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Cruise_control', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Cruise_inhibit', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Cruise_accel', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Cruise_decel', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Cruise_resume', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Cyl_strt_active', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Delay_eng_stop', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Dis_overspd', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Dis_pilot_post', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Dis_rvd_inj', 'F_M_FLT_GRP_SIZE_C_CPV','APP_NUMBER_OF_INJECTORS_CPV')
F_M.FaultGroup('F_M_Doc_in_t_inval', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_consum', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_dosing_act', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_egr', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_empty_tank', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_incct_reag', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_low_tank', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_noxlvlotl', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_noxlvltamp', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_tampering', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_very_mt_tk', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Induc_very_lo_tk', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Dpf_dp_sens_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Dpf_in_t_inval', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Dpf_out_dew_pt', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Dpf_out_t_inval', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Dpf_regen', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Dti_inj', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Ecu_case_tp_sens', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Ecu_case_temp_cf', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Ecu_case_temp_df', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Egr_air_cl_lp', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Egr_disable', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Egrh_ctrl', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Egrh_diag', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Egrh_hb_fdb_sens', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Eng_1st_start', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Eng_brk_disable', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Eng_brk_overrun', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Eng_brk_warm_up', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Eng_speed_max', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Esm_exh_brk_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Esm_exh_brk_ovr', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Exh_brk_cl_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Exh_brk_deenerg', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Exh_brk_disable', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Exh_brk_ovrspd', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Fan', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Fuel_temp_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Fuel_temp_df', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Glow_plug_drive', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Gp_disable', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Gp_heat_tempo', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Gp_postheat', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Gsi_inhibit', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Hp_crt_ctrl', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Hp_diag_dis', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Hp_drive', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Hp_learn_dis', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_I_c_off_mode', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Idle_slow_lrn', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Ignition_cnt_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Ignition_Switch', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Im_crt_ctrl', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Im_drive', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Im_stable_cond', 'F_M_FLT_GRP_SIZE_G_CPV')
F_M.FaultGroup('F_M_Imt1_spn1127', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Imv_only', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Imv_only_ff_wax', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Increased_idle', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Inj_bal_diag', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Inj_bal_spd', 'F_M_FLT_GRP_SIZE_D_CPV')
F_M.FaultGroup('F_M_Inj_rvd_freq_lim', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Injector', 'F_M_FLT_GRP_SIZE_A_CPV','APP_NUMBER_OF_INJECTORS_CPV')
F_M.FaultGroup('F_M_Invalid_torque', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Lp_drive_oc', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Lp_drive_sc2vbat', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Lp_drive_sc2g', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Ip_temp_sens_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Ip_temp_sens_df', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Iso_diagp', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_J1939_spn157', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Lift_pump', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Lift_pump_pres', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Limp_home', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Map_sensor_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Mdp_acc_active', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Mdp_check_strat', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Mdp_init_upd', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Oil_temp_model', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Open_im', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Open_hp', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_P3_sensor_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Pm_snsr', 'F_M_FLT_GRP_SIZE_G_CPV')
F_M.FaultGroup('F_M_Pmc_strt_active', 'F_M_FLT_GRP_SIZE_G_CPV')
F_M.FaultGroup('F_M_Pres_cal', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Pres_cal_high', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Pres_lim', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Pres_meas', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Press_offset_lrn_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Pto_cruise', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Rail_pres_min', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Chkd_railp_max2', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Railp_sens_frz', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Reduced_trq', 'F_M_FLT_GRP_SIZE_I_CPV')
F_M.FaultGroup('F_M_Reduced_trq1', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Reduced_trq2', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Reduced_trq3', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Reduced_trq4', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Reduced_trq5', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Brc_res_meas', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Rpc_build_dis', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Rpc_ctrl_dis', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Rvd_regul', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Sas', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Sas_engstart', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Sas_temp_dsbl', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Scr_in_t_inval', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Spc_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Spc_entr_extd_md', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Spci_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Spcs_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Speed_dns_inval', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Spn1176', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Starter_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Stop_engine', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_T1_ana_sensor_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_T1_dig_sensor_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_T3_sensor_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_T5_sensor_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Throt_fl_lrn', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Throt_track_1', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Throt_track_2', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Thrtl_deenerg', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Thrtl_deenrg_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Thrtl_hb_diag', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Thrtl_enable', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Thrtl_fb_sens_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Thrtl_fb_sens_df', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Thrtl_hb_fdb_sens', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Tune_pulse_strat', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Turb_in_t_inval', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Turb_out_t_inv', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vag', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgt_boost_ctrl', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgth_ctrl', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgth_disable', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgth_pos', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgth_pos_lrn', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgth_sens', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgth_sens_err', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgtl_sens_err', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgtl_ctrl', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgtl_disable', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgtl_pos_lrn', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vgtl_sens', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vspdl', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Vspdl_inhibit', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Acc_signal_rd_cf', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Wraf_control', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Water_in_fuel', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Wraf_diag', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Wraf_htr_stop', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Egrh_fb_sens_cf', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Egrh_fb_sens_df', 'F_M_FLT_GRP_SIZE_C_CPV')
F_M.FaultGroup('F_M_Egrh_hb_diag', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Egrh_fdb_sens', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Turb_out_ext_def', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Turb_out_ext_err', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Turb_out_dew_pt', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Ic_out_t_inv', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_intk_pl_t_inv', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Veh_dist_flt', 'F_M_FLT_GRP_SIZE_B_CPV')
F_M.FaultGroup('F_M_Rbm_gen_inc_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Egr_dis', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Nox_high', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Nox_monitor', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Egrh_disable', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Thrtl_disable', 'F_M_FLT_GRP_SIZE_A_CPV')
F_M.FaultGroup('F_M_Thrtl_ctrl', 'F_M_FLT_GRP_SIZE_A_CPV')


F_M.Fault('F_M_Variant_coding', '0','P_L_CDS_VARIANT_CODING_FLT' ,'SUP_0' , 'SUP_1')
F_M.Fault('F_M_J1939_syspm4_tmo',0)
F_M.Fault('F_M_Can_maf_temp_sens',0)
F_M.Fault('F_M_Can_maf_gas_ovrtmp',0)
F_M.Fault('F_M_Can_maf_pabs_sens',0)
F_M.Fault('F_M_Can_maf_dp_sens',0)
F_M.Fault('F_M_Can_maf_gas_hi_temp',0)
F_M.Fault('F_M_Can_maf_sens_hi_temp',0)
F_M.Fault('F_M_Can_maf_sens_ovrtmp',0)
# #### Fault Manager for FID configuration ####
# F_M.FaultFid('Name of Fault', 'Size', 'iumpr', 'iumpr_grp', 'fault_index', 'dimension_str')
# Only 'Name of Fault' and 'Size' is compulsory
#########################
F_M.FaultFid('F_M_Ac_fluid_p_ss_df','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Ac_fluid_p_ss_cf','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Atmosp_sensor_df','F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_Cool_t_def_ext','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Cruise_Switch', 'F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Dpf_dp_sens_df','F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_Fuel_filt_pres_sens_cf', 'F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_Fuel_filt_pres_sens_df', 'F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_Ic_temp_sens_cf', 'F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_Ic_temp_sens_df', 'F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_Map_sensor_df','F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_Oil_pres_sens_cf', 'F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_Oil_pres_sens_df', 'F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_P3_sensor_df','F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_T1_ana_sensor_df','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_T1_dig_sensor_df','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_T3_sensor_df','F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_T5_sensor_df','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Vgth_sens_def','F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_Vgtl_sens_def','F_M_FLT_FID_SIZE_B_CPV')
F_M.FaultFid('F_M_Egrh_sens_cf','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Egrh_sens_df','F_M_FLT_FID_SIZE_A_CPV')

F_M.FaultFid('F_M_Oil_temp_cf','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Oil_temp_df','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Wif_Sensor_cf','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Wif_Sensor_df','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Acc_signal_rd_df','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Boostp_sensor_cf', 'F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Boostp_sensor_df', 'F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Anlg_amf_sens_cf', 'F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Anlg_amf_sens_df', 'F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Oil_level_sens_cf','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Oil_level_sens_df','F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Ext_air_temp_cf', 'F_M_FLT_FID_SIZE_A_CPV')
F_M.FaultFid('F_M_Ext_air_temp_df', 'F_M_FLT_FID_SIZE_A_CPV')
# Fault Sig generation
F_M.FaultSig('F_M_Dummy_sig_1')
F_M.FaultSig('F_M_Dummy_sig_2')

F_M.Fault('F_M_Ac_fatc_tq_val', '0')
F_M.Fault('F_M_Ac_fluid_pres_hi', '0')
F_M.Fault('F_M_Ac_fluid_pres_lo', '0')
F_M.Fault('F_M_Ac_relay_oc', '0')
F_M.Fault('F_M_Ac_relay_sc2g', '0')
F_M.Fault('F_M_Ac_relay_sc2v', '0')
F_M.Fault('F_M_Acc_funct_check', '0' ,'P_L_ACC_FUNCT_CHECK_FAULT' , 'ADC', 'PROG' , 'WIN')
F_M.Fault('F_M_Adc', '0')
F_M.Fault('F_M_Alt_reg_oc', '0')
F_M.Fault('F_M_Alt_reg_sc2g', '0')
F_M.Fault('F_M_Alt_reg_sc2vbat', '0')
F_M.Fault('F_M_Alt_regul', '0')
F_M.Fault('F_M_Alt_sensor', '0')
F_M.Fault('F_M_Amf_corr_hi_1', '0')
F_M.Fault('F_M_Amf_corr_hi_2', '0')
F_M.Fault('F_M_Amf_corr_hi_3', '0')
F_M.Fault('F_M_Amf_corr_hi_4', '0')
F_M.Fault('F_M_Amf_corr_hi_5', '0')
F_M.Fault('F_M_Amf_corr_lo_1', '0')
F_M.Fault('F_M_Amf_corr_lo_2', '0')
F_M.Fault('F_M_Amf_corr_lo_3', '0')
F_M.Fault('F_M_Amf_corr_lo_4', '0')
F_M.Fault('F_M_Amf_corr_lo_5', '0')
F_M.Fault('F_M_Amf_heat_oc', '0')
F_M.Fault('F_M_Amf_heat_sc2v', '0')
F_M.Fault('F_M_Amf_plau_hi', '0')
F_M.Fault('F_M_Amf_plau_lo', '0')
F_M.Fault('F_M_Amf_ref_hi', '0')
F_M.Fault('F_M_Amf_ref_lo', '0')
F_M.Fault('F_M_Amf_sensor_hi', '0')
F_M.Fault('F_M_Amf_sensor_lo', '0')
F_M.Fault('F_M_Aps_cam_crk_spd', '0')
F_M.Fault('F_M_Aps_cam_drift', '0')
F_M.Fault('F_M_Aps_cam_erratic', '0')
F_M.Fault('F_M_Aps_cam_learning', '0')
F_M.Fault('F_M_Aps_cam_lost', '0')
F_M.Fault('F_M_Aps_cam_missing', '0')
F_M.Fault('F_M_Aps_cam_over_spd', '0')
F_M.Fault('F_M_Aps_crank_early', '0')
F_M.Fault('F_M_Aps_crank_lost', '0')
F_M.Fault('F_M_Aps_crank_missing', '0')
F_M.Fault('F_M_Aps_crk_dir_sens', '0')
F_M.Fault('F_M_Aps_crk_over_spd', '0')
F_M.Fault('F_M_Aps_eng_spd_frz', '0')
F_M.Fault('F_M_Aps_gap_missed', '0')
F_M.Fault('F_M_Atc_lamp_oc', '0')
F_M.Fault('F_M_Atc_lamp_sc', '0')
F_M.Fault('F_M_Atc_lamp_sc2g', '0')
F_M.Fault('F_M_Atm_pres_hi', '0')
F_M.Fault('F_M_Atm_pres_lo', '0')
F_M.Fault('F_M_Atm_pres_noi', '0')
F_M.Fault('F_M_Atmosp', '0')
F_M.Fault('F_M_Baro_failure', '0')
F_M.Fault('F_M_Baro_oor', '0')
F_M.Fault('F_M_Baro_spi', '0')
F_M.Fault('F_M_Batt_correl', '0',)
F_M.Fault('F_M_Batt_curr_hi', '0')
F_M.Fault('F_M_Batt_curr_lo', '0')
F_M.Fault('F_M_Batt_curr_noi', '0')
F_M.Fault('F_M_Batt_not_charg', '0')
F_M.Fault('F_M_Batt_over_temp', '0')
F_M.Fault('F_M_Batt_soc_irrat', '0')
F_M.Fault('F_M_Batt_soc_low', '0')
F_M.Fault('F_M_Batt_soh_low', '0')
F_M.Fault('F_M_Batt_syst_volt', '0')
F_M.Fault('F_M_Batt_temp_hi', '0')
F_M.Fault('F_M_Batt_temp_lo', '0')
F_M.Fault('F_M_Batt_temp_noi', '0')
F_M.Fault('F_M_Batt_v_rational', '0')
F_M.Fault('F_M_Battery', '0',)
F_M.Fault('F_M_Battery_pbatt_hi', '0',)
F_M.Fault('F_M_Battery_pbatt_lo', '0',)
F_M.Fault('F_M_Boostp_drift', '0')
F_M.Fault('F_M_Boostp_drift_lo', '0')
F_M.Fault('F_M_Boostp_drift_hi', '0')
F_M.Fault('F_M_Boostp_map_xc', '0')
F_M.Fault('F_M_Boostp_map_xc_lo', '0')
F_M.Fault('F_M_Boostp_map_xc_hi', '0')
F_M.Fault('F_M_Boostp_plau', '0')
F_M.Fault('F_M_Boostp_plau_lo','0')
F_M.Fault('F_M_Boostp_plau_hi','0')
F_M.Fault('F_M_Boostp_sensor_lo', '0')
F_M.Fault('F_M_Boostp_sensor_hi', '0')
F_M.Fault('F_M_Boostp_sensor_noi', '0')
F_M.Fault('F_M_Boostp_sensor_overp', '0')
F_M.Fault('F_M_Brake_accel', '0')
F_M.Fault('F_M_Brake_decel', '0')
F_M.Fault('F_M_Brake_stop', '0')
F_M.Fault('F_M_Brake_switch', '0')
F_M.Fault('F_M_Brc_hi_res_drop', 'APP_NUMBER_OF_INJECTORS_CPV')
F_M.Fault('F_M_Brc_hi_res_level', 'APP_NUMBER_OF_INJECTORS_CPV')
F_M.Fault('F_M_Brc_lo_res_drop', 'APP_NUMBER_OF_INJECTORS_CPV')
F_M.Fault('F_M_Brc_lo_res_level', 'APP_NUMBER_OF_INJECTORS_CPV')
F_M.Fault('F_M_Bus_off_can0', '0')
F_M.Fault('F_M_Bus_off_can1', '0')
F_M.Fault('F_M_Passiv_err_can0', '0')
F_M.Fault('F_M_Passiv_err_can1', '0')
F_M.Fault('F_M_C2i_data', 'APP_NUMBER_OF_INJECTORS_CPV')
F_M.Fault('F_M_C2i_ram_integrity', '0')
F_M.Fault('F_M_C2mio_config', '0')
F_M.Fault('F_M_C2mio_severe', '0')
F_M.Fault('F_M_C2mio_spi', '0')
F_M.Fault('F_M_C2mio_state', '0')
F_M.Fault('F_M_Cabin_temp_s2b', '0')
F_M.Fault('F_M_Cabin_temp_s2g', '0')
F_M.Fault('F_M_Cc_egr_comms', '0')
F_M.Fault('F_M_Cc_egr_hardware', '0')
F_M.Fault('F_M_Cc_tsc1', '0')
F_M.Fault('F_M_Ce_lamp', '0')
F_M.Fault('F_M_Ce_lamp_oc', '0')
F_M.Fault('F_M_Ce_lamp_sc2g', '0')
F_M.Fault('F_M_Ce_lamp_sc2v', '0')
F_M.Fault('F_M_Clutch', '0')
F_M.Fault('F_M_Clutch_bottom', '0')
F_M.Fault('F_M_Clutch_coherence', '0')
F_M.Fault('F_M_Clutch_top', '0')
F_M.Fault('F_M_Coolant_drive_oc', '0')
F_M.Fault('F_M_Coolant_drive_sc2b', '0')
F_M.Fault('F_M_Coolant_drive_sc2g', '0')
F_M.Fault('F_M_Coolant_grad', '0')
F_M.Fault('F_M_Coolant_hi', '0')
F_M.Fault('F_M_Coolant_lo', '0')
F_M.Fault('F_M_Coolant_plau', '0')
F_M.Fault('F_M_Coolant_temp', '0')
F_M.Fault('F_M_Coolant_temp_xc', '0')
F_M.Fault('F_M_Cruise_switch_cnt')
F_M.Fault('F_M_Cruise_accel_stuck')
F_M.Fault('F_M_Cruise_lamp_sc2b', '0')
F_M.Fault('F_M_Cruise_lamp_oc', '0')
F_M.Fault('F_M_Cruise_lamp_sc2g', '0')
F_M.Fault('F_M_Cruise_decel_stuck')
F_M.Fault('F_M_Cruise_on_off_stuck')
F_M.Fault('F_M_Cruise_res_can_stuck')
F_M.Fault('F_M_Accel_button')
F_M.Fault('F_M_Decel_button')
F_M.Fault('F_M_Res_button')
F_M.Fault('F_M_Dcu_dm01_ambtp', '0')
F_M.Fault('F_M_Dcu_dm01_mil', '0')
F_M.Fault('F_M_Dcu_dm01_redtrq', '0')
F_M.Fault('F_M_DOC_IN_ADC', '0')
F_M.Fault('F_M_Doc_in_temp_cnt', '0','F_M_DOC_IN_TEMP_CNT','LO_FLT','HI_FLT','EX_FLT')
F_M.Fault('F_M_Doc_in_temp_raw', '0','F_M_DOC_IN_TEMP_RAW','LO_FLT','HI_FLT')
F_M.Fault('F_M_Doc_in_temp_noi', '0')
F_M.Fault('F_M_Doc_in_temp_plau', '0')
F_M.Fault('F_M_Doc_in_temp_xc', '0')
F_M.Fault('F_M_Doc_lightoff', '0')
F_M.Fault('F_M_Dpf_dp_plugged_dp', '0')
F_M.Fault('F_M_Dpf_dp_overload_dp', '0')
F_M.Fault('F_M_Dpf_dp_overload_mdl', '0')
F_M.Fault('F_M_Dpf_dp_plugged_mdl', '0')
F_M.Fault('F_M_Dpf_dp_empty_can', '0')
F_M.Fault('F_M_Dpf_dp_plau1', '0')
F_M.Fault('F_M_Dpf_dp_plau2_neg', '0')
F_M.Fault('F_M_Dpf_dp_plau2_tbc', '0')
F_M.Fault('F_M_Dpf_dp_sens_noi', '0')
F_M.Fault('F_M_Dpf_dp_sensor_hi', '0')
F_M.Fault('F_M_Dpf_dp_sensor_lo', '0')
F_M.Fault('F_M_Dpf_eff', '0')
F_M.Fault('F_M_Dpf_in_temp', '0')
F_M.Fault('F_M_Dpf_in_temp_hi', '0')
F_M.Fault('F_M_Dpf_in_temp_lo', '0')
F_M.Fault('F_M_Dpf_in_temp_noi', '0')
F_M.Fault('F_M_Dpf_in_temp_plau', '0')
F_M.Fault('F_M_Dpf_in_temp_xc', '0')
F_M.Fault('F_M_Dpf_leak', '0')
F_M.Fault('F_M_Dpf_out_temp_plau', '0')
F_M.Fault('F_M_Dpf_out_temp_xc', '0')
F_M.Fault('F_M_Dropout_cu_relay', '0')
F_M.Fault('F_M_Dti_1', '0')
F_M.Fault('F_M_Dti_2', '0')
F_M.Fault('F_M_Dti_3', '0')
F_M.Fault('F_M_Dti_Mode06', '0')
F_M.Fault('F_M_Ecu_case_tp_hi', '0')
F_M.Fault('F_M_Ecu_case_tp_lo', '0')
F_M.Fault('F_M_Ecu_case_tp_noi', '0')
F_M.Fault('F_M_Ecu_pcb_temp', '0')
F_M.Fault('F_M_Edp_write', '0')
F_M.Fault('F_M_Edp_nvm', '0')
F_M.Fault('F_M_Egr_error_air_hi', '0')
F_M.Fault('F_M_Egr_error_air_lo', '0')
F_M.Fault('F_M_Egr_fdb_pos', '0')
F_M.Fault('F_M_Egrh_control', '0')
F_M.Fault('F_M_Egrh_cool_bp_oc', '0')
F_M.Fault('F_M_Egrh_cool_bp_scg', '0')
F_M.Fault('F_M_Egrh_cool_bp_scv', '0')
F_M.Fault('F_M_Egrh_fdb_hi', '0')
F_M.Fault('F_M_Egrh_fdb_lo', '0')
F_M.Fault('F_M_Egrh_hb_curr', '0')
F_M.Fault('F_M_Egrh_hb_ena', '0')
F_M.Fault('F_M_Egrh_hb_oc', '0')
F_M.Fault('F_M_Egrh_hb_ot', '0')
F_M.Fault('F_M_Egrh_hb_sc', '0')
F_M.Fault('F_M_Egrh_hb_sc2b', '0')
F_M.Fault('F_M_Egrh_hb_sc2g', '0')
F_M.Fault('F_M_Egrh_hb_sc2v', '0')
F_M.Fault('F_M_Egrh_hb_sc_ld', '0')
F_M.Fault('F_M_Egrh_hb_self', '0')
F_M.Fault('F_M_Egrh_hb_th_wrn', '0')
F_M.Fault('F_M_Egrh_hb_uv', '0')
F_M.Fault('F_M_Egrh_hb_wrn_cr', '0')
F_M.Fault('F_M_Egrh_low_flow', '0')
F_M.Fault('F_M_Egrl_dp_drift_hi', '0')
F_M.Fault('F_M_Egrl_dp_drift_lo', '0')
F_M.Fault('F_M_Egrl_dp_plau', '0')
F_M.Fault('F_M_Egrl_in_p_drift', '0')
F_M.Fault('F_M_Egrl_in_p_plau', '0')
F_M.Fault('F_M_Egrl_in_temp_xc', '0')
F_M.Fault('F_M_Egrl_low_flow', '0')
F_M.Fault('F_M_Eng_brk_ena_sw_elec', '0')
F_M.Fault('F_M_Eng_brk_sw_1_stuck', '0')
F_M.Fault('F_M_Eng_brk_sw_2_stuck', '0')
F_M.Fault('F_M_Eng_brk_sw_plau', '0')
F_M.Fault('F_M_Eng_spd_gauge_oc', '0')
F_M.Fault('F_M_Eng_spd_gauge_sc2g', '0')
F_M.Fault('F_M_Eng_spd_gauge_sc2v', '0')
F_M.Fault('F_M_Exh_brk_vlv_sc2vbatt', '0')
F_M.Fault('F_M_Exh_brk_vlv_oc', '0')
F_M.Fault('F_M_Exh_brk_vlv_sc2g', '0')
F_M.Fault('F_M_Esc_ana_sw_oc', '0')
F_M.Fault('F_M_Esc_ana_sw_sc2g', '0')
F_M.Fault('F_M_Esc_ana_sw_sc2v', '0')
F_M.Fault('F_M_Esc_ana_sw_unplau', '0')
F_M.Fault('F_M_Esm_esc_dec_stk', '0')
F_M.Fault('F_M_Esm_esc_inc_stk', '0')
F_M.Fault('F_M_Esm_esc_sw_plaus', '0')
F_M.Fault('F_M_Esc_switch','0', 'ICV_ESC','INC_STCK','DEC_STCK','BOTH_ON')
F_M.Fault('F_M_Esc_switch_inc_stuck', '0')
F_M.Fault('F_M_Esc_switch_dec_stuck', '0')
F_M.Fault('F_M_Esc_switch_inc_dec', '0')
F_M.Fault('F_M_Esm_0_trq', '0')
F_M.Fault('F_M_Esm_access_torq','0')
F_M.Fault('F_M_Esm_alterna_torq','0')
F_M.Fault('F_M_Esm_air_cond','0')
F_M.Fault('F_M_Esm_adc', 'ESM_ADC_SAFETY_NUMBER_CPV')
F_M.Fault('F_M_Esm_battery','0')
F_M.Fault('F_M_Esm_brk_switch', '0')
F_M.Fault('F_M_Esm_clutch', '0')
F_M.Fault('F_M_Esm_cruise_ctrl', '0')
F_M.Fault('F_M_Esm_cont_trq', '0')
F_M.Fault('F_M_Esm_cool_temp', '0')
F_M.Fault('F_M_Esm_cruise_regul', '0')
F_M.Fault('F_M_Esm_cruise_trq', '0')
F_M.Fault('F_M_Esm_cruise_switch', '0')
F_M.Fault('F_M_Esm_ecu_error', '0')
F_M.Fault('F_M_Esm_ecu_warning', '0')
F_M.Fault('F_M_Esm_eng_spd', '0')
F_M.Fault('F_M_Esm_engine_off', '0')
F_M.Fault('F_M_Esm_exh_brk_adc', '0')
F_M.Fault('F_M_Esm_exh_brk', '0')
F_M.Fault('F_M_Esm_fc_disabl_inj', '0')
F_M.Fault('F_M_Esm_fc_hp_disabl', '0')
F_M.Fault('F_M_Esm_gnd_track2', '0')
F_M.Fault('F_M_Esm_inj_bal', '0')
F_M.Fault('F_M_Esm_J1939_ccvsto', '0')
F_M.Fault('F_M_Esm_j1939_eec2to', '0')
F_M.Fault('F_M_Esm_j1939_pedal', '0')
F_M.Fault('F_M_Esm_j1939_pto_to', '0')
F_M.Fault('F_M_Esm_mdp', '0')
F_M.Fault('F_M_Esm_mem_code_l2', '0')
F_M.Fault('F_M_Esm_mem_data_l2', '0')
F_M.Fault('F_M_Esm_mem_ram_l2', '0')
F_M.Fault('F_M_Esm_mm_disabl_inj', '0')
F_M.Fault('F_M_Esm_mm_hp_disabl', '0')
F_M.Fault('F_M_Esm_mm_l2_trip', '0')
F_M.Fault('F_M_Esm_mm_l3_trip', '0')
F_M.Fault('F_M_Esm_mm_query', '0')
F_M.Fault('F_M_Esm_mm_reset', '0')
F_M.Fault('F_M_Esm_mm_timeout', '0')
F_M.Fault('F_M_Esm_mm_trip', '0')
F_M.Fault('F_M_Esm_op_mode', '0')
F_M.Fault('F_M_Esm_outen_fail', '0')
F_M.Fault('F_M_Esm_ped_foot', '0')
F_M.Fault('F_M_Esm_ped_hand', '0')
F_M.Fault('F_M_Esm_pfc_fail', '0')
F_M.Fault('F_M_Esm_pls_chk_bank', '0')
F_M.Fault('F_M_Esm_pls_chk_c2i', '0')
F_M.Fault('F_M_Esm_pls_chk_l1qt', '0')
F_M.Fault('F_M_Esm_pls_chk_nbr', '0')
F_M.Fault('F_M_Esm_pls_chk_toff', '0')
F_M.Fault('F_M_Esm_pls_chk_ton', '0')
F_M.Fault('F_M_Esm_pls_chk_tooth', '0')
F_M.Fault('F_M_Esm_pls_chk_type', '0')
F_M.Fault('F_M_Esm_pulse_cmp_l1', '0')
F_M.Fault('F_M_Esm_pulse_cmp_l2', '0')
F_M.Fault('F_M_Esm_pwoff_injlck', '0')
F_M.Fault('F_M_Esm_pwoff_reset', '0')
F_M.Fault('F_M_Esm_qst_tout', '0')
F_M.Fault('F_M_Esm_reduced', '0')
F_M.Fault('F_M_Esm_rpc', '0', 'ESM_ESM_RPC_FAULT', 'RANGE', 'GRAD_L1', 'GRAD_L2')
F_M.Fault('F_M_Esm_tpu_ram', '0')
F_M.Fault('F_M_Esm_tsc1', '0')
F_M.Fault('F_M_Esm_tsc1_to', '0')
F_M.Fault('F_M_Esm_vdg_both_on', '0')
F_M.Fault('F_M_Esm_vdg_dec_stck', '0')
F_M.Fault('F_M_Esm_vdg_inc_stck', '0')
F_M.Fault('F_M_Esm_veh_speed', '0')
F_M.Fault('F_M_Exh_brk_ctrl', '0')
F_M.Fault('F_M_Exh_brk_stuck_open', '0')
F_M.Fault('F_M_Exh_brk_stuck_shut', '0')
F_M.Fault('F_M_Exh_brk_sw_1_stuck', '0')
F_M.Fault('F_M_Exh_brk_sw_2_stuck', '0')
F_M.Fault('F_M_Exh_brk_sw_plau', '0')
F_M.Fault('F_M_Exh_over_temp', '0')
F_M.Fault('F_M_Exhaust_brake_adc', '0')
F_M.Fault('F_M_Ext_air_temp', '0')
F_M.Fault('F_M_Ext_air_temp_xc', '0')
F_M.Fault('F_M_Ebrake_sc2b', '0')
F_M.Fault('F_M_Ebrake_fet_off_st', '0')
F_M.Fault('F_M_Fan_typ2', '0')
F_M.Fault('F_M_Fan_typ1', '0')
F_M.Fault('F_M_Fan1_drive_oc', '0')
F_M.Fault('F_M_Fan1_drive_sc2g', '0')
F_M.Fault('F_M_Fan1_drive_sc2v', '0')
F_M.Fault('F_M_Fan2_drive_oc', '0')
F_M.Fault('F_M_Fan2_drive_sc2g', '0')
F_M.Fault('F_M_Fan2_drive_sc2v', '0')
F_M.Fault('F_M_Fci_acc_decode', 'APP_NUMBER_OF_ACCEL_CPV')
F_M.Fault('F_M_Fci_bank_sc2gnd', 'P_L_INJ_NUMBER_OF_BANKS_CPV')
F_M.Fault('F_M_Fci_bank_sc2vbat', 'P_L_INJ_NUMBER_OF_BANKS_CPV')
F_M.Fault('F_M_Fci_ecu_drive', 'P_L_INJ_NUMBER_OF_BANKS_CPV')
F_M.Fault('F_M_Fci_inj_bal_loop', '0')
F_M.Fault('F_M_Fci_inj_bal_low', 'APP_NUMBER_OF_INJECTORS_CPV')
F_M.Fault('F_M_Fci_inj_bal_trim', '0')
F_M.Fault('F_M_Fci_oc_inj', 'APP_NUMBER_OF_INJECTORS_CPV')
F_M.Fault('F_M_Fci_sc_inj', 'APP_NUMBER_OF_INJECTORS_CPV')
F_M.Fault('F_M_Fci_spi_inj', 'P_L_INJ_NUMBER_OF_BANKS_CPV')
F_M.Fault('F_M_Flash_code_sw_stk', '0')
F_M.Fault('F_M_Fuel_filt_pres', '0')
F_M.Fault('F_M_Fuel_filt_pres_adc', '0')
F_M.Fault('F_M_Fuel_filt_plugged_lvl1', '0')
F_M.Fault('F_M_Fuel_filt_plugged_lvl2', '0')
F_M.Fault('F_M_Fuel_filt_plugged_flow', '0')
F_M.Fault('F_M_Fuel_signal_invalid', '0')
F_M.Fault('F_M_Fuel_htr_drv_oc', '0')
F_M.Fault('F_M_Fuel_htr_drv_s2b', '0')
F_M.Fault('F_M_Fuel_htr_drv_s2g', '0')
F_M.Fault('F_M_Fuel_temp', '0')
F_M.Fault('F_M_Fuel_temp_lo', '0')
F_M.Fault('F_M_Fuel_temp_hi', '0')
F_M.Fault('F_M_Fuel_temp_grad', '0')
F_M.Fault('F_M_Fuel_temp_plau', '0')
F_M.Fault('F_M_Fuel_temp_xc', '0')
F_M.Fault('F_M_Glow_plug_oc', '0')
F_M.Fault('F_M_Glow_plug_rly', '0')
F_M.Fault('F_M_Glow_plug_sc2g', '0')
F_M.Fault('F_M_Glow_plug_sc', '0')
F_M.Fault('F_M_Hp_crt_ctrl', '0','P_L_HP_CRT_CTRL_FAULT','TRIM_HIGH','TRIM_LOW')
F_M.Fault('F_M_Hp_crt_fb', '0', 'P_L_HP_CRT_FB_FAULT', 'EX', 'HIGH', 'LOW')
F_M.Fault('F_M_Hp_ctrl_trim_hi', '0')
F_M.Fault('F_M_Hp_ctrl_trim_lo', '0')
F_M.Fault('F_M_Hp_ol_slope', '0')
F_M.Fault('F_M_Hp_ol_slope_step', '0')
F_M.Fault('F_M_Hp_open_timeout', '0')
F_M.Fault('F_M_Hpv_drive_oc', '0')
F_M.Fault('F_M_Hpv_drive_sc2g', '0')
F_M.Fault('F_M_Hpv_drive_sc2v', '0')
F_M.Fault('F_M_I_c_strt_cnd_late', '0')
F_M.Fault('F_M_Ic_out_temp_plau', '0')
F_M.Fault('F_M_Ic_out_temp_xc', '0')
F_M.Fault('F_M_Ic_temp_hi', '0')
F_M.Fault('F_M_Ic_temp_lo', '0')
F_M.Fault('F_M_Ic_temp_noi', '0')
F_M.Fault('F_M_Ici_gp_lamp_oc', '0')
F_M.Fault('F_M_Ici_gp_lamp_sc', '0')
F_M.Fault('F_M_Ici_gp_lamp_sc2g', '0')
F_M.Fault('F_M_Ici_mi_lamp', '0')
F_M.Fault('F_M_Ici_mi_lamp_oc', '0')
F_M.Fault('F_M_Ici_mi_lamp_sc', '0' )
F_M.Fault('F_M_Ici_mi_lamp_sc2g', '0')
F_M.Fault('F_M_Im_crt_ctrl', '0', 'P_L_IM_CRT_CTRL_FAULT', 'TRIM_LOW', 'TRIM_HIGH')
F_M.Fault('F_M_Im_crt_fb', '0','P_L_IM_CRT_FB_FAULT', 'LOW', 'HIGH')
F_M.Fault('F_M_Im_ctrl_pwm_high', '0')
F_M.Fault('F_M_Im_ctrl_qhi_high', '0')
F_M.Fault('F_M_Im_ctrl_qhi_low', '0')
F_M.Fault('F_M_Im_ctrl_qlo_high', '0')
F_M.Fault('F_M_Im_ctrl_qlo_low', '0')
F_M.Fault('F_M_Imv_drive_oc', '0')
F_M.Fault('F_M_Imv_drive_sc', '0')
F_M.Fault('F_M_Imv_drive_sc2g', '0')
F_M.Fault('F_M_Imv_drive_sc2v', '0')
F_M.Fault('F_M_Imv_drive_sc2vbatt', '0')
F_M.Fault('F_M_Inj_low_railp', '0')
F_M.Fault('F_M_Inlet_air_hi', '0')
F_M.Fault('F_M_Inlet_air_lo', '0')
F_M.Fault('F_M_Inlet_air_noi', '0')
F_M.Fault('F_M_Inlet_air_temp_xc', '0')
F_M.Fault('F_M_Intake_plen_temp_xc', '0')
F_M.Fault('F_M_Intercooler_temp_xc', '0')
F_M.Fault('F_M_Intk_pl_temp_plau', '0')
F_M.Fault('F_M_Intk_pl_temp_xc', '0')
F_M.Fault('F_M_Ip_temp_hi', '0')
F_M.Fault('F_M_Ip_temp_lo', '0')
F_M.Fault('F_M_Ip_temp_noi', '0')
F_M.Fault('F_M_J1939_a1doc_tmo', '0')
F_M.Fault('F_M_J1939_a1defi_tmo', '0')
F_M.Fault('F_M_J1939_a1scrdsi1_t', '0')
F_M.Fault('F_M_J1939_amb_tmo', '0')
F_M.Fault('F_M_J1939_at1ig1_tmo', '0')
F_M.Fault('F_M_J1939_at1ig2_tmt', '0')
F_M.Fault('F_M_J1939_at1igc1_tmo', '0')
F_M.Fault('F_M_J1939_at1og1_tmo', '0')
F_M.Fault('F_M_J1939_at1og2_tmo', '0')
F_M.Fault('F_M_J1939_at1ogc1_tmo', '0')
F_M.Fault('F_M_J1939_at1t1i_tmo', '0')
F_M.Fault('F_M_J1939_ccvs1_tmout', '0')
F_M.Fault('F_M_J1939_Cm1_tmo', '0')
F_M.Fault('F_M_J1939_dd_timeout', '0')
F_M.Fault('F_M_J1939_dm1_tmo', '0')
F_M.Fault('F_M_J1939_ebc1_tmo', '0')
F_M.Fault('F_M_J1939_ebc2_tmo', '0')
F_M.Fault('F_M_J1939_eec2_timeout', '0')
F_M.Fault('F_M_J1939_eec3_tmout', '0')
F_M.Fault('F_M_J1939_etc1_tmout','0')
F_M.Fault('F_M_J1939_etc2_tmo','0')
F_M.Fault('F_M_J1939_etc7_tmo','0')
F_M.Fault('F_M_J1939_erc1_tmo','0')
F_M.Fault('F_M_J1939_pto_timeout', '0')
F_M.Fault('F_M_J1939_tco1_tmo', '0')
F_M.Fault('F_M_J1939_tsc1_to', '0')
F_M.Fault('F_M_Low_fuel_level_sw', '0')
F_M.Fault('F_M_Lp_relay_oc', '0')
F_M.Fault('F_M_Lp_relay_sc2g', '0')
F_M.Fault('F_M_Lp_relay_sc2v', '0')
F_M.Fault('F_M_Oilp_gauge_oc', '0')
F_M.Fault('F_M_Oilp_gauge_sc2g', '0')
F_M.Fault('F_M_Oilp_gauge_sc2v', '0')
F_M.Fault('F_M_oil_pres_lamp' , '0')
F_M.Fault('F_M_Oil_pre_lmp_oc','0')
F_M.Fault('F_M_Oil_pre_lmp_sc2v','0')
F_M.Fault('F_M_Oil_pre_lmp_sc2g','0')
F_M.Fault('F_M_Map_drift_lo', '0')
F_M.Fault('F_M_Map_drift_hi', '0')
F_M.Fault('F_M_Map_drift', '0')
F_M.Fault('F_M_Map_plau', '0')
F_M.Fault('F_M_Map_plau_lo', '0')
F_M.Fault('F_M_Map_plau_hi', '0')
F_M.Fault('F_M_Map_plau_noref', '0')
F_M.Fault('F_M_Map_sensor_hi', '0')
F_M.Fault('F_M_Map_sensor_lo', '0')
F_M.Fault('F_M_Map_sensor_noi', '0')
F_M.Fault('F_M_Map_sensor_overp', '0')
F_M.Fault('F_M_Mdp_map_check', '0')
F_M.Fault('F_M_Mdp_min_absolute', 'APP_NUMBER_OF_INJECTORS_CPV')
F_M.Fault('F_M_Mdp_no_upd_cond', 'I_C_ACC_NUMBER_MDP_ZONE_CPV')
F_M.Fault('F_M_Mdp_no_upd_strat', 'I_C_ACC_NUMBER_MDP_ZONE_CPV')
F_M.Fault('F_M_Mdp_trim_hi_inj', 'APP_NUMBER_OF_INJECTORS_CPV', 'I_C_MDP_TRIM_HI_INJ_FAULT', 'HI', 'ME', 'LO', 'SL_H', 'SL_M', 'SL_L')
F_M.Fault('F_M_Mdp_trim_low_inj', 'APP_NUMBER_OF_INJECTORS_CPV', 'I_C_MDP_TRIM_LOW_INJ_FAULT', 'HI', 'ME', 'LO', 'SL_H', 'SL_M', 'SL_L')
F_M.Fault('F_M_Mdp_upd_failed', 'APP_NUMBER_OF_INJECTORS_CPV')
F_M.Fault('F_M_Memory_int_code', '0')
F_M.Fault('F_M_Memory_int_cvn', '0')
F_M.Fault('F_M_Memory_int_data', '0')
F_M.Fault('F_M_Memory_int_ram', '0')
F_M.Fault('F_M_Neutral_stk_cl', '0')
F_M.Fault('F_M_Neutral_stk_op', '0')
F_M.Fault('F_M_Oil_level','0')
F_M.Fault('F_M_Oil_level_adc','0')
F_M.Fault('F_M_Oil_level_sensor','0')
F_M.Fault('F_M_Oil_pres_adc', '0')
F_M.Fault('F_M_Oil_press_cnts', '0')
F_M.Fault('F_M_Oil_pres_cal_hi_stp', '0')
F_M.Fault('F_M_Oil_pres_cal_lo_run', '0')
F_M.Fault('F_M_Oil_pres_cal_hi_run', '0')
F_M.Fault('F_M_Oil_temp_sens_hi', '0')
F_M.Fault('F_M_Oil_temp_sens_lo', '0')
F_M.Fault('F_M_Oil_temp_sens_grad', '0')
F_M.Fault('F_M_Oil_temp_sensor'    	 ,'0')
F_M.Fault('F_M_Oil_temp_plau', '0')
F_M.Fault('F_M_Oil_temp_xc', '0')
F_M.Fault('F_M_Overpressure_hpv', '0')
F_M.Fault('F_M_Overpressure_imv', '0')
F_M.Fault('F_M_Overpressure_und', '0')
F_M.Fault('F_M_P3_drift', '0')
F_M.Fault('F_M_P3_drift_lo', '0')
F_M.Fault('F_M_P3_drift_hi', '0')
F_M.Fault('F_M_P3_plau', '0')
F_M.Fault('F_M_P3_sensor_hi', '0')
F_M.Fault('F_M_P3_sensor_lo', '0')
F_M.Fault('F_M_P3_sensor_noi', '0')
F_M.Fault('F_M_P_l_nvm_device', '0')
F_M.Fault('F_M_Pedal_foot_coh', '0')
F_M.Fault('F_M_Pedal_foot_t1_hi', '0')
F_M.Fault('F_M_Pedal_foot_t1_lo', '0')
F_M.Fault('F_M_Pedal_foot_t2_hi', '0')
F_M.Fault('F_M_Pedal_foot_t2_lo', '0')
F_M.Fault('F_M_Pedal_foot_t2', '0','P_L_PEDAL_FOOT_T2_FLT' ,'SUP_0' , 'SUP_1')
F_M.Fault('F_M_Pedal_foot_t1', '0','P_L_PEDAL_FOOT_T1_FLT' ,'SUP_0' , 'SUP_1')
F_M.Fault('F_M_Pedal_foot_correl', '0')
F_M.Fault('F_M_Pedal_foot_limph', '0')
F_M.Fault('F_M_Pedal_foot_reduc', '0')
F_M.Fault('F_M_Pedal_foot_stuck', '0')
F_M.Fault('F_M_Pedal_hand_reduc', '0')
F_M.Fault('F_M_Pedal_hand_correl', '0')
F_M.Fault('F_M_Hand_throttle_reduc', '0')
F_M.Fault('F_M_Pedal_hand_t1' , '0' ,'P_L_PEDAL_HAND_T1_FLT' ,'SUP_0' , 'SUP_1')
F_M.Fault('F_M_Pedal_hand_t1_hi' , '0')
F_M.Fault('F_M_Pedal_hand_t1_lo' , '0')
F_M.Fault('F_M_Pedal_hand_t2' , '0' ,'P_L_PEDAL_HAND_T2_FLT' ,'SUP_0' , 'SUP_1')
F_M.Fault('F_M_Pedal_hand_t2_hi' , '0')
F_M.Fault('F_M_Pedal_hand_t2_lo' , '0')
F_M.Fault('F_M_Pedal_hand_coh', '0')
F_M.Fault('F_M_Pedal_hand_limph', '0')
F_M.Fault('F_M_Hand_throttle_limph', '0')
F_M.Fault('F_M_Pedal_hand_stuck', '0')
F_M.Fault('F_M_Hand_throttle_stuck', '0')
F_M.Fault('F_M_Pedal_limph', '0')
F_M.Fault('F_M_Pedal_reduc', '0')
F_M.Fault('F_M_Rail_pres_frz', '0')
F_M.Fault('F_M_Rail_pres_drop', '0')
F_M.Fault('F_M_Rail_pres_grad', '0')
F_M.Fault('F_M_Rail_pres_hi', '0')
F_M.Fault('F_M_Rail_pres_lo', '0')
F_M.Fault('F_M_Railp_cal', '0', 'P_L_RAILP_CAL_FAULT', 'LOW', 'HIGH', 'MED_TST_FLT')
F_M.Fault('F_M_Rpc_build_lowtk', '0')
F_M.Fault('F_M_Rpc_build_nrmtk', '0')
F_M.Fault('F_M_Rpc_ctrl_2_neg', '0')
F_M.Fault('F_M_Rpc_ctrl_2_pos', '0')
F_M.Fault('F_M_Rpc_ctrl_ho_neg', '0')
F_M.Fault('F_M_Rpc_ctrl_ho_pos', '0')
F_M.Fault('F_M_Rpc_ctrl_io_neg', '0')
F_M.Fault('F_M_Rpc_ctrl_io_pos', '0')
F_M.Fault('F_M_Rpc_ctrl_lt_neg', '0')
F_M.Fault('F_M_Rpc_ctrl_lt_pos', '0')
F_M.Fault('F_M_Rpc_ctrl_rd_neg', '0')
F_M.Fault('F_M_Rpc_ctrl_rd_pos', '0')
F_M.Fault('F_M_Rpc_overp_t_out', '0')
F_M.Fault('F_M_Rpc_plv_is_open', '0')
F_M.Fault('F_M_Rpc_sas_rpf', '0')
F_M.Fault('F_M_Rpc_vlc_ofst_clmp', '0')
F_M.Fault('F_M_Rpc_vlc_ofst_high', '0')
F_M.Fault('F_M_Sas_in_lamp_oc', '0')
F_M.Fault('F_M_Sas_in_lamp_sc2g', '0')
F_M.Fault('F_M_Sas_in_lamp_sc2v', '0')
F_M.Fault('F_M_Scr_in_temp_plau', '0')
F_M.Fault('F_M_Scr_in_temp_xc', '0')
F_M.Fault('F_M_Sr_hsd_sc2g', '0')
F_M.Fault('F_M_Sr_hsd_sc2v', '0')
F_M.Fault('F_M_Sr_lsd_sc2g', '0')
F_M.Fault('F_M_Sr_lsd_sc2v', '0')
F_M.Fault('F_M_Sr_oc', '0')
F_M.Fault('F_M_Start_relay_oc', '0')
F_M.Fault('F_M_Start_relay_sc', '0')
F_M.Fault('F_M_Start_relay_sc2g', '0')
F_M.Fault('F_M_Start_rly_drive', '0')
F_M.Fault('F_M_Stuck_cu_relay', '0')
F_M.Fault('F_M_Sw_watchdog', '0')
F_M.Fault('F_M_T2_temp_cnt', '0')
F_M.Fault('F_M_Toss_speed', '0')
F_M.Fault('F_M_Throt_control', '0')
F_M.Fault('F_M_Throt_track_1_hi', '0')
F_M.Fault('F_M_Throt_track_1_lo', '0')
F_M.Fault('F_M_Throt_track_2_hi', '0')
F_M.Fault('F_M_Throt_track_2_lo', '0')
F_M.Fault('F_M_Throt_correlation', '0')
F_M.Fault('F_M_Throt_spring_defect', '0')
F_M.Fault('F_M_Thrtl_hb_oc', '0')
F_M.Fault('F_M_Thrtl_hb_ot', '0')
F_M.Fault('F_M_Thrtl_hb_sc2b', '0')
F_M.Fault('F_M_Thrtl_hb_sc2g', '0')
F_M.Fault('F_M_Thrtl_hb_sc2v', '0')
F_M.Fault('F_M_Thrtl_hb_sc', '0')
F_M.Fault('F_M_Thrtl_hb_sc_ld', '0')
F_M.Fault('F_M_Thrtl_hb_uv', '0')
F_M.Fault('F_M_Torque_switch', '0', 'P_L_TORQUE_SWITCH', 'SUP_0', 'SUP_1', 'SUP_2')
F_M.Fault('F_M_Torque_sw_uplau', '0')
F_M.Fault('F_M_Torque_sw_stuck', '0')
F_M.Fault('F_M_Turb_in_temp', '0')
F_M.Fault('F_M_Turb_in_temp_plau', '0')
F_M.Fault('F_M_Turb_in_tp_hi', '0')
F_M.Fault('F_M_Turb_in_tp_lo', '0')
F_M.Fault('F_M_Turb_in_tp_noi', '0')
F_M.Fault('F_M_Turb_out_temp_plau', '0')
F_M.Fault('F_M_Turbine_in_temp_xc', '0')
F_M.Fault('F_M_Turbine_out_temp_xc', '0')
F_M.Fault('F_M_Tyre_size_max_wear', '0')
F_M.Fault('F_M_Vdg_rpm_ofst_sw', '0')
F_M.Fault('F_M_Veh_dist', '0')
F_M.Fault('F_M_Veh_speed', '0')
F_M.Fault('F_M_Veh_spd_oc', '0')
F_M.Fault('F_M_Veh_spd_sc2b', '0')
F_M.Fault('F_M_Veh_spd_sc2g', '0')
F_M.Fault('F_M_Vext1', '0')
F_M.Fault('F_M_Vext2', '0')
F_M.Fault('F_M_vext2aux', '0')
F_M.Fault('F_M_Vext3', '0')
F_M.Fault('F_M_Vext4', '0')
F_M.Fault('F_M_Vext_spi', '0')
F_M.Fault('F_M_Vext_vccs', '0')
F_M.Fault('F_M_Vgth_pos_hi', '0')
F_M.Fault('F_M_Vgth_pos_lo', '0')
F_M.Fault('F_M_Vgth_overboost', '0')
F_M.Fault('F_M_Vgth_pos_ctrl', '0')
F_M.Fault('F_M_Vgth_pos_lrn', '0')
F_M.Fault('F_M_Vgth_underboost', '0')
F_M.Fault('F_M_Vgth_valve_oc', '0')
F_M.Fault('F_M_Vgth_valve_sc2g', '0')
F_M.Fault('F_M_Vgth_valve_sc2v', '0')
F_M.Fault('F_M_Vgtl_err_press_hi', '0')
F_M.Fault('F_M_Vgtl_err_press_lo', '0')
F_M.Fault('F_M_Vgtl_pos_lrn', '0')
F_M.Fault('F_M_Vpu', '0')
F_M.Fault('F_M_Vss_overrun', '0')
F_M.Fault('F_M_Vss_signal_loss', '0')
F_M.Fault('F_M_Vss_consistency', '0')
F_M.Fault('F_M_Water_in_fuel_fdb', '0')
F_M.Fault('F_M_Wif_lamp_oc', '0')
F_M.Fault('F_M_Wif_lamp_sc2g', '0')
F_M.Fault('F_M_Wif_lamp_sc2v', '0')
F_M.Fault('F_M_Wif_sensor_sc2g', '0')
F_M.Fault('F_M_Wif_sensor_sc2v', '0')
F_M.Fault('F_M_Wif_sensor', '0')
F_M.Fault('F_M_Water_in_fuel', '0')
F_M.Fault('F_M_Water_in_fuel_plaus1', '0')
F_M.Fault('F_M_Water_in_fuel_plaus2', '0')
F_M.Fault('F_M_Wraf_com_oc', '0')
F_M.Fault('F_M_Wraf_fco', '0')
F_M.Fault('F_M_Wraf_fco_0', '0')
F_M.Fault('F_M_Wraf_fco_1', '0')
F_M.Fault('F_M_Wraf_fco_delay', '0')
F_M.Fault('F_M_Wraf_fco_delay_0', '0')
F_M.Fault('F_M_Wraf_fco_delay_1', '0')
F_M.Fault('F_M_Wraf_fco_trans', '0')
F_M.Fault('F_M_Wraf_fco_trans_0', '0')
F_M.Fault('F_M_Wraf_fco_trans_1', '0')
F_M.Fault('F_M_Wraf_htr_oc', '0')
F_M.Fault('F_M_Wraf_htr_sc2b', '0')
F_M.Fault('F_M_Wraf_htr_sc2g', '0')
F_M.Fault('F_M_Wraf_ip_diag_hi', '0')
F_M.Fault('F_M_Wraf_ip_diag_low', '0')
F_M.Fault('F_M_Wraf_ip_oc', '0')
F_M.Fault('F_M_Wraf_ip_sc2g', '0')
F_M.Fault('F_M_Wraf_letoff_resp', '0')
F_M.Fault('F_M_Wraf_level_hi', '0')
F_M.Fault('F_M_Wraf_level_lo', '0')
F_M.Fault('F_M_Wraf_oc_tag', '0')
F_M.Fault('F_M_Wraf_resp_neg_dly', '0')
F_M.Fault('F_M_Wraf_resp_neg_slow', '0')
F_M.Fault('F_M_Wraf_resp_pos_dly', '0')
F_M.Fault('F_M_Wraf_resp_pos_slow', '0')
F_M.Fault('F_M_Wraf_s2vbat_all', '0')
F_M.Fault('F_M_Wraf_sens_air_val', '0')
F_M.Fault('F_M_Wraf_sens_heater', '0')
F_M.Fault('F_M_Wraf_sens_plau', '0')
F_M.Fault('F_M_Wraf_sens_rng_h', '0')
F_M.Fault('F_M_Wraf_sens_rng_l', '0')
F_M.Fault('F_M_Wraf_sensor', '0')
F_M.Fault('F_M_Wraf_spi', '0')
F_M.Fault('F_M_Wraf_srst', '0')
F_M.Fault('F_M_Wraf_stg_time_out', '0')
F_M.Fault('F_M_Wraf_time_out', '0')
F_M.Fault('F_M_Wraf_vs_oc', '0')
F_M.Fault('F_M_Wraf_vs_sc2g', '0')
#F_M.Fault('F_M_Variant_coding', '0')
F_M.Fault('F_M_Dpf_rgn_frq_high', '0')
F_M.Fault('F_M_Esm_vdg_err',0)
F_M.Fault('F_M_Oil_level_lamp_oc',0)
F_M.Fault('F_M_Oil_level_lamp_sc2b',0)
F_M.Fault('F_M_Oil_level_lamp_sc2g',0)
F_M.Fault('F_M_Thrtl_fdb_lo', '0')
F_M.Fault('F_M_Thrtl_fdb_hi', '0')
F_M.Fault('F_M_Thrtl_fdb_noi', '0')
F_M.Fault('F_M_Thrtl_atsk_count', '0')
F_M.Fault('F_M_Thrtl_obj_stuck', '0')
F_M.Fault('F_M_Thrtl_pos', '0')
F_M.Fault('F_M_Thrtl_spr_broken', '0')
F_M.Fault('F_M_Thrtl_vbatt_hi', '0')
F_M.Fault('F_M_Thrtl_vbatt_lo', '0')
F_M.Fault('F_M_Thrtl_vlv_stuck', '0')
F_M.Fault('F_M_Thrt_lrn_1st_cl', '0')
F_M.Fault('F_M_Thrt_lrn_1st_op', '0')
F_M.Fault('F_M_Thrt_lrn_cl_lgdv', '0')
F_M.Fault('F_M_Thrt_lrn_cl_shdv', '0')
F_M.Fault('F_M_Thrt_lrn_op_lgdv', '0')
F_M.Fault('F_M_Thrt_lrn_op_shdv', '0')
F_M.Fault('F_M_Egrh_lrn_1st_cl',0)
F_M.Fault('F_M_Egrh_fdb_noi',0)
F_M.Fault('F_M_Egrh_lrn_cl_lgdv',0)
F_M.Fault('F_M_Egrh_pos',0)
F_M.Fault('F_M_Egrh_lrn_cl_shdv',0)
F_M.Fault('F_M_Egrh_atsk_count',0)
F_M.Fault('F_M_Egrh_valve_stuck',0)
F_M.Fault('F_M_Egrh_lrn_op_lgdv',0)
F_M.Fault('F_M_Egrh_lrn_1st_op',0)
F_M.Fault('F_M_Egrh_obj_stuck',0)
F_M.Fault('F_M_Egrh_lrn_op_shdv',0)
F_M.Fault('F_M_Egrh_vbatt_hi',0)
F_M.Fault('F_M_Egrh_vbatt_lo',0)
F_M.Fault('F_M_Egrh_spr_broken',0)

# ######################################################################################
# Mode06 Fault Definition
# ######################################################################################
# NOTE : Make sure to configure "namesup" field to 1 not 0, if there is no supplementary entry 
#        i.e 3rd entry of F_M.Mode6Fault should not be 0, but instead 1
F_M.Mode6Fault('F_M_Wraf_letoff_resp'   , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Wraf_level_hi'      , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Wraf_level_lo'      , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Doc_lightoff'       , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Doc_in_temp_plau'   , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_in_temp_plau'   , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Amf_plau_hi'        , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Amf_plau_lo'        , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Egr_error_air_hi'   , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Egr_error_air_lo'   , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Vgth_overboost'     , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Vgth_underboost'    , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_dp_plau1'       , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_dp_plau2_tbc'   , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_dp_plau2_neg'   , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_dp_plugged_dp'  , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_dp_plugged_mdl' , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_dp_overloaded'  , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_dp_overload_dp' , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_dp_overload_mdl', '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_leak'           , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_rgn_frq_high'    ,'0' ,'3'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dpf_dp_empty_can'   , '0' ,'1'   ,'VAL','MIN','MAX')
F_M.Mode6Fault('F_M_Dti_Mode06'         , '0' ,'3'   ,'VAL','MIN','MAX')




# #### DTI ####
# Parameter stem name, demand Ctype, can optionally override subm, dmnd, DMND_APV
# names where the naming convention has been broken in the application code

# For up to date comments see dti_generic1.py comment block
#        DTIs are split into two groups, control and short.
#        short types are an override which has a 16 bit type (normally S16),
#        control types are an override which has a BOOL_TYPE.
#        Each DTI is made up of a demand and a mode/subm portion.
#        Each DTI can be set by one of three sources, an APV, an ISO test or
#        by a Bypass setting from a HIL. Currently HIL not implemented.
#
#        Each record in dti.c that is autogenerated creates pointers to the various
#        sources. ISO sources are externed in from dti_iso_sub.c.
#        Also created are the various APV and variable records which are required,
#        as well as the T55 entries. By default the name of the DTI is used to create
#        all the constituent components, e.g a stem of DTI_Egr would yield a subm var
#        of DTI_Egr_subm, and a demand APV of DTI_EGR_DMND_APV.
#
#        The name of a DTI.Short or .Control should be DTI_Xxx
#        The name of a DTI.IsoShort or .Control should be the same name with iso, i.e DTI_Iso_xxx
#        The name of the DTI.IsoConfig should be the same name as the DTI, i.e DTI_Xxx
#        The DTI.IsoConfig needs to ensure the correct field is filled in depending on the type,
#        i.e
#                DTI_ISO_OUTPUT_CONTROL_VAL or
#                DTI_ISO_OUTPUT_SHORT_VAL
#
#        Each of these autogenerated names can be overriden by declaring a field in
#        config.py. The list below details what is currently valid.
#
#        subm        - override for default name construction of subm variable
#        dmnd        - override for default name construction of dmnd variable
#        SUBM_APV    - override for default name construction of subm APV
#        DMND_APV    - override for default name construction of dmnd APV
#        var         - override for type to inherit data dictionary data from (usually the item that the DTI overrides/controls
#        DMND_MAX_APV    - override for APV MAX defalt value (short only)
#        DMND_MIN_APV    - override for APV MIN defalt value (short only)
#        DEFAULT_SUBM_APV    - default value for SUBM APV
#        DEFAULT_DMND_APV    - default value for DMND APV

DTI.Control('DTI_Ac_active',
var = 'BOOL_TYPE',
dmnd_type= 'BOOL_TYPE',
subm_type = 'BOOL_TYPE',
dmnd = 'DTI_Ac_active_dmnd',
subm = 'DTI_Ac_active_subm',
DEFAULT_APV = '0'
)
DTI.Control('DTI_Egrh_pwo',
var = 'BOOL_TYPE',
dmnd_type= 'BOOL_TYPE',
subm_type = 'BOOL_TYPE',
dmnd = 'DTI_Egrh_pwo_dmnd',
subm = 'DTI_Egrh_pwo_subm',
DEFAULT_APV = '0'
)

DTI.Control('DTI_Egrh_lrn',
var = 'BOOL_TYPE',
dmnd_type= 'BOOL_TYPE',
subm_type = 'BOOL_TYPE',
dmnd = 'DTI_Egrh_lrn_dmnd',
subm = 'DTI_Egrh_lrn_subm',
DEFAULT_APV = '0'
)


DTI.Control('DTI_Egrh_cln',
var = 'BOOL_TYPE',
dmnd_type= 'BOOL_TYPE',
subm_type = 'BOOL_TYPE',
dmnd = 'DTI_Egrh_cln_dmnd',
subm = 'DTI_Egrh_cln_subm',
DEFAULT_APV = '0'
)

DTI.Control('DTI_Egrh_atsk',
var = 'BOOL_TYPE',
dmnd_type= 'BOOL_TYPE',
subm_type = 'BOOL_TYPE',
dmnd = 'DTI_Egrh_atsk_dmnd',
subm = 'DTI_Egrh_atsk_subm',
DEFAULT_APV = '0'
)


DTI.Short('DTI_Acc_assp_frequence',
    var = 'P_L_Acc_band_pass_filter_freq',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '3.6 * BIN4',
    DMND_MAX_APV = '8.4 * BIN4'
    )
DTI.Short('DTI_Acc_assp_gain',
    var = 'P_L_Acc_filter_gain_control',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0.1 * BIN10',
    DMND_MAX_APV = '2 * BIN10'
    )
DTI.Short('DTI_Acc_assp_time_cst',
    var = 'P_L_Acc_integrator_time_constant',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '40 * DEC0',
    DMND_MAX_APV = '600 * DEC0'
    )
DTI.Short('DTI_After_fuel',
    var = 'FQD_After_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_After_us_sep',
    var = 'ITD_After_us_sep_dmnd',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '65535 * BIN0'
    )
DTI.Short('DTI_Alt_duty_cycle',
    var = 'P_L_Alt_duty_cycle_output',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Alt_outp_pwm',
    var = 'ASM_Desired_alt_duty_cycle',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Amf_analog',
    var = 'IN_Amf_analog',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN5',
    DMND_MAX_APV = '2000 * BIN5'    
    )
DTI.Short('DTI_Batt_current',
    var = 'IN_Battery_current_raw',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN8',
    DMND_MAX_APV = '100 * BIN8'
    )
DTI.Short('DTI_Batt_temperature',
    var = 'IN_Batt_temp_raw',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-40 * BIN4',
    DMND_MAX_APV = '105 * BIN4'
    )
DTI.Short('DTI_Atm_pres',
    var = 'IN_Atmospheric_pressure',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '500 * BIN6'
    )
DTI.Short('DTI_Boostp',
    var = 'IN_Boost_pressure',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '500 * BIN6'
    )
DTI.Short('DTI_Calib_injector_num',
    var = 's_s_sync_lp_injector_to_run',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = 'APP_NUMBER_OF_INJECTORS_CPV - 1'
    )
DTI.Short('DTI_Calib_pilot_trim',
    var = 'I_C_Calib_pilot_trim_dmnd_cpy',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-500 * DEC0',
    DMND_MAX_APV = '500 * DEC0'
    )
DTI.Short('DTI_Chkd_after_fuel',
    var = 'DTI_Dummy_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Chkd_main_fuel',
    var = 'DTI_Dummy_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Chkd_pilot0_fuel',
    var = 'DTI_Dummy_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Chkd_pilot1_fuel',
    var = 'DTI_Dummy_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Chkd_pilot2_fuel',
    var = 'DTI_Dummy_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Chkd_post1_fuel',
    var = 'DTI_Dummy_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Chkd_post2_fuel',
    var = 'DTI_Dummy_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )

DTI.Short('DTI_Comb_mode',
    var = 'P_T_Comb_mode_req',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = 'P_T_NUM_COMB_MODES_CPV-1'
    )
DTI.Short('DTI_Coolant_temp_dutyc',
    var = 'P_L_Coolant_temp_out_dutyc',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Coolant_temp_freq',
    var = 'P_L_Coolant_temp_out_freq',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '15.375 * BIN4',
    DMND_MAX_APV = '1000 * BIN4'
    )      
DTI.Short('DTI_Desired_set_volt',
    var = 'ASM_Desired_set_point_voltage',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN10',
    DMND_MAX_APV = '32 * BIN10'
    )
DTI.Short('DTI_Dpf_dp',
    var = 'IN_Dpf_dp',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '500 * BIN6'
    )
DTI.Short('DTI_Dpf_in_temp',
    var = 'IN_Dpf_in_temp',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-50 * BIN2',
    DMND_MAX_APV = '1000 * BIN2'
    )
DTI.Short('DTI_Driver_brake_torque',
    var = 'T_D_Driver_brake_torque_pct',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = 'T_D_BRAKE_TORQ_MIN_CPV',
    DMND_MAX_APV = 'T_D_BRAKE_TORQ_MAX_CPV'
    )
DTI.Short('DTI_Egr_rate',
    var = 'ACM_Egr_rate_dsrd_unlimited',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN16',
    DMND_MAX_APV = '0.9999847412109375 * BIN16'
    )
DTI.Short('DTI_Egrh_drive',
    var = 'ACM_Egrh_valve_drive_duty_cycle',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Egrh_position',
    var = 'ACM_Egrh_position_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Egrl_fract',
    var = 'ACM_Egrl_fract_desired',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN15',
    DMND_MAX_APV = '1 * BIN15'
    )
DTI.Short('DTI_Egrl_position',
    var = 'DTI_Dummy_egrl_position_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Engine_speed_dutyc',
    var = 'ICI_Engine_speed_out_dutyc',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Engine_speed_freq',
    var = 'ICI_Engine_speed_out_freq',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '1000 * BIN0'
    )
DTI.Short('DTI_Exh_brk_pres',
    var = 'ACM_Exh_brk_valve_duty_cycle',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '500 * BIN6'
    )  
DTI.Short('DTI_Ext_air_temp',
    var = 'IN_Ext_air_temp',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-50 * BIN2',
    DMND_MAX_APV = '200 * BIN2'
    )
DTI.Short('DTI_Fan1_raw_output',
    var = 'ETC_Fan1_raw_output',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Gear_ratio',
    var = 'IN_Gear_ratio_raw',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = 'APP_NUMBER_OF_GEAR_RATIO_CPV - 1'
    )
DTI.Short('DTI_Glow_plug',
    var = 'DTI_Dummy_glow_plug_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )

DTI.Control('DTI_Hand_ped_sel_sw_mem_rst',
            var = 'BOOL_TYPE',
            dmnd_type= 'BOOL_TYPE',
            subm_type = 'BOOL_TYPE',
            dmnd = 'DTI_Hand_ped_sel_sw_mem_rst_dmnd',
            subm = 'DTI_Hand_ped_sel_sw_mem_rst_subm',
            DEFAULT_APV = '0'
            )

DTI.Short('DTI_Hp_pwm_frequency',
    var = 'DTI_Dummy_hp_pwm_frequency_dmnd',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '31 * BIN4',
    DMND_MAX_APV = '2500 * BIN4'
    )
DTI.Short('DTI_Hp_crt',
    var = 'DTI_Dummy_hp_crt_dmnd',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN4',
    DMND_MAX_APV = '2500 * BIN4'
    )
DTI.Short('DTI_Hp_crt_igain',
    var = 'RPC_Hp_crt_igain',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN3',
    DMND_MAX_APV = '4000 * BIN3'
    )
DTI.Short('DTI_Hp_crt_pgain',
    var = 'RPC_Hp_crt_pgain',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN3',
    DMND_MAX_APV = '4000 * BIN3'
    )
DTI.Short('DTI_Hp_crt_dgain',
    var = 'RPC_Hp_crt_dgain',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN3',
    DMND_MAX_APV = '4000 * BIN3'
    )
DTI.Short('DTI_Ic_after_fuel',
    var = 'I_C_Selected_after_fuel_qty',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Ic_after_hyd_us_sep',
    var = 'I_C_Selected_after_hyd_us_sep',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '50000 * BIN0'
    )
DTI.Short('DTI_Ic_after_hyd_deg_sep',
    var = 'DTI_Dummy_hyd_deg_sep_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_after_hyd_timing',
    var = 'DTI_Dummy_hyd_timing',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-180 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_main_fuel',
    var = 'I_C_Selected_main_fuel_qty',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Ic_main_hyd_timing',
    var = 'DTI_Dummy_hyd_timing',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-180 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_pilot0_fuel',
    var = 'I_C_Selected_pilot0_fuel_qty',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Ic_pilot0_hyd_deg_sep',
    var = 'DTI_Dummy_hyd_deg_sep_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_pilot0_hyd_us_sep',
    var = 'I_C_Selected_pilot0_hyd_us_sep',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '50000 * BIN0'
    )
DTI.Short('DTI_Ic_pilot0_hyd_timing',
    var = 'DTI_Dummy_hyd_timing',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-180 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_pilot1_fuel',
    var = 'I_C_Selected_pilot1_fuel_qty',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Ic_pilot1_hyd_deg_sep',
    var = 'DTI_Dummy_hyd_deg_sep_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_pilot1_hyd_us_sep',
    var = 'I_C_Selected_pilot1_hyd_us_sep',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '50000 * BIN0'
    )
DTI.Short('DTI_Ic_pilot1_hyd_timing',
    var = 'DTI_Dummy_hyd_timing',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-180 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_pilot2_fuel',
    var = 'I_C_Selected_pilot2_fuel_qty',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Ic_pilot2_hyd_deg_sep',
    var = 'DTI_Dummy_hyd_deg_sep_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_pilot2_hyd_timing',
    var = 'DTI_Dummy_hyd_timing',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-180 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_pilot2_hyd_us_sep',
    var = 'I_C_Selected_pilot2_hyd_us_sep',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '50000 * BIN0'
    )
DTI.Short('DTI_Ic_post1_fuel',
    var = 'I_C_Selected_post1_fuel_qty',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Ic_post1_hyd_deg_sep',
    var = 'DTI_Dummy_hyd_deg_sep_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_post1_hyd_timing',
    var = 'DTI_Dummy_hyd_timing',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-180 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_post1_hyd_us_sep',
    var = 'ITD_Chkd_post1_hyd_us_sep',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '50000 * BIN0'
    )
DTI.Short('DTI_Ic_post2_fuel',
    var = 'I_C_Selected_post2_fuel_qty',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Ic_post2_hyd_deg_sep',
    var = 'DTI_Dummy_hyd_deg_sep_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_post2_hyd_timing',
    var = 'DTI_Dummy_hyd_timing',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-180 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_post2_hyd_us_sep',
    var = 'I_C_Selected_post2_hyd_us_sep',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '50000 * BIN0'
    )
DTI.Short('DTI_Ic_post3_fuel',
    var = 'I_C_Selected_post3_fuel_qty',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Ic_post3_hyd_deg_sep',
    var = 'DTI_Dummy_hyd_deg_sep_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_post3_hyd_timing',
    var = 'DTI_Dummy_hyd_timing',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-180 * BIN6',
    DMND_MAX_APV = '180 * BIN6'
    )
DTI.Short('DTI_Ic_post3_hyd_us_sep',
    var = 'I_C_Selected_post3_hyd_us_sep',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '50000 * BIN0'
    )
DTI.Short('DTI_Ic_pre_fuel',
    var = 'I_C_Selected_pre_fuel_qty',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Ic_pre_hyd_us_sep',
    var = 'I_C_Selected_pre_hyd_us_sep',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '50000 * BIN0'
    )
DTI.Short('DTI_Idle_speed',
    var = 'T_D_Idle_target_startup_offset',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN2',
    DMND_MAX_APV = '8000 * BIN2'
    )
DTI.Short('DTI_Im_crt',
    var = 'RPC_Im_crt_dmnd_raw',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN4',
    DMND_MAX_APV = '2.5 * BIN4'
    )
DTI.Short('DTI_Im_crt_trim_dgain',
    var = 'RPC_Im_crt_trim_dgain',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-4000 * BIN3',
    DMND_MAX_APV = '4000 * BIN3'
    )
DTI.Short('DTI_Im_crt_trim_igain',
    var = 'RPC_Im_crt_trim_igain',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-4000 * BIN3',
    DMND_MAX_APV = '4000 * BIN3'
    )
DTI.Short('DTI_Im_crt_trim_pgain',
    var = 'RPC_Im_crt_trim_pgain',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-4000 * BIN3',
    DMND_MAX_APV = '4000 * BIN3'
    )
DTI.Short('DTI_Im_crt_trim_qgain',
    var = 'RPC_Im_crt_trim_qgain',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-250 * BIN7',
    DMND_MAX_APV = '250 * BIN7'
    )
DTI.Short('DTI_Im_pwm_frequency',
    var = 'DTI_Dummy_Im_pwm_frequency_dmnd',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '31 * BIN4',
    DMND_MAX_APV = '2500 * BIN4'
    )
DTI.Short('DTI_Inj_1_bal_trim',
    var = 'I_C_External_cbc_trim_val',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-500 * BIN0',
    DMND_MAX_APV = '500 * BIN0'
    )
DTI.Short('DTI_Inj_2_bal_trim',
    var = 'I_C_External_cbc_trim_val',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-500 * BIN0',
    DMND_MAX_APV = '500 * BIN0'
    )
DTI.Short('DTI_Inj_3_bal_trim',
    var = 'I_C_External_cbc_trim_val',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-500 * BIN0',
    DMND_MAX_APV = '500 * BIN0'
    )
DTI.Short('DTI_Inj_4_bal_trim',
    var = 'I_C_External_cbc_trim_val',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-500 * BIN0',
    DMND_MAX_APV = '500 * BIN0'
    )
DTI.Short('DTI_Inlet_air_temp',
    var = 'IN_Inlet_air_temperature',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-50 * BIN2',
    DMND_MAX_APV = '150 * BIN2'
    )
DTI.Short('DTI_Ip_temp',
    var = 'IN_Intake_plenum_temp',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-50 * BIN2',
    DMND_MAX_APV = '1000 * BIN2'
    )
DTI.Short('DTI_Main_timing',
    var = 'ITD_Main_timing_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-180 * BIN7',
    DMND_MAX_APV = '180 * BIN7'
    )
DTI.Short('DTI_Map',
    var = 'IN_Manifold_abs_pressure',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '500 * BIN6'
    )
DTI.Short('DTI_Mdp_inj_to_update',
    var = 'DTI_Dummy_mdp_inj_to_upd_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = 'APP_NUMBER_OF_INJECTORS_CPV - 1'
    )
DTI.Short('DTI_Mdp_injector_num',
    var = 'DTI_Dummy_mdp_inj_to_upd_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = 'APP_NUMBER_OF_INJECTORS_CPV - 1'
    )
DTI.Short('DTI_Mdp_period',
    var = 'I_C_Spc_elapsed_time_nvv',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * DEC0',
    DMND_MAX_APV = '55000 * DEC0'
    )
DTI.Short('DTI_Mdp_pilot_trim',
    var = 'DTI_Dummy_mdp_pilot_trim_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '-500 * BIN0',
    DMND_MAX_APV = '500 * BIN0'
    )
DTI.Short('DTI_Mdp_rail_pressure',
    var = 'DTI_Dummy_mdp_rail_press_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '5000 * BIN0'
    )
DTI.Short('DTI_P3',
    var = 'IN_P3_exhaust_pressure',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '500 * BIN6'
    )
DTI.Short('DTI_Pilot1_deg_sep',
    var = 'ITD_Pilot1_sep_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-90 * BIN6',
    DMND_MAX_APV = '90 * BIN6'
    )
DTI.Short('DTI_Pilot1_fuel',
    var = 'FQD_Pilot1_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Pilot2_deg_sep',
    var = 'ITD_Pilot2_sep_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-90 * BIN6',
    DMND_MAX_APV = '90 * BIN6'
    )
DTI.Short('DTI_Pilot2_fuel',
    var = 'FQD_Pilot2_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Pls_after_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Pls_main_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Pls_pilot0_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Pls_pilot1_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Pls_pilot2_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Pls_post1_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Pls_post2_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Pls_post3_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Pls_post4_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Pls_post5_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Pls_pre_ton',
    var = 'DTI_Dummy_pls_ton_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-15000 * DEC0',
    DMND_MAX_APV = '15000 * DEC0'
    )
DTI.Short('DTI_Post1_fuel',
    var = 'FQD_Post1_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Post1_timing',
    var = 'ITD_Post1_timing_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-360 * BIN6',
    DMND_MAX_APV = '360 * BIN6'
    )
DTI.Short('DTI_Post2_fuel',
    var = 'FQD_Post2_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Post2_timing',
    var = 'ITD_Post2_timing_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-360 * BIN6',
    DMND_MAX_APV = '360 * BIN6'
    )
DTI.Short('DTI_Pressure',
    var = 'DTI_Dummy_pressure_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '2500 * BIN0'
    )
DTI.Short('DTI_Spc_inj_nb',
    var = 'I_C_Spc0_inj_to_upd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = 'APP_NUMBER_OF_INJECTORS_CPV - 1'
    )
DTI.Short('DTI_Spc_ol_dec_step',
    var = 'I_C_Spc_ol_mdp_trim_step',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN4',
    DMND_MAX_APV = '100 * BIN4'
    )
DTI.Short('DTI_Spc_ol_inc_step',
    var = 'I_C_Spc_ol_mdp_trim_step',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN4',
    DMND_MAX_APV = '100 * BIN4'
    )
DTI.Short('DTI_Spc_rail_p_index',
    var = 'I_C_Spc0_railp_index',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '5 * BIN0'
    )
DTI.Short('DTI_Spcs_inj_nb',
    var = 'I_C_Spcs_inj_to_upd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = 'APP_NUMBER_OF_INJECTORS_CPV - 1'
    )
DTI.Short('DTI_Spcs_rail_p_index',
    var = 'I_C_Spcs_railp_index',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '5 * BIN0'
    )
DTI.Short('DTI_Thrtl_drive',
    var= 'DTI_Dummy_thrtl_drive_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-100 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
     
DTI.Short('DTI_Throt_duty_cycle',
    var = 'ACM_Throt_duty_cycle',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Throt_position',
    var = 'ACM_Throt_desired_position',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Turb_in_temp',
    var = 'IN_Turbine_in_temp',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-50 * BIN2',
    DMND_MAX_APV = '1000 * BIN2'
    )
DTI.Short('DTI_Vdg_prp_gain',
    var = 'T_D_Vdg_prop_gain_signal',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN10',
    DMND_MAX_APV = '10* BIN10'
    )

DTI.Short('DTI_Vdg_deriv_gain',
    var = 'T_D_Vdg_deriv_gain_signal',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN10',
    DMND_MAX_APV = '10* BIN10'
    )

DTI.Short('DTI_Vdg_int_gain',
    var = 'T_D_Vdg_int_gain_signal',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN10',
    DMND_MAX_APV = '10* BIN10'
    )

DTI.Short('DTI_Vdg_rpm',
    var = 'T_D_Vdg_rpm_pedal_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN2',
    DMND_MAX_APV = '8000 * BIN2'
    )

DTI.Short('DTI_Veh_spd_dutyc',
    var = 'P_L_Veh_spd_out_dutyc',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN4',
    DMND_MAX_APV = '100 * BIN4'
    )
DTI.Short('DTI_Veh_spd_freq',
    var = 'P_L_Veh_spd_out_freq',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '1 * BIN4',
    DMND_MAX_APV = '1000 * BIN4'
    )      

DTI.Short('DTI_Vehicle_acceleration',
    var = 'IN_Vehicle_acceleration',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-8 * BIN12',
    DMND_MAX_APV = '7.9998 * BIN12'
    )
DTI.Short('DTI_Vehicle_speed',
    var = 'IN_Vehicle_speed',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '500 * BIN7'
    )
DTI.Short('DTI_Vgt_boost_pressure',
    var = 'ACM_Vgt_boost_pressure_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN6',
    DMND_MAX_APV = '500 * BIN6'
    )

DTI.Short('DTI_Vgt_max_eng_pr',
    var = 'ACM_Vgt_mx_eng_pr_rm_out_nxt',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN12',
    DMND_MAX_APV = '8 * BIN12'
    )
	
DTI.Short('DTI_Vgth_position',
    var = 'ACM_Vgth_position_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Vgth_pwm',
    var = 'ACM_Vgth_pos_ctrl_duty_cycle',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Vgth_valve',
    var = 'P_L_Vgth_valve_drive_duty_cycle',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Vgtl_position',
    var = 'ACM_Vgtl_position_dmnd_ol',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Vgtl_pwm',
    var = 'ACM_Vgtl_pos_ctrl_duty_cycle',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Wraf_dfco_delay',
    var = 'P_L_Wraf_dfco_delay',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * DEC3',
    DMND_MAX_APV = '60 * DEC3'
    )
DTI.Short('DTI_Wraf_ipk_hi',
    var = 'P_L_Wraf_diag_ipk_dfco_hi',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-10 * BIN10',
    DMND_MAX_APV = '10 * BIN10'
    )
DTI.Short('DTI_Wraf_ipk_lo',
    var = 'P_L_Wraf_diag_ipk_dfco_lo',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-10 * BIN10',
    DMND_MAX_APV = '10 * BIN10'
    )
DTI.Short('DTI_Wraf_ipk_time',
    var = 'P_L_Wraf_diag_lbd_dfco_time',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * DEC2',
    DMND_MAX_APV = '655 * DEC2'
    )
DTI.Short('DTI_Wraf_min_fuel',
    var = 'DTI_Dummy_wraf_min_fuel_dmnd',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '65535 * BIN0'
    )
DTI.Short('DTI_Wraf_min_time',
    var = 'P_L_Wraf_min_time_threshold',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * DEC0',
    DMND_MAX_APV = '65535 * DEC0'
    )
DTI.Short('DTI_Wraf_plau_lbd',
    var = 'P_L_Wraf_diag_lbd_plau_lbd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN11',
    DMND_MAX_APV = '10 * BIN11'
    )
DTI.Short('DTI_Wraf_plau_q',
    var = 'P_L_Wraf_diag_lbd_plau_inj_q',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '255 * BIN7'
    )
DTI.Short('DTI_Idle_target_ext',
    var = 'T_D_Idle_target_minimum_ext',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.Short('DTI_Intercooler_out_temp',
    var = 'IN_Intercooler_out_temp',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '-50 * BIN2',
    DMND_MAX_APV = '1000 * BIN2'
    )	
DTI.Short('DTI_Oil_pressure',
    var = 'DTI_Dummy_Oil_pressure',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN4',
    DMND_MAX_APV = '1000 * BIN4'
    )
DTI.Short('DTI_Oil_press_gauge_dutyc',
    var = 'DTI_Dummy_oil_press_gauge_dutyc',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7'
    )
DTI.Short('DTI_Oil_press_gauge_freq',
    var = 'DTI_Dummy_oil_press_gauge_freq',
	dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN0',
    DMND_MAX_APV = '1000 * BIN0'
    )
DTI.Short('DTI_Pedal_foot_position',
    var = 'ICV_Pedal_foot_position',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7')

DTI.Short('DTI_Pedal_hand_position',
    var = 'ICV_Pedal_hand_position',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7')

DTI.Short('DTI_Pedal_position',
    var = 'IN_Pedal_position',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7')


DTI.Short('DTI_Can_maf_abs_pres',
	var = 'IN_Can_maf_abs_pres',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE')

DTI.Short('DTI_Can_maf_gas_temp',
	var = 'IN_Can_maf_gas_temp',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE')

DTI.Short('DTI_Exh_brk_pwm',
    var = 'DTI_Dummy_exh_brk_pwm_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE',
    DMND_MIN_APV = '0 * BIN7',
    DMND_MAX_APV = '100 * BIN7')
		
DTI.Short('DTI_Amf_can',
	var = 'IN_Amf_can',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE')

DTI.Short('DTI_Lift_pump_pwm',
    var = 'DTI_Dummy_lift_pump_pwm_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE')

DTI.Control('DTI_Ac_compressor',
            var = 'BOOL_TYPE',
            subm_type = 'BOOL_TYPE',
            DEFAULT_APV = 'FALSE')

DTI.Control('DTI_Ac_eng_cool_req',
            var = 'BOOL_TYPE',
            subm_type = 'BOOL_TYPE',
            DEFAULT_APV = 'FALSE')
			
			
DTI.Control('DTI_Ac_emerg_shut_off',
              var = 'BOOL_TYPE',
              subm_type = 'BOOL_TYPE',
              dmnd = 'DTI_Ac_emerg_shut_off_dmnd',
              subm = 'DTI_Ac_emerg_shut_off_subm',
              DEFAULT_APV = 'FALSE')

DTI.Control('DTI_Actuator_relay',
    var = 'SMC_Energise_actuator_relay',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Atc_lamp',
    var = 'P_L_Atc_lamp_drive',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Batt_warn_lamp',
    var = 'DTI_Dummy_iso_batt_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Brk_light_sw_mem_rst',
    var = 'P_L_Brk_light_switch_stored',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Brk_safety_sw_mem_rst',
    var = 'P_L_Brk_safety_switch_stored',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Calib_pilot_control',
    var = 'DTI_Dummy_calib_pilot_dmnd',
    dmnd_type = 'DTI_CALIB_PILOT_CONTROL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Charge_mode',
    var = 'DTI_Dummy_asm_charge_mode_dmnd',
    dmnd_type = 'DTI_BP_CHARGE_MODE_DMND_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Clutch_bott_sw_rst',
    var = 'P_L_Clutch_switch_bottom_stored',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Clutch_switch',
    var = 'IN_Clutch_switch',
    dmnd_type = 'DTI_CLUTCH_SWITCH_DMND_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Clutch_top_sw_rst',
    var = 'P_L_Clutch_switch_top_stored',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Cruise_control_lamp',
    var = 'DTI_Dummy_cruise_cntrl_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )

DTI.Control('DTI_Cu_relay',
    var = 'SMC_Energise_cu_relay',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Dis_pilot_post_0',
    var = 'DTI_Dummy_dis_pilot_post_0_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Dis_pilot_post_1',
    var = 'DTI_Dummy_dis_pilot_post_0_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Dis_pilot_post_2',
    var = 'DTI_Dummy_dis_pilot_post_0_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Dis_pilot_post_3',
    var = 'DTI_Dummy_dis_pilot_post_0_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Disable_acc_strat',
    var = 'DTI_Dummy_dis_acc_strat_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Dpf_regen',
    var = 'BOOL_TYPE',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Dpf_reg_lamp_active',
    var = 'DTI_Dummy_dpf_reg_lamp_act_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Dpf_regen_inh_lamp',
    var = 'DTI_Dummy_dpf_rgn_inh_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Dpf_warn_lamp',
    var = 'DTI_Dummy_dpf_warn_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ebrake_lamp',
    var = 'DTI_Dummy_ebrake_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Egrh_cooler_bypass',
    var = 'ACM_Egrh_cooler_byp_enable',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Egrl_dp_learn',
    var = 'BOOL_TYPE',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Eng_spd_rly',
    var = 'P_L_Eng_spd_rly_request',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Engine_stop_req',
    var = 'DTI_Dummy_engine_stop_req_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Esm_ecu_error_rst',
    var = 'DTI_Dummy_esm_ecu_err_rst_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Fan2_raw_output',
    var = 'ETC_Fan2_output',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Fault_1',
    var = 'DTI_Dummy_fault_dmnd',
    dmnd_type = 'DTI_FAULT_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Fault_2',
    var = 'DTI_Dummy_fault_dmnd',
    dmnd_type = 'DTI_FAULT_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Fault_3',
    var = 'DTI_Dummy_fault_dmnd',
    dmnd_type = 'DTI_FAULT_TYPE',
    subm_type = 'BOOL_TYPE'
    ) 
DTI.Control('DTI_Fault_mode06',
    var = 'DTI_Dummy_fault_mode06_dmnd',
    dmnd_type = 'DTI_FAULT_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Fuel_htr_lamp',
    var = 'DTI_Dummy_fuel_htr_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )    
DTI.Control('DTI_Ic_after_method',
    var = 'DTI_Dummy_ic_method_dmnd',
    dmnd_type = 'DTI_I_C_TIMING_METHOD_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ic_pilot0_method',
    var = 'DTI_Dummy_ic_method_dmnd',
    dmnd_type = 'DTI_I_C_TIMING_METHOD_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ic_pilot1_method',
    var = 'DTI_Dummy_ic_method_dmnd',
    dmnd_type = 'DTI_I_C_TIMING_METHOD_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ic_pilot2_method',
    var = 'DTI_Dummy_ic_method_dmnd',
    dmnd_type = 'DTI_I_C_TIMING_METHOD_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ic_post1_method',
    var = 'DTI_Dummy_ic_method_dmnd',
    dmnd_type = 'DTI_I_C_TIMING_METHOD_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ic_post2_method',
    var = 'DTI_Dummy_ic_method_dmnd',
    dmnd_type = 'DTI_I_C_TIMING_METHOD_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ic_post3_method',
    var = 'DTI_Dummy_ic_method_dmnd',
    dmnd_type = 'DTI_I_C_TIMING_METHOD_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ici_cruise_lamp',
    var = 'P_L_Cruise_lamp_output',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ici_dpf_lamp',
    var = 'DTI_Dummy_iso_ici_dpf_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ici_etc_lamp',
    var = 'F_M_Etc_lamp_output',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ici_gp_lamp',
    var = 'ICI_Glow_plug_lamp_state',
    dmnd_type = 'DTI_ICI_GP_LAMP_TYPE',
    subm_type = 'BOOL_TYPE',
    )
DTI.Control('DTI_Ici_mi_lamp',
    var = 'ICI_Mi_lamp_output',
    dmnd_type = 'DTI_ICI_MI_LAMP_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ici_oil_pres_lamp',
    var = 'DTI_Dummy_ici_oil_pres_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ici_sas_inhib_lamp',
    var = 'DTI_Dummy_iso_icisasinhlmp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ici_wif_lamp',
    var = 'ICI_Water_in_fuel_lamp_output',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ignition_sw_mem_rst',
    var = 'DTI_Dummy_ign_sw_mem_rst_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Im_use_low_freq',
    var = 'RPC_Im_use_low_freq',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Inj_1_shut_off',
    var = 'DTI_Dummy_Inj_shut_off_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Inj_2_shut_off',
    var = 'DTI_Dummy_Inj_shut_off_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Inj_3_shut_off',
    var = 'DTI_Dummy_Inj_shut_off_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Inj_4_shut_off',
    var = 'DTI_Dummy_Inj_shut_off_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Inj_bal_disable',
    var = 'DTI_Dummy_Inj_bal_disable_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Inj_bal_flt_disable',
    var = 'DTI_Dummy_Inj_bal_flt_dis_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_J1939_oil_lvl_trigger',
            var = 'BOOL_TYPE',
            dmnd_type= 'BOOL_TYPE',
            subm_type = 'BOOL_TYPE',
            dmnd = 'DTI_J1939_oil_lvl_trigger_dmnd',
            subm = 'DTI_J1939_oil_lvl_trigger_subm',
            DEFAULT_APV = '0')
DTI.Control('DTI_Lift_pump',
    var = 'RPC_Lp_pump_powered',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_map_upd_mode_0',
    var = 'DTI_Dummmy_mdp_mapupd_mode_dmnd',
    dmnd_type = 'DTI_MDP_MAP_UPD_MODE_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_map_upd_mode_1',
    var = 'DTI_Dummmy_mdp_mapupd_mode_dmnd',
    dmnd_type = 'DTI_MDP_MAP_UPD_MODE_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_map_upd_mode_2',
    var = 'DTI_Dummmy_mdp_mapupd_mode_dmnd',
    dmnd_type = 'DTI_MDP_MAP_UPD_MODE_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_map_upd_mode_3',
    var = 'DTI_Dummmy_mdp_mapupd_mode_dmnd',
    dmnd_type = 'DTI_MDP_MAP_UPD_MODE_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_map_upd_mode_4',
    var = 'DTI_Dummmy_mdp_mapupd_mode_dmnd',
    dmnd_type = 'DTI_MDP_MAP_UPD_MODE_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_map_upd_mode_5',
    var = 'DTI_Dummmy_mdp_mapupd_mode_dmnd',
    dmnd_type = 'DTI_MDP_MAP_UPD_MODE_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_map_update',
    var = 'DTI_Dummy_mdp_map_update_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_nvm_reset',
    var = 'DTI_Dummy_mdp_nvm_reset_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Performance_mode',
    var = 'DTI_Dummy_asm_perf_mode_dmnd',
    dmnd_type = 'DTI_BP_PERFORMANCE_MODE_DMND_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_pilot_control',
    var = 'DTI_Dummy_mdp_pilot_ctrl_dmnd',
    dmnd_type = 'DTI_MDP_OPEN_LOOP_ACTIVE_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_upd_zone_sel_0',
    var = 'DTI_Dummy_mdp_upd_zone_sel_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Oil_pres_sw_mem_rst',
    var = 'BOOL_TYPE',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE',
    DEFAULT_APV = 'FALSE'
    )
DTI.Control('DTI_Mdp_upd_zone_sel_1',
    var = 'DTI_Dummy_mdp_upd_zone_sel_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_upd_zone_sel_2',
    var = 'DTI_Dummy_mdp_upd_zone_sel_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Mdp_upd_zone_sel_3',
    var = 'DTI_Dummy_mdp_upd_zone_sel_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Pls_iso_1',
    var = 'DTI_Dummy_pls_iso_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Pls_iso_2',
    var = 'DTI_Dummy_pls_iso_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Pls_iso_3',
    var = 'DTI_Dummy_pls_iso_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Pls_iso_4',
    var = 'DTI_Dummy_pls_iso_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Pto_cruise_lamp_dc',
    var = 'DTI_Dummy_pto_cruise_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Rail_control_state',
    var = 'DTI_Dummy_rail_ctrl_state_dmnd',
    dmnd_type = 'DTI_RAIL_CONTROL_STATE_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Rvd_perform',
    var = 'RPC_Perform_rvd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Spc_stop',
    var = 'DTI_Dummy_spc_stop_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Spcs_mode_required',
    var = 'I_C_Spcs_mode_required',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Starter_relay',
    var = 'SMC_Starter_activation_request',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Starter_rly_output',
    var = 'P_L_Starter_relay_output',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Vgth_comp_bypass',
    var = 'DTI_Dummy_vgth_comp_bypass_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.Control('DTI_Vgth_learn_req',
    var = 'DTI_Dummy_vgt_learn_req_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Vgtl_learn_req',
    var = 'DTI_Dummy_vgt_learn_req_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Water_in_fuel_mem_rst',
    var = 'P_L_Water_in_fuel_stored',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Wraf_htr_mode',
    var = 'DTI_Dummy_htr_mode',
    dmnd_type = 'DTI_WRAF_HTR_MODE_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_C_c_wh',
    var = 'DTI_Dummy_wh_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_C_c_ptc',
    var = 'DTI_Dummy_ptc_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Lnt_desox_request',
    var = 'DTI_Dummy_lnt_desox_request_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Ici_oil_level_lamp',
    var = 'BOOL_TYPE',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Fuel_htr',
    var = 'DTI_Dummy_fuel_htr_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )

DTI.Control('DTI_Thrtl_atsk',
    var = 'ACM_Thrtl_atsk_enable',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Thrtl_cln',
    var = 'ACM_Thrtl_cln_reset',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Thrtl_lrn',
    var = 'ACM_Thrtl_lrn_1st_proc_enable',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.Control('DTI_Thrtl_pwo',
    var = 'ACM_Thrtl_pwo_test_enable',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )

DTI.IsoShort('DTI_Iso_hp_crt_pgain')
DTI.IsoShort('DTI_Iso_hp_crt_igain')
DTI.IsoShort('DTI_Iso_hp_crt_dgain')
DTI.IsoShort('DTI_Iso_im_crt_trim_pgain')
DTI.IsoShort('DTI_Iso_im_crt_trim_igain')
DTI.IsoShort('DTI_Iso_im_crt_trim_dgain')

DTI.IsoShort('DTI_Iso_driver_brake_torque',
    var = 'T_D_Actual_brake_torque',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_fan1_raw_output',
    var = 'DTI_Dummy_iso_fan1_raw_op_dmnd',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_hp_crt',
    var = 'DTI_ISO_HYD_ST_HP_CLS_CT_APV',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoShort('DTI_Iso_ic_after_fuel',
    var = 'DTI_Dummy_iso_ic_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoShort('DTI_Iso_ic_post1_fuel',
    var = 'DTI_Dummy_iso_ic_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoShort('DTI_Iso_ic_post2_fuel',
    var = 'DTI_Dummy_iso_ic_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoShort('DTI_Iso_ic_post3_fuel',
    var = 'DTI_Dummy_iso_ic_fuel_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoShort('DTI_Iso_idle_speed',
    var = 'T_D_Idle_target_startup_offset',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_idle_target_ext',
    var = 'T_D_Idle_target_minimum_ext',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_im_crt',
    var = 'DTI_ISO_HYD_ST_IM_CLS_CT_APV',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_im_pwm_frequency',
    var = 'DTI_Dummy_Im_pwm_frequency_dmnd',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_mdp_period',
    var = 'I_C_Spc_elapsed_time_nvv',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoShort('DTI_Iso_indicated_torque',
    var = 'T_D_Mapped_indicated_torque',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoShort('DTI_Iso_pedal_position',
    var = 'IN_Pedal_position',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_pressure',
    var = 'DTI_Dummy_pressure_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )

DTI.IsoShort('DTI_Iso_inj_1_bal_trim',
    var = 'I_C_External_cbc_trim_val',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_inj_2_bal_trim',
    var = 'I_C_External_cbc_trim_val',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_inj_3_bal_trim',
    var = 'I_C_External_cbc_trim_val',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_inj_4_bal_trim',
    var = 'I_C_External_cbc_trim_val',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_egrl_position',
    var = 'DTI_Dummy_egrl_position_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_egrh_position',
    var = 'ACM_Egrh_position_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_ic_main_fuel',
    var = 'I_C_Selected_main_fuel_qty',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_alt_duty_cycle',
    var = 'P_L_Alt_duty_cycle_output',
    dmnd_type = 'U16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_glow_plug',
    var = 'DTI_Dummy_glow_plug_dmnd',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoShort('DTI_Iso_vgth_valve',
    var = 'P_L_Vgth_valve_drive_duty_cycle',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_engine_speed_dutyc',
    var = 'ICI_Engine_speed_out_dutyc',
    dmnd_type = 'S16',
    subm_type = 'BOOL_TYPE',
    )
DTI.IsoShort('DTI_Iso_engine_speed_freq',
    var = 'ICI_Engine_speed_out_freq',
    dmnd_type = 'U16',
    subm_type = 'BOOL_TYPE',
    )
DTI.IsoShort('DTI_Iso_exh_brk_pwm',
    var = 'DTI_Dummy_exh_brk_pwm_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoShort('DTI_Iso_lift_pump_pwm',
    var = 'DTI_Dummy_lift_pump_pwm_dmnd',
    dmnd_type = 'S16',
    subm_type = 'DTI_SUBM_TYPE'
    )

DTI.IsoControl('DTI_Iso_ac_compressor',
    var = 'DTI_Dummy_iso_ac_comp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_atc_lamp',
    var = 'DTI_Dummy_iso_atc_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_batt_warn_lamp',
    var = 'DTI_Dummy_iso_batt_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_cruise_control_lamp',
    var = 'DTI_Dummy_cruise_cntrl_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_disable_acc_strat',
    var = 'DTI_Dummy_iso_dis_accstrat_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_dpf_learn_coef',
    var = 'DTI_Dummy_iso_dpf_lrn_coef_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_dpf_reg_lamp_active',
    var = 'DTI_Dummy_dpf_reg_lamp_act_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_dpf_regen',
    var = 'DTI_Dummy_iso_dpf_regen_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_dpf_regen_inh_lamp',
    var = 'DTI_Dummy_dpf_rgn_inh_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_dpf_warn_lamp',
    var = 'DTI_Dummy_dpf_warn_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_ebrake_lamp',
    var = 'DTI_Dummy_ebrake_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_engine_stop_req',
    var = 'DTI_Dummy_iso_eng_stp_req_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_eng_spd_rly',
    var = 'DTI_Dummy_eng_spd_rly_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE',
    )
DTI.IsoControl('DTI_Iso_fuel_htr',
    var = 'DTI_Dummy_iso_fuel_htr_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_fan2_raw_output',
    var = 'ETC_Fan2_output',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_fuel_htr_lamp',
    var = 'DTI_Dummy_fuel_htr_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_gp_lamp',
    var = 'DTI_Dummy_iso_gp_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_ici_dpf_lamp',
    var = 'DTI_Dummy_iso_ici_dpf_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_ici_etc_lamp',
    var = 'DTI_Dummy_iso_ici_etc_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_ici_gp_lamp',
    var = 'DTI_Dummy_iso_gp_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_ici_mi_lamp',
    var = 'DTI_Dummy_ici_mi_lamp_dmnd',
    dmnd_type = 'DTI_ICI_MI_LAMP_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_ici_oil_pres_lamp',
    var = 'DTI_Dummy_ici_oil_pres_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_ici_sas_inhib_lamp',
    var = 'DTI_Dummy_iso_icisasinhlmp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )

DTI.IsoControl('DTI_Iso_ici_wif_lamp',
    var = 'ICI_Water_in_fuel_lamp_output',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_inj_1_shut_off',
    var = 'DTI_Dummy_iso_inj_shutoff_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_inj_2_shut_off',
    var = 'DTI_Dummy_iso_inj_shutoff_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_inj_3_shut_off',
    var = 'DTI_Dummy_iso_inj_shutoff_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_inj_4_shut_off',
    var = 'DTI_Dummy_iso_inj_shutoff_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_lift_pump',
    var = 'DTI_Dummy_iso_lift_pump_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_mdp_nvm_reset',
    var = 'DTI_Dummy_iso_mdp_nvm_rst_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_pls_iso_1',
    var = 'DTI_Dummy_iso_pls_iso_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoControl('DTI_Iso_pls_iso_2',
    var = 'DTI_Dummy_iso_pls_iso_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoControl('DTI_Iso_pls_iso_3',
    var = 'DTI_Dummy_iso_pls_iso_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoControl('DTI_Iso_pls_iso_4',
    var = 'DTI_Dummy_iso_pls_iso_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'DTI_SUBM_TYPE'
    )
DTI.IsoControl('DTI_Iso_pto_cruise_lamp_dc',
    var = 'DTI_Dummy_pto_cruise_lamp_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_rail_control_state',
    var = 'DTI_Dummy_iso_railctl_st_dmnd',
    dmnd_type = 'DTI_RAIL_CONTROL_STATE_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_rvd_perform',
    var = 'DTI_Dummy_iso_rvd_perform_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_spc_stop',
    var = 'DTI_Dummy_iso_spc_stop_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )
DTI.IsoControl('DTI_Iso_starter_relay',
    var = 'DTI_Dummy_iso_start_relay_dmnd',
    dmnd_type = 'BOOL_TYPE',
    subm_type = 'BOOL_TYPE'
    )

DTI.Control('DTI_Ici_lop_lamp',
            var = 'ICI_Lop_lamp_output',            
            subm_type = 'BOOL_TYPE',
            dmnd_type = 'BOOL_TYPE')            
DTI.IsoControl('DTI_Iso_ici_lop_lamp',
            var = 'ICI_Lop_lamp_output',            
            dmnd_type = 'BOOL_TYPE',
            subm_type = 'BOOL_TYPE')            

DTI.Control('DTI_Ici_ce_lamp',
            var = 'ICI_Ce_lamp_dmnd',            
            subm_type = 'BOOL_TYPE',
            dmnd_type = 'BOOL_TYPE')            
DTI.IsoControl('DTI_Iso_ici_ce_lamp',
            var = 'ICI_Ce_lamp_dmnd',            
            dmnd_type = 'BOOL_TYPE',
            subm_type = 'BOOL_TYPE')            

DTI.Control('DTI_Ici_driv_mi_lamp',
            var = 'ICI_Mi_lamp_output',            
            subm_type = 'BOOL_TYPE',
            dmnd_type = 'BOOL_TYPE')            
DTI.IsoControl('DTI_Iso_ici_driv_mi_lamp',
            var = 'ICI_Mi_lamp_output',            
            dmnd_type = 'BOOL_TYPE',
            subm_type = 'BOOL_TYPE')
DTI.IsoControl('DTI_Iso_dis_pilot_post_0',
               var = 'DTI_Dummy_dis_pilot_post_0_dmnd',
               dmnd_type = 'BOOL_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_dis_pilot_post_1',
               var = 'DTI_Dummy_dis_pilot_post_0_dmnd',
               dmnd_type = 'BOOL_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_dis_pilot_post_2',
               var = 'DTI_Dummy_dis_pilot_post_0_dmnd',
               dmnd_type = 'BOOL_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_dis_pilot_post_3',
               var = 'DTI_Dummy_dis_pilot_post_0_dmnd',
               dmnd_type = 'BOOL_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_inj_bal_flt_disable',
               var = 'DTI_Dummy_Inj_bal_flt_dis_dmnd',
               dmnd_type = 'BOOL_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_c_c_wh',
               var = 'DTI_Dummy_wh_dmnd',
               dmnd_type = 'BOOL_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_c_c_ptc',
               var = 'DTI_Dummy_ptc_dmnd',
               dmnd_type = 'BOOL_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_inj_bal_disable',
               var = 'DTI_Dummy_Inj_bal_disable_dmnd',
               dmnd_type = 'BOOL_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_mdp_map_upd_mode_0',
               var = 'DTI_Dummmy_mdp_mapupd_mode_dmnd',
               dmnd_type = 'DTI_MDP_MAP_UPD_MODE_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_mdp_map_upd_mode_1',
               var = 'DTI_Dummmy_mdp_mapupd_mode_dmnd',
               dmnd_type = 'DTI_MDP_MAP_UPD_MODE_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_mdp_upd_zone_sel_0',
               var = 'DTI_Dummy_mdp_upd_zone_sel_dmnd',
               dmnd_type = 'BOOL_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_mdp_upd_zone_sel_1',
               var = 'DTI_Dummy_mdp_upd_zone_sel_dmnd',
               dmnd_type = 'BOOL_TYPE',
               subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_starter_rly_output',
                var = 'P_L_Starter_relay_output',
                dmnd_type = 'BOOL_TYPE',
                subm_type = 'DTI_SUBM_TYPE'
              )
DTI.IsoControl('DTI_Iso_lnt_desox_request',
                var = 'DTI_Dummy_lnt_desox_request_dmnd',
                dmnd_type = 'BOOL_TYPE',
                subm_type = 'BOOL_TYPE'
              )
DTI.IsoControl('DTI_Iso_cu_relay',
                var = 'SMC_Energise_cu_relay',
                dmnd_type = 'BOOL_TYPE',
                subm_type = 'BOOL_TYPE'
              )
           
