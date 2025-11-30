r1_value = int(input('Enter value of resistor 1.\n'))
r2_value = int(input('Enter value of resistor 2.\n'))
r3_value = int(input('Enter value of resistor 3.\n'))
voltage_value = int(input('Enter Voltage DC. \n'))

r_total = r1_value+r2_value+r3_value
voltage = voltage_value
i_constant = voltage/r_total
v_drop_r1 = i_constant*r1_value
v_drop_r2 = i_constant*r2_value
v_drop_r3 = i_constant*r3_value

print(f'Voltage: {voltage_value} V')
print(f'Total resistance: {r1_value+r2_value+r3_value} Ω')
print(f'Constant current: {i_constant*1000:.3f} mA ({voltage/r_total:.3f} A)')
print(f'Voltage drop across Resistors\n'
      f'R1: {v_drop_r1:.3f} V\n'
      f'R2: {v_drop_r2:.3f} V\n'
      f'R3: {v_drop_r3:.3f} V')