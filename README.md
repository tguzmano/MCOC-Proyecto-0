# MCOC-Proyecto-0
## Introducción
El proyecto-0 busca mostrar el efecto de pérdida de significancia en operaciones aritméticas de punto flotante. Para esto se utiliza el cálculo de determinante de una matriz.
## Este Ejemplo
Para este ejemplo, se puede observar cómo varía la significancia dependiendo de la dimensión de la matriz. Se utilizaron matrices de 2x2, 4x4, 8x8, 16x16 y 32x32.
Se define cada arreglo para dos tipos de datos:
1. Arreglo con tipo de datos 'dtype=no.float32'
2. Arreglo con tipo de datos 'dtype=np.float64'
## Resultados
Los resultados obtenidos se muestran a través del error relativo, el cual es calculado de la siguiente manera:
'''
Error_Relativo = (Determinante_Calculado - Determinante_Exacto) / Determinante_Exacto
'''
Para este caso el error relativo va aumentando a medida que crece la dimensionalidad de la matriz, puesto que para llevar a cabo el cálculo del determinante es necesario realizar internamente operaciones aritméticas, lo que implica una pérdida de significancia al momento de realizar el cálculo respectivo.

Output de la consola:
'''
Matriz 2x2
  Determinante_float32 = 2.29874000000   (error_float32 = 0.0000004779713728%)
  Determinante_float64 = 2.29873775337   (error_float64 = 0.0000000000000000%)
  
Matriz 4x4
  Determinante_float32 = -1.2440300000   (error_float32 = 0.0000071426346007%)
  Determinante_float64 = -1.2440309828   (error_float64 = 0.0000000000000000%)

Matriz 8x8
  Determinante_float32 = 27.1310000000   (error_float32 = 0.000007083369713%)
  Determinante_float64 = 27.1310444023   (error_float64 = 0.0000000000000000%)
  
Matriz 16x16
  Determinante_float32 = -1144240.0000   (error_float32 = 0.0000215138738992%)
  Determinante_float64 = -1144241.2462   (error_float64 = 0.0000000000000000%)
  
Matriz 32x32
  Determinante_float32 = -103194000000e+05   (error_float32 = 0.00015619550273%)
  Determinante_float64 = -103194620999e+05   (error_float64 = 0.00000000000000%)
