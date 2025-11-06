# wire_runner

## Instrucciones

- Conexión por ssh `ssh rpi@cablecam.local`
-  `cd cablecam`
- `python test_move.py`
- Enter position in mm (or 'exit' to quit or 'home' to go home). Las distancias están en mm y es capaz de llegar sobre 60 metros

## metodos disponibles por conexion serial

- `moveto_mm`
- `ensable_stepper`
- `disable_stepper`
- `home`
- `close_serial`
- `open_serial`

## metodos disponibles en arduino

- "Homing"
- "Moveto_step"
- "Moveto_mm"
- "Disable_Stepper"
- "Enable_Stepper"

La revisión del switch de final de carrera de largo total (LIMIT_PIN2 -> GPIO 9) no está habilitado!


## I/O arduino

- EN_PIN 4
- STEP_PIN 6
- DIR_PIN 5
- LIMIT_PIN1 8
- LIMIT_PIN2 9
- Conversion pulsos a mm por reduccion 5:1 
    - `float pulse_to_mm = radius_mm * 0.18 * M_PI / 180.0;`