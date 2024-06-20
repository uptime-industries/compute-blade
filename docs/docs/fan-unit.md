---
sidebar_position: 7
---

# Fan Unit

![Fan Unit](/img/fan-unit/Fan-Unit-Scheme.svg)

---

The Fan Units are Desinged to cool all Blade Runner enclosure. Each Fan Unit can be used to cool two Compute Blades. There are two types of Fan Units standard and smart.

## Comparison of Fan Units

|                     Feture              | Standard | Smart |
| :-------------------------------------- | :------: | :---: |
| v5 PWM Fan Header                       |    ✅   |   ✅  |
| Can be powered from both left and right |    ✅   |   ✅  |
| 2 UART Ports                            |    ❌   |   ✅  |
| 2 temperature sensors                   |    ❌   |   ✅  |
| 2 Load indicator LEDs                   |    ❌   |   ✅  |
| 2 Digital RGB LEDs                      |    ❌   |   ✅  |
| LED conected to GPIO25                  |    ❌   |   ✅  |
| Programable Button                      |    ❌   |   ✅  |
| Reset and BOOT buttons                  |    ❌   |   ✅  |

:::note
When using the standard Fan Unit only the Left pins can be used for PWM
:::
## Monting a Faning
The Fan Units are designed for 40x20mm Fans like the [NF-A4x20 5V PWM](https://noctua.at/en/products/fan/nf-a4x20-5v-pwm). To attach the fan to the Fan Unit follow the folloing steps:

1. Connect the plastic [left](https://github.com/uptime-industries/compute-blade/blob/main/fan-unit/fan-bracket/left.stl) and [right](https://github.com/uptime-industries/compute-blade/blob/main/fan-unit/fan-bracket/right.stl) fan brackets to the fan.
The Numbs on the buttom of the bracket should face the back of the Fan Unit.
2. Attach the Fan to the Fan Unit. Insert the frount of the fan breack first then press firmly on the back.
3. connect The Fan Cable to the 4 Pin Fan Header

Your fan is not installed in the Fan Unit.

:::tip
Need Help with installing your fan unit in a Blade Runner click [here](/blade-runner/)
:::

## Ideas for Smart Fan Unit
Adjusts the speed and color of the digital LEDs depending on the temperature of the airflow. You can specify the desired speed from both blades simply by UART.

Blades can report processor temperatures via UART, and the Smart Fan Unit sets the fan speed and color of the digital LEDs.

The programable button can be use for identification of the Smart Fan Unit.

## Images
To see more Images of the Fan Units see our [GitHub](https://github.com/uptime-industries/compute-blade/tree/main/fan-unit/img).