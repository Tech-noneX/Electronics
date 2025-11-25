# Resistance calculation

## Schematics

![schematics](schematics_resistor_series.svg)

## resistors

* $R_1$ = 300Ω
* $R_2$ = 200Ω
* $R_3$ = 1kΩ
* Power supply; $V=9VDC$ (Battery)

## Calculations to be made

* Total current ; $I_{total}$
* Total resistance ; $R_{total}$
* Voltage drop ; $V_{drop}$

## Formulas to be used

* Ohms law to calculate Resistance($R$), Voltage($V$), Current($I$) ; $R = \frac{V}{I}$

-----

* Total resistance (series); $R_{total}=R_1+R_2+R_3\dots$

-----

### Calculation - Total resistance $R_{total}$

* First we calculate total resistance to be able to calculate total current.

$R_{total}=R_1+R_2+R_3$

$R_{total}=300+200+1000$

$R_{total}=1500\Omega$
-

### Calculation - Total current $I_{total}$

* Using $R_{total}$ we are able to calculate $I_{total}$ as we know voltage $V=9V$
* As we have all components in series current is constant.

$I_{total}=\frac{V}{R_{total}}$

$I_{total}=\frac{9}{1500}$

$I_{total}=6mA(0.006A)$
-

### Calculation - Voltage drop $V_{drop}(R_1, R_2,R_3)$

* Voltage drop across $R_1$

$V_{R_1}=I_{total}×R_1$

$V_{R_1}=0.006×300$

$V_{R_1}=1.8V$
-

* Voltage drop across $R_2$

$V_{R_2}=I_{total}×R_2$

$V_{R_2}=0.006×200$

$V_{R_2}=1.2V$
-

* Voltage drop across $R_3$

$V_{R_3}=I_{total}×R_3$

$V_{R_3}=0.006×1000$

$V_{R_3}=6V$
-
