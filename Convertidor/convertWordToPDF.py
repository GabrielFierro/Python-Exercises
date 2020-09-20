from docx2pdf import convert 

print('Ingrese la ruta absoluta del archivo a convertir')
archivo = input()

print('Ingrese el nombre del archivo resultante')
name = input() + '.pdf' # Setea la extensión pese a que el usuario la ingrese

print('Ingrese la ruta absoluta donde desea que se guarde el archivo')
rutaAbsoluta = input()

# Carga el archivo de tipo .docx
convert(archivo) 
# Convierte el archivo de tipo .docx a un archivo con formato .pdf
convert(archivo, name)
# Guarda en la ruta indicada, el archivo convertido a pdf
convert(rutaAbsoluta)